
# from pyvirtualdisplay import Display

# # Start a virtual display
# virtual_display = Display(visible=0, size=(800, 600))  
# virtual_display.start()


import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from random import uniform

# Load historical data from Excel to train the model
data = pd.read_excel('/Users/yash/Desktop/Road To Placement/Project/MoistureDataset.xlsx')

# Ensure the 'Humidity (%)' column is present
if 'Humidity (%)' not in data.columns:
    raise KeyError("The dataset does not contain a 'Humidity (%)' column.")

# Extract the moisture readings and train the Isolation Forest
moisture = data['Humidity (%)'].values.reshape(-1, 1)
iso_forest = IsolationForest(contamination=0.05, random_state=42)
iso_forest.fit(moisture)
print("Isolation Forest model trained on historical data.")

# Function to simulate real-time sensor reading.
def read_sensor():
    # Simulate normal moisture readings between 40 and 90.
    # Occasionally simulate an anomaly (e.g., values above 90).
    val = uniform(40, 90)
    if np.random.rand() < 0.2:  # 10% chance to simulate an anomaly
        val = uniform(91, 120)
    return val

# Tkinter-based UI for real-time monitoring
class MoistureApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Real-Time Furniture Moisture Detection")
        self.geometry("400x200")
        self.running = False
        
        # Title label
        self.label_title = tk.Label(self, text="Real-Time Moisture Monitoring", font=("Arial", 16))
        self.label_title.pack(pady=10)
        
        # Current moisture reading label
        self.label_moisture = tk.Label(self, text="Current Moisture: --", font=("Arial", 14))
        self.label_moisture.pack(pady=5)
        
        # Status label (Normal/Anomaly)
        self.label_status = tk.Label(self, text="Status: --", font=("Arial", 14))
        self.label_status.pack(pady=5)
        
        # Start/Stop monitoring button
        self.btn_toggle = tk.Button(self, text="Start Monitoring", command=self.toggle_monitoring)
        self.btn_toggle.pack(pady=10)
    
    def toggle_monitoring(self):
        if not self.running:
            self.running = True
            self.btn_toggle.config(text="Stop Monitoring")
            self.update_reading()
        else:
            self.running = False
            self.btn_toggle.config(text="Start Monitoring")
    
    def update_reading(self):
        if self.running:
            current_moisture = read_sensor()
            prediction = iso_forest.predict([[current_moisture]])
            status = 'Normal' if prediction[0] == 1 else 'Anomaly'
            
            # Update UI labels with the latest reading and status
            self.label_moisture.config(text=f"Current Moisture: {current_moisture:.2f}")
            self.label_status.config(text=f"Status: {status}")
            if status == 'Anomaly':
                self.label_status.config(fg="red")
                print("ALARM: Excess moisture detected!")  # Replace with actual alarm/notification if needed
            else:
                self.label_status.config(fg="green")
            
            # Schedule the next sensor reading update after 2000 ms (2 seconds)
            self.after(2000, self.update_reading)

if __name__ == "__main__":
    import sys
    if sys.platform == "darwin":  # Check if running on macOS
        import os
        os.system("defaults write org.python.python ApplePersistenceIgnoreState NO")

    app = MoistureApp()
    app.mainloop()

