"""Offline scaffold/release regression tests; no third-party dependencies."""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_repository import check, REQUIRED


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        for rel in REQUIRED:
            source = ROOT / rel
            target = self.repo / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    def rewrite_json(self, rel, update):
        p = self.repo / rel
        obj = json.loads(p.read_text(encoding="utf-8"))
        obj.update(update)
        p.write_text(json.dumps(obj), encoding="utf-8")

    def test_valid_scaffold(self):
        self.assertEqual([], check(self.repo, "scaffold"))

    def test_release_is_closed_by_default(self):
        errors = check(self.repo, "release")
        self.assertIn("GATE BLOCKED: tests_executed", errors)
        self.assertIn("LICENSE: placeholder has not been replaced", errors)
        self.assertIn("MISSING RELEASE ARTIFACT", errors)

    def test_missing_file_fails_closed(self):
        (self.repo / "README.md").unlink()
        self.assertIn("MISSING: README.md", check(self.repo))

    def test_malformed_json_fails_closed(self):
        (self.repo / "contracts/api.json").write_text("[]")
        self.assertIn("INVALID OBJECT: contracts/api.json", check(self.repo))

    def test_schema_version_bool_fails_closed(self):
        self.rewrite_json("contracts/api.json", {"schema_version": True})
        self.assertIn("SCHEMA: API contract must be version 1", check(self.repo))

    def test_api_package_mismatch_fails_closed(self):
        self.rewrite_json("contracts/api.json", {"name": "different"})
        self.assertIn("CONTRACT: name != package_identifier", check(self.repo))

    def test_api_version_mismatch_fails_closed(self):
        self.rewrite_json("contracts/api.json", {"api_version": "2.0.0"})
        self.assertIn("CONTRACT: api_version != component version", check(self.repo))

    def test_invalid_semver_fails_closed(self):
        self.rewrite_json("config/component.json", {"version": "01.2.3"})
        self.assertIn("VERSION: invalid SemVer", check(self.repo))

    def test_bad_public_entrypoints_fails_closed(self):
        self.rewrite_json("contracts/api.json", {"public_entrypoints": ["x", "x"]})
        self.assertIn("CONTRACT: duplicate public_entrypoints", check(self.repo))

    def test_state_mismatch_fails_closed(self):
        p = self.repo / "PROJECT_STATE.yaml"
        p.write_text(p.read_text().replace("source_version: 0.1.0", "source_version: 9.9.9"))
        self.assertIn("STATE: source_version mismatch", check(self.repo))

    def test_unassessed_privacy_policy_blocks_release(self):
        errors = check(self.repo, "release")
        self.assertIn("PRIVACY: data_classification not assessed", errors)
        self.assertIn("PRIVACY: network_egress not assessed", errors)

    def test_invalid_data_classification_fails_scaffold(self):
        self.rewrite_json("config/component.json", {"data_classification": "verified"})
        self.assertIn("PRIVACY: invalid data_classification", check(self.repo))

    def test_invalid_network_egress_fails_scaffold(self):
        self.rewrite_json("config/component.json", {"network_egress": "any"})
        self.assertIn("PRIVACY: invalid network_egress", check(self.repo))

    def test_remote_egress_requires_allowlist(self):
        self.rewrite_json("config/component.json", {"network_egress": "allowlisted_remote"})
        self.assertIn("PRIVACY: remote egress requires an allowlist", check(self.repo))

    def test_non_remote_egress_rejects_remote_allowlist(self):
        self.rewrite_json("config/component.json", {
            "network_egress": "none",
            "network_egress_allowlist": ["https://example.org"],
        })
        self.assertIn("PRIVACY: allowlist requires allowlisted_remote mode", check(self.repo))

    def test_path_escape_is_not_accepted(self):
        self.rewrite_json("config/release-gate.json", {"release_artifact_path": "../../etc/passwd"})
        self.assertIn("MISSING RELEASE ARTIFACT", check(self.repo, "release"))


if __name__ == "__main__":
    unittest.main()
