# 🤖 AI Object Detection Assistant

A **unique and intelligent** real-time camera object detection system that combines computer vision, voice feedback, and smart memory management. This isn't just another YOLO demo - it's a production-ready AI assistant that learns from your environment and provides contextual feedback.

## ✨ Unique Features

- **🎯 Real-time Detection**: Uses YOLOv8 for lightning-fast object recognition
- **🗣️ Voice Feedback**: Speaks object names when first detected
- **🧠 Smart Memory**: Remembers objects to avoid repetitive voice output
- **🔌 Special Alerts**: Unique charger detection with voice announcements
- **🎨 Modern UI**: Clean interface with confidence-based color coding
- **⚡ Performance Optimized**: Multi-threaded architecture for smooth operation

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Webcam (built-in or external)
- macOS, Windows, or Linux

### Installation

1. **Clone or download this project**
   ```bash
   # If you have git installed
   git clone <repository-url>
   cd newproj.py
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the assistant**
   ```bash
   python app.py
   ```

## 🎮 How to Use

### Basic Operation
1. **Start the application**: Run `python app.py`
2. **Allow camera access**: Grant permission when prompted
3. **Point camera at objects**: The AI will detect and label them
4. **Listen for voice feedback**: New objects will be announced
5. **Watch for special alerts**: Chargers get special treatment!

### Controls
- **`q`**: Quit the application
- **`s`**: Speak current status (object count in memory)

### Visual Indicators
- **🟢 Green boxes**: High confidence detections (>80%)
- **🟡 Yellow boxes**: Medium confidence detections (60-80%)
- **🔴 Red boxes**: Low confidence detections (<60%)

## 🔧 Technical Details

### Architecture
- **Main Thread**: Camera capture and display
- **AI Thread**: YOLO model inference
- **Voice Thread**: Text-to-speech processing
- **Memory System**: Object tracking with time-based expiration

### Memory System
- Objects are "remembered" for 10 seconds
- Voice feedback only occurs for newly detected objects
- Prevents repetitive announcements
- Tracks unique objects across detection sessions

### Special Features
- **Charger Detection**: Identifies phones, chargers, and related devices
- **Confidence Visualization**: Color-coded bounding boxes
- **Performance Monitoring**: Real-time FPS and memory tracking

## 📱 Supported Objects

The YOLOv8 model can detect **80+ common objects** including:
- People, animals, vehicles
- Electronics (phones, laptops, chargers)
- Furniture, appliances, food items
- And many more!

## 🛠️ Customization

### Adjusting Memory Duration
```python
# In app.py, modify this line:
self.memory_duration = 10  # Change to desired seconds
```

### Adding Custom Alerts
```python
# In _draw_detections method, add your own logic:
if "your_object" in class_name.lower():
    # Your custom handling here
    pass
```

### Changing Voice Settings
```python
# In _initialize_voice method:
self.voice_engine.setProperty('rate', 150)      # Speech speed
self.voice_engine.setProperty('volume', 0.8)    # Volume level
```

## 🔍 Troubleshooting

### Common Issues

**Camera not working?**
- Check camera permissions
- Ensure no other apps are using the camera
- Try different camera index (change `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`)

**Voice not working?**
- Install system text-to-speech engines
- On macOS: System Preferences → Accessibility → Speech
- On Windows: Settings → Time & Language → Speech

**Model loading slow?**
- First run downloads YOLOv8 weights (~6MB)
- Ensure stable internet connection
- Subsequent runs will be much faster

**Performance issues?**
- Reduce camera resolution in `_initialize_camera()`
- Use `yolov8n.pt` (nano) for speed, `yolov8s.pt` (small) for accuracy

### Performance Tips
- Close other applications using the camera
- Ensure good lighting for better detection
- Use USB 3.0 webcam for higher frame rates
- Adjust `memory_duration` based on your needs

## 🎯 Use Cases

- **Home Security**: Monitor entryways and valuable items
- **Accessibility**: Help visually impaired users identify objects
- **Smart Home**: Trigger actions based on object detection
- **Productivity**: Track workspace items and reminders
- **Education**: Learn object recognition and AI concepts

## 🔮 Future Enhancements

- **Gesture Recognition**: Control with hand movements
- **Object Tracking**: Follow objects across frames
- **Custom Models**: Train on your specific objects
- **Cloud Integration**: Save detection logs and analytics
- **Mobile App**: Remote monitoring and alerts

## 📚 Dependencies

- **ultralytics**: YOLOv8 object detection
- **opencv-python**: Computer vision and camera handling
- **pyttsx3**: Text-to-speech synthesis
- **playsound**: Audio playback for alerts
- **numpy**: Numerical computations
- **Pillow**: Image processing

## 🤝 Contributing

Feel free to enhance this project! Some ideas:
- Add support for custom object detection models
- Implement object counting and statistics
- Create a web interface for remote monitoring
- Add support for multiple cameras
- Implement object tracking across frames

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Ultralytics**: For the excellent YOLOv8 implementation
- **OpenCV**: For robust computer vision capabilities
- **pyttsx3**: For cross-platform text-to-speech

---

**Ready to experience the future of AI-powered object detection?** 🚀

Run `python app.py` and let your AI assistant guide you through the world of computer vision!
