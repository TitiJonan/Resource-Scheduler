# Resource Scheduler App Documentation

## Overview
The **Resource Scheduler** is a Flask-based application designed to optimize employee allocation in a bank or call center. It assigns tasks to employees using scheduling algorithms like **Round Robin, Priority Scheduling, and Shortest Job Next**. The goal is to minimize customer wait times, maximize resource utilization, and ensure fair task distribution.

## Features
- **Dynamic Task Allocation**: Assigns employees to tasks based on availability and workload.
- **Scheduling Algorithms**:
  - Round Robin (equal distribution of tasks)
  - Priority Scheduling (VIP & Corporate customers prioritized)
  - Shortest Job Next (minimizes service delays)
- **Real-time Monitoring**: Tracks agent availability and workload, updating every 5 seconds.
- **Performance Metrics**:
  - Average customer waiting time
  - Agent utilization rate
  - Fairness in task distribution
- **Dockerized & Deployed using CI/CD** on Railway

---

## 1. Installation & Setup

### **Prerequisites**
- Python 3.10+
- Docker
- Railway account (for deployment)
- GitHub repository with CI/CD pipeline configured

### **Local Setup**
```sh
# Clone the repository
git clone https://github.com/your-repo/resource-scheduler.git
cd resource-scheduler

# Create a virtual environment & install dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run the application
python resource_scheduler.py
```

The app should now be running at **http://127.0.0.1:5000**.

---

## 2. API Endpoints

### **1. Home Route**
```http
GET /
```
**Response:**
```json
{"message": "Welcome to the Resource Scheduler API"}
```

### **2. Assign Task**
```http
POST /assign_task
```
**Request Body:**
```json
{
  "customer_id": 1,
  "priority": "VIP",
  "service_time": 5
}
```
**Response:**
```json
{"message": "Task assigned to Agent 2"}
```

### **3. Get Agent Status**
```http
GET /agents
```
**Response:**
```json
[
  {"agent_id": 1, "status": "Busy"},
  {"agent_id": 2, "status": "Free"}
]
```

---

## 3. Deployment
### **Using Docker**
```sh
# Build the Docker image
docker build -t resource-scheduler .

# Run the container
docker run -p 5000:5000 resource-scheduler
```
### **Using Railway**
1. Push changes to GitHub (`git push origin main`).
2. Railway automatically deploys using GitHub Actions.
3. Access the app at `https://your-app.up.railway.app/`.

---

## 4. CI/CD Pipeline
- **GitHub Actions** automates testing & deployment.
- **Docker Hub** stores container images.
- **Railway** deploys the latest version.

---

## 5. Contributors
- *Logonyi Nelson Emmanuel*
- *Ambasiize Titi Jonan*
