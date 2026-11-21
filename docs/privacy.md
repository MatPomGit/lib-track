# Prywatność śledzenia

Trajektorie osób, nagrania, punkty kluczowe twarzy i ruchy ciała mogą stanowić dane osobowe, a w określonych zastosowaniach biometryczne. `track_id` jest tymczasowym identyfikatorem obiektu w sesji, nie mechanizmem rozpoznawania tożsamości.

Domyślnie nie przechowywać surowych obrazów ani trajektorii w publicznym Git, CI, PR czy Pages. Odbiorca określa dozwolony zakres danych, retencję, usuwanie, kontrolę dostępu i zgodę uczestnika eksperymentu. Przesyłanie poza host wymaga jawnej konfiguracji.

Numery seryjne, adresy sprzętu i szczegóły autoryzacji należą do kontrolowanego prywatnego katalogu `devices`; biblioteka dokumentuje wyłącznie kontrakt abstrakcyjny.
