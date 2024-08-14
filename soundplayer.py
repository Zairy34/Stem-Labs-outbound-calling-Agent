import pygame
import os

class SoundInit:
    def __init__(self,path_mp3file) -> None:
        self.path_mp3file = path_mp3file
        pygame.mixer.init()
    
    def play_sound(self, file_name):
        try:
            pygame.mixer.music.load(os.path.join(self.path_mp3file, file_name))
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except Exception as e:
            print(f"Error playing {file_name}: {e}")
            
            
            
    def run(self):
        files = os.listdir(self.path_mp3file)
        for file in files:
                self.play_sound(file)
        
if __name__ == "__main__":
   pass
    
    
    
