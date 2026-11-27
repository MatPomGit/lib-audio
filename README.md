# lib-audio

Akwizycja i przetwarzanie dźwięku, rozpoznawanie mowy, VAD, synteza głosu oraz analiza akustyczna.

Status: **EXPERIMENTAL / PARTIAL_IMPLEMENTATION / NOT_RELEASED** . Dodano walidowaną reprezentację offline PCM16 i testy kontraktowe; brak akwizycji z urządzeń i przetwarzania mowy; lokalne pakiety wymagają odbioru.

## Moduły

| Moduł | Zadanie | Status |
| --- | --- | --- |
| [capture](src/lib_audio/capture/README.md) | Kontrakt bloku PCM16 offline; odczyt plików i urządzeń pozostaje planowany | PARTIAL |
| [vad](src/lib_audio/vad/README.md) | Detekcja aktywności mowy i segmentacja | PLANNED |
| [asr](src/lib_audio/asr/README.md) | Adaptery rozpoznawania mowy offline i streaming | PLANNED |
| [tts](src/lib_audio/tts/README.md) | Adaptery syntezy mowy, w tym lokalnego Piper | PLANNED |
| [features](src/lib_audio/features/README.md) | Analiza prozodii i parametrów akustycznych | PLANNED |

Biblioteka odpowiada za tor audio i operacje mowy. lib-vlm/audio przekazuje nagrania do modeli multimodalnych, lecz nie implementuje VAD/ASR/TTS; lib-sig odpowiada za ogólne sygnały naukowe i DSP. Nie budować własnego silnika Piper ani Whisper, jedynie adaptery.

Zobacz [architekturę](ARCHITECTURE.md), [kontrakt i przykład użycia](docs/contracts.md), [uruchomienie ze źródeł](docs/installation.md), [zgodność](docs/compatibility.md), [plan testów](docs/testing.md), [roadmap](docs/roadmap.md) i [prywatność](docs/privacy.md). Eksperymentalne symbole obu modułów opisano w `contracts/api.json`. Nie publikowano Release ani Pages.

## Eksperymentalny blok PCM16

`src/lib_audio/capture/pcm.py` udostępnia `AudioChunk` dla niezmiennych bajtów PCM signed 16-bit little-endian z przeplotem kanałów. Wymaga jawnej domeny zegara monotonicznego, źródła, strumienia i indeksu ramki; odrzuca niekompletne ramki, niepoprawne znaczniki oraz payload powyżej 64 MiB. Nie wykonuje I/O, normalizacji ani resamplingu. Nie należy traktować go jako stabilnego publicznego API.

Testy offline po ustawieniu `PYTHONPATH=src`: `python -m unittest discover -s tests -v` (pełna regresja) albo `python -m unittest discover -s tests -p 'test_pcm.py' -v` (tylko PCM). `repr(AudioChunk)` nie wypisuje surowych próbek. Wyniki testów i gotowość pakietu wymagają niezależnego potwierdzenia na finalnym SHA.

## Generator stereo Kotlin/JVM

Niezależny moduł generuje Float PCM z indeksowaniem absolutnym, stałomocowym przejściem kanałów i trybem ciszy. Zobacz [stereo](docs/stereo.md). Brak odtwarzania i kalibracji akustycznej.

Python: `python -m pip install .`. JVM: JDK 17, Gradle 9.6.0, `gradle test jar publishMavenJavaPublicationToBuildRepository`. Artefakt lokalny: `org.matpomgit:lib-audio-stereo:0.1.0`. Żadna dystrybucja zdalna nie jest skonfigurowana.
