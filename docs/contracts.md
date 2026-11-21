# Planowany kontrakt śledzenia

**Status: PROPOSED / NOT_IMPLEMENTED.** `contracts/api.json` ma puste `public_entrypoints`, ponieważ żadna klasa nie została jeszcze zaimplementowana.

| Typ | Planowane pola |
| --- | --- |
| `TrackObservation` | `observation_id`, `stream_id`, `timestamp_monotonic_s`, `frame_id`, `geometry`, `confidence?` |
| `TrackState` | `track_id`, `timestamp_monotonic_s`, `position`, `velocity?`, `covariance?`, `status`, `source` |
| `TrackTrajectory` | `track_id`, `states[]`, `start_s`, `end_s?`, `lifecycle_status` |
| `CoordinateFrame` | `frame_id`, `units`, `transform_ref?`, `calibration_ref?` |
| `TrackingMetrics` | `metric_name`, `value`, `definition`, `matching_policy`, `dataset_ref` |
| `TrackingError` | `code`, `retryable`, `details?` |

Układ obrazu ma jednostkę px, współrzędne przestrzenne zasadniczo m; orientacja i przestrzeń odniesienia muszą być opisane jawnie. `timestamp_monotonic_s` ma jednostkę sekundy i oznacza czas obserwacji, nie chwilę wykonania inferencji. `track_id` to lokalny identyfikator obiektu w jednej sesji, nie identyfikator osoby.

Docelowe błędy: `INVALID_GEOMETRY`, `TIMEBASE_MISMATCH`, `FRAME_MISMATCH`, `OUT_OF_ORDER`, `UNSUPPORTED_OBSERVATION`, `TRACK_TERMINATED`. Nie wolno domniemywać metryk lub confidence, których backend nie dostarczył.

Zgodność API i wersjonowanie zostaną utrwalone przy pierwszej implementacji.
