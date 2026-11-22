# Proponowany kontrakt API

**Status: PROPOSED / NOT_IMPLEMENTED.** `contracts/api.json:public_entrypoints` pozostaje puste. Poniższe wymagania dotyczą przyszłej implementacji, nie potwierdzonego API.

| Typ logiczny | Planowane pola i jednostki | Status |
| --- | --- | --- |
| `AudioChunk` | `source_id`, `stream_id`, `clock_id`, `timestamp_s`, `first_frame_index`, `frame_count`, `sample_rate_hz`, `channel_count`, `encoding`, `pcm_or_ref` | PLANNED |
| `SpeechSegment` | `source_id`, `clock_id`, `start_s`, `end_s`, `text?`, `language?`, `confidence?` | PLANNED |
| `VoiceRequest` | `text`, `voice_id`, `synthesis_parameters`, `request_id` | PLANNED |
| `AcousticFeatures` | `f0_hz`, `intensity_db`, `jitter`, `shimmer`, `validity_flags` | PLANNED |

## Czas i indeksowanie próbek

- `clock_id` identyfikuje **domenę i epokę zegara monotonicznego** strumienia/sesji. Po restarcie lub resecie zegara wymagany jest nowy identyfikator. `timestamp_s` jest czasem pierwszej ramki w sekundach tej domeny; **nie jest datą UTC/Unix**.
- `first_frame_index` to nieujemny całkowity indeks pierwszej ramki w strumieniu; `frame_count` to liczba ramek (ramka zawiera próbkę każdego kanału). `sample_rate_hz > 0` i `channel_count > 0`. Czas trwania bez luk wynosi `duration_s = frame_count / sample_rate_hz`.
- Dla równomiernych próbek nominalny czas ramki `i` to `timestamp_s + i / sample_rate_hz`, dla `0 <= i < frame_count`. Przedział bloku i segmentów jest półotwarty **[start_s, end_s)**. Koniec segmentu musi być późniejszy od początku i dotyczyć tej samej domeny czasu.
- `first_frame_index` zapewnia ciągłość numeracji. Nie wolno jednak wyliczać bezwzględnego `timestamp_s` wyłącznie z indeksu, gdy urządzenie ma dryft, restart, luki lub zmienny zegar. Trzeba zachować pierwotny znacznik i informację o pochodzeniu pomiaru.
- Znaczniki różnych `clock_id` **nie są porównywalne**, dopóki nie zapisano jawnej transformacji między domenami (przesunięcie, skala/dryft, niepewność i źródło synchronizacji). UTC można przechowywać oddzielnie jako opcjonalną metadaną, nie jako zamiennik czasu monotonicznego.
- Resampling/segmentacja wymaga zachowania `input_rate_hz`, `output_rate_hz`, odwzorowania indeksów, opóźnienia filtru (jeśli występuje) i źródłowego `clock_id`. Granice należy przeliczać deterministycznie z określoną regułą zaokrąglania, bez ukrytych zmian czasu.

## Walidacja i błędy

Wymagane są identyfikatory źródła, jednostki, reprezentacja PCM, zakres amplitudy, jawne operacje normalizacji oraz status brakujących metryk (`null`/flaga, nigdy domniemane zero). Wartości NaN/nieskończone, niewłaściwa liczba kanałów, ujemne indeksy, nakładające się lub brakujące ramki oraz nieciągły zegar muszą zwrócić błąd albo jawne oznaczenie utraty danych. Planowane kody: `INVALID_INPUT`, `UNSUPPORTED_FORMAT`, `UNAVAILABLE`, `TIMEOUT`, `DATA_LOSS`, `CLOCK_MISMATCH`. Sposób postępowania przy dryfcie i lukach jest częścią kontraktu adaptera.

Nie podawać zmyślonej pewności ASR ani jakości. Zmiany niekompatybilne w publicznym API po jego wdrożeniu wymagają SemVer, migracji oraz testów odbiorców. [Przepływy i granice zaufania](architecture/data-flow.md) oraz [prywatność](privacy.md).
