import simpleaudio as sa

def alert():
        wave_obj = sa.WaveObject.from_wave_file("alert_sound.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        
        return "Alert sound played"
        
        
