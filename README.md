# Music Genre Classifier

This project is a music genre classification web application. It utilizes Support Vector Machine (SVM) for audio files and VGG19 model for image files to predict the genre of the input.

## Features

- Music genre classification for audio files (SVM)
- Music genre classification for image files (VGG19)
- User-friendly web interface

## Project Structure

The repository is organized as follows:

- `my_app/`: Front-end application
- `svm_service/`: SVM classifier service
- `vgg19_service/`: VGG19 classifier service
- `tests/`: Tests for both SVM and VGG19 services
- `docker-compose.yml`: Docker Compose configuration
- `Jenkinsfile`: Jenkins pipeline script
- `requirements.txt`: Python dependencies
- `test-reports/`: JUnit test reports

### Prerequisites

Make sure you have the following tools installed:

- Docker
- Python 3.8

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/music-genre-classifier.git
   cd music-genre-classifier

2. Build the Docker containers:
   ```bash
   docker-compose up --build -d

3. Access the application at http://localhost:3000

## Usage

### Uploading a Music File

1. Open the web application.
2. Click on the "Choose a music file" button.
3. Select an audio file (WAV format).
4. Click "Upload and Classify."

### Uploading an Image File

1. Open the web application.
2. Click on the "Choose an image file" button.
3. Select an image file (PNG format).
4. Click "Upload and Classify."