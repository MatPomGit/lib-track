"""Contract tests for immutable, finite tracking observations."""

import sys
from pathlib import Path
import unittest
from dataclasses import FrozenInstanceError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from lib_track.core.observation import TrackObservation


def observation(**changes):
    values = dict(observation_id="o1", stream_id="cam", timestamp_monotonic_s=0.0,
                  clock_domain="camera-clock-epoch-1", frame_id="image",
                  geometry_px=(10.0, 20.0))
    values.update(changes)
    return TrackObservation(**values)


class ObservationTests(unittest.TestCase):
    def test_valid_observation_preserves_unknown_confidence(self):
        item = observation()
        self.assertIsNone(item.confidence)
        self.assertEqual(item.geometry_px, (10.0, 20.0))
        with self.assertRaises(FrozenInstanceError):
            item.frame_id = "other"

    def test_invalid_identity_and_clock_fields(self):
        for field in ("observation_id", "stream_id", "clock_domain", "frame_id"):
            with self.subTest(field=field), self.assertRaises(ValueError):
                observation(**{field: " "})

    def test_nonfinite_time_and_geometry_are_rejected(self):
        for value in (float("nan"), float("inf"), True):
            with self.subTest(value=value), self.assertRaises(ValueError):
                observation(timestamp_monotonic_s=value)
            with self.subTest(geometry=value), self.assertRaises(ValueError):
                observation(geometry_px=(value, 1.0))

    def test_confidence_is_optional_but_bounded(self):
        self.assertEqual(observation(confidence=0.0).confidence, 0.0)
        self.assertEqual(observation(confidence=1.0).confidence, 1.0)
        for value in (-0.1, 1.1, float("nan"), True):
            with self.subTest(value=value), self.assertRaises(ValueError):
                observation(confidence=value)


if __name__ == "__main__":
    unittest.main()
