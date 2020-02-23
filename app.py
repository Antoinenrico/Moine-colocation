Eimport RPi.GPIO as GPIO
import pygame
import time
import curses
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_BP_moine.html')

@app.route('/bonjour/<name>')
def hello(name):
    return render_template('page_nom.html', name=name)

@app.route('/moine')
def moine():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21,GPIO.IN) #rondelle verte

    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()

    ## Init
    ## Drumset index
    i = 0
    k = 0
    currentDrumset= '/home/pi/Desktop/a/rico'
    p = pygame.mixer.Sound(currentDrumset + '/Verg2.wav')    
    m = pygame.mixer.Sound(currentDrumset + '/Verg1.wav')
    z = pygame.mixer.Sound(currentDrumset + '/1.wav')
    e = pygame.mixer.Sound(currentDrumset + '/2.wav')    
    d = pygame.mixer.Sound(currentDrumset + '/3.wav')
    f = pygame.mixer.Sound(currentDrumset + '/5.wav')
    g = pygame.mixer.Sound(currentDrumset + '/4.wav')
    ## Screen display$
    print("ok avant test lum")
    while(k==0):
        while(i==0):
            ##print("ok dans la boucle while")
            if GPIO.input(21)==0:
                ## Update the song folder to the selected drum set
                print("m vaut moine")
                m.play()
                time.sleep(26)
                i=1;
        i=0;
        while(i==0):
            ##print("ok dans la boucle while")
            if GPIO.input(21)==0:
                ## Update the song folder to the selected drum set
                print("z vaut 1")
                z.play()
                time.sleep(46)
                i=1;
        i=0;
        while(i==0):
            ##print("ok dans la boucle while")
            if GPIO.input(21)==0:
                ## Update the song folder to the selected drum set
                print("e vaut 2")
                e.play()
                time.sleep(46)
                i=1;
        i=0;
        while(i==0):
            ##print("ok dans la boucle while")
            if GPIO.input(21)==0:
                ## Update the song folder to the selected drum set
                print("d vaut 3")
                d.play()
                time.sleep(46)
                i=1;
                k=1;
        while(i==0):
            ##print("ok dans la boucle while")
            if GPIO.input(21)==0:
                ## Update the song folder to the selected drum set
                print("f vaut 5")
                f.play()
                time.sleep(52)
                i=1;
                k=1;
        while(i==0):
            ##print("ok dans la boucle while")
            if GPIO.input(21)==0:
                ## Update the song folder to the selected drum set
                print("g vaut 4")
                g.play()
                time.sleep(52)
                i=1;
                k=1;
    while(k==0):
        while(i==0):
            ##print("ok dans la boucle while")
            if GPIO.input(21)==0:
                ## Update the song folder to the selected drum set
                print("p vaut le doigt")
                p.play()
                time.sleep(57)
                i=1;
        i=0;
    return render_template('index_BP_home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')