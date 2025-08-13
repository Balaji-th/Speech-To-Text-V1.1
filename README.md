# Real-time Speech-to-Text with Faster Whisper & Gradio

This project is a simple yet powerful web application that transcribes audio from your microphone in real-time. It uses the highly optimized [Faster Whisper](https://github.com/guillaumekln/faster-whisper) model for fast and accurate speech-to-text conversion, with a user-friendly interface built with [Gradio](https://www.gradio.app/).

## Features

- **🎤 Real-time Transcription**: Record audio directly from your browser and get the transcription instantly.
- **🚀 Fast & Accurate**: Powered by `faster-whisper`, a reimplementation of OpenAI's Whisper model that is up to 4 times faster.
- **🗣️ Voice Activity Detection (VAD)**: Automatically detects speech, filtering out silent periods for cleaner and more accurate transcriptions.
- **🎨 Simple UI**: An intuitive and easy-to-use interface that requires no setup.

## How to Run the Application

To get this application running on your local machine, follow these simple steps.

### 1. Prerequisites

Make sure you have Python 3.8 or higher installed on your system.

### 2. Clone the Repository (Optional)

If you have downloaded the files, you can skip this step.

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 3. Install Dependencies

This project requires a few Python libraries. You can install them using pip:

```bash
pip install gradio faster_whisper torch
```

*Note: `torch` is required by the `faster-whisper` model.*

### 4. Run the Application

Once the dependencies are installed, you can start the application by running the `main.py` script:

```bash
python main.py
```

This will launch a local web server. Open your browser and navigate to the URL provided in the console (usually `http://127.0.0.1:7860`) to start using the application.

## Technologies Used

- **Python**: The core programming language.
- **Gradio**: For creating the simple and interactive web interface.
- **Faster Whisper**: For the high-performance speech-to-text model.
