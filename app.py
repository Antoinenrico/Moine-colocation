import os
import RPi.GPIO as GPIO
import pygame, time
from random import *
from enum import Enum
from flask import Flask, render_template








app = Flask(__name__)

@app.route('/')
def index():
# this function plays some random animals noise when the webpage button
	return render_template('index.html')


@app.route('/moine')
def moine():
# this function plays some random animals noise when the webpage button
	randa=randint(0,len(fil)-1)
	pygame.mixer.music.load(PlaylistDrumset + fil[randa])
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() > 0:
		time.sleep(1)
	return render_template('index.html')
	
	
@app.route('/start')
def start():
    pygame.init()
    pygame.mixer.init() 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21,GPIO.IN) 
    #rondelle verte
    #GPIO.add_even_detect(21,GPIO.BOTH, callback=light_callback, bouncetime=75)   
    if GPIO.input(21)==0:
        print("coucou toua")
        light_callback()
    return render_template('index.html')


@app.route('/stop')
def stop():
    #GPIO.remove_even_detect(21)
    # Il connait pas cette commande
    pygame.quit()
    return render_template('index.html')

def liste_fichier_repertoire():
    fil = []
    fil = os.listdir("/home/pi/Desktop/Playlist/List")    
    return fil

def light_callback():
    if GPIO.input(21)==0:
        print("go moine")
        moine()
    else:
        pygame.mixer.music.stop()

if __name__ == '__main__':
    PlaylistDrumset= '/home/pi/Desktop/Playlist/List/'	
    fil = []
    fil = liste_fichier_repertoire()
    for i, f in enumerate(fil):
        print("fichier ", f)
        if i > 50:
            break
    app.run(debug=True, host='0.0.0.0')
