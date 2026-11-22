# Etapy realizacji

| Etap | Zadanie | Status |
| --- | --- | --- |
| D0 | Struktura, kontrakty i dokumentacja | IN_PROGRESS |
| D1 | Typy danych, walidacja i jednostki (częściowo: offline `AudioChunk` PCM16, testy kontraktowe) | IN_PROGRESS |
| D2 | Jeden lokalny adapter i mockowane testy | NOT_STARTED |
| D3 | Strumieniowanie, synchronizacja i obsługa błędów | NOT_STARTED |
| D4 | E2E na uprawnionym host i odbiorca | NOT_STARTED |

Dotychczas potwierdzono wyłącznie jednostkowe działanie `AudioChunk` w izolowanym CI na Pythonie 3.11. Zakończenie D1 wymaga pozostałych kontraktów i jawnej weryfikacji. Integracja nie powinna uruchamiać modeli ani urządzeń na stałych runnerach bez preflight. Release/Pages są osobno zatwierdzanymi zadaniami. Dokumentacja nie jest dowodem wykonania.
