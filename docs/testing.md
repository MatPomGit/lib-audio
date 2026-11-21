# Strategia testowania

Testy offline z danymi syntetycznymi poprzedzają integrację z rzeczywistym urządzeniem, serwisem lub modelem.

1. Odczyt syntetycznego WAV 16/24/32-bit z kontrolą skalowania.
2. Zgodność długości czasowej i resamplingu.
3. VAD na ciszy oraz znanych syntetycznych segmentach.
4. Mock ASR/TTS i timeout, brak modelu, nieprawidłowy voice_id.
5. Test lokalnego Piper/ASR na uprawnionym host po preflight.

Wynik testu dokumentować w raporcie z SHA, wersją backendu, jednostkami i konfiguracją źródła. Nie utożsamiać przejścia walidatorów szkieletu z działającym przetwarzaniem sygnału.

Kontrole repozytorium:

```bash
python scripts/validate_repository.py --phase scaffold
python scripts/validate_documentation.py
python scripts/validate_pages.py
python -m unittest discover -s tests -v
```
