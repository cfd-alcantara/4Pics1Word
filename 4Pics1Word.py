import os
from tkinter import *
import random, string

#checks for existing load data
file_exists = os.path.isfile("game_progress.txt")

#retrieves data
def load():
    global coinval
    global level
    global level
    global picNum
    if file_exists:
        with open("game_progress.txt", "r") as r:
            data = r.readlines()
            coinval = int(data[0])
            picNum = int(data[1])

    else:
        coinval = 100
        picNum = 0

#saves to text file
def upload():
    with open("game_progress.txt", "w") as u:
        u.write(str(coinval) + "\n")
        u.write(str(picNum) + "\n")

# call load() and assign the returned values to coinval and level
load()

f = open("picList.txt", "r")
x = f.readlines()

picfiles = list()
for p in x:
    fn = p.strip().split(';')
    picfiles.append(fn[1])

answer = []

# SKIP
def changeImage():
    global coinval
    global hint_count
    if coinval >= 10:
        global picNum
        picNum += 1
        if picNum == 50:
            finishLevel()
        elif picNum < 50:
            pics.config(file=os.path.join('assets', picfiles[picNum] + ".png"))
            nextPic.config(text="SKIP", bg="gold")
            for i in range(answer_len):
                box_label.destroy()

            answer.clear()
            hint_count = 0

            create_display_boxes()
            randomizer()
    elif coinval <= 9:
        pass

# MAIN STUFF
root = Tk()
root.geometry("400x600")
root.title("4 PICS 1 WORD")
root.configure(bg="#141821")

# UI STUFF
pics = PhotoImage(file=os.path.join('assets', picfiles[picNum] + ".png"))
lblpic = Label(root, image=pics)
lblpic.place(x=49, y=60)
nextPic = Button(root, text="SKIP", font="verdana 15", bg="gold",
                 command=lambda: [changeImage(), changeLevel(), changeCoin()])
nextPic.place(x=325, y=550)

# HINT
hint_count = 0
hint_image = PhotoImage(file = os.path.join('assets', "hint.png"))
hint_button = Button(root, image = hint_image, borderwidth = 2, command = lambda:[give_hint(), changeCoin_Hint()])
hint_button.place(x = 325, y = 483)

# LEVEL
frame_1 = Frame(root, width=300, height=50, bg='medium blue', highlightbackground="medium blue")
level = Label(frame_1, text="Level: " + str(picNum + 1), bg='medium blue', font="verdana 15")
level.place(x=10, y=8.5)

# CHANGE LEVEL
def changeLevel():
    if picNum < 50:
        level.config(text="Level: " + str(picNum + 1))

# COIN
coin_file = PhotoImage(file=os.path.join('assets', "coin.png"))
coin_image = Label(frame_1, image=coin_file, bg="medium blue")
coin_image.place(x=280, y=0)
coin = Label(frame_1, text=coinval, font="verdana 15", bg="medium blue")
coin.place(x=337, y=8.5)
frame_1.pack(side=TOP, fill=BOTH)


# CHANGE COIN
def changeCoin():
    global coinval
    if picNum < 50:
        if coinval >= 10:
            coinval -= 10
            coin.config(text=coinval)
            upload()  # call the upload function to save the new coin value to the file
        elif coinval <= 9:
            pass

def changeCoin_Hint():
    global coinval
    if picNum < 50:
        if coinval >= 2:
            coinval -= 2
            coin.config(text = coinval)
            upload() # call the upload function to save the new coin value to the file
        elif coinval <= 1:
            pass

# KEYBOARD
frmLetter = Frame(root, width="200", height="75", bg="black")
frmLetter.place(x=110, y=483)


def randomizer():
    if picNum < 50:
        ranLet = random.choices(string.ascii_uppercase, k=8 - len(picfiles[picNum]))
        random_correctletter = random.sample(tuple((picfiles[picNum]).upper()), k=len(picfiles[picNum]))
        bothrandom = random.sample(ranLet + random_correctletter, k=8)

        # Button 1
        b1 = Button(frmLetter, text=bothrandom[0], font="verdana 20", width=2, height=1, fg="white", bg="#20262f",
                    command=lambda: [disable(b1), add(bothrandom[0])])
        b1.grid(row=1, column=1)
        # Button 2
        b2 = Button(frmLetter, text=bothrandom[1], font="verdana 20", width=2, height=1, fg="white", bg="#20262f",
                    command=lambda: [disable(b2), add(bothrandom[1])])
        b2.grid(row=1, column=2)
        # Button 3
        b3 = Button(frmLetter, text=bothrandom[2], font="verdana 20", width=2, height=1, fg="white", bg="#20262f",
                    command=lambda: [disable(b3), add(bothrandom[2])])
        b3.grid(row=1, column=3)
        # Button 4
        b4 = Button(frmLetter, text=bothrandom[3], font="verdana 20", width=2, height=1, fg="white", bg="#20262f",
                    command=lambda: [disable(b4), add(bothrandom[3])])
        b4.grid(row=1, column=4)
        # Button 5
        b5 = Button(frmLetter, text=bothrandom[4], font="verdana 20", width=2, height=1, fg="white", bg="#20262f",
                    command=lambda: [disable(b5), add(bothrandom[4])])
        b5.grid(row=2, column=1)
        # Button 6
        b6 = Button(frmLetter, text=bothrandom[5], font="verdana 20", width=2, height=1, fg="white", bg="#20262f",
                    command=lambda: [disable(b6), add(bothrandom[5])])
        b6.grid(row=2, column=2)
        # Button 7
        b7 = Button(frmLetter, text=bothrandom[6], font="verdana 20", width=2, height=1, fg="white", bg="#20262f",
                    command=lambda: [disable(b7), add(bothrandom[6])])
        b7.grid(row=2, column=3)
        # Button 8
        b8 = Button(frmLetter, text=bothrandom[7], font="verdana 20", width=2, height=1, fg="white", bg="#20262f",
                    command=lambda: [disable(b8), add(bothrandom[7])])
        b8.grid(row=2, column=4)

