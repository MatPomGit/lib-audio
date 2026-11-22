# Strategia testowania

**Scaffold CI nie testuje działania przetwarzania audio.** Testy offline na danych syntetycznych powinny poprzedzać połączenie z rzeczywistymi urządzeniami, uczestnikami lub modelami.

1. Odczyt WAV 16/24/32-bit: kanały, skalowanie i jawna reprezentacja PCM.
2. Długość bloku i resampling: `frame_count / sample_rate_hz`, indeksy wejścia/wyjścia, opóźnienie, reguła zaokrąglania.
3. Zegar: nowy `clock_id` po restarcie, luki i duplikaty ramek, dryft, `CLOCK_MISMATCH` dla niesynchronizowanych domen oraz niepewność mapowania.
4. Segmenty: półotwarte granice czasu, nieprawidłowe przedziały i brak prawidłowej jednostki.
5. VAD: cisza i znane syntetyczne segmenty, błędy detekcji.
6. Mock ASR/TTS: brak modelu, timeout, nieprawidłowy `voice_id`, brak wymyślonego `confidence`.
7. Prywatność: nieocenione `data_classification` i `network_egress` blokują wydanie; zewnętrzny egress wymaga allowlisty. Przed uruchomieniem adaptera wymagany przegląd zakresu danych i retencji.
8. Lokalny Piper/ASR oraz E2E z konsumentem: wyłącznie na uprawnionym host po preflight i odrębnych testach integracyjnych.

Raport: polecenia, środowisko, finalny commit SHA, konfiguracja zegara/backendu, dane syntetyczne lub ich pochodzenie, wynik i ograniczenia. `NOT_RUN` nie jest `PASS`.

Walidacja samego szkieletu:

```bash
python scripts/validate_repository.py --phase scaffold
python scripts/validate_documentation.py
python scripts/validate_pages.py
python -m unittest discover -s tests -v
python -m mkdocs build --strict
python scripts/validate_rendered_pages.py --strict
```
