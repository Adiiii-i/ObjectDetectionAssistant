@echo off
chcp 65001 >nul
echo 🤖 AI Object Detection Assistant - Installation Script
echo ======================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher first.
    echo 💡 Visit: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set python_version=%%i
echo ✅ Python %python_version% detected

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ pip is not installed. Please install pip first.
    pause
    exit /b 1
)

echo ✅ pip detected

REM Create virtual environment
echo.
echo 🔧 Setting up virtual environment...
python -m venv venv

REM Activate virtual environment
echo 📦 Activating virtual environment...
call venv\Scripts\activate.bat

echo ✅ Virtual environment created and activated

REM Upgrade pip
echo 📦 Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo 📥 Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Installation failed. Please check the error messages above.
    pause
    exit /b 1
)

echo.
echo 🎉 Installation completed successfully!
echo.
echo 🚀 To run the assistant:
echo    1. Activate the virtual environment:
echo       venv\Scripts\activate.bat
echo    2. Run the application:
echo       python app.py
echo.
echo 💡 For first run, make sure you have:
echo    • Camera access permissions
echo    • Internet connection (to download YOLOv8 model)
echo    • Text-to-speech enabled on your system
echo.
echo 📚 Check README.md for detailed usage instructions!
echo.
pause
