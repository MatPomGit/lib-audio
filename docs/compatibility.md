# Zgodność i potwierdzone środowiska

| Środowisko | Zakres | Stan dowodowy |
| --- | --- | --- |
| GitHub-hosted Ubuntu, Python 3.11 | Import `AudioChunk`, regresja jednostkowa, walidacja dokumentacji i stron | PASS na `90c9a7648c67` ([CI #45017602414](https://github.com/MatPomGit/lib-audio/actions/runs/45017602414)) |
| Windows / PowerShell | Uruchomienie ze źródeł z `PYTHONPATH=src` | NOT_RUN |
| Inne wersje Pythona i systemy | Import, testy i wydajność | NOT_RUN |
| Piper / ASR / VAD | Backend i zewnętrzne SDK | NOT_IMPLEMENTED / NOT_RUN |
| Aparatura, sygnał z mikrofonu, E2E odbiorcy | Przetwarzanie rzeczywistych danych i integracja | NOT_IMPLEMENTED / NOT_RUN |

Wynik na jednym przypiętym SHA nie oznacza zwalidowanej kompatybilności całej rodziny Python 3.11+ ani Windows. Po zmianie kodu lub dokumentacji testy CI należy wykonać ponownie na aktualnym HEAD. [Instrukcja uruchomienia](installation.md) · [Plan testów](testing.md).
