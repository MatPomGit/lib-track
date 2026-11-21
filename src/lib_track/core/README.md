# core

Schemat obserwacji, detekcji i stanu śledzenia.

`TrackObservation` przenosi `observation_id`, `stream_id`, czas, `frame_id`, geometrię i jakość detekcji. `TrackState` przenosi stabilny, lokalny `track_id`, stan ruchu, niepewność i cykl życia ścieżki. `track_id` nie jest rozpoznawaniem tożsamości osoby i nie powinien mieć semantyki trwałego identyfikatora biometrycznego.

**Status: PLANNED / NOT_IMPLEMENTED.** [Planowany kontrakt](../../../docs/contracts.md) i [walidacja](../../../docs/testing.md).
