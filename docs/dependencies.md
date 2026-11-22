# Zależności

Planowany rdzeń Python ma zachować możliwie małe zależności. NumPy/SciPy mogą dostarczyć arytmetykę macierzową i filtrację; OpenCV może pozostać opcjonalnym adapterem detekcji/geometrycznym, a ROS2/rclpy zależnością tylko konsumenta.

Tracking to warstwa kojarzenia i aktualizacji stanu, a nie dostawca modeli detekcyjnych. Ani biblioteka, ani jej dystrybucja nie powinny zawierać wag modeli, prywatnych nagrań czy cudzych SDK bez osobnego przeglądu licencji.

Żadna zależność nie jest jeszcze wybrana lub zainstalowana w projekcie. **AUDIT NOT_RUN**.
