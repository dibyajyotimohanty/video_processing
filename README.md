# Video Processing Django Project

This project is a Django-based web application for uploading, processing videos, and extracting subtitles. It allows users to upload videos, process them to extract subtitles using `mkvextract`, search for phrases within videos, and retrieve timestamps where the phrases occur. It also supports Docker containerization for easy setup and deployment.

## Features

- **Video Upload**: Users can upload videos to the server.
- **Subtitle Extraction**: Extract subtitles from videos using `mkvextract` and store them in PostgreSQL.
- **Phrase Search**: Search for phrases within the subtitles and retrieve the corresponding timestamps.
- **List View**: View a list of uploaded videos with their subtitles and search functionality.

---

## Setup Instructions

### 1. Prerequisites

Before starting, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.x (optional if not using Docker)
- PostgreSQL (optional if not using Docker)

---

### 2. Clone the Repository

```bash
git clone https://github.com/dibyajyotimohanty/video_processing.git
cd video_processing
```


Docker Setup
Ensure Docker and Docker Compose are installed, then follow these steps to set up the project in a containerized environment.

a. Build and Run the Project

```bash
docker-compose up --build
```

This command will:

Build the Docker image for the web app and the PostgreSQL database.

Start the services.
b. Access the Web Application
Once the containers are running, you can access the application at:

http://localhost:8000


### Manual Setup Without Docker
If you want to run the project without Docker, follow these steps:

a. Create and Activate a Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
```

b. Install Dependencies
```bash
pip install -r requirements.txt
```

c. Set Up PostgreSQL
Install PostgreSQL and create a database with the following details:

```bash
Database: mydb
Username: myuser
Password: mypassword
```
Update the settings.py file with your database credentials if necessary.

d. Apply Migrations 

```bash
python manage.py migrate
```

e. Run the Development Server

```bash
python manage.py runserver
```

You can now access the web app at http://localhost:8000


### Project Structure
```bash
video-processing/
│
├───manage.py
├───docker-compose.yml
├───Dockerfile
├───ReadMe.md
├───requirements.txt
├───media
│   └───videos
├───Screenshot
├───videos
│   ├───migrations
│   │   └───__pycache__
│   ├───templates
│   │   └───videos
│   └───__pycache__
└───video_processing
    └───__pycache__
```

### Subtitles and Video Processing
**- Extracting Subtitles**
>We are using mkvextract to extract subtitles from video files. Ensure you have mkvtoolnix installed locally, or use the Docker container where the required tool is already set up.

**- Searching within Subtitles**
>Use the search functionality to query the subtitles database for phrases within videos. The search results will include the timestamp of the phrase in the video.

---
Note - The mp4 files provided were actually MKV files. Hence, to extract subtitles, I used `mkvextract` tool.
The required `ccextractor` tool was simply unable to extract the embedded subtitles, providing the reason that the video is actually an MKV file.