# Code written by Pratik Shastrakar, references taken from Youtube and Tutorials Point.

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from tkinter import Tk
import tkinter as to
import tkinter as tk



# Backend using pytube module
FolderName = "" # initialized to null

# Asking user to enter correct location path directory
def openLocation():
    global FolderName
    FolderName = filedialog.askdirectory()
    if(len(FolderName) > 1):
        locationError.config(text=FolderName, fg="green")
    else:
        locationError.config(text="Please select proper location!", fg="red")

# Taking video choice from the drop down menu
def downloadVideo():
    choice = ytdChoices.get()
    url = ytdEntry.get()

    if(len(url) > 1):
        ytdError.config(text="")
        yt = YouTube(url)

# choice selection section
        if choice == choices[0]:
            select = yt.streams.filter(progressive=True).first()  # highest
        elif(choice == choices[1]):
            select = yt.streams.filter(
                progressive=True, file_extension='mp4').last()
        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Please check the link", fg="red")
# download status updatation

    select.download(FolderName)
    ytdError.config(text="Download Completed!")

#************************
# Front End (GUI)
root = Tk()
root.title("Youtube Video Downloader")

# set window size
root.geometry("350x400")  
root.columnconfigure(0, weight=1)

# icon
# root = tk.Tk()
root.iconbitmap(r'C:\Users\Pratik Shastrakar\Documents\GitHub\Youtube-Video-downloader\yt_icon.ico')


# label for URL text
ytdLabel = Label(root, text="Enter the URL of the Video", font=("jost", 15))
ytdLabel.grid()

ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50, textvariable=ytdEntryVar)
ytdEntry.grid()

# error tag prompt
ytdError = Label(root, text="Download Status", fg="red", font=("jost", 10))
ytdError.grid()

# video saving location
saveLabel = Label(root, text="Download file to", font=("jost", 15, "bold"))
saveLabel.grid()

# save button for location
saveEntry = Button(root, width=10, bg="red", fg="white",text="Choose Path", command=openLocation)
saveEntry.grid()

# error messaage prompt
locationError = Label(root, text="Path not selected",fg="red", font=("jost", 10))
locationError.grid()

# download quality selection
ytdQuality = Label(root, text="Select Quality", font=("jost", 15))
ytdQuality.grid()

# choices [(TO BE RE-WRITTEN PROPERLY), more options will be added, minor issue with OnlyAudio.]
choices = ["144p (Lowest)", "720p (Highest)", "Only Audio"]
ytdChoices = ttk.Combobox(root, values=choices)
ytdChoices.grid()

# download button
downloadButton = Button(root, width=10, text="Download",bg="red", fg="white", command=downloadVideo)
downloadButton.grid()

# Download progress bar to be added later
'''
here
'''
# empty space added to shift Dev Label to the bottom
emptySpace0 = Label(root, text="")
emptySpace0.grid()
emptySpace1 = Label(root, text="")
emptySpace1.grid()
emptySpace2 = Label(root, text="")
emptySpace2.grid()
emptySpace3 = Label(root, text="")
emptySpace3.grid()
emptySpace4 = Label(root, text="")
emptySpace4.grid()
emptySpace5 = Label(root, text="")
emptySpace5.grid()

# Dev label
devloperName = Label(root, text="Made by Pratik Shastrakar",font=("jost",8))
devloperName.grid()

# USername @pstricks01
myUserName = Label(root, text="@pstricks01",font=("jost",8))
myUserName.grid()

root.mainloop()
