# Dokumentacja lib-audio

Akwizycja i przetwarzanie dźwięku, rozpoznawanie mowy, VAD, synteza głosu oraz analiza akustyczna.

- [Architektura](architecture/README.md), [moduły](architecture/components.md), [przepływy](architecture/data-flow.md), [dystrybucja](architecture/distribution.md).
- [Kontrakt](contracts.md), [zależności](dependencies.md), [konsumenci](consumers.md), [zgodność](compatibility.md).
- [Testy](testing.md), [roadmap](roadmap.md), [instalacja](installation.md), [prywatność](privacy.md), [ADR-0004](adr/0004-boundaries.md).

`AudioChunk` w `src/lib_audio/capture/pcm.py` jest zaimplementowany eksperymentalnie i testowany offline. Integracje z plikami, urządzeniami, VAD, ASR, TTS i odbiorcami pozostają **NOT_IMPLEMENTED**. Nie ma stabilnego API ani wydania. [Uruchomienie z repozytorium](installation.md) · [Macierz weryfikacji](compatibility.md).

Tylko katalog `pages/` może być źródłem przyszłych publicznych stron; wdrożenie Pages wymaga odrębnej decyzji.
