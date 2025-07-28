"""
Accent Correction Tool

A real-time, on-device accent correction tool that helps users improve their pronunciation
through phoneme-level feedback and personalized coaching.
"""

__version__ = "0.1.0"
__author__ = "Nadav Koplovich"
__email__ = "koplonadav@gmail.com"

from .audio import AudioProcessor
from .models import AcousticModel, VADModel
from .feedback import FeedbackEngine
from .personalization import PersonalizationEngine
from .utils import Config, Logger

__all__ = [
    "AudioProcessor",
    "AcousticModel", 
    "VADModel",
    "FeedbackEngine",
    "PersonalizationEngine",
    "Config",
    "Logger",
] 