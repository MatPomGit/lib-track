# lib-track

**Tracking:** wspólna biblioteka do śledzenia obiektów, osób, punktów i trajektorii w czasie. Celem jest utrzymywanie tożsamości śledzonego obiektu na podstawie kolejnych obserwacji, w 2D lub 3D, niezależnie od konkretnego silnika wizji, robota lub symulatora.

**Status: ARCHITECTURE_ONLY / NOT_IMPLEMENTED / NOT_RELEASED.** Repozytorium zawiera obecnie dokumentację planowanych modułów, bez wykonywalnego API.

## Moduły

| Moduł | Odpowiedzialność | Status |
| --- | --- | --- |
| [core](src/lib_track/core/README.md) | Schemat obserwacji, detekcji i stanu śledzenia | PLANNED |
| [detections](src/lib_track/detections/README.md) | Normalizacja detekcji 2D/3D, punktów kluczowych i pomiarów | PLANNED |
| [association](src/lib_track/association/README.md) | Kojarzenie detekcji ze ścieżkami i utrzymanie identyfikatorów | PLANNED |
| [motion](src/lib_track/motion/README.md) | Predykcja stanu i filtrowanie trajektorii | PLANNED |
| [geometry](src/lib_track/geometry/README.md) | Transformacje współrzędnych i fuzja źródeł | PLANNED |
| [trajectories](src/lib_track/trajectories/README.md) | Historia położeń, życia i zdarzeń ścieżki | PLANNED |
| [evaluation](src/lib_track/evaluation/README.md) | Ewaluacja jakości śledzenia | PLANNED |

`lib-track` obsługuje **tracking**, nie ogólne przetwarzanie obrazu (`lib-vis`), biosygnały i DSP (`lib-sig`), transport ROS2 (`lib-ros`) ani inferencję multimodalnych modeli (`lib-vlm`). `lib-eye` utrzymuje semantykę pomiarów spojrzenia; `lib-track` może udostępniać ogólne mechanizmy kojarzenia obserwacji bez kopiowania algorytmów okulograficznych.

Przykładowe zastosowania to analiza ruchu awatarów, śledzenie sylwetek i dłoni, analiza trajektorii obiektów robota oraz śledzenie plamki świetlnej. Istniejący projekt `alf-light-tracking` pozostaje właścicielem swojego zastosowania ROS2.

[Architektura](ARCHITECTURE.md) · [kontrakty](docs/contracts.md) · [testy](docs/testing.md) · [roadmap](docs/roadmap.md) · [prywatność](docs/privacy.md).

Nie ma obecnie zarejestrowanych symboli API, testów trackingowych ani potwierdzonego odbiorcy produkcyjnego. Wydanie i witryna GitHub Pages nie są publikowane.
