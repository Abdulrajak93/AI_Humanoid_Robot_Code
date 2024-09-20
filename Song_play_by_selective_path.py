import pygame
import os
def play_mp3(file_path):
    pygame.mixer.init()
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return
    try:
        # load and play the MP3 file
        pygame.mixer.music.load(file_path)
        print(f"Playing {os.path.basename(file_path)}...")
        pygame.mixer.music.play()
        
        # wait for the music to finish playing2
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print(f"An error occured while playing the file: {e}")
    finally:
        #stop the music and quit pygame mixer
        pygame.mixer.music.stop()
        pygame.mixer.quit()
if __name__ == "__main__":
    mp3_file_path = r"C:\Users\syedr\OneDrive\Desktop\Ai_robot\pk.mp3"
    play_mp3(mp3_file_path)