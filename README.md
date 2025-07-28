# Accent Correction Tool

A real-time, on-device accent correction tool that helps users improve their pronunciation through phoneme-level feedback and personalized coaching.

## Features

- **Real-time phoneme detection**: Identifies pronunciation errors as you speak
- **Multi-language support**: English (General American), Palestinian Arabic, and Hebrew
- **Personalized feedback**: Adapts to your specific error patterns over time
- **Deep articulatory explanations**: Provides detailed guidance on tongue position, voicing, etc.
- **On-device processing**: Privacy-focused with no audio data sent to servers
- **Audio hints**: Native exemplars and corrective audio clips
- **Spaced repetition**: Intelligent drill scheduling based on your weak phonemes

## Architecture

### Core Components

1. **Voice Activity Detection (VAD)**: Silero VAD for real-time speech segmentation
2. **Acoustic Model**: wav2vec2-XLSR or Whisper for phoneme posterior extraction
3. **G2P (Grapheme-to-Phoneme)**: espeak-ng/phonemizer for reference phoneme sequences
4. **Alignment & Scoring**: CTC forced alignment or GOP (Goodness of Pronunciation) scoring
5. **Feedback Engine**: Rule-based articulatory guidance + TTS reference audio
6. **Personalization**: Confusion matrix tracking and spaced repetition scheduling

### Technical Stack

- **Audio Processing**: PyTorch, torchaudio, librosa
- **ASR**: Transformers, wav2vec2-XLSR, Whisper
- **VAD**: Silero VAD
- **G2P**: phonemizer, espeak-ng
- **TTS**: Coqui TTS (local)
- **Web Interface**: Flask (future)
- **Data Storage**: SQLite, JSON

## Project Structure

```
accent-correction-tool/
├── data/
│   ├── audio/           # Reference audio samples
│   ├── configs/         # Model configurations
│   └── models/          # Pre-trained models
├── docs/                # Documentation
├── src/
│   ├── audio/           # Audio processing modules
│   ├── feedback/        # Feedback generation
│   ├── models/          # ML models and scoring
│   ├── personalization/ # User adaptation
│   └── utils/           # Utilities
├── tests/               # Test suite
├── requirements.txt      # Python dependencies
├── setup.py            # Package setup
├── config.yaml         # Main configuration
└── README.md           # This file
```

## Installation

### Prerequisites

- Python 3.8+
- FFmpeg (for audio processing)
- espeak-ng (for G2P - install via system package manager)

### Quick Setup

**Option 1: Automated Setup (Recommended)**
```bash
git clone https://github.com/KoploNadav/accent-correction-tool.git
cd accent-correction-tool
./setup.sh
```

**Option 2: Manual Setup**

1. Clone the repository:
```bash
git clone https://github.com/KoploNadav/accent-correction-tool.git
cd accent-correction-tool
```

2. Install system dependencies:
```bash
# On macOS
brew install portaudio espeak-ng ffmpeg

# On Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y ffmpeg espeak-ng portaudio19-dev python3-dev

# On Windows (using chocolatey)
choco install ffmpeg espeak-ng
```

3. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Desktop Application

```bash
# Show help
python3 src/main.py --help

# Run in desktop mode (default)
python3 src/main.py --mode desktop --language english

# Run in web mode (future)
python3 src/main.py --mode web --language english
```

### Testing the Installation

```bash
# Run all tests
python3 -m pytest tests/ -v

# Test specific component
python3 -m pytest tests/test_config.py -v
```

## Configuration

Edit `config.yaml` to customize:

- Target languages and accents
- Model paths and settings
- Feedback preferences
- Personalization parameters

## Development

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black src/
flake8 src/
```

### Type Checking

```bash
mypy src/
```

## Roadmap

### Milestone 0 (1-2 weeks)
- [ ] Desktop prototype (English only)
- [ ] Basic phoneme scoring
- [ ] Post-utterance feedback

### Milestone 1 (2-4 weeks)
- [ ] Real-time chunking
- [ ] Palestinian Arabic and Hebrew support
- [ ] Personal confusion matrix

### Milestone 2 (4-8 weeks)
- [ ] Open-ended conversation mode
- [ ] Basic prosody detection
- [ ] Progress reports

### Milestone 3 (Web version)
- [ ] WebAssembly port
- [ ] Web interface
- [ ] Cloud fallback options

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details.