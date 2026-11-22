# Planowane komponenty

| Moduł | Odpowiedzialność | Ograniczenia | Status |
| --- | --- | --- | --- |
| `lib_audio.capture` | Odczyt plików i urządzeń audio, strumieniowanie bloków PCM | Jasny sample rate, liczba kanałów, brak automatycznego zapisu rozmów | PLANNED |
| `lib_audio.vad` | Detekcja aktywności mowy i segmentacja | Znormalizowane przedziały czasu, sensitivity i zasady false positives | PLANNED |
| `lib_audio.asr` | Adaptery rozpoznawania mowy offline i streaming | Odpowiedź tekstowa, czas, confidence gdy dostępne, model_id/digest | PLANNED |
| `lib_audio.tts` | Adaptery syntezy mowy, w tym lokalnego Piper | Voice ID, właściwa próbka wyjściowa, latency i kontrola bufora | PLANNED |
| `lib_audio.features` | Analiza prozodii i parametrów akustycznych | F0, energia, tempo, jednostki, zakres interpretacji i ograniczenia | PLANNED |

Biblioteka odpowiada za tor audio i operacje mowy. lib-vlm/audio przekazuje nagrania do modeli multimodalnych, lecz nie implementuje VAD/ASR/TTS; lib-sig odpowiada za ogólne sygnały naukowe i DSP. Nie budować własnego silnika Piper ani Whisper, jedynie adaptery.

Publiczne symbole implementować dopiero po teście kontraktowym; `contracts/api.json` rejestruje tylko rzeczywistą implementację.
