# Kompatybilność

| Środowisko | Zakres | Status |
| --- | --- | --- |
| Python 3.11 | `TrackObservation`, testy jednostkowe z biblioteki standardowej | CI UNIT TESTS; stan dla konkretnego SHA w GitHub Actions |
| Python >3.11 | Import i walidacja obserwacji | NOT_VERIFIED |
| Linux | Uruchomienie regresji w izolowanym GitHub-hosted runnerze | CI UNIT TESTS; nie oznacza instalacji pakietu |
| Windows | Import, testy syntetyczne | NOT_RUN |
| OpenCV / NumPy / SciPy | Potencjalne adaptery i metody numeryczne, bez obecnej zależności runtime | NOT_RUN |
| ROS2, Unity, Unreal | Integracja przez aplikację konsumenta | NOT_RUN |
| Rzeczywiste kamery / roboty | Tracking na hostach docelowych | NOT_RUN |

Obecny moduł punktu 2D nie jest jeszcze dystrybuowanym pakietem. Brak `pyproject.toml`, testu build i clean-install. Nie deklarować wsparcia sprzętu, SDK ani kolejnych wersji Pythona bez testu z podaniem SHA i środowiska.
