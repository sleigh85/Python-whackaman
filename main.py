import tkinter

import customtkinter
from tkinter import *
from PIL import Image
import random
from time import *
import threading
import pygame


width = 1440
height = 900
score = 0
bush = 0
highscore = 0
countdown = 30

#screen set up-->

#size, title, theme & background
customtkinter.set_default_color_theme('blue')
customtkinter.set_appearance_mode('dark')

app = customtkinter.CTk()
app.geometry('1440x900')
bg = customtkinter.CTkImage(Image.open('bluebg.png'), size=(width, height))
Home_screen = customtkinter.CTkLabel(app, image=bg, text='')
Home_screen.place(relx=0.5, rely=0.5, anchor=CENTER)

app.title('Whack-a-Man')

#start button
def start_game():
    bg_music.play()
    global score
    score = 0
    score_label.configure(text=f'Score:{score}')
    start_btn.place_forget()
    t = threading.Thread(target=whac_a_man)
    t.start()

start_btn = customtkinter.CTkButton(
    master=Home_screen,
    text='Start',
    command=start_game,
    width=80,
    height=60,
    border_width=5,
    corner_radius=20,
    border_spacing=5,
    fg_color='#f61f12',
    border_color='#0A0201',
    text_color='#ffffff',
    font=("Oswald", 25),
    hover=False
)
start_btn.place(x=600, y=50)

#counter
my_counter = customtkinter.CTkLabel(
    master=Home_screen,
    font=("PokemonGB", 30),
    text=f'Men left:{countdown}'
)

#scoreboard
score_label = customtkinter.CTkLabel(
    master=Home_screen,
    text=f'Score:{score}',
    bg_color='#1b31be',
    width=220,
    height=50,
    text_color='#ffffff',
    font=("PokemonGB", 25)
)
score_label.place(x=110, y=50)


#highscore
hs_board = customtkinter.CTkLabel(
    master=Home_screen,
    text=f'High Score:{highscore}',
    bg_color='#1b31be',
    width=220,
    height=50,
    text_color='#ffffff',
    font=("PokemonGB", 25)
)
hs_board.place(x=960, y=50)

#bushes setup
a_bush = customtkinter.CTkImage(Image.open('bush.png'), size=(125, 125))
bush1 = customtkinter.CTkLabel(app, image=a_bush, fg_color='#9fc5e8', text='')
bush1.place(x=280, y=260)
bush2 = customtkinter.CTkLabel(app, image=a_bush, text='', fg_color='#9fc5e8')
bush2.place(x=620, y=260)
bush3 = customtkinter.CTkLabel(app, image=a_bush, text='', fg_color='#9fc5e8')
bush3.place(x=1000, y=260)
bush4 = customtkinter.CTkLabel(app, image=a_bush, text='', fg_color='#9fc5e8')
bush4.place(x=100, y=560)
bush5 = customtkinter.CTkLabel(app, image=a_bush, text='', fg_color='#9fc5e8')
bush5.place(x=450, y=560)
bush6 = customtkinter.CTkLabel(app, image=a_bush, text='', fg_color='#9fc5e8')
bush6.place(x=800, y=560)
bush7 = customtkinter.CTkLabel(app, image=a_bush, text='', fg_color='#9fc5e8')
bush7.place(x=1150, y=560)

man = customtkinter.CTkImage(Image.open('manclipart2.png'), size=(125, 125))


#countdown to start game
def ready_set_whack():
    hs_board.configure(text='Ready')
    sleep(1)
    hs_board.configure(text='Set')
    sleep(1)
    hs_board.configure(text='Whack!')
    sleep(1)
    hs_board.place_forget()

#add arcade music
pygame.mixer.init()
bg_music = pygame.mixer.Sound('arcade-music-loop.wav')
boing_sound = pygame.mixer.Sound('boing_x.wav')


