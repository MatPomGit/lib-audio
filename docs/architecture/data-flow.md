# Przepływ danych i granice zaufania

**Plan:** źródło (plik/urządzenie/usługa) → walidacja → blok PCM ze znacznikiem pochodzenia → transformacja → odbiorca. Żaden etap nie jest jeszcze zaimplementowany.

## Reprezentacja czasu

Każdy blok otrzymuje `source_id`, `stream_id`, `clock_id`, `timestamp_s` pierwszej ramki, `first_frame_index`, `frame_count`, `sample_rate_hz` i `channel_count`. Ramki są indeksowane liczbami całkowitymi, przedziały czasu mają postać półotwartą [start_s, end_s). `clock_id` rozróżnia epokę zegara monotonicznego także po restarcie. Dwie domeny czasowe wolno porównywać dopiero po udokumentowanej transformacji z niepewnością. Nie zastępować czasu monotonicznego czasem UTC.

Resampling musi rejestrować indeksy wejścia/wyjścia, stawki próbkowania, opóźnienie filtrów, regułę zaokrąglenia i pochodzenie czasu. Dryft, skoki zegara, powielone/zaginione ramki i brakujące kanały wymagają jawnego statusu błędu lub jakości. Szczegóły: [kontrakt](../contracts.md).

## Kontrola przepływu dla każdego adaptera

Przed implementacją adaptera udokumentować: źródło i odbiorcę; klasy danych i podstawę przetwarzania; pola i jednostki; transport oraz serializację; domenę zegara i synchronizację; zakres uprawnień; retencję i usuwanie; lokalizację przetwarzania; wymagane endpointy oraz politykę ruchu sieciowego (`none`, `loopback` lub `allowlisted_remote`). Gdy którykolwiek punkt nie jest ustalony, status pozostaje `not_assessed` i integracja z danymi rzeczywistymi jest niedopuszczona.

Domyślnie zakaz automatycznego zapisu nagrań i transkrypcji; także usługa na loopback jest oddzielną granicą zaufania. Zewnętrzny endpoint wymaga jawnej zgody, autoryzacji, minimalizacji danych i kontroli egress. Do CI, Issues i Pages wolno kierować wyłącznie dane syntetyczne bez identyfikatorów uczestników. Zobacz [prywatność](../privacy.md) i [model zagrożeń](../security/threat-model.md).

**Walidacja funkcjonalna i sprzętowa: NOT_RUN.**
