# Architektura lib-track

`lib-track` zapewni dziedzinowo neutralną warstwę śledzenia w czasie: obserwacje z detektora → kojarzenie międzyklatkowe → filtr stanu ruchu → zarządzanie trajektoriami → ocena jakości.

```text
Camera / LiDAR / pose detector / ROS2 / synthetic observations
                       |
                  detections
                       |
                core + geometry
                       |
             association + motion
                       |
               trajectories
                       |
                 evaluation
                       |
          consumer (robot / XR / experiment)
```

Obserwacje są dostarczane przez konsumenta lub istniejące biblioteki. `lib-track` nie odczytuje kamer, nie uruchamia modeli detekcyjnych, nie steruje aktuatorami ani nie utrzymuje infrastruktury agenta. Własność generowania klatek ma `lib-vis`, transportu ROS2 `lib-ros`, interpretacji spojrzenia `lib-eye`, a kontraktów sprzętu prywatny `devices`.

Docelowy kontrakt wymaga jawnego identyfikatora strumienia, monotonicznego timestampu wraz z `clock_domain`, `frame_id`, jednostki pozycji, jawnej informacji o dostępności niepewności oraz przejść statusów tracku. Pierwsza implementacja obsługuje tylko punktową geometrię 2D w pikselach, bez kowariancji i bez stanów tracku. Brak kowariancji oznacza niepewność nieznaną, a kojarzenie pomiarów z różnych zegarów wymaga zweryfikowanej transformacji czasów. Funkcje wymagające kalibracji lub transformacji między układami odniesienia nie mogą jej domniemywać.

Moduł `src/lib_track/core/observation.py` zawiera obecnie eksperymentalne, importowalne API `TrackObservation`. Pozostałe moduły i pełna ścieżka śledzenia pozostają planowane. Szczegóły: [komponenty](docs/architecture/components.md), [przepływy](docs/architecture/data-flow.md), [kontrakt](docs/contracts.md) i [ADR-0004](docs/adr/0004-tracking-boundaries.md).
