"""
Real-Time Camera Object Detection Assistant
==========================================

A unique AI-powered assistant that detects objects in real-time using your webcam,
provides voice feedback, maintains memory of detected objects, and includes
special alerts for specific items like chargers.

Features:
- Real-time object detection using YOLOv8
- Voice feedback for newly detected objects
- Memory system to avoid repetitive voice output
- Special alerts for chargers
- Clean, modern UI with bounding boxes and confidence scores
"""

import cv2
import numpy as np
import time
import threading
import queue
import os
from datetime import datetime, timedelta
from ultralytics import YOLO
import pyttsx3
from playsound import playsound
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

class ObjectDetectionAssistant:
    def __init__(self):
        """Initialize the Object Detection Assistant with all components."""
        self.model = None
        self.cap = None
        self.voice_engine = None
        self.detection_memory = {}  
        self.memory_duration = 10  
        self.voice_queue = queue.Queue()
        self.is_running = False
        self.charger_alert_cooldown = 0
        self.charger_alert_duration = 5 
        
        # Initialize components
        self._initialize_model()
        self._initialize_voice()
        self._initialize_camera()
    
        self.voice_thread = threading.Thread(target=self._voice_worker, daemon=True)
        self.voice_thread.start()
    
    def _initialize_model(self):
        """Initialize YOLOv8 model for object detection."""
        try:
            print("🔄 Loading YOLOv8 model...")
            self.model = YOLO('yolov8n.pt')  
            print("✅ YOLOv8 model loaded successfully!")
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            print("💡 Make sure you have internet connection for first run")
            print("💡 If the issue persists, try updating PyTorch or ultralytics")
            exit(1)
    
    def _initialize_voice(self):
        """Initialize text-to-speech engine."""
        try:
            self.voice_engine = pyttsx3.init()
           
            voices = self.voice_engine.getProperty('voices')
            if voices:
                self.voice_engine.setProperty('voice', voices[0].id) 
            self.voice_engine.setProperty('rate', 150)  
            self.voice_engine.setProperty('volume', 0.8) 
            print("✅ Voice engine initialized!")
        except Exception as e:
            print(f"⚠️  Voice initialization failed: {e}")
            self.voice_engine = None
    
    def _initialize_camera(self):
        """Initialize webcam capture."""
        try:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                raise Exception("Could not open camera")
            
            
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cap.set(cv2.CAP_PROP_FPS, 30)
            
            print("✅ Camera initialized successfully!")
        except Exception as e:
            print(f"❌ Camera initialization failed: {e}")
            exit(1)
    
    def _voice_worker(self):
        """Background thread for processing voice commands."""
        while self.is_running:
            try:
                if not self.voice_queue.empty():
                    text = self.voice_queue.get(timeout=1)
                    if self.voice_engine:
                        self.voice_engine.say(text)
                        self.voice_engine.runAndWait()
                time.sleep(0.1)
            except queue.Empty:
                continue
            except Exception as e:
                print(f"⚠️  Voice error: {e}")
    
    def _should_speak(self, object_name):
        """Check if we should speak the object name based on memory."""
        current_time = datetime.now()
        
        if object_name in self.detection_memory:
            time_diff = current_time - self.detection_memory[object_name]
            if time_diff.total_seconds() < self.memory_duration:
                return False
        
        # Update memory
        self.detection_memory[object_name] = current_time
        return True
    
    def _handle_charger_detection(self, frame):
        """Handle special charger detection with visual and audio alerts."""
        current_time = time.time()
        
        if current_time - self.charger_alert_cooldown > self.charger_alert_duration:
            self.charger_alert_cooldown = current_time
            
            
            cv2.putText(frame, "🔌 CHARGER DETECTED!", (50, 50), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            
            
            try:
               
                pass
            except:
                pass
            
    
            if self.voice_engine:
                self.voice_queue.put("Charger detected! Please connect your device.")
    
    def _draw_detections(self, frame, results):
        """Draw bounding boxes and labels on the frame."""
        for result in results:
            boxes = result.boxes
            if boxes is not None:
                for box in boxes:
                    # Get box coordinates
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    
                  
                    conf = float(box.conf[0])
                    cls = int(box.cls[0])
                    class_name = result.names[cls]
                    
                   
                    if conf > 0.8:
                        color = (0, 255, 0)  
                    elif conf > 0.6:
                        color = (0, 255, 255)  
                    else:
                        color = (0, 0, 255)  
                    
                  
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    
                  
                    label = f"{class_name}: {conf:.2f}"
                    
                    
                    (label_width, label_height), _ = cv2.getTextSize(
                        label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2
                    )
                    
                   
                    cv2.rectangle(frame, (x1, y1 - label_height - 10), 
                                (x1 + label_width, y1), color, -1)
                    
                   
                    cv2.putText(frame, label, (x1, y1 - 5), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                    
                    
                    if self._should_speak(class_name):
                        if self.voice_engine:
                            self.voice_queue.put(f"I see a {class_name}")
                    
                    
                    if "charger" in class_name.lower() or "cell phone" in class_name.lower():
                        self._handle_charger_detection(frame)
    
    def _add_ui_overlay(self, frame):
        """Add UI elements and status information to the frame."""
       
        cv2.putText(frame, "AI Object Detection Assistant", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
       
        cv2.putText(frame, "Press 'q' to quit, 's' to speak status", (10, frame.shape[0] - 20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
        
      
        memory_count = len(self.detection_memory)
        cv2.putText(frame, f"Objects in memory: {memory_count}", (10, frame.shape[0] - 40), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
        
       
        timestamp = datetime.now().strftime("%H:%M:%S")
        cv2.putText(frame, timestamp, (frame.shape[1] - 100, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)
    
    def run(self):
        """Main detection loop."""
        self.is_running = True
        print("🚀 Starting Object Detection Assistant...")
        print("📱 Press 'q' to quit, 's' to speak current status")
        print("🎯 Special alert: Charger detection with voice announcement")
        
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    print("❌ Failed to read frame from camera")
                    break
                
               
                results = self.model(frame, verbose=False)
                
                
                self._draw_detections(frame, results)
                
                
                self._add_ui_overlay(frame)
                
               
                cv2.imshow('AI Object Detection Assistant', frame)
                
               
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('s'):
                    
                    if self.voice_engine:
                        memory_count = len(self.detection_memory)
                        status_msg = f"Currently tracking {memory_count} objects in memory"
                        self.voice_queue.put(status_msg)
                
               
                time.sleep(0.01)
                
        except KeyboardInterrupt:
            print("\n⚠️  Interrupted by user")
        except Exception as e:
            print(f"❌ Error in main loop: {e}")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources."""
        print("🧹 Cleaning up...")
        self.is_running = False
        
        if self.cap:
            self.cap.release()
        
        cv2.destroyAllWindows()
        
        if self.voice_engine:
            self.voice_engine.stop()
        
        print("✅ Cleanup complete!")

def main():
    """Main entry point."""
    print("=" * 60)
    print("🤖 AI Object Detection Assistant")
    print("=" * 60)
    print("This assistant will:")
    print("• Detect objects in real-time using your webcam")
    print("• Provide voice feedback for new objects")
    print("• Remember objects to avoid repetitive speech")
    print("• Give special alerts for chargers")
    print("=" * 60)
    
    try:
        assistant = ObjectDetectionAssistant()
        assistant.run()
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        print("💡 Make sure all dependencies are installed correctly")

if __name__ == "__main__":
    main()
