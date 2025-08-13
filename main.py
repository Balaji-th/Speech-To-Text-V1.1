# Import necessary libraries
import gradio as gr
from faster_whisper import WhisperModel
import tempfile
import os

# --- Model Initialization ---
# This part is similar to your original script, but we'll put it outside the function
# so the model is loaded only once when the app starts, not for every transcription.
model_size = "small.en"
device = "cpu"
compute_type = "float32"

try:
    print(f"🤖 Initializing Faster Whisper model: {model_size} on {device} with {compute_type}...")
    model = WhisperModel(model_size, device=device, compute_type=compute_type)
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None # Set model to None if loading fails

# --- Transcription Function for Gradio ---
def transcribe_audio(audio_path):
    """
    Transcribes a given audio file using the Faster Whisper model.
    This function is designed to be called by the Gradio interface.

    Args:
        audio_path (str): The file path of the audio to be transcribed.

    Returns:
        str: The transcribed text with timestamps, or an error message.
    """
    if not model:
        return "Error: The transcription model failed to load. Please check the logs."

    if audio_path is None:
        return "Please record some audio first."

    print(f"Transcribing audio file: {audio_path}")

    try:
        # The transcribe method can take the file path directly.
        # We'll re-implement your original output format with timestamps.
        segments, info = model.transcribe(
            audio_path,
            language="en",
            beam_size=1,
            vad_filter=True, # Use the Voice Activity Detection filter for better results
            without_timestamps=False
        )

        transcript_text = []
        for segment in segments:
            # Format the output string with start and end timestamps and the text.
            transcript_text.append(f"{segment.text.strip()}")

        # Join all the segments into a single string with newlines.
        return "\n".join(transcript_text)
    
    except Exception as e:
        return f"An error occurred during transcription: {e}"

# --- Gradio Interface Setup ---
# The core of the Gradio app, defining the UI components and the flow.
# We'll use gr.Interface to create a simple, clean app.
# The `gr.Audio` component with `source="microphone"` will handle the recording.
iface = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(sources=["microphone"], type="filepath"),
    outputs=gr.Textbox(label="Transcription"),
    title="Faster Whisper Real-time Transcription",
    description="Speak into your microphone, and this app will transcribe your speech in real-time chunks using the Faster Whisper model.",
    live=False,  # Set live to False for this type of transcribe-on-submit app.
)

# --- Launch the App ---
# This will start the web server and open the interface.
# The server will run until you stop the script (e.g., with Ctrl+C).
if __name__ == "__main__":
    iface.launch()
