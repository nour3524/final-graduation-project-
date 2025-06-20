🔐 Insider Lens: Hybrid UEBA Insider Threat Detection System — Enterprise-Ready Prototype


⸻

📖 Project Overview

The Hybrid User and Entity Behavior Analytics (H-UEBA) Insider Threat Detection System is a fully functional, fully integrated academic prototype specifically designed for enterprise environments.

While not yet deployed in a real organization, this system provides a complete, ready-to-deploy architecture that can be adopted and extended by enterprises who wish to implement advanced insider threat detection.

⸻

🎯 Why Hybrid UEBA?

Insider threats represent one of the most serious risks to modern organizations — caused by employees, contractors, or partners who misuse legitimate access. Traditional perimeter security (firewalls, antivirus, IDS) offers little defense against malicious insiders who already have authorized credentials.

This system proposes a hybrid detection model that combines:
	•	✅ Continuous behavioral monitoring (logs + network activity)
	•	✅ Physical identity verification via face recognition
	•	✅ AI-powered real-time anomaly detection using Large Language Models (LLM)
	•	✅ Remote admin control via email approval for sensitive access

👉 This exact architecture can be adopted by companies seeking to upgrade their internal security posture.

⸻

💼 Who Can Benefit

This system is ideal for:
	•	Enterprises building insider threat monitoring platforms
	•	SOC (Security Operation Center) teams seeking new UEBA solutions
	•	Research labs validating hybrid AI + behavioral models
	•	Enterprise security architects designing future defense-in-depth systems

⸻

🔧 Why It Is Not Yet Deployed
	•	This system was developed inside a controlled academic environment.
	•	It is technically ready for enterprise deployment.
	•	Deployment was not performed due to:
	•	Lab resource limitations
	•	Organizational approvals
	•	Scope limitation (academic research boundaries)
	•	The full architecture, logic, and implementation are complete and available for direct adoption or customization by companies.

⸻

✅ Complete Features List

Feature	Description
OS Log Collection	Windows Security Events via WMI & NXLog
Network Monitoring	Live DNS queries, active connections
Multi-PC Log Forwarding	Multiple clients forward logs to centralized monitor
Centralized Detection	Real-time AI analysis using LLM (Ollama)
Face Recognition	Auto-lock/unlock PC via real-time face verification
Admin Approval Flow	Email-based remote access authorization
Centralized Database	SQL Server backend for full data retention & auditing


⸻

🏗 Full System Architecture

1️⃣ Log Collection
	•	Client PCs continuously collect:
	•	OS security logs
	•	Network activity logs

2️⃣ Log Forwarding
	•	Logs are automatically forwarded to a central monitoring server for real-time detection.

3️⃣ Real-Time Detection
	•	Ollama-powered LLM AI classifies incoming logs as malicious or normal behavior.

4️⃣ Physical Access Verification
	•	Face Recognition monitors who is physically present at the PC.
	•	Unauthorized faces trigger immediate access blocking.

5️⃣ Admin Approval
	•	Admin receives email notification with photo evidence.
	•	Admin can approve or deny the access remotely.

⸻

🗄 Database Design (SQL Server)
	•	Database: UEBA_Analytics

Tables:

Table	Purpose
Users	Stores authorized users & face encodings
HostLogs	Stores OS security logs
NetworkLogs	Stores network activity logs
MaliciousLogs	Stores detection results after AI classification

SQL Code Samples

Users Table

CREATE TABLE Users (
  id INT IDENTITY PRIMARY KEY,
  name NVARCHAR(100),
  email NVARCHAR(100),
  assigned_pc NVARCHAR(100),
  photo_path NVARCHAR(255),
  encoding_data VARBINARY(MAX)
)

HostLogs Table

CREATE TABLE HostLogs (
  id INT IDENTITY PRIMARY KEY,
  event_id NVARCHAR(50),
  event_type NVARCHAR(100),
  timestamp DATETIME,
  user NVARCHAR(100),
  log_data NVARCHAR(MAX)
)

NetworkLogs Table

CREATE TABLE NetworkLogs (
  id INT IDENTITY PRIMARY KEY,
  timestamp DATETIME,
  source_ip NVARCHAR(100),
  destination_ip NVARCHAR(100),
  dns_query NVARCHAR(255)
)

MaliciousLogs Table

CREATE TABLE MaliciousLogs (
  id INT IDENTITY PRIMARY KEY,
  timestamp DATETIME,
  log_content NVARCHAR(MAX),
  classification NVARCHAR(50),
  source NVARCHAR(50)
)


⸻

🗂 Full Repository Structure

UEBA-Hybrid-System/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── main.py                # Face recognition system launcher
├── db.py                  # Database connection module
├── detection.py           # Real-time LLM-based detection
├── auto_lock_unlock.py    # Face recognition auto-lock logic
├── create_encodings.py    # Face encoding generator
├── os_collector.py        # Host log collector
├── network_collector.py   # Network log collector
├── feature_selection_notebook.ipynb (research stage only)
│
├── haarcascade_frontalface_default.xml
├── dlib-19.24.1-cp311-cp311-win_amd64.whl
│
├── /known_faces/
├── /intruder_captures/
├── /logs/ (HostLogs, NetworkLogs, MaliciousLogs)


⸻

⚙ Full Installation Guide

1️⃣ Clone The Repository

git clone https://github.com/<your-repo>/UEBA-Hybrid-System.git
cd UEBA-Hybrid-System

2️⃣ Setup Python Environment

python -m venv venv
venv\Scripts\activate   (Windows)
source venv/bin/activate  (Linux/Mac)

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Install Dlib (Windows Only)

pip install dlib-19.24.1-cp311-cp311-win_amd64.whl

5️⃣ Install Ollama (LLM AI Engine)
	•	Download and install Ollama from: https://ollama.com
	•	Start Ollama server:

ollama run llama3


⸻

🚀 How To Run The System

Start Face Recognition System

python main.py

Start Log Collectors (On Client PCs)

python os_collector.py
python network_collector.py

Start Detection Engine (On Central Server)

python detection.py


⸻

📧 Email Notification Setup
	•	Edit your email credentials inside the code for admin alert:

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'your_admin_email'
MAIL_PASSWORD = 'your_app_password'

⚠ Use Google App Passwords for security.

⸻

📊 Datasets Used (For Initial Research Only)

While developing this system, the following datasets were used during the training phase for offline ML model evaluation:
	•	CICIDS 2017
	•	DARPA 1999

👉 Note: These datasets were only used during experimental development, and are NOT part of the live real-time detection system.

⸻

📜 License

Academic Research License

This system was developed as part of a Computer Science Graduation Project for research, educational, and academic demonstration only.
It provides an enterprise-ready architecture for companies wishing to implement advanced insider threat detection solutions.

⸻

🧠 Final Note

⚠ This system is not deployed in production — but fully designed for companies who wish to adopt, customize, and integrate it into their own enterprise environments.
⚠ The architecture, modules, detection flow, and real-time engine are fully operational within the lab environment, ready for corporate adaptation.

⸻

👨‍💻 Contributors
	•	Alaa Omar
	•	Nour Ehab
	•	Safeya Iyad 
	•	Salma Muhammed 
 
Supervised by:
	•	Dr. Mohamed El Emam
	•	Eng. Bassant Kassem
