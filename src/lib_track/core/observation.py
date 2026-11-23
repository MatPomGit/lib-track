"""Validated, immutable 2D point observations; no identity inference or association."""

from dataclasses import dataclass
from math import isfinite


def _finite_real(value: object) -> bool:
    """Accept finite Python reals without leaking int-to-float overflow."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        return isfinite(value)
    except OverflowError:
        return False


@dataclass(frozen=True, slots=True)
class TrackObservation:
    """A point in pixel coordinates with an explicitly scoped monotonic clock."""

    observation_id: str
    stream_id: str
    timestamp_monotonic_s: float
    clock_domain: str
    frame_id: str
    geometry_px: tuple[float, float]
    confidence: float | None = None

    def __post_init__(self) -> None:
        for field in ("observation_id", "stream_id", "clock_domain", "frame_id"):
            value = getattr(self, field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{field} must be a nonempty string")
        if not _finite_real(self.timestamp_monotonic_s):
            raise ValueError("timestamp_monotonic_s must be finite")
        point = self.geometry_px
        if not isinstance(point, tuple) or len(point) != 2 or any(
            not _finite_real(v) for v in point
        ):
            raise ValueError("geometry_px must be a finite 2D tuple")
        if self.confidence is not None and (
            not _finite_real(self.confidence) or not 0 <= self.confidence <= 1
        ):
            raise ValueError("confidence must be in [0, 1] or unknown")
