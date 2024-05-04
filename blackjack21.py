import customtkinter
import random

#p and c score and deck

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]*4
score = 0
computer_score = 0

#check variables

first_function_used = False
too_much_computer = False
player_lost = False
too_much_player = False
resultats_used = False

#creating window

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("800x600")

# Creating Frames

left_frame = customtkinter.CTkFrame(app)
left_frame.pack(side="left", fill="both", expand=True)

right_frame = customtkinter.CTkFrame(app)
right_frame.pack(side="right", fill="both", expand=True)


# LEFT FRAME - PLAYER CHOICES


# The function of calling a taking move

def take_black_jack():
    global score 
    global first_function_used
    global player_lost
    global too_much_player
    if first_function_used == False and too_much_player == False:
        random.shuffle(deck)
        current = deck.pop()
        card_label = customtkinter.CTkLabel(left_frame, text="Your card - %d"% current)
        card_label.pack()
        score += current
        all_card_label = customtkinter.CTkLabel(left_frame, text="All your cards now - %d"% score)
        all_card_label.pack()
        if score > 21:
            too_much_player = True
    elif score == 21:
        score21_label_player = customtkinter.CTkLabel(right_frame, text="Player won!")
        score21_label_player.pack()
    elif player_lost == False:
        blocked_label = customtkinter.CTkLabel(left_frame, text="You've already clicked pass")
        blocked_label.pack()
        player_lost = True

# The function of calling a passing move

def pass_black_jack():
    global first_function_used
    
    if first_function_used == False:
        pass
    first_function_used = True

# Buttons for Left Frame

the_player_label = customtkinter.CTkLabel(left_frame, text="Player choice")
the_player_label.pack()

take_button = customtkinter.CTkButton(left_frame, text="Take", command=take_black_jack)
take_button.pack()

pass_button = customtkinter.CTkButton(left_frame, text="Pass", command=pass_black_jack)
pass_button.pack()

# RESULTATS

def resultats():
    global score 
    global computer_score
    global resultats_used

    if resultats_used == True:
        pass
    elif computer_score >= 21 and score <= 21:
        score_label = customtkinter.CTkLabel(right_frame, text="You won!")
        score_label.pack()
    elif score >= 21 and computer_score <= 21:
        score_label = customtkinter.CTkLabel(right_frame, text="Defeat! Computer won!")
        score_label.pack()
    elif computer_score <= 21 and score <= 21:
        if computer_score > score:
            score_label = customtkinter.CTkLabel(right_frame, text="Defeat! Computer won!")
            score_label.pack()
        elif score > computer_score:
            score_label = customtkinter.CTkLabel(right_frame, text="Best game! You won!")
            score_label.pack()
        elif score == computer_score:
            score_label = customtkinter.CTkLabel(right_frame, text="Draw! Nobody won")
            score_label.pack()
    elif computer_score >= 21 and score >= 21:
        score_label = customtkinter.CTkLabel(right_frame, text="Draw! Nobody won")
        score_label.pack()

    resultats_used = True


# RIGHT FRAME - COMPUTER CHOICES


def take_black_jack_computer():
    global computer_score
    global first_function_used
    global too_much_computer
    global resultats_used

    if first_function_used == True and too_much_computer == False and resultats_used == False:
        random.shuffle(deck)
        computer_current = deck.pop()
        card_label = customtkinter.CTkLabel(right_frame, text="Your card - %d"% computer_current)
        card_label.pack()
        computer_score += computer_current
        all_card_label = customtkinter.CTkLabel(right_frame, text="All computer cards now - %d"% computer_score)
        all_card_label.pack()
        if computer_score > 21:
            too_much_computer = True
        elif computer_score == 21:
            score21_label = customtkinter.CTkLabel(right_frame, text="Computer won!")
            score21_label.pack()
    
# Creating right frame buttons

the_computer_label = customtkinter.CTkLabel(right_frame, text="Computer choice")
the_computer_label.pack()

take_button_computer = customtkinter.CTkButton(right_frame, text="Take", command=take_black_jack_computer)
take_button_computer.pack()

result_button = customtkinter.CTkButton(right_frame, text="Result", command=resultats)
result_button.pack()

# Starting!

app.mainloop()
