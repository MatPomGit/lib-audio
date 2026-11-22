"""Offline PCM16 chunk contract; no capture, network, or device access."""
from dataclasses import dataclass
from math import isfinite

_MAX_PCM_BYTES = 64 * 1024 * 1024


@dataclass(frozen=True)
class AudioChunk:
    """Immutable interleaved signed 16-bit little-endian PCM frames.

    timestamp_s is the first frame's monotonic clock-domain time, never UTC.
    first_frame_index counts frames (not individual channel samples).
    """

    source_id: str
    stream_id: str
    clock_id: str
    timestamp_s: float
    first_frame_index: int
    sample_rate_hz: int
    channel_count: int
    pcm_s16le: bytes

    def __post_init__(self) -> None:
        for field in ("source_id", "stream_id", "clock_id"):
            value = getattr(self, field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{field} must be nonempty")
        if isinstance(self.timestamp_s, bool) or not isinstance(self.timestamp_s, (int, float)) or not isfinite(self.timestamp_s) or self.timestamp_s < 0:
            raise ValueError("timestamp_s must be finite and nonnegative")
        for field in ("first_frame_index", "sample_rate_hz", "channel_count"):
            value = getattr(self, field)
            if type(value) is not int or (value < 0 if field == "first_frame_index" else value <= 0):
                raise ValueError(f"{field} is invalid")
        if type(self.pcm_s16le) is not bytes:
            raise TypeError("pcm_s16le must be immutable bytes")
        if len(self.pcm_s16le) > _MAX_PCM_BYTES:
            raise ValueError("PCM resource limit exceeded")
        if len(self.pcm_s16le) % (2 * self.channel_count):
            raise ValueError("PCM must contain complete interleaved frames")

    @property
    def frame_count(self) -> int:
        return len(self.pcm_s16le) // (2 * self.channel_count)

    @property
    def duration_s(self) -> float:
        return self.frame_count / self.sample_rate_hz

    @property
    def end_s(self) -> float:
        """Exclusive nominal end in the same monotonic clock domain."""
        return self.timestamp_s + self.duration_s
