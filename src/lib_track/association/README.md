# association

Kojarzenie detekcji ze ścieżkami i utrzymanie identyfikatorów.

Kojarzenie opiera się na zgodności czasu, geometrii i jawnej macierzy kosztów. Metody nearest-neighbour/Hungarian/gating są planowanymi alternatywami. Przy braku obserwacji tracking powinien zwracać stan `lost` i status niepewności, zamiast wymyślać nową detekcję. Automatyczna identyfikacja osób nie należy do podstawowego zakresu.

**Status: PLANNED / NOT_IMPLEMENTED.** [Planowany kontrakt](../../../docs/contracts.md) i [walidacja](../../../docs/testing.md).
