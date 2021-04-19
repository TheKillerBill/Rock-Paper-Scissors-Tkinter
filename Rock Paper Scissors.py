from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()
root.title("Rock Paper Scissors")
root.iconbitmap("dev/paper.ico")

#Images

scissors_img = ImageTk.PhotoImage( Image.open("dev/scissors.png")  )
stone_img = ImageTk.PhotoImage( Image.open("dev/stone.png")  )
paper_img = ImageTk.PhotoImage( Image.open("dev/papers.png")  )
user_img = ImageTk.PhotoImage( Image.open("dev/user.png")  )
computer_img = ImageTk.PhotoImage( Image.open("dev/computer.png")  )

# Frame Up and Frame Down

Frame_up = Frame(root)
Frame_up.grid( row = 0 )
Frame_down = Frame(root)
Frame_down.grid( row = 1 )

# PC and User text

Label_pc = Label( Frame_up , text="PC" , font = ('Orelega One','24')  )
Label_pc.grid( row = 0 , column = 0 , padx = 50 , pady = 5 )

Label_user = Label( Frame_up , text="User" , font = ('Orelega One','24')  )
Label_user.grid( row = 0 , column = 2 , padx = 50 , pady = 5 )

# PC and User Images

canvas_pc = Canvas(Frame_up , width = 125 , height = 125 )
canvas_pc.create_image( 62.5, 62.5 , image= computer_img ) 
canvas_pc.grid( row = 1 , column = 0 , padx = 50 , pady = 5 )


canvas_user = Canvas(Frame_up, width = 125 , height = 125 )
canvas_user.create_image( 62.5 , 62.5 , image= user_img ) 
canvas_user.grid( row = 1 , column = 2 , padx = 50 , pady = 5 )

# Score Variables 

user_wins = 0
pc_wins = 0

#Functions



def close_prog():
    root.destroy()

def play():
    Frame_down.grid_forget()
    Label_PcScore = Label(Frame_up, bg = "#81809C" , text = 'Pc :   ' + str(0) , font = ('Orelega One','20'))
    Label_PcScore.grid( row = 2 , column = 0 )
    Label_UserScore = Label(Frame_up, bg = "#81809C" , text = 'User :   ' + str(0) , font = ('Orelega One','20'))
    Label_UserScore.grid( row = 2 , column = 2 )
    Frame_Play.grid( row = 1 , pady = 30)
    Label_Score = Label( Frame_up , text='Score' , font = ('Orelega One','20') )
    Label_Score.grid( row = 2 , column = 1 )

def clicked( choice ):
    global Label_UserChose
    Label_UserChose = Label( Frame_Play , text='So you chose ' + choice , font = ('Orelega One','20') )
    Label_UserChose.grid( row = 2 , column = 2 )
    disable_buttons()
    work(choice)


def work( choice ):

    choices = ( 'rock' , 'scissors' , 'paper' )
    pc_choice = choices[ random.randint(0,2) ]
    global user_wins
    global pc_wins
    if choice == 'rock' and pc_choice == 'scissors' or choice == 'paper' and pc_choice == 'rock' or choice == 'scissors' and pc_choice == 'paper':
        user_wins += 1
        Label_UserScore = Label(Frame_up, bg = "#81809C" , text = 'User :   ' + str(user_wins) , font = ('Orelega One','20'))
        Label_UserScore.grid( row = 2 , column = 2 )
    elif choice == 'scissors' and pc_choice == 'rock' or choice == 'rock' and pc_choice == 'paper' or choice == 'paper' and pc_choice == 'scissors':
        pc_wins += 1
        Label_PcScore = Label(Frame_up, bg = "#81809C" , text = 'Pc :   ' + str(pc_wins) , font = ('Orelega One','20'))
        Label_PcScore.grid( row = 2 , column = 0 )

    global Label_PcWaits
    Label_PcWaits = Label( Frame_Play , text = 'Pc awaits your choice...' , font = ('Orelega One','20') , fg = '#81809C' )
    Label_PcWaits.grid( row = 0 , column = 0 , padx = 50 )
    global Label_PcChoice
    Label_PcChoice = Label( Frame_Play , text = 'Pc chose ' + pc_choice , font = ('Orelega One','20')  )
    Label_PcChoice.grid( row = 1 , column = 0 , padx = 50 )
    

