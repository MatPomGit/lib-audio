# lib_audio

Akwizycja i przetwarzanie dźwięku, rozpoznawanie mowy, VAD, synteza głosu oraz analiza akustyczna.

[capture](capture/README.md) · [vad](vad/README.md) · [asr](asr/README.md) · [tts](tts/README.md) · [features](features/README.md).

Stan: **PARTIAL_IMPLEMENTATION / EXPERIMENTAL / NOT_RELEASED**. `capture/pcm.py` zawiera testowany offline kontrakt `AudioChunk` (PCM16 s16le, przeplot kanałów, niezmienny `bytes`, limit 64 MiB). Pozostałe moduły są planowane; nie ma instalowalnego pakietu, urządzeń, sieci ani stabilnego publicznego API. [Kontrakty](../../docs/contracts.md) · [Uruchomienie](../../docs/installation.md).
