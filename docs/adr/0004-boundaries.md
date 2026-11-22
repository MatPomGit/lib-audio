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

Oddzielne kontrakty i testy źródeł. Kontrakt czasu wymaga identyfikatora domeny/epoki zegara, indeksu ramek i jawnej transformacji przy synchronizacji urządzeń. Klasyfikacja danych, egress i retencja podlegają bramce przed implementacją adaptera. Zobacz [kontrakt](../contracts.md), [przepływy](../architecture/data-flow.md) i [prywatność](../privacy.md). Nie deklarować wsparcia bez rzeczywistych testów.
