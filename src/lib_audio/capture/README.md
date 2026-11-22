# capture

Eksperymentalna reprezentacja offline PCM16. Odczyt plików i urządzeń oraz strumieniowanie pozostają w planie.

Jasny sample rate, liczba kanałów, brak automatycznego zapisu rozmów.

Zasady: identyfikator źródła, znormalizowane jednostki, jawny timestamp, opis błędów i limit zasobów. Gdy funkcjonalność zależy od zewnętrznego runtime, testować ją na jawnej wersji backendu i sprzętu.

Status: **PARTIAL / EXPERIMENTAL / NOT_RELEASED**. Dostępny jest tylko `AudioChunk` w `pcm.py` (signed 16-bit little-endian, interleaved, maks. 64 MiB, jawny zegar monotoniczny). Dane PCM nie są drukowane przez `repr()`. Brak I/O i stabilnego API. [Kontrakty](../../../docs/contracts.md), [testy](../../../docs/testing.md).
