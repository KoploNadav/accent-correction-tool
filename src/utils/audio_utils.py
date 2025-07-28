"""
Audio utility functions for the accent correction tool.
"""

import numpy as np
from typing import Tuple, Optional


def normalize_audio(audio_data: np.ndarray) -> np.ndarray:
    """Normalize audio data to [-1, 1] range.
    
    Args:
        audio_data: Input audio data
        
    Returns:
        Normalized audio data
    """
    if len(audio_data) == 0:
        return audio_data
    
    max_val = np.max(np.abs(audio_data))
    if max_val > 0:
        return audio_data / max_val
    return audio_data


def resample_audio(audio_data: np.ndarray, 
                  original_rate: int, 
                  target_rate: int) -> np.ndarray:
    """Resample audio to target sample rate.
    
    Args:
        audio_data: Input audio data
        original_rate: Original sample rate
        target_rate: Target sample rate
        
    Returns:
        Resampled audio data
    """
    if original_rate == target_rate:
        return audio_data
    
    # Simple linear interpolation for now
    # TODO: Use proper resampling library
    ratio = target_rate / original_rate
    new_length = int(len(audio_data) * ratio)
    
    indices = np.linspace(0, len(audio_data) - 1, new_length)
    return np.interp(indices, np.arange(len(audio_data)), audio_data)


def segment_audio(audio_data: np.ndarray, 
                  sample_rate: int, 
                  segment_duration: float) -> list:
    """Segment audio into fixed-length chunks.
    
    Args:
        audio_data: Input audio data
        sample_rate: Audio sample rate
        segment_duration: Duration of each segment in seconds
        
    Returns:
        List of audio segments
    """
    segment_length = int(segment_duration * sample_rate)
    segments = []
    
    for i in range(0, len(audio_data), segment_length):
        segment = audio_data[i:i + segment_length]
        if len(segment) == segment_length:  # Only full segments
            segments.append(segment)
    
    return segments


def compute_spectrogram(audio_data: np.ndarray, 
                       sample_rate: int,
                       n_fft: int = 512,
                       hop_length: int = 256) -> np.ndarray:
    """Compute spectrogram from audio data.
    
    Args:
        audio_data: Input audio data
        sample_rate: Audio sample rate
        n_fft: FFT window size
        hop_length: Hop length between frames
        
    Returns:
        Spectrogram as numpy array
    """
    # TODO: Implement proper spectrogram computation
    # For now, return dummy spectrogram
    num_frames = (len(audio_data) - n_fft) // hop_length + 1
    return np.random.randn(num_frames, n_fft // 2 + 1)


def detect_silence(audio_data: np.ndarray, 
                   threshold: float = 0.01) -> bool:
    """Detect if audio segment contains silence.
    
    Args:
        audio_data: Input audio data
        threshold: RMS threshold for silence detection
        
    Returns:
        True if audio is silence, False otherwise
    """
    rms = np.sqrt(np.mean(audio_data ** 2))
    return rms < threshold 