def whac_a_man():
    ready_set_whack()
    my_counter.place(x=570, y=130)
    global countdown
    countdown = 30
    global score
    global highscore
    for i in range(0, 30):
        countdown -= 1
        my_counter.configure(text=f'Men left:{countdown}')
        bush = random.randint(1, 7)
        if bush == 1:
            trigger_man1.configure(state='normal', image=man, fg_color='#9fc5e8')
            trigger_man1.place(x=280, y=230)
            sleep(1)
            trigger_man1.configure(state='disabled', text='')
            trigger_man1.place_forget()
        elif bush == 2:
            trigger_man2.configure(state='normal', image=man, fg_color='#9fc5e8')
            trigger_man2.place(x=620, y=230)
            sleep(1)
            trigger_man2.configure(state='disabled', text='')
            trigger_man2.place_forget()
        elif bush == 3:
            trigger_man3.configure(state='normal', image=man, fg_color='#9fc5e8')
            trigger_man3.place(x=1000, y=230)
            sleep(1)
            trigger_man3.configure(state='disabled', text='')
            trigger_man3.place_forget()
        elif bush == 4:
            trigger_man4.configure(state='normal', image=man, fg_color='#9fc5e8')
            trigger_man4.place(x=100, y=530)
            sleep(1)
            trigger_man4.configure(state='disabled', text='')
            trigger_man4.place_forget()
        elif bush == 5:
            trigger_man5.configure(state='normal', image=man, fg_color='#9fc5e8')
            trigger_man5.place(x=450, y=530)
            sleep(1)
            trigger_man5.configure(state='disabled', text='')
            trigger_man5.place_forget()
        elif bush == 6:
            trigger_man6.configure(state='normal', image=man, fg_color='#9fc5e8')
            trigger_man6.place(x=800, y=530)
            sleep(1)
            trigger_man6.configure(state='disabled', text='')
            trigger_man6.place_forget()
        elif bush == 7:
            trigger_man7.configure(state='normal', image=man, fg_color='#9fc5e8')
            trigger_man7.place(x=1150, y=530)
            sleep(1)
            trigger_man7.configure(state='disabled', text='')
            trigger_man7.place_forget()
    my_counter.place_forget()
    start_btn.place(x=600, y=50)
    hs_board.place(x=960, y=50)
    if score > highscore:
        hs_board.configure(text=f"High Score: {score}")
        sleep(5)
        start_game()
    elif score <= highscore:
        score_label.configure(text=f'Your score: {score}')
        sleep(5)
        start_game()
def onwhack():
    boing_sound.play()
    global bush
    global score
    if bush == 1:
        trigger_man1.configure(state='disabled', image='man')
    elif bush == 2:
        trigger_man2.configure(state='disabled', image='man')
    elif bush == 3:
        trigger_man3.configure(state='disabled', image='man')
    elif bush == 4:
        trigger_man4.configure(state='disabled', image='man')
    elif bush == 5:
        trigger_man5.configure(state='disabled', image='man')
    elif bush == 6:
        trigger_man6.configure(state='disabled', image='man')
    elif bush == 7:
        trigger_man7.configure(state='disabled', image='man')
    score += 10
    score_label.configure(text=f'Score:{score}')

#ready men
trigger_man1 = customtkinter.CTkButton(
    master=Home_screen,
    command=onwhack,
    text='',
    state='disabled',
    fg_color='#21c65a',
    height=10,
    width=10,
    corner_radius=0,
    hover=False
)
trigger_man2 = customtkinter.CTkButton(
    master=Home_screen,
    command=onwhack,
    text='',
    state='disabled',
    fg_color='#21c65a',
    height=10,
    width=10,
    corner_radius=0,
    hover=False
)
trigger_man3 = customtkinter.CTkButton(
    master=Home_screen,
    command=onwhack,
    text='',
    state='disabled',
    fg_color='#21c65a',
    height=10,
    width=10,
    corner_radius=0,
    hover=False
)
trigger_man4 = customtkinter.CTkButton(
    master=Home_screen,
    command=onwhack,
    text='',
    state='disabled',
    fg_color='#21c65a',
    height=10,
    width=10,
    corner_radius=0,
    hover=False
)
trigger_man5 = customtkinter.CTkButton(
    master=Home_screen,
    command=onwhack,
    text='',
    state='disabled',
    fg_color='#21c65a',
    height=10,
    width=10,
    corner_radius=0,
    hover=False
)
trigger_man6 = customtkinter.CTkButton(
    master=Home_screen,
    command=onwhack,
    text='',
    state='disabled',
    fg_color='#21c65a',
    height=10,
    width=10,
    corner_radius=0,
    hover=False
)
trigger_man7 = customtkinter.CTkButton(
    master=Home_screen,
    command=onwhack,
    text='',
    state='disabled',
    fg_color='#21c65a',
    height=10,
    width=10,
    corner_radius=0,
    hover=False
)
#init
app.mainloop()

