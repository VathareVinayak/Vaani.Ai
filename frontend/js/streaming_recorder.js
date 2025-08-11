// streaming_recorder.js

async function startStreamingRecording() {
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    alert("Your browser does not support audio recording.");
    return;
  }

  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  const mediaRecorder = new MediaRecorder(stream);

  mediaRecorder.start(2000); // chunk every 2 seconds

  mediaRecorder.ondataavailable = async (event) => {
    if (event.data.size > 0) {
      try {
        const response = await fetch("/api/stt_chunk", {
          method: "POST",
          body: event.data,
          headers: { "Content-Type": "audio/webm" },
        });

        const result = await response.json();
        console.log("Partial Transcription:", result.partial_transcription);
        console.log("Partial Translation:", result.partial_translation);

        // Update your UI with partial results here
        document.getElementById("partialTranscription").innerText = result.partial_transcription;
        document.getElementById("partialTranslation").innerText = result.partial_translation;

        // Optionally, you can play back partial TTS audio if implemented later
      } catch (error) {
        console.error("Error sending chunk:", error);
      }
    }
  };

  mediaRecorder.onstop = () => {
    console.log("Recording stopped.");
  };

  // For stopping recording, you may want to expose stop function externally:
  return mediaRecorder;
}
