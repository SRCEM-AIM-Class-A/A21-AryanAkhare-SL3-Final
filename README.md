# FinalProject - Flask & Django Web Apps (Dockerized)

This project contains **two web applications**:

- 🧪 A simple **Flask** app (runs on port `5000`)
- 📦 A basic **Django** app (runs on port `8000`)

Both are containerized using **Docker Compose** for easy deployment on any machine.

---

## 🏗 Folder Structure

FinalProject/ │ ├── django_app/ │ ├── my_django_project_final/ │ ├── manage.py │ ├── requirements.txt │ └── Dockerfile │ ├── flask_app/ │ ├── app.py │ ├── requirements.txt │ ├── templates/ │ │ └── home.html │ ├── static/ │ │ └── style.css │ └── Dockerfile │ ├── docker-compose.yml └── README.md


---

## 🚀 How to Run the Project

### Prerequisites

- 🐳 [Docker](https://www.docker.com/products/docker-desktop) installed
- Docker Compose comes bundled with Docker Desktop

---

### Step-by-Step

1. **Clone the project**

```bash
git clone https://github.com/yourusername/FinalProject.git
cd FinalProject

docker-compose up --build
