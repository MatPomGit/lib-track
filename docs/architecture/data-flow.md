# Przepływ danych i granice zaufania

Przebieg: **detektor lub sensor → obserwacje → walidacja jednostek / czasu / układu współrzędnych → association + motion → track history → miary jakości → odbiorca**.

Źródłem może być obraz, dane LiDAR, pozycja nadana przez ROS2, punkty kluczowe lub dane syntetyczne. `lib-track` nie otwiera kamery i nie zarządza topologią ROS2. Obserwacje powinny mieć jawny `stream_id`, `timestamp_monotonic_s`, `frame_id`, jednostkę pozycji i informację o błędach pomiarowych.

Kalibracja jest niezbędna przy przeliczeniu 2D na 3D, a predykcja nie może być oznaczona jako obserwacja rzeczywista. Tracki osób lub ruchów kończyn mogą stanowić dane osobowe, dlatego domyślnie nie są zapisywane, logowane ani przesyłane do usług zewnętrznych.

Przy opóźnionych lub odwróconych czasowo próbkach wymagany jest jawny sposób ich obsługi. Brak walidacji na sprzęcie i danych rzeczywistych: **NOT_RUN**.
