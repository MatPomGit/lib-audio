# Przepływ danych

Plan: **źródło → walidacja schematu → blok/strumień → transformacja → metadane pochodzenia → odbiorca**. Import i eksport powinny być opcjonalne; nie zapisywać domyślnie danych z urządzeń do repo.

sampling_rate_hz, kanały, próbki PCM float/int, czas rozpoczęcia monotoniczny w sekundach, duration_s. Dla każdego bloku utrzymać identyfikator, monotoniczny czas, jednostki i źródło. Resampling, segmentacja lub normalizacja powinny pozostawić ślad w metadanych. Nieregularne próbki, brakujące kanały oraz skoki czasu muszą zwracać ostrzeżenia lub błędy.

Nie logować surowych nagrań, próbek biologicznych, transkrypcji ani danych osób badanych do publicznego CI. Adaptery lokalnych usług są osobną granicą zaufania, nawet dla loopback. Stan testów rzeczywistego przetwarzania: **NOT_RUN**.
