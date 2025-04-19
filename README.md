# Final Project - Dockerized Flask and Django Applications

This project contains two separate web applications — one built using **Flask** and the other using **Django** — both containerized with Docker and managed via Docker Compose.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/SRCEM-AIM-Class-A/A21-AryanAkhare-SL3-Final.git
cd A21-AryanAkhare-SL3-Final
```

### 2. Download Requirements

To ensure all dependencies are available, download the requirements for both applications:

- **Flask App**:

  ```bash
  pip install -r requirements.txt
  ```

- **Django App**:

  ```bash
  pip install -r my_django_project_final/requirements.txt
  ```

### 3. Build and Run the Containers

Use Docker Compose to build and start both apps:

```bash
docker-compose up --build
```

This will:

- Build the Docker images for Flask and Django apps.
- Start both apps in separate containers.

### 🌐 Accessing the Applications

After running, visit these links in your local browser:

| Application | URL | Port |
| --- | --- | --- |
| Flask App | http://localhost:5000 | 5000 |
| Django App | http://localhost:8000 | 8000 |

⚠️ Even if the terminal/logs show `0.0.0.0` or `172.x.x.x`, you should open `localhost` in your browser. Docker maps the container ports to your local machine.

### 🐳 Docker Hub Images

Docker images are also available publicly:

- **Flask App**: `aryanakhare/finalproject-flask_app_final`
- **Django App**: `aryanakhare/finalproject-django_app_final`

To pull them manually:

```bash
docker pull aryanakhare/finalproject-flask_app_final
docker pull aryanakhare/finalproject-django_app_final
```

### 🛑 Stopping & Cleaning Up

To stop the containers:

```bash
CTRL + C
```

To stop and remove everything cleanly:

```bash
docker-compose down
```

### 👤 Author

- **Aryan Akhare**
- SL3 Final Project – AIM Class A
- GitHub: @aryanakhare