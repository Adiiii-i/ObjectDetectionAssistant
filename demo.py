#!/usr/bin/env python3
"""
Demo Script for AI Object Detection Assistant
============================================

This script tests the core components without requiring camera access.
Useful for verifying your installation and testing individual features.
"""

import sys
import time

def test_imports():
    """Test if all required packages can be imported."""
    print("🧪 Testing package imports...")
    
    try:
        import cv2
        print("✅ OpenCV imported successfully")
    except ImportError as e:
        print(f"❌ OpenCV import failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ NumPy imported successfully")
    except ImportError as e:
        print(f"❌ NumPy import failed: {e}")
        return False
    
    try:
        from ultralytics import YOLO
        print("✅ Ultralytics imported successfully")
    except ImportError as e:
        print(f"❌ Ultralytics import failed: {e}")
        return False
    
    try:
        import pyttsx3
        print("✅ pyttsx3 imported successfully")
    except ImportError as e:
        print(f"❌ pyttsx3 import failed: {e}")
        return False
    
    try:
        from playsound import playsound
        print("✅ playsound imported successfully")
    except ImportError as e:
        print(f"❌ playsound import failed: {e}")
        return False
    
    return True

def test_yolo_model():
    """Test YOLO model loading."""
    print("\n🤖 Testing YOLO model...")
    
    try:
        from ultralytics import YOLO
        import torch
        print("🔄 Loading YOLOv8 model (this may take a moment on first run)...")
        
        # Try to load the model with weights_only=False for compatibility
        model = YOLO('yolov8n.pt')
        print("✅ YOLOv8 model loaded successfully!")
        
        # Test basic inference on a dummy image
        dummy_image = np.zeros((640, 640, 3), dtype=np.uint8)
        results = model(dummy_image, verbose=False)
        print("✅ Model inference test passed!")
        
        return True
        
    except Exception as e:
        print(f"❌ YOLO model test failed: {e}")
        print("💡 This might be a PyTorch compatibility issue. Let's try the main app instead.")
        return False

def test_voice_engine():
    """Test text-to-speech engine."""
    print("\n🗣️  Testing voice engine...")
    
    try:
        import pyttsx3
        
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        if voices:
            print(f"✅ Voice engine initialized with {len(voices)} voice(s)")
            print(f"   Available voices: {[v.name for v in voices]}")
        else:
            print("⚠️  Voice engine initialized but no voices found")
        
        # Test speech (optional)
        test_speech = input("\n🎤 Test speech? (y/n): ").lower().strip()
        if test_speech == 'y':
            print("🔊 Speaking test message...")
            engine.say("Hello! This is a test of the voice engine.")
            engine.runAndWait()
            print("✅ Speech test completed!")
        
        return True
        
    except Exception as e:
        print(f"❌ Voice engine test failed: {e}")
        print("💡 Voice might still work in the main app. Let's continue.")
        return False

def test_camera_access():
    """Test camera access (if available)."""
    print("\n📷 Testing camera access...")
    
    try:
        import cv2
        
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print(f"✅ Camera accessible! Frame size: {frame.shape}")
                cap.release()
                return True
            else:
                print("⚠️  Camera accessible but can't read frames")
                cap.release()
                return False
        else:
            print("⚠️  Camera not accessible (may be in use by another application)")
            return False
            
    except Exception as e:
        print(f"❌ Camera test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("=" * 60)
    print("🧪 AI Object Detection Assistant - System Test")
    print("=" * 60)
    
    all_tests_passed = True
    
    # Test imports
    if not test_imports():
        all_tests_passed = False
    
    # Test YOLO model
    if not test_yolo_model():
        all_tests_passed = False
    
    # Test voice engine
    if not test_voice_engine():
        all_tests_passed = False
    
    # Test camera access
    if not test_camera_access():
        print("⚠️  Camera test failed - this is normal if camera is in use")
        # Don't fail the overall test for camera issues
    
    # Summary
    print("\n" + "=" * 60)
    if all_tests_passed:
        print("🎉 All core tests passed! Your system is ready.")
        print("🚀 Run 'python app.py' to start the full application!")
    else:
        print("❌ Some tests failed. Please check the error messages above.")
        print("💡 Make sure all dependencies are installed correctly.")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
