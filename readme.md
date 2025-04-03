Furniture Moisture Detection System

Overview:
The Furniture Moisture Detection System is a real-time monitoring application that detects abnormal moisture levels in furniture using machine learning. The system utilizes an Isolation Forest model trained on historical moisture data to identify anomalies and provides a Tkinter-based GUI for live monitoring.

Features:
- Real-time moisture monitoring with simulated sensor readings.
- Machine learning-based anomaly detection using Isolation Forest.
- User-friendly GUI built with Tkinter.
- Alerts for abnormal moisture levels to indicate potential furniture damage.

Installation:

1. Clone the Repository:
   git clone https://github.com/yashsiwacha/moisture-detection.git
   cd moisture-detection

2. Install Dependencies:
   Ensure you have Python 3.12+ installed, then run:
   pip install -r requirements.txt

3. Run the Application:
   python moisture.py

File Structure:
moisture-detection
│── moisture.py            # Main application script
│── MoistureDataset.xlsx   # Historical moisture data (for training)
│── requirements.txt       # Required dependencies
│── README.txt             # Project documentation

How It Works:
1. Data Training: The app loads historical moisture data from MoistureDataset.xlsx and trains an Isolation Forest model.
2. Real-time Monitoring: The system simulates sensor readings and classifies each reading as normal or anomalous.
3. User Interface: A Tkinter GUI displays the moisture levels and highlights anomalies in red.

Future Enhancements:
- Integration with actual moisture sensors.
- Cloud-based storage & analytics using AWS IoT.
- Mobile app for remote monitoring.

License:
This project is licensed under the MIT License.

Developed by Yash Siwach
