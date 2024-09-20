import pyttsx3
import PyPDF2

def speak(text):
    speaker = pyttsx3.init()
    speaker.setProperty('rate',120)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice',voices[1].id)
    speaker.say(text)
    speaker.runAndWait()
    
def read_pdf(file_path):
    try:
        #open the pdf file
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            #Iterate through the pages and rerad text
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                print(f"Regarding page {page_num + 1}...")
                speak(text)
    except Exception as e:
        print(f"An error occured: {e}")
        speak("Sorry, I couldn't read the pdf file.")
    
if __name__ == "__main__":
    file_path = r"C:\Users\syedr\OneDrive\Desktop\Ai_robot\Pellichoopulu_1.pdf"
    read_pdf(file_path)
