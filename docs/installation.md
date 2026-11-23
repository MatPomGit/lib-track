# Instalacja

Nie ma jeszcze dystrybuowanego pakietu `lib-track` ani konfiguracji `pyproject.toml`. Dostępny jest eksperymentalny, importowalny ze źródeł `TrackObservation`, ale pełne algorytmy śledzenia nie zostały zaimplementowane.

Na Pythonie 3.11+ w katalogu repozytorium można wykonać testy źródeł, bez instalowania zależności:

```bash
python -m unittest discover -s tests -v
```

Testy dodają katalog `src/` do ścieżki modułów. Nie jest to walidacja instalacji pakietu. Wydanie wymaga manifestu PEP 517/518, budowy wheel/sdist, clean-install w pustym środowisku, testu importu i przeglądu licencji oraz zależności. Konfiguracje sprzętu pozostają w prywatnym rejestrze `devices`.
