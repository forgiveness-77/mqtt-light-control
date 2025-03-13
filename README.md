
# MQTT Light Control

A web-based application to control a light over MQTT. The system includes a web interface using MQTT.js to send ON/OFF commands and a Python script simulating an ESP8266 that listens and prints the light status.

---

## 📌 Project Overview
This project simulates controlling an IoT-based light system:
- **Web Interface**: Users can turn the light **ON** or **OFF** via buttons.
- **Simulated Device**: A Python script mimics an ESP8266, listening for MQTT messages and displaying the light status.

---

## 🛠️ Technologies Used
- **HTML/CSS/JavaScript** (for the web interface)
- **MQTT.js** (for MQTT communication over WebSockets)
- **Python (paho-mqtt)** (for simulating the IoT device)
- **Mosquitto MQTT Broker** (test.mosquitto.org)

---

## 📊 Project Structure

```bash
mqtt-light-control/ 
├── index.html # Web interface for controlling the light 
├── light_simulation.py # Simulated IoT device (ESP8266) using Python 
└── README.md # Project documentation
```


---

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/mqtt-light-control.git
cd mqtt-light-control
```

### 2. Run the Simulated IoT Device
Ensure Python is installed. Install paho-mqtt if needed:
```bash
pip install paho-mqtt
```
Then, run the script:
```bash
python light_simulation.py
```

### 3. Launch the Web Interface
-Open index.html in your browser.
-Click the Turn ON or Turn OFF buttons.
-The Python script should print:
```bash
Light is TURNED ON
Light is TURNED OFF
```
