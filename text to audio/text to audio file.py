import pyttsx3
import PyPDF2

audio_reader = pyttsx3.init()
pdf_reader = PyPDF2.PdfReader('text.pdf', 'rb')
for i in range(len(pdf_reader.pages) ):
  text = pdf_reader.pages[i].extract_text()
  legible_text = text.strip().replace('\n',' ')
  #print(legible_text)

  # Queues the cleaned text to be spoken by the pyttsx3 engine
  audio_reader.say(legible_text)

# Processes all the queued speech commands (from audio_reader.say() and waits for them to complete.
audio_reader.runAndWait()
audio_reader.save_to_file(" ".join([pdf_reader.pages[i].extract_text().strip().replace('\n',' ') for i in range(len(pdf_reader.pages))]), 'file.mp3')
# Stops the pyttsx3 engine, releasing any resources it was using.
audio_reader.stop()