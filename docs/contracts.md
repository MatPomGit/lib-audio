# Proponowany kontrakt API

**Status: PROPOSED, NOT_IMPLEMENTED.** Publiczne `contracts/api.json:public_entrypoints` pozostaje puste.

| Typ logiczny | Pola / jednostki | Status |
| --- | --- | --- |
| `AudioChunk` | pcm_or_ref, sample_rate_hz, channel_count, frame_count, timestamp_s, encoding | PLANNED |
| `SpeechSegment` | start_s, end_s, text?, language?, confidence? | PLANNED |
| `VoiceRequest` | text, voice_id, synthesis_parameters, request_id | PLANNED |
| `AcousticFeatures` | f0_hz, intensity_db, jitter, shimmer, validity_flags | PLANNED |

Kryteria: jawny identyfikator źródła, typ i jednostki, określona reprezentacja timestampu, kontrola dostępu, zdefiniowany model błędu (`INVALID_INPUT`, `UNSUPPORTED_FORMAT`, `UNAVAILABLE`, `TIMEOUT`, `DATA_LOSS`) oraz opis niepewności i obróbki próbek.

Jednostki referencyjne: sampling_rate_hz, kanały, próbki PCM float/int, czas rozpoczęcia monotoniczny w sekundach, duration_s. Brak metryki nie jest wartością zero; nie wymyślać współczynników jakości ani confidence. Breaking changes wymagają SemVer i migracji konsumenta.
