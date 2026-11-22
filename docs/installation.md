# Uruchomienie z repozytorium

**Status: EXPERIMENTAL / NOT_RELEASED.** Dostępny jest wyłącznie moduł offline `AudioChunk`; brak instalowalnego pakietu, dystrybucji PyPI, `pip install` i wymagań sprzętowych. Działanie potwierdzono w CI na Pythonie 3.11 (Linux). To nie jest deklaracja obsługi innych systemów.

## Uruchomienie testów z katalogu głównego

W powłoce Bash (Linux):

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

W Windows PowerShell (instrukcja, **niepotwierdzona testem Windows**):

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
Remove-Item Env:PYTHONPATH
```

Przykład użycia bez dostępu do urządzeń znajduje się w [kontrakcie AudioChunk](contracts.md). Moduł importuje się z `lib_audio.capture.pcm` po dodaniu `src` do ścieżki Pythona. Nie używa sieci, odczytu plików ani modeli mowy.

Powyższe polecenia dotyczą testów jednostkowych, **nie** instalacji ani weryfikacji środowisk produkcyjnych. Pierwsze wydanie będzie wymagało oddzielnej walidacji instalacji z konkretnego SHA/tagu, licencji, zależności, prywatności i odbiorców.
