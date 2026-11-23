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
        for value in (float("nan"), float("inf"), -float("inf"), True):
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


    def test_invalid_identifier_types(self):
        for field in ("observation_id", "stream_id", "clock_domain", "frame_id"):
            for value in (None, "", "\t ", 42, False, []):
                with self.subTest(field=field, value=value):
                    with self.assertRaises(ValueError):
                        observation(**{field: value})

    def test_invalid_time_types_and_geometry_shapes(self):
        for value in (None, "0.0", [], {}):
            with self.subTest(timestamp=value), self.assertRaises(ValueError):
                observation(timestamp_monotonic_s=value)

        for point in (
            None, [], [10.0, 20.0], (), (10.0,), (10.0, 20.0, 30.0),
            (10.0, None), (10.0, "20"), (10.0, True),
            (10.0, float("nan")), (10.0, float("inf")),
        ):
            with self.subTest(geometry=point), self.assertRaises(ValueError):
                observation(geometry_px=point)

    def test_extreme_integer_inputs_raise_value_error(self):
        huge = 10 ** 400
        for changes in (
            {"timestamp_monotonic_s": huge},
            {"geometry_px": (huge, 1.0)},
            {"geometry_px": (1.0, huge)},
            {"confidence": huge},
        ):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                observation(**changes)

    def test_valid_numeric_values_include_ints(self):
        item = observation(
            timestamp_monotonic_s=7,
            geometry_px=(0, -3.5),
            confidence=1,
        )
        self.assertEqual(item.timestamp_monotonic_s, 7)
        self.assertEqual(item.geometry_px, (0, -3.5))
        self.assertEqual(item.confidence, 1)

if __name__ == "__main__":
    unittest.main()
