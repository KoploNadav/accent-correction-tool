"""
Logging utilities for the accent correction tool.
"""

import logging
import sys
from pathlib import Path
from typing import Optional
from loguru import logger


class Logger:
    """Logging manager for the accent correction tool."""
    
    def __init__(self, log_level: str = "INFO", log_file: Optional[str] = None):
        """Initialize logger.
        
        Args:
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            log_file: Optional log file path
        """
        self.log_level = log_level
        self.log_file = log_file
        
        # Remove default handler
        logger.remove()
        
        # Add console handler
        logger.add(
            sys.stderr,
            level=log_level,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
                   "<level>{level: <8}</level> | "
                   "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
                   "<level>{message}</level>",
            colorize=True
        )
        
        # Add file handler if specified
        if log_file:
            log_path = Path(log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)
            logger.add(
                log_file,
                level=log_level,
                format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | "
                       "{name}:{function}:{line} - {message}",
                rotation="10 MB",
                retention="1 week"
            )
    
    def debug(self, message: str) -> None:
        """Log debug message."""
        logger.debug(message)
    
    def info(self, message: str) -> None:
        """Log info message."""
        logger.info(message)
    
    def warning(self, message: str) -> None:
        """Log warning message."""
        logger.warning(message)
    
    def error(self, message: str) -> None:
        """Log error message."""
        logger.error(message)
    
    def critical(self, message: str) -> None:
        """Log critical message."""
        logger.critical(message)
    
    def exception(self, message: str) -> None:
        """Log exception with traceback."""
        logger.exception(message)
    
    def success(self, message: str) -> None:
        """Log success message."""
        logger.success(message)
    
    def trace(self, message: str) -> None:
        """Log trace message."""
        logger.trace(message)
    
    def bind(self, **kwargs):
        """Bind contextual data to logger."""
        return logger.bind(**kwargs)
    
    def contextualize(self, **kwargs):
        """Create a contextualized logger."""
        return logger.bind(**kwargs)


# Global logger instance
_logger = Logger()


def get_logger(name: str = None) -> Logger:
    """Get logger instance.
    
    Args:
        name: Logger name (optional)
        
    Returns:
        Logger instance
    """
    if name:
        return _logger.bind(name=name)
    return _logger


def setup_logging(log_level: str = "INFO", log_file: Optional[str] = None) -> Logger:
    """Setup logging configuration.
    
    Args:
        log_level: Logging level
        log_file: Optional log file path
        
    Returns:
        Configured logger instance
    """
    global _logger
    _logger = Logger(log_level, log_file)
    return _logger 