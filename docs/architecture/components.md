# Komponenty biblioteki

| Moduł | Własność | Status |
| --- | --- | --- |
| `lib_track.core` | Schemat obserwacji, detekcji i stanu śledzenia | PLANNED |
| `lib_track.detections` | Normalizacja detekcji 2D/3D, punktów kluczowych i pomiarów | PLANNED |
| `lib_track.association` | Kojarzenie detekcji ze ścieżkami i utrzymanie identyfikatorów | PLANNED |
| `lib_track.motion` | Predykcja stanu i filtrowanie trajektorii | PLANNED |
| `lib_track.geometry` | Transformacje współrzędnych i fuzja źródeł | PLANNED |
| `lib_track.trajectories` | Historia położeń, życia i zdarzeń ścieżki | PLANNED |
| `lib_track.evaluation` | Ewaluacja jakości śledzenia | PLANNED |

Algorytmy są projektowane niezależnie od OpenCV, ROS2, Unity i Unreal, aby nie wymagać tych środowisk do podstawowych testów. Śledzenie nie zakłada identyfikacji biometrycznej osoby. Adapters sprzętowe powinny mapować dane z zachowaniem pochodzenia i znaczników czasu.

Nie istnieje jeszcze importowalny kod. [Kontrakty](../contracts.md) są propozycją, a nie publicznym API.
