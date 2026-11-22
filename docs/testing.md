# Strategia testowania

Testy należy wykonywać na syntetycznych, deterministycznych ścieżkach, a następnie na uprawnionych danych rzeczywistych.

1. Jednoobiektowy ruch liniowy: odchylenie pozycji i prędkości względem ground truth.
2. Dwa przecinające się obiekty: stabilność ID i liczba przełączeń tożsamości.
3. Zanik, zasłonięcie i ponowne pojawienie się: cykl `active/lost/terminated`.
4. Niejednorodny `delta_t`, opóźnione obserwacje i odwrócona chronologia.
5. Projekcja 2D/3D z jawną kalibracją, brak kalibracji i rozbieżne frame_id.
6. IoU, IDF1, MOTA i HOTA obliczane na opisanych fixture, bez fikcyjnych wyników.
7. Dwa niezależne, niesynchronizowane zegary: brak mapowania `clock_domain` musi skutkować `TIMEBASE_MISMATCH` bez kojarzenia; poprawne mapowanie o określonej tolerancji dopuszcza skojarzenie, zaś nieaktualne lub zbyt niepewne mapowanie je blokuje.
8. Brak `measurement_covariance` i `TrackState.covariance`: brak musi pozostać nieznany, nie być zamieniany na zero; filtr wymagający kowariancji odrzuca pomiar, a niekowariancyjny może go obsłużyć zgodnie z kontraktem. Zweryfikować jednostki i macierz niedodatnio półokreśloną.
9. Integracja z `alf-light-tracking` lub innym konsumentem ROS2 dopiero po osobnym preflight i uzgodnieniu kontraktu.

Raport: exact SHA, wersje pakietów i backendu, plik fixture, definicja metryki, wynik `PASS/FAIL/NOT_RUN` i ograniczenia. Trwały runner nie wykonuje niezaufanych PR.

Kontrole aktualnego szkieletu:

```bash
python scripts/validate_repository.py --phase scaffold
python scripts/validate_documentation.py
python scripts/validate_pages.py
python -m unittest discover -s tests -v
```
