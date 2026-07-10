"""Packaging helpers for the emotion detector project.

This package exposes a simple public API for consumers who want to
import the core emotion detection function from a single place.
"""

__all__ = ["emotion_detector"]
__version__ = "0.1.0"

from emotion_detector.emotion_detection import emotion_detector

# Re-export for `from packaging import emotion_detector`
