# Kontrakt śledzenia

**Status: EXPERIMENTAL / PARTIALLY_IMPLEMENTED / NOT_RELEASED.** Kanoniczne `contracts/api.json` rejestruje jeden publiczny symbol: `lib_track.core.observation.TrackObservation`. Pozostałe typy oraz asocjacja obserwacji nie są zaimplementowane.

| Typ | Status | Pola |
| --- | --- | --- |
| `TrackObservation` | IMPLEMENTED (eksperymentalny) | `observation_id: str`, `stream_id: str`, `timestamp_monotonic_s: float`, `clock_domain: str`, `frame_id: str`, `geometry_px: tuple[float, float]`, `confidence: float | None = None` |
| `TrackState` | PROPOSED | `track_id`, `timestamp_monotonic_s`, `clock_domain`, `position`, `velocity?`, `covariance?`, `status`, `source` |
| `TrackTrajectory` | PROPOSED | `track_id`, `states[]`, `start_s`, `end_s?`, `lifecycle_status` |
| `CoordinateFrame` | PROPOSED | `frame_id`, `units`, `transform_ref?`, `calibration_ref?` |
| `TrackingMetrics` | PROPOSED | `metric_name`, `value`, `definition`, `matching_policy`, `dataset_ref` |
| `TrackingError` | PROPOSED | `code`, `retryable`, `details?` |

`TrackObservation` przyjmuje dwuelementową krotkę współrzędnych `geometry_px` wyrażonych w pikselach, nie dowolną geometrię 2D/3D. Pola identyfikatorów muszą być niepustymi napisami. Znacznik czasu, obie współrzędne oraz niepusty `confidence` muszą być skończonymi liczbami typu `int` lub `float`, z wyłączeniem `bool`. Wartości całkowite przekraczające zakres konwersji na `float` są odrzucane przez `ValueError`. `confidence` może wynosić `None` (nieznana pewność) albo należeć do przedziału [0, 1]. Nie są normalizowane białe znaki identyfikatorów. Klasa używa `dataclass(frozen=True, slots=True)`, ale nie narzuca unikalności identyfikatorów ani monotonicznej kolejności pomiarów w strumieniu.

`timestamp_monotonic_s` reprezentuje sekundę w lokalnej domenie zegara `clock_domain` (zegar wraz z epoką), a nie czas wykonania inferencji. Obecny konstruktor sprawdza skończoność pojedynczej wartości, lecz nie weryfikuje zgodności zegarów ani kolejności kolejnych próbek. Samo `stream_id` nie ustanawia wspólnej domeny. Przyszłe kojarzenie obserwacji z różnych zegarów wymaga jawnej transformacji czasu, z uwzględnieniem offsetu, ewentualnego dryfu, przedziału ważności i tolerancji. Odrzucenie niezgodności jako `TIMEBASE_MISMATCH` należy do planowanej warstwy asocjacji.

W aktualnym `TrackObservation` nie istnieje pole `measurement_covariance`. Nie wolno interpretować jego braku jako kowariancji zerowej ani przeliczać `confidence` na wariancję. W przyszłym rozszerzeniu niepewność będzie reprezentowana w jednostkach kwadratowych układu odniesienia i walidowana pod kątem wymiaru, symetrii i dodatniej półokreśloności. Analogicznie brak `TrackState.covariance` w planowanym kontrakcie oznacza niepewność nieznaną.

`TrackState`, `TrackingError` i kody `INVALID_GEOMETRY`, `TIMEBASE_MISMATCH`, `FRAME_MISMATCH`, `OUT_OF_ORDER`, `UNSUPPORTED_OBSERVATION`, `TRACK_TERMINATED` są projektowane, a nie zaimplementowane. Dzisiaj niepoprawne pola `TrackObservation` powodują `ValueError`. Brak transformacji 2D/3D i nie należy domniemywać kalibracji.

Wersja `0.1.0` jest eksperymentalnym kontraktem źródłowym, bez wydania pakietu. Zgodność `contracts/api.json`, `config/component.json` i `PROJECT_STATE.yaml` musi być utrzymywana. Niezgodne zmiany udostępnionego API wymagają aktualizacji wersji SemVer, opisu migracji i testów odbiorców, zgodnie z [AGENTS.md](../AGENTS.md).
