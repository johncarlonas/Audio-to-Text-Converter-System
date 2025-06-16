const uploadForm = document.getElementById("uploadForm");
const audioInput = document.getElementById("audio");
const fileNameInput = document.getElementById("fileName");
const textArea = document.getElementById("text");
const loadingOverlay = document.getElementById("loadingOverlay");
const downloadBtn = document.getElementById("download");
const copyBtn = document.getElementById("copy");

let generatedText = "";

// Handle form submission
uploadForm.addEventListener("submit", async function (e) {
  e.preventDefault();

  const file = audioInput.files[0];
  const fileName = fileNameInput.value.trim() || "transcript";

  if (!file) {
    alert("Please choose an audio file.");
    return;
  }

  loadingOverlay.classList.remove("hidden");

  const formData = new FormData();
  formData.append("audio", file);
  formData.append("filename", fileName);

  try {
    const response = await fetch("/transcribe", {
      method: "POST",
      body: formData,
    });

    const text = await response.text();

    if (!response.ok || text.toLowerCase().startsWith("error")) {
      textArea.value = "Error: " + text;
    } else {
      textArea.value = text;
      generatedText = text;
    }
  } catch (err) {
    textArea.value = "Error: Could not upload or transcribe.";
    console.error(err);
  } finally {
    loadingOverlay.classList.add("hidden");
  }
});

// Download button
downloadBtn.addEventListener("click", () => {
  const filename = fileNameInput.value.trim();
  if (!generatedText || !filename) {
    alert("Make sure text is generated and a file name is provided.");
    return;
  }

  const blob = new Blob([generatedText], { type: "text/plain" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = filename + ".txt";
  link.click();
  URL.revokeObjectURL(link.href);
});

// Copy button
copyBtn.addEventListener("click", () => {
  navigator.clipboard.writeText(textArea.value)
    .then(() => alert("Copied to clipboard!"))
    .catch(() => alert("Failed to copy!"));
});
