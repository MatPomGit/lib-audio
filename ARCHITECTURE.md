# Architektura lib-audio

Planowana biblioteka obejmuje akwizycję audio, VAD, ASR, TTS (w tym adapter lokalnego Piper) i analizę prozodii. `lib-sig` odpowiada za ogólne DSP, a `lib-vlm` za multimodalne wejścia do modeli; `lib-audio` nie implementuje od nowa silników Whisper ani Piper.

## Granice danych

Dla bloków PCM planowane są jawne identyfikatory źródła, liczba kanałów, częstotliwość próbkowania, indeks pierwszej ramki, liczba ramek i identyfikator zegara. `timestamp_s` oznacza czas pierwszej ramki w nazwanej domenie zegara monotonicznego, **nie UTC**. Próbki z różnych zegarów wymagają zwalidowanej transformacji z niepewnością; resampling nie może usuwać metadanych pochodzenia.

[Dokładny kontrakt czasu i segmentów](docs/contracts.md) · [Komponenty](docs/architecture/components.md) · [Przepływy i bezpieczeństwo](docs/architecture/data-flow.md) · [Prywatność](docs/privacy.md) · [ADR-0004](docs/adr/0004-boundaries.md).

Każdy adapter przed implementacją wymaga określenia klasy danych, trybu ruchu sieciowego, dopuszczonych endpointów, uprawnień i retencji. Stan tych ustaleń jest jawny w `config/component.json`. Nie wolno uznać `not_assessed` za przyzwolenie na przesyłanie danych.

**Status: ARCHITECTURE_ONLY / NOT_IMPLEMENTED.** Katalogi `src/lib_audio/*` zawierają wyłącznie README; nie ma kodu backendów ani testów funkcjonalnych.
