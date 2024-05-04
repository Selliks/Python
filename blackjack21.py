import tkinter
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
best_game = False

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
# PLAYER CHOICES
# LEFT FRAME
the_player_label = customtkinter.CTkLabel(left_frame, text="Player choice")
the_player_label.pack()

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
            defeat_label = customtkinter.CTkLabel(left_frame, text="Defeat! Your score - %d! Don't worry, it's game! "% score)
            defeat_label.pack()
            too_much_player = True
        elif score == 21:
            score21_label = customtkinter.CTkLabel(left_frame, text="Great move! You Won! 21/21")
            score21_label.pack()  
    elif player_lost == False:
        blocked_label = customtkinter.CTkLabel(left_frame, text="You've already clicked pass")
        blocked_label.pack()
        player_lost = True

# The function of calling a passing move

def pass_black_jack():
    global score 
    global computer_score
    global first_function_used
    global too_much_computer
    global best_game
    
    if too_much_computer == True and best_game == False:
        pass
    elif computer_score > 21:
        score_label = customtkinter.CTkLabel(right_frame, text="The computer lost!")
        score_label.pack()
        too_much_computer = True
    elif computer_score <= 21 and score <= 21:
        if computer_score > score:
            score_label = customtkinter.CTkLabel(left_frame, text="Defeat! Computer won!")
            score_label.pack()
        elif score > computer_score:
            score_label = customtkinter.CTkLabel(left_frame, text="Best game! You won!")
            score_label.pack()
        elif score == computer_score:
            score_label = customtkinter.CTkLabel(left_frame, text="Draw! Nobody won")
            score_label.pack()
    
    first_function_used = True and best_game == True

# Buttons for left frame
take_button = customtkinter.CTkButton(left_frame, text="Take", command=take_black_jack)
pass_button = customtkinter.CTkButton(left_frame, text="Pass", command=pass_black_jack)
take_button.pack()
pass_button.pack()

# RIGHT FRAME
the_computer_label = customtkinter.CTkLabel(right_frame, text="Computer choice")
the_computer_label.pack()
def take_black_jack_computer():
    global computer_score
    global first_function_used
    global too_much_computer
    if first_function_used == True or too_much_player == True and too_much_computer == False:
        random.shuffle(deck)
        computer_current = deck.pop()
        card_label = customtkinter.CTkLabel(right_frame, text="Your card - %d"% computer_current)
        card_label.pack()
        computer_score += computer_current
        all_card_label = customtkinter.CTkLabel(right_frame, text="All computer cards now - %d"% computer_score)
        all_card_label.pack()
        if computer_score > 21:
            defeat_label = customtkinter.CTkLabel(right_frame, text="Defeat! Computer score - %d! "% computer_score)
            defeat_label.pack()
            too_much_computer = True
        elif computer_score == 21:
            score21_label = customtkinter.CTkLabel(right_frame, text="Computer won!")
            score21_label.pack()
    

take_button_computer = customtkinter.CTkButton(right_frame, text="Take", command=take_black_jack_computer)
take_button_computer.pack()

app.mainloop()