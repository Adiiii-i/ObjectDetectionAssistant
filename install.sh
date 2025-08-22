#!/bin/bash

echo "🤖 AI Object Detection Assistant - Installation Script"
echo "======================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher first."
    echo "💡 Visit: https://www.python.org/downloads/"
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python version $python_version is too old. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python $python_version detected"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

echo "✅ pip3 detected"

# Create virtual environment (optional but recommended)
echo ""
echo "🔧 Setting up virtual environment..."
python3 -m venv venv

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

echo "✅ Virtual environment created and activated"

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Installation completed successfully!"
    echo ""
    echo "🚀 To run the assistant:"
    echo "   1. Activate the virtual environment:"
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        echo "      source venv/Scripts/activate"
    else
        echo "      source venv/bin/activate"
    fi
    echo "   2. Run the application:"
    echo "      python app.py"
    echo ""
    echo "💡 For first run, make sure you have:"
    echo "   • Camera access permissions"
    echo "   • Internet connection (to download YOLOv8 model)"
    echo "   • Text-to-speech enabled on your system"
    echo ""
    echo "📚 Check README.md for detailed usage instructions!"
else
    echo "❌ Installation failed. Please check the error messages above."
    exit 1
fi
