"""
Main entry point for the accent correction tool.
"""

import argparse
import sys
from pathlib import Path

from .utils.config import Config
from .utils.logger import setup_logging, get_logger
from .audio import AudioProcessor
from .models import AcousticModel, VADModel
from .feedback import FeedbackEngine
from .personalization import PersonalizationEngine


def main():
    """Main application entry point."""
    parser = argparse.ArgumentParser(description="Accent Correction Tool")
    parser.add_argument(
        "--config", 
        type=str, 
        default="config.yaml",
        help="Path to configuration file"
    )
    parser.add_argument(
        "--log-level", 
        type=str, 
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging level"
    )
    parser.add_argument(
        "--log-file", 
        type=str, 
        help="Log file path"
    )
    parser.add_argument(
        "--language", 
        type=str, 
        default="english",
        choices=["english", "arabic", "hebrew"],
        help="Target language"
    )
    parser.add_argument(
        "--mode", 
        type=str, 
        default="desktop",
        choices=["desktop", "web"],
        help="Application mode"
    )
    
    args = parser.parse_args()
    
    try:
        # Setup logging
        logger = setup_logging(args.log_level, args.log_file)
        logger.info("Starting Accent Correction Tool")
        
        # Load configuration
        config = Config(args.config)
        logger.info(f"Loaded configuration from {args.config}")
        
        # Initialize components
        logger.info("Initializing components...")
        
        # Audio processor
        audio_processor = AudioProcessor(config)
        logger.info("Audio processor initialized")
        
        # VAD model
        vad_model = VADModel(config)
        logger.info("VAD model initialized")
        
        # Acoustic model
        acoustic_model = AcousticModel(config)
        logger.info("Acoustic model initialized")
        
        # Feedback engine
        feedback_engine = FeedbackEngine(config)
        logger.info("Feedback engine initialized")
        
        # Personalization engine
        personalization_engine = PersonalizationEngine(config)
        logger.info("Personalization engine initialized")
        
        # Start the application
        logger.info(f"Starting in {args.mode} mode for {args.language}")
        
        if args.mode == "desktop":
            run_desktop_mode(
                config, 
                audio_processor, 
                vad_model, 
                acoustic_model, 
                feedback_engine, 
                personalization_engine,
                args.language
            )
        elif args.mode == "web":
            run_web_mode(
                config, 
                audio_processor, 
                vad_model, 
                acoustic_model, 
                feedback_engine, 
                personalization_engine,
                args.language
            )
        
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.exception(f"Application error: {e}")
        sys.exit(1)


def run_desktop_mode(config, audio_processor, vad_model, acoustic_model, 
                     feedback_engine, personalization_engine, language):
    """Run desktop mode application."""
    logger = get_logger("desktop")
    logger.info("Starting desktop mode")
    
    # TODO: Implement desktop GUI or CLI interface
    logger.info("Desktop mode not yet implemented")
    
    # For now, just run a simple test
    logger.info("Running basic functionality test...")
    
    # Test audio capture
    logger.info("Testing audio capture...")
    # audio_processor.test_capture()
    
    # Test VAD
    logger.info("Testing VAD...")
    # vad_model.test()
    
    # Test acoustic model
    logger.info("Testing acoustic model...")
    # acoustic_model.test()
    
    logger.info("Basic tests completed")


def run_web_mode(config, audio_processor, vad_model, acoustic_model, 
                 feedback_engine, personalization_engine, language):
    """Run web mode application."""
    logger = get_logger("web")
    logger.info("Starting web mode")
    
    # TODO: Implement web interface
    logger.info("Web mode not yet implemented")


if __name__ == "__main__":
    main() 