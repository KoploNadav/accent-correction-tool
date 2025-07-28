"""
Tests for configuration management.
"""

import pytest
from pathlib import Path
from src.utils.config import Config


class TestConfig:
    """Test cases for Config class."""
    
    def test_config_loading(self):
        """Test that configuration loads correctly."""
        config = Config("config.yaml")
        assert config.config is not None
        assert isinstance(config.config, dict)
    
    def test_get_value(self):
        """Test getting configuration values."""
        config = Config("config.yaml")
        
        # Test existing value
        sample_rate = config.get("audio.sample_rate")
        assert sample_rate == 16000
        
        # Test non-existent value with default
        non_existent = config.get("non.existent", "default")
        assert non_existent == "default"
    
    def test_set_value(self):
        """Test setting configuration values."""
        config = Config("config.yaml")
        
        # Set a new value
        config.set("test.value", "test_value")
        assert config.get("test.value") == "test_value"
        
        # Update existing value
        config.set("audio.sample_rate", 22050)
        assert config.get("audio.sample_rate") == 22050
    
    def test_language_config(self):
        """Test language configuration methods."""
        config = Config("config.yaml")
        
        # Test enabled languages
        enabled = config.get_enabled_languages()
        assert "english" in enabled
        
        # Test language enabled check
        assert config.is_language_enabled("english") is True
    
    def test_path_methods(self):
        """Test path-related methods."""
        config = Config("config.yaml")
        
        # Test data path
        data_path = config.get_data_path()
        assert data_path.exists() or data_path.parent.exists()
        
        # Test model path
        model_path = config.get_model_path("test_model")
        assert "test_model" in str(model_path)
        
        # Test audio path
        audio_path = config.get_audio_path("samples")
        assert "samples" in str(audio_path) 