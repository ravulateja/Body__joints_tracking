
#Real-Time Human Pose Detection using MediaPipe and OpenCV

A simple real-time human pose detection system built with MediaPipe, OpenCV, and Python. It captures video from your webcam and overlays human pose landmarks directly onto the video stream.

🔍 Features
Real-time human pose detection using MediaPipe Pose

Visualizes 33 key landmark points of the human body

Uses OpenCV to capture video and display output

Can be used as a base for posture analysis, fitness apps, gesture recognition, etc.

🛠️ Tech Stack
Python 3.x

OpenCV

MediaPipe

NumPy

TensorFlow (can be used later for model integration)

📦 Installation
Clone the repository:


git clone https://github.com/your-username/pose-detection-opencv-mediapipe.git
cd pose-detection-opencv-mediapipe
Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
🧪 Usage
Run the script using Python:


python pose_detection.py
A webcam window will open.

Press q to exit.

📁 File Structure

├── pose_detection.py       # Main script to run pose detection
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
🧠 How It Works
Captures webcam video frame by frame.

Uses MediaPipe’s Pose model to detect body landmarks.

Draws connections and landmarks on the frame using OpenCV.

Displays the processed frame in a real-time OpenCV window.



🔮 Future Work
Export pose data to CSV or DataFrame

Integrate a pose classification model using TensorFlow

Track and analyze posture over time

Add support for multiple persons

💡 Requirements

opencv-python
mediapipe
numpy
pandas
tensorflow
🤝 Contributing
Contributions are welcome! Please open an issue or pull request for improvements or bug fixes.

📄 License
This project is licensed under the MIT License. See LICENSE for more information.
