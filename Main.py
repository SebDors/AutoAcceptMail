from python_imagesearch.imagesearch import imagesearch
import pyautogui
import time
from tkinter import messagebox

CountAccept = 0
CountDelete = 0


def CheckWindowsIsMinimised():
    # check if windows is minimised
    NotMinimised1 = imagesearch("Screenshots/NotMinimised1.png")
    NotMinimised2 = imagesearch("Screenshots/NotMinimised2.png")
    if NotMinimised1 != -1 or NotMinimised2 != -1:
        MinimisedPos = imagesearch("Screenshots/FenetreMinime1.png")
        if MinimisedPos[0] != -1:
            pyautogui.moveTo(MinimisedPos[0]+25, MinimisedPos[1]+20)
            pyautogui.click(button="left")
        else:
            print("not found fenetre minime1")

        MinimisedPos = imagesearch("Screenshots/FenetreMinime2.png")
        if MinimisedPos[0] != -1:
            pyautogui.moveTo(MinimisedPos[0]+25, MinimisedPos[1]+20)
            pyautogui.click(button="left")
        else:
            print("not found fenetre minime2")
    else:
        print("Full screen")
        print(NotMinimised1[0], NotMinimised1[1])
        print(NotMinimised2[0], NotMinimised2[1])


def BoucleSeenEnseignement():
    StopBoucle = 0
    global CountAccept
    global CountDelete
    while StopBoucle < 4:
        PosEnseignement = imagesearch("Screenshots/SeenEnseignement.png")
        if PosEnseignement[0] != -1:
            pyautogui.moveTo(PosEnseignement[0], PosEnseignement[1])
            pyautogui.click(button="left")
            time.sleep(0.5)
            PosAccepter = imagesearch("Screenshots/Accepter.png")
            PosSupprimer = imagesearch(
                "Screenshots/Supprimer_du_calendrier.png")
            if PosAccepter[0] != -1:
                pyautogui.moveTo(PosAccepter[0], PosAccepter[1])
                pyautogui.click(button="left")
                CountAccept += 1
            if PosSupprimer[0] != -1:
                pyautogui.moveTo(PosSupprimer[0]+25, PosSupprimer[1]+10)
                pyautogui.click(button="left")
                CountDelete += 1
            else:
                print("not find Accepter et Supprimer")
        else:
            # print("Not found Enseignement ")
            pyautogui.moveTo(530, 300)
            pyautogui.scroll(-400)
            StopBoucle += 1


def BoucleNewEnseignement():
    global CountAccept
    global CountDelete
    StopBoucle = 0
    while StopBoucle < 4:
        PosEnseignement = imagesearch("Screenshots/NewEnseignement.png")
        if PosEnseignement[0] != -1:
            pyautogui.moveTo(PosEnseignement[0], PosEnseignement[1])
            pyautogui.click(button="left")
            time.sleep(0.5)
            PosAccepter = imagesearch("Screenshots/Accepter.png")
            PosSupprimer = imagesearch(
                "Screenshots/Supprimer_du_calendrier.png")
            if PosAccepter[0] != -1:
                pyautogui.moveTo(PosAccepter[0], PosAccepter[1])
                pyautogui.click(button="left")
                CountAccept += 1
            elif PosSupprimer[0] != -1:
                pyautogui.moveTo(PosSupprimer[0]+25, PosSupprimer[1]+10)
                pyautogui.click(button="left")
                CountDelete += 1
            else:
                print("not find Accepter et Supprimer")
        else:
            # print("Not found Enseignement ")
            pyautogui.moveTo(530, 300)
            pyautogui.scroll(-400)
            StopBoucle += 1


# Open Microsoft courrier
pos = imagesearch("Screenshots/CourrierImage.png")
if pos[0] != -1:
    # print("position : ", pos[0], pos[1])
    pyautogui.moveTo(pos[0]+25, pos[1]+20)
    pyautogui.click(button="left")
else:
    print("Image courrier not found")
    messagebox.showinfo("Error", "Courrier not Found")

time.sleep(1.5)  # let the app open
CheckWindowsIsMinimised()
BoucleNewEnseignement()
pyautogui.moveTo(530, 300)
pyautogui.scroll(1700)
time.sleep(1)
BoucleSeenEnseignement()
pyautogui.moveTo(530, 300)
pyautogui.scroll(1700)
FinalMessage2 = f'Accepted {CountAccept} Mail and deleted {CountDelete} mails'
messagebox.showinfo("Finish", FinalMessage2)
