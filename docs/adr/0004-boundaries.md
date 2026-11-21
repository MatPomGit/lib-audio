# ADR-0004: granice lib-audio

Data: 2026-11-21  
Status: proposed

## Kontekst

Akwizycja i przetwarzanie dźwięku, rozpoznawanie mowy, VAD, synteza głosu oraz analiza akustyczna. Funkcje tego obszaru przenikają przez kilka projektów, przez co łatwo o duplikację.

## Propozycja

Biblioteka odpowiada za tor audio i operacje mowy. lib-vlm/audio przekazuje nagrania do modeli multimodalnych, lecz nie implementuje VAD/ASR/TTS; lib-sig odpowiada za ogólne sygnały naukowe i DSP. Nie budować własnego silnika Piper ani Whisper, jedynie adaptery.

## Alternatywy

- Duplikowanie kodu w aplikacjach: trudniejsze testy i utrzymanie.
- Jeden megaprojekt sensorów/modeli: nadmierne zależności oraz brak jawnych granic.

## Konsekwencje

Oddzielne kontrakty i testy źródeł. Zamierzone jednostki: sampling_rate_hz, kanały, próbki PCM float/int, czas rozpoczęcia monotoniczny w sekundach, duration_s. Nie deklarować wsparcia bez rzeczywistych testów.
