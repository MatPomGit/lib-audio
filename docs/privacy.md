# Prywatność, klasyfikacja danych i retencja

Nagrania głosu, transkrypcje i identyfikatory mówcy mogą stanowić dane osobowe; próbki wykorzystywane do jednoznacznej identyfikacji biometrycznej mogą wymagać dodatkowej ochrony. Nie wolno umieszczać rzeczywistych danych uczestników, sekretów ani surowych nagrań w Git, publicznym CI, Issues lub Pages.

## Weryfikowalna bramka przed uruchomieniem

`config/component.json` deklaruje pola `data_classification`, `network_egress`, `network_egress_allowlist`. Aktualne `not_assessed` oznacza **brak oceny**, a nie brak ruchu sieciowego ani brak danych osobowych. Walidator szkieletu sprawdza typy i dopuszczalne wartości; walidator wydania blokuje nieocenione pola.

Dla **każdego** adaptera należy udokumentować: klasy danych, cel i podstawę prawną przetwarzania, przepływ między podmiotami/usługami, klasę dostępu, retencję i usuwanie, storage/logging, tryb egress i listę autoryzowanych endpointów, szyfrowanie oraz dowód testowy kontroli. Potwierdzenie schematu repozytorium nie zastępuje analizy ryzyka konkretnego badania ani oceny prawnej.

Tryby egress: `none` (bez wyjścia), `loopback` (wyłącznie lokalna usługa, wciąż granica zaufania), `allowlisted_remote` (jawne, uprzednio zatwierdzone endpointy). Nieoceniony tryb `not_assessed` **blokuje integrację na danych rzeczywistych**. Po ustawieniu `allowlisted_remote` lista endpointów nie może być pusta. Samo dopisanie adresu nie jest autoryzacją transmisji.

Rejestr urządzeń i poufne parametry dostępowe znajdują się w prywatnym `devices`; w tej bibliotece mogą istnieć jedynie abstrakcyjne kontrakty i dane syntetyczne. [Pełne wymagania przepływu](architecture/data-flow.md).
