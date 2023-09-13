@echo off
echo Serial2CSV - Setup Script
echo Author: Sukarna Jana
echo Version: 0.0.1V
echo Last Update: 13-09-2023
echo.

setlocal enabledelayedexpansion

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    python3 --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo Python is not installed. Please install Python and try again.
        pause
        exit /b 1
    )
)

REM Try to install packages using pip
pip install -r requirements.txt >nul 2>&1
if %errorlevel% neq 0 (
    REM If pip fails, try pip3
    pip3 install -r requirements.txt >nul 2>&1
    if %errorlevel% neq 0 (
        echo Failed to install required packages.
        pause
        exit /b 1
    )
)

echo Packages installed successfully.
pause
exit /b 0