def disable_buttons():
    Button_Rock = Button( Frame_Buttons, image = stone_img , bd = 0 , command=lambda: clicked('rock') , state= DISABLED )
    Button_Rock.grid( row = 0 , column = 0 , padx = 10 )
    Button_Scissors = Button( Frame_Buttons, image = scissors_img , bd = 0  , command=lambda: clicked('scissors') , state= DISABLED)
    Button_Scissors.grid( row = 0 , column = 1 , padx = 10 )
    Button_Paper = Button( Frame_Buttons, image = paper_img , bd =  0  , command=lambda: clicked('paper') , state= DISABLED)
    Button_Paper.grid( row = 0 , column = 2 , padx = 10 )

def enable_buttons():
    Button_Rock = Button( Frame_Buttons, image = stone_img , bd = 0 , command=lambda: clicked('rock')  )
    Button_Rock.grid( row = 0 , column = 0 , padx = 10 )
    Button_Scissors = Button( Frame_Buttons, image = scissors_img , bd = 0  , command=lambda: clicked('scissors') )
    Button_Scissors.grid( row = 0 , column = 1 , padx = 10 )
    Button_Paper = Button( Frame_Buttons, image = paper_img , bd =  0  , command=lambda: clicked('paper') )
    Button_Paper.grid( row = 0 , column = 2 , padx = 10 )


def playagain():
    global Label_PcChoice
    Label_PcChoice.destroy()
    enable_buttons()
    global Label_UserChose
    Label_UserChose.destroy()
    global Label_PcWaits
    Label_PcWaits = Label( Frame_Play , text = 'Pc awaits your choice...' , font = ('Orelega One','20')  )
    Label_PcWaits.grid( row = 0 , column = 0 , padx = 50 )



#Frame Play

Frame_Play = Frame( root )
Label_PcWaits = Label( Frame_Play , text = 'Pc awaits your choice...' , font = ('Orelega One','20')  )
Label_PcWaits.grid( row = 0 , column = 0 , padx = 50 )

Label_UserChoice = Label( Frame_Play , text = "What's your choice? " , font = ('Orelega One','20') )
Label_UserChoice.grid( row = 0 , column = 2 , padx = 50 )


Button_Play = Button( Frame_Play , text = "Play Again" , font = ('Orelega One','24') , width = 10 , command= playagain )
Button_Play.grid( row = 2, column = 1 , padx = 10  , pady = 10 )

Button_Quit = Button( Frame_Play , text = "Quit" , font = ('Orelega One','24') , width = 10 , command = close_prog )
Button_Quit.grid( row = 3 , column = 1 , padx = 10 , pady = 10 )



#Frame Buttons

Frame_Buttons = Frame( Frame_Play )
Frame_Buttons.grid( row = 1 , column = 2 )

Button_Rock = Button( Frame_Buttons, image = stone_img , bd = 0 , command=lambda: clicked('rock') )
Button_Rock.grid( row = 0 , column = 0 , padx = 10 )

Button_Scissors = Button( Frame_Buttons, image = scissors_img , bd = 0  , command=lambda: clicked('scissors'))
Button_Scissors.grid( row = 0 , column = 1 , padx = 10 )

Button_Paper = Button( Frame_Buttons, image = paper_img , bd =  0  , command=lambda: clicked('paper'))
Button_Paper.grid( row = 0 , column = 2 , padx = 10 )


#Frame Down

Button_Play = Button( Frame_down , text = "Play" , font = ('Orelega One','24') , width = 10 , command = play)
Button_Play.grid( row = 0, padx = 10  , pady = 10 )

Button_Quit = Button( Frame_down , text = "Quit" , font = ('Orelega One','24') , width = 10 , command = close_prog )
Button_Quit.grid( row = 1 , padx = 10 , pady = 10 )



root.mainloop()