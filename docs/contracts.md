# Planowany kontrakt śledzenia

**Status: PROPOSED / NOT_IMPLEMENTED.** `contracts/api.json` ma puste `public_entrypoints`, ponieważ żadna klasa nie została jeszcze zaimplementowana.

| Typ | Planowane pola |
| --- | --- |
| `TrackObservation` | `observation_id`, `stream_id`, `timestamp_monotonic_s`, `clock_domain`, `frame_id`, `geometry`, `measurement_covariance?`, `confidence?` |
| `TrackState` | `track_id`, `timestamp_monotonic_s`, `clock_domain`, `position`, `velocity?`, `covariance?`, `status`, `source` |
| `TrackTrajectory` | `track_id`, `states[]`, `start_s`, `end_s?`, `lifecycle_status` |
| `CoordinateFrame` | `frame_id`, `units`, `transform_ref?`, `calibration_ref?` |
| `TrackingMetrics` | `metric_name`, `value`, `definition`, `matching_policy`, `dataset_ref` |
| `TrackingError` | `code`, `retryable`, `details?` |

Układ obrazu ma jednostkę px, współrzędne przestrzenne zasadniczo m; orientacja i przestrzeń odniesienia muszą być opisane jawnie. `timestamp_monotonic_s` ma jednostkę sekundy i oznacza czas obserwacji, nie chwilę wykonania inferencji. `track_id` to lokalny identyfikator obiektu w jednej sesji, nie identyfikator osoby.

**Domeny czasu.** `timestamp_monotonic_s` jest monotoniczny wyłącznie w obrębie `clock_domain` (identyfikatora zegara i jego epoki). Samo `stream_id` nie oznacza wspólnego zegara. Kojarzenie obserwacji z różnych domen wymaga jawnie skonfigurowanej transformacji czasu do jednej domeny odniesienia (offset, opcjonalny dryf, przedział ważności, maksymalna niepewność synchronizacji i tolerancja kojarzenia). Brak transformacji, przekroczona tolerancja lub nieznana epoka powodują `TIMEBASE_MISMATCH` i odrzucenie kojarzenia, nie ciche porównanie timestampów. Obsługę próbek out-of-order określa odbiorca, bez automatycznej reinterpretacji zegara.

**Niepewność pomiarowa.** `measurement_covariance?` reprezentuje macierz kowariancji w jednostkach kwadratowych i układzie geometrii obserwacji. Brak pola oznacza `unknown`, nigdy kowariancję zerową. Taką obserwację wolno odrzucić z jawnym błędem albo przetwarzać algorytmem niewymagającym kowariancji, lecz nie wolno konstruować fikcyjnej macierzy. Analogicznie brak `TrackState.covariance?` oznacza nieznaną niepewność, a nie pewny stan; `confidence?` jest odrębną wielkością dostawcy i nie jest automatycznie wariancją. Jednostki, wymiar, symetria i dodatnia półokreśloność dostępnej macierzy wymagają walidacji.

Docelowe błędy: `INVALID_GEOMETRY`, `TIMEBASE_MISMATCH`, `FRAME_MISMATCH`, `OUT_OF_ORDER`, `UNSUPPORTED_OBSERVATION`, `TRACK_TERMINATED`. Nie wolno domniemywać metryk lub confidence, których backend nie dostarczył.

Zgodność API i wersjonowanie zostaną utrwalone przy pierwszej implementacji. Zmiana niekompatybilna po udostępnieniu publicznego API wymaga zgodnie z [AGENTS.md](../AGENTS.md) aktualizacji MAJOR (SemVer), opisu migracji oraz testów kompatybilności odbiorców; nie wolno uznać samego numeru schematu za dowód zgodności.
