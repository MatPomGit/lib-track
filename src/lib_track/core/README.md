# core

Moduł `core` zawiera zaimplementowany, eksperymentalny `TrackObservation` w `observation.py`. Jest to niemutowalny model pojedynczego punktu 2D w pikselach, zawierający identyfikatory obserwacji i strumienia, `timestamp_monotonic_s`, `clock_domain`, `frame_id`, `geometry_px` oraz opcjonalny `confidence`. Konstruktor waliduje typy, skończoność liczb i przedział pewności, zgłaszając `ValueError` przy niepoprawnych danych.

`TrackState` i mechanizm nadawania stabilnego, lokalnego `track_id`, aktualizacja stanu ruchu, niepewność oraz cykl życia ścieżki są nadal planowane. `track_id` nie będzie trwałym identyfikatorem biometrycznym osoby.

**Status: PARTIAL / EXPERIMENTAL / NOT_RELEASED.** [Kontrakt](../../../docs/contracts.md) i [testy](../../../docs/testing.md).
