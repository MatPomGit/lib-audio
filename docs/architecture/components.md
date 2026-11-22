# Komponenty: stan implementacji

| Moduł | Odpowiedzialność | Ograniczenia | Status |
| --- | --- | --- | --- |
| `lib_audio.capture` | Eksperymentalny `AudioChunk` PCM16 offline; odczyt urządzeń i plików planowany | Jawny sample rate, liczba kanałów, czas monotoniczny, brak I/O i zapisu nagrań | PARTIAL |
| `lib_audio.vad` | Detekcja aktywności mowy i segmentacja | Znormalizowane przedziały czasu, sensitivity i zasady false positives | PLANNED |
| `lib_audio.asr` | Adaptery rozpoznawania mowy offline i streaming | Odpowiedź tekstowa, czas, confidence gdy dostępne, model_id/digest | PLANNED |
| `lib_audio.tts` | Adaptery syntezy mowy, w tym lokalnego Piper | Voice ID, właściwa próbka wyjściowa, latency i kontrola bufora | PLANNED |
| `lib_audio.features` | Analiza prozodii i parametrów akustycznych | F0, energia, tempo, jednostki, zakres interpretacji i ograniczenia | PLANNED |

Biblioteka odpowiada za tor audio i operacje mowy. lib-vlm/audio przekazuje nagrania do modeli multimodalnych, lecz nie implementuje VAD/ASR/TTS; lib-sig odpowiada za ogólne sygnały naukowe i DSP. Nie budować własnego silnika Piper ani Whisper, jedynie adaptery.

`AudioChunk` jest wewnętrznym eksperymentalnym symbolem objętym testami, lecz nie jest zadeklarowany jako stabilny punkt wejścia. `contracts/api.json:public_entrypoints=[]` pozostaje puste do odrębnej decyzji o API.
