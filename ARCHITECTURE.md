# Architektura lib-audio

Planowana biblioteka obejmuje akwizycję audio, VAD, ASR, TTS (w tym adapter lokalnego Piper) i analizę prozodii. `lib-sig` odpowiada za ogólne DSP, a `lib-vlm` za multimodalne wejścia do modeli; `lib-audio` nie implementuje od nowa silników Whisper ani Piper.

## Granice danych

Offline `AudioChunk` implementuje identyfikatory źródła, strumienia i zegara, liczbę kanałów, częstotliwość próbkowania, indeks pierwszej ramki oraz obliczaną liczbę ramek. `timestamp_s` oznacza czas pierwszej ramki w nazwanej domenie zegara monotonicznego, **nie UTC**. Próbki z różnych zegarów wymagają zwalidowanej transformacji z niepewnością; resampling nie może usuwać metadanych pochodzenia.

[Dokładny kontrakt czasu i segmentów](docs/contracts.md) · [Komponenty](docs/architecture/components.md) · [Przepływy i bezpieczeństwo](docs/architecture/data-flow.md) · [Prywatność](docs/privacy.md) · [ADR-0004](docs/adr/0004-boundaries.md).

Każdy adapter przed implementacją wymaga określenia klasy danych, trybu ruchu sieciowego, dopuszczonych endpointów, uprawnień i retencji. Stan tych ustaleń jest jawny w `config/component.json`. Nie wolno uznać `not_assessed` za przyzwolenie na przesyłanie danych.

**Status: PARTIAL_IMPLEMENTATION / NOT_RELEASED.** `src/lib_audio/capture/pcm.py` udostępnia wyłącznie eksperymentalny, nieinstalowalny kontrakt bloku PCM16 offline z testami jednostkowymi. Brak odczytu plików, urządzeń, backendów audio, VAD/ASR/TTS i publicznego stabilnego API. Surowy PCM nie jest wyświetlany w `repr(AudioChunk)`.
