#!/bin/bash

# Accent Correction Tool Setup Script
# This script sets up the development environment for the accent correction tool

set -e  # Exit on any error

echo "🎤 Setting up Accent Correction Tool..."

# Check if we're on macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "📱 Detected macOS"
    
    # Check if Homebrew is installed
    if ! command -v brew &> /dev/null; then
        echo "❌ Homebrew is not installed. Please install it first:"
        echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        exit 1
    fi
    
    echo "🍺 Installing system dependencies..."
    brew install portaudio espeak-ng ffmpeg
    
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "🐧 Detected Linux"
    
    # Check if apt is available (Ubuntu/Debian)
    if command -v apt &> /dev/null; then
        echo "📦 Installing system dependencies..."
        sudo apt-get update
        sudo apt-get install -y ffmpeg espeak-ng portaudio19-dev python3-dev
    else
        echo "⚠️  Please install the following system dependencies manually:"
        echo "   - ffmpeg"
        echo "   - espeak-ng"
        echo "   - portaudio"
        echo "   - python3-dev"
    fi
else
    echo "⚠️  Unsupported OS. Please install dependencies manually."
fi

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install it first."
    exit 1
fi

echo "🐍 Python 3 found: $(python3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Run tests to verify installation
echo "🧪 Running tests..."
python3 -m pytest tests/ -v

echo "✅ Setup complete!"
echo ""
echo "🎉 Accent Correction Tool is ready to use!"
echo ""
echo "To run the application:"
echo "  source venv/bin/activate"
echo "  python3 src/main.py --help"
echo ""
echo "To run tests:"
echo "  python3 -m pytest tests/ -v"
echo ""
echo "Repository: https://github.com/KoploNadav/accent-correction-tool" 