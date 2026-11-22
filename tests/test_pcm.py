"""Contract tests for the dependency-free PCM16 representation."""
import unittest
from lib_audio.capture.pcm import AudioChunk


def chunk(**changes):
    fields = dict(source_id="mic", stream_id="run-1", clock_id="mono-1",
                  timestamp_s=1.25, first_frame_index=10,
                  sample_rate_hz=8000, channel_count=2,
                  pcm_s16le=b"\x00\x00\xff\x7f\x01\x00\x00\x80")
    fields.update(changes)
    return AudioChunk(**fields)


class PCMContractTests(unittest.TestCase):
    def test_frames_and_half_open_timing(self):
        x = chunk()
        self.assertEqual(x.frame_count, 2)
        self.assertEqual(x.duration_s, 2 / 8000)
        self.assertAlmostEqual(x.end_s, 1.25025)

    def test_empty_chunk_is_valid(self):
        self.assertEqual(chunk(pcm_s16le=b"").frame_count, 0)

    def test_reject_partial_interleaved_frame(self):
        with self.assertRaises(ValueError):
            chunk(pcm_s16le=b"\x00\x00")

    def test_reject_invalid_metadata(self):
        invalid = (
            {"source_id": " "}, {"stream_id": ""}, {"clock_id": " "},
            {"source_id": None}, {"sample_rate_hz": 0},
            {"sample_rate_hz": True}, {"sample_rate_hz": 8000.5},
            {"timestamp_s": float("nan")}, {"timestamp_s": float("inf")},
            {"timestamp_s": float("-inf")}, {"timestamp_s": -0.5},
            {"timestamp_s": True}, {"timestamp_s": 10 ** 400},
            {"first_frame_index": -1}, {"first_frame_index": True},
            {"channel_count": 0}, {"channel_count": True},
        )
        for fields in invalid:
            with self.subTest(fields=fields), self.assertRaises(ValueError):
                chunk(**fields)

    def test_reject_mutable_payload(self):
        with self.assertRaises(TypeError):
            chunk(pcm_s16le=bytearray(8))

    def test_resource_limit(self):
        at_limit = b"\x00" * (64 * 1024 * 1024)
        self.assertEqual(chunk(pcm_s16le=at_limit).frame_count, len(at_limit) // 4)
        with self.assertRaises(ValueError):
            chunk(pcm_s16le=at_limit + b"\x00" * 4)

    def test_repr_omits_audio_payload(self):
        rendered = repr(chunk(pcm_s16le=b"ABCD"))
        self.assertNotIn("ABCD", rendered)
        self.assertNotIn("pcm_s16le", rendered)
        self.assertIn("sample_rate_hz=8000", rendered)

    def test_immutable_metadata(self):
        x = chunk()
        with self.assertRaises(AttributeError):
            x.clock_id = "changed"


if __name__ == "__main__":
    unittest.main()
