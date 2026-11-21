# ADR-0004: niezależna biblioteka trackingu

Data: 2026-11-21  
Status: proposed

## Kontekst

Obserwacje obrazu i sygnałów nie są jeszcze stabilnymi ścieżkami obiektów. Tracking wymaga wspólnego modelu czasu, geometrii, kojarzenia obserwacji i cyklu życia identyfikatora. Takie funkcje występują w projektach robotycznych i XR.

## Propozycja

`lib-track` ma posiadać algorytmy śledzenia, stan tracku, trajektorie i ich ewaluację. Obserwacje dostarczają detektory oraz biblioteki `lib-vis`, `lib-ros`, `lib-eye` lub aplikacje. Nie przenosić całych aplikacji takich jak `alf-light-tracking` do biblioteki i nie dublować DSP z `lib-sig`.

## Alternatywy

- Implementacja trackingu w każdym projekcie konsumenta: duplikacja logiki identyfikacji ścieżek.
- Dołączenie trackingu do `lib-vis`: wyklucza nieobrazowe obserwacje 3D/LiDAR i wiąże tracking z kamerą.

## Konsekwencje

Jeden kontrakt 2D/3D i cyklu życia, możliwość testów syntetycznych, ale obowiązek jawnego czasu, jednostek i kalibracji. Nie deklarować identyfikacji osób ani wsparcia konkretnego hardware bez testów.
