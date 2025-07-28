"""
Configuration management for the accent correction tool.
"""

import os
import yaml
from pathlib import Path
from typing import Dict, Any, Optional


class Config:
    """Configuration manager for the accent correction tool."""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize configuration.
        
        Args:
            config_path: Path to configuration file. Defaults to 'config.yaml'.
        """
        if config_path is None:
            config_path = "config.yaml"
        
        self.config_path = Path(config_path)
        self.config = self._load_config()
        
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        
        with open(self.config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        return config
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value using dot notation.
        
        Args:
            key: Configuration key (e.g., 'audio.sample_rate')
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value using dot notation.
        
        Args:
            key: Configuration key (e.g., 'audio.sample_rate')
            value: Value to set
        """
        keys = key.split('.')
        config = self.config
        
        # Navigate to the parent of the target key
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        # Set the value
        config[keys[-1]] = value
    
    def save(self) -> None:
        """Save current configuration to file."""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            yaml.dump(self.config, f, default_flow_style=False, indent=2)
    
    def get_audio_config(self) -> Dict[str, Any]:
        """Get audio processing configuration."""
        return self.get('audio', {})
    
    def get_language_config(self, language: str) -> Dict[str, Any]:
        """Get configuration for a specific language."""
        return self.get(f'languages.{language}', {})
    
    def get_model_config(self, model_type: str) -> Dict[str, Any]:
        """Get configuration for a specific model type."""
        return self.get(f'models.{model_type}', {})
    
    def get_scoring_config(self) -> Dict[str, Any]:
        """Get scoring configuration."""
        return self.get('scoring', {})
    
    def get_feedback_config(self) -> Dict[str, Any]:
        """Get feedback configuration."""
        return self.get('feedback', {})
    
    def get_personalization_config(self) -> Dict[str, Any]:
        """Get personalization configuration."""
        return self.get('personalization', {})
    
    def get_storage_config(self) -> Dict[str, Any]:
        """Get storage configuration."""
        return self.get('storage', {})
    
    def get_debug_config(self) -> Dict[str, Any]:
        """Get debug configuration."""
        return self.get('debug', {})
    
    def get_performance_config(self) -> Dict[str, Any]:
        """Get performance configuration."""
        return self.get('performance', {})
    
    def is_language_enabled(self, language: str) -> bool:
        """Check if a language is enabled."""
        return self.get(f'languages.{language}.enabled', False)
    
    def get_enabled_languages(self) -> list:
        """Get list of enabled languages."""
        languages = self.get('languages', {})
        return [lang for lang, config in languages.items() 
                if config.get('enabled', False)]
    
    def get_data_path(self, subpath: str = "") -> Path:
        """Get data directory path."""
        data_path = Path("data") / subpath
        data_path.mkdir(parents=True, exist_ok=True)
        return data_path
    
    def get_model_path(self, model_name: str) -> Path:
        """Get model file path."""
        return self.get_data_path("models") / model_name
    
    def get_audio_path(self, subpath: str = "") -> Path:
        """Get audio directory path."""
        return self.get_data_path("audio") / subpath 