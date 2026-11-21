# lib-audio

Akwizycja i przetwarzanie dźwięku, rozpoznawanie mowy, VAD, synteza głosu oraz analiza akustyczna.

Status: **ARCHITECTURE_ONLY / NOT_IMPLEMENTED / NOT_RELEASED**. Biblioteka zawiera strukturę planowanych modułów i kontraktów, bez instalowalnego pakietu i rzeczywistego przetwarzania danych.

## Moduły

| Moduł | Zadanie | Status |
| --- | --- | --- |
| [capture](src/lib_audio/capture/README.md) | Odczyt plików i urządzeń audio, strumieniowanie bloków PCM | PLANNED |
| [vad](src/lib_audio/vad/README.md) | Detekcja aktywności mowy i segmentacja | PLANNED |
| [asr](src/lib_audio/asr/README.md) | Adaptery rozpoznawania mowy offline i streaming | PLANNED |
| [tts](src/lib_audio/tts/README.md) | Adaptery syntezy mowy, w tym lokalnego Piper | PLANNED |
| [features](src/lib_audio/features/README.md) | Analiza prozodii i parametrów akustycznych | PLANNED |

Biblioteka odpowiada za tor audio i operacje mowy. lib-vlm/audio przekazuje nagrania do modeli multimodalnych, lecz nie implementuje VAD/ASR/TTS; lib-sig odpowiada za ogólne sygnały naukowe i DSP. Nie budować własnego silnika Piper ani Whisper, jedynie adaptery.

Zobacz [architekturę](ARCHITECTURE.md), [kontrakt](docs/contracts.md), [plan testów](docs/testing.md), [roadmap](docs/roadmap.md) i [prywatność](docs/privacy.md). Publiczne symbole w `contracts/api.json` pozostają puste do czasu implementacji. Nie publikowano Release ani Pages.
