# Architektura lib-audio

Akwizycja i przetwarzanie dźwięku, rozpoznawanie mowy, VAD, synteza głosu oraz analiza akustyczna. Proponowana warstwa obejmuje format danych i źródła, kontrolę jakości, adaptery istniejących backendów oraz jawne metadane pochodzenia.

Biblioteka odpowiada za tor audio i operacje mowy. lib-vlm/audio przekazuje nagrania do modeli multimodalnych, lecz nie implementuje VAD/ASR/TTS; lib-sig odpowiada za ogólne sygnały naukowe i DSP. Nie budować własnego silnika Piper ani Whisper, jedynie adaptery.

Jednostki i czas: sampling_rate_hz, kanały, próbki PCM float/int, czas rozpoczęcia monotoniczny w sekundach, duration_s. Przetwarzanie nie powinno modyfikować źródłowych danych bez jawnej deklaracji transformacji, a metryki jakości powinny zawierać próg, okno i status ważności.

Opis modułów: [komponenty](docs/architecture/components.md) i [przepływ danych](docs/architecture/data-flow.md); decyzja projektowa: [ADR-0004](docs/adr/0004-boundaries.md). Katalogi `src/lib_audio/*` obecnie zawierają tylko README.

**Brak kodu i testów backendów: NOT_IMPLEMENTED / NOT_RUN.**
