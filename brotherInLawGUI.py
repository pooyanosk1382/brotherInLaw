import threading
import time
import tkinter as tk
from tkinter import PhotoImage

barrier = threading.Barrier(2)


def firstBrotherInLaw():
    line1.set("First family start the trip")
    time.sleep(1)
    for _ in range(4):
        line1.set("First family start going to next toll")
        for i in range(142):
            time.sleep(0.02)

        line1.set("First family reached the toll " + str(_+1))
        time.sleep(1)
        barrier.wait()

        line1.set("First family meet the second family")
        time.sleep(1)
    line1.set("First family reach the destination")


def secondBrotherInLaw():
    line2.set("second family start the trip")
    time.sleep(1)
    for _ in range(4):
        line2.set("Second family start going to next toll")
        for i in range(142):
            time.sleep(0.04)

        line2.set("Second family reached the toll " + str(_+1))
        time.sleep(1)
        barrier.wait()

        line2.set("Second family meet the first family")
        time.sleep(1)
    line2.set("Second family reach the destination")


root = tk.Tk()
root.title("Trip of families")
root.geometry("640x427")
background_image = tk.PhotoImage(file="sea.png")

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

line1 = tk.StringVar()
line2 = tk.StringVar()

image1 = PhotoImage(file="family1.png").subsample(10, 10)
image2 = PhotoImage(file="family2.png").subsample(10, 10)

label1 = tk.Label(root, image=image1, textvariable=line1, font=("Arial", 22), compound="left")
label1.pack(pady=30)
label2 = tk.Label(root, image=image2, textvariable=line2, font=("Arial", 22), compound="left")
label2.pack(pady=30)

firstGroom = threading.Thread(target=firstBrotherInLaw)
secondGroom = threading.Thread(target=secondBrotherInLaw)
firstGroom.start()
secondGroom.start()

root.mainloop()

firstGroom.join()
secondGroom.join()

print("All threads have completed.")