def disable(i):
    i['state'] = 'disabled'

frmBox = Frame(root, width="200", height="75", bg="black")
frmBox.place(x=110, y=400)

# KEYBOARD RESULTS DISPLAY
def create_display_boxes():
    global display_boxes
    display_boxes = []
    global answer_len
    if picNum < 50:
        answer_len = len(picfiles[picNum])
        for i in range(answer_len):
            global box_label
            if answer_len == 3: # 3 LETTERS
                frmBox.place(x=130,y=400)
            if answer_len == 4: # 4 LETTERS
                frmBox.place(x=110,y=400)
            if answer_len == 5: # 5 LETTERS
                frmBox.place(x=87,y=400)
            if answer_len == 6: # 6 LETTERS
                frmBox.place(x=65,y=400)
            if answer_len == 7: # 7 LETTERS
                frmBox.place(x=40,y=400)
            if answer_len == 8: # 8 LETTERS
                frmBox.place(x=10,y=400)
            box_label = Label(frmBox, text='', font=("verdana", 20), width=2, bd=1, relief="solid")
            box_label.grid(row=0, column=i, padx=5)
            display_boxes.append(box_label)

def give_hint():
    global hint_count
    global hint_box
    if picNum < 50:
        if coinval >= 2:
            hint_box = picfiles[picNum]
            answer.append(hint_box[hint_count])
            if hint_count < len(hint_box):
                hint_count += 1
                if hint_count == len(hint_box):
                    hint_count = 0
            global display_boxes
            for i in answer:
                tried = len(answer)
                display_boxes[tried - 1]['text'] = i.upper()
            if len(answer) == len(picfiles[picNum]):
                check()
                create_display_boxes()
                randomizer()
        elif coinval < 10:
            pass

def check():
    joined_answer = ''.join(answer)
    global picNum
    global display_boxes
    global coinval
    if joined_answer.lower() == picfiles[picNum]:
        picNum += 1
        if picNum == 50:
            finishLevel()
        elif picNum < 50:
            coinval += 10
            coin.config(text = coinval)
            upload()
        
            pics.config(file=os.path.join('assets', picfiles[picNum] + ".png"))
            
            answer.clear()
            global answer_len
            for i in range(answer_len):
                box_label.destroy()
        
            changeLevel()
    else:
        answer.clear()
        for i in range(answer_len):
            box_label.destroy()

def add(i):
    answer.append(i)
    global display_boxes
    for i in answer:
        tried = len(answer)
        display_boxes[tried - 1]['text'] = i

    if len(answer) != len(picfiles[picNum]):
        pass
    
    else:
        check()
        create_display_boxes()
        randomizer()
        upload()

def finishLevel():
    frame_1.destroy()
    frmBox.destroy()
    frmLetter.destroy()
    hint_button.destroy()
    lblpic.destroy()
    root.title("CONGRATULATIONS YOU HAVE FINISHED 4PICS1WORD")
    endCanvas = Canvas(root, width=400, height=600, bg="#141821")
    endCanvas.pack()
    endLabel1 = Label(endCanvas, text="CONGRATULATIONS YOU HAVE", font="verdana 17", bg="#141821", fg="gold")
    endLabel2 = Label(endCanvas, text="FINISHED 4PICS1WORD!!!", font="verdana 20", bg="#141821", fg="gold")
    endLabel1.place(x=15, y=100)
    endLabel2.place(x=17, y=130)

    # ADD BUTTON QUIT
    close = Button(endCanvas, text="QUIT GAME", font="verdana 15", bg="#20262f", fg="white", relief="raised",width=15,height=2,command= root.destroy)
    close.place(x=100, y=250)

    credlines1 = Label(endCanvas,text="Credits:", font="verdana 15", bg="#141821", fg="white")
    credlines2 = Label(endCanvas, text="CARL FRANCIS ALCANTARA", font="verdana 15", bg="#141821", fg="white")
    credlines3 = Label(endCanvas, text="CHRISTOPHER KYLE SANTOS", font="verdana 15", bg="#141821", fg="white")
    credlines4 = Label(endCanvas, text="JOHN ROBERT SANTOS", font="verdana 15", bg="#141821", fg="white")

    credlines1.place(x=155,y=350)
    credlines2.place(x=60, y=400)
    credlines3.place(x=45, y=450)
    credlines4.place(x=75, y=500)

create_display_boxes()

randomizer()

root.mainloop()
