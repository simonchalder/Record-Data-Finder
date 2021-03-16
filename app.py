#Imports

from dotenv import load_dotenv
import os
import discogs_client
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

# Tkinter app window creation

# -------------------------------------------------------------------------------------------

root = Tk() # Create the window widget
root.geometry('1290x850+300+100') # width and height of app window
root.title("Record Data Finder") # menu bar title
root.iconbitmap("./app_logo.ico")
messagebox.showinfo("Information","Record Data Finder, an App by Simon Chalder")
# -------------------------------------------------------------------------------------------

# Discogs API call using Discogs client

# -------------------------------------------------------------------------------------------

d = discogs_client.Client('RecordDataFinder/0.1', user_token=os.environ['USER_TOKEN'])

# --------------------------------------------------------------------------------------------

# Function definitions

# --------------------------------------------------------------------------------------------

def clicked(): # function will be called when artist search button is clicked
    results = d.search(artist_input.get(),type='artist') # artist search to API using artist input box as search term
    artist_id = results[0].id # Taking the first artist result and storing it in a variable
    artist = d.artist(artist_id) # Finding the releases associated with the artist
    
    for y in artist.releases: # Filter search results to show master releases only
        x = str(y)
        if 'Master' in x:
            release_box.insert(0, x)
        else:
            continue
        
def submit(): # Function will be called when the release search button is clicked
    
    record = d.master(release_input.get()) # release search to discogs API using release number given in release input box
    
    title = record.title # Variable creation for various release fields
    tracklist = record.main_release.tracklist
    url = record.main_release.url
    formats = record.main_release.formats[0]['name']

    try:
        num_for_sale = record.main_release.data['num_for_sale']
    except Exception:
        num_for_sale = "N/A"

    try:
        lowest_price = record.main_release.data['lowest_price']
    except Exception:
        lowest_price = "N/A"

    try:
        year = record.main_release.data['year']
    except Exception:
        year = "N/A"

    try:
        country = record.main_release.data['country']
    except Exception:
        country = "N/A"

    try:
        catno = record.main_release.data['catno']
    except Exception:
        catno = "N/A"

    # Outputting results to the various release info boxes

    title_box.insert(0, title)

    for x in tracklist:
        tracklist_box.insert(0, x)

    url_box.insert(0, url)

    format_box.insert(0, formats)

    sales_box.insert(0, str(num_for_sale))

    price_box.insert(0, str(lowest_price))

    year_box.insert(0, str(year))

    country_box.insert(0, country)

    catno_box.insert(0, str(catno))

# -------------------------------------------------------------------------------------------

# Tk Widget creation

# -------------------------------------------------------------------------------------------
img = ImageTk.PhotoImage(Image.open("./app-logo.gif"))
panel = Label(root, image = img)
panel.grid(column=0, row=0)
# Artist input box

artist_input = Entry(root, width=50)
artist_input.insert(0,"Enter artists name here")
artist_input.grid(column=0, row=1)

# Artist search button

artist_button = Button(root, text="Submit", padx=20, pady=10, command=clicked)
artist_button.grid(column=1, row=1, pady=20)

# Release results box

release_box = Listbox(root, width=90, height=19, )
release_box.grid(column=0, row=2, columnspan=2, padx=20, rowspan=3)

# Release number input box

release_input = Entry(root, width=50)
release_input.insert(0,"Enter release number")
release_input.grid(column=0, row=5)

# Release search button

release_button = Button(root, text="Submit", padx=20, pady=10, command=submit)
release_button.grid(column=1, row=5, pady=20)

# Title box and label

title_label = Label(root, text="Title")
title_label.grid(column=2, row=1, sticky=E)

title_box = Listbox(root, width=90, height=1)
title_box.grid(column=3, row=1)

# Tracklist box and label

tracks_label = Label(root, text="Tracklist")
tracks_label.grid(column=2, row=2, sticky=E)

tracklist_box = Listbox(root, width=90)
tracklist_box.grid(column=3, row=2)

# Url box and label

url_label = Label(root, text="Discogs Url")
url_label.grid(column=2, row=3, sticky=E)

url_box = Listbox(root, width=90, height=1)
url_box.grid(column=3, row=3)

# Formats box and label

format_label = Label(root, text="Formats")
format_label.grid(column=2, row=4, sticky=E)

format_box = Listbox(root, width=90, height=1)
format_box.grid(column=3, row=4, pady=20)

# Sales box and label

sales_label = Label(root, text="Number currently for sale")
sales_label.grid(column=2, row=5, sticky=E)

sales_box = Listbox(root, width=30, height=1)
sales_box.grid(column=3, row=5, sticky=W, pady=20)

# Price box and label

price_label = Label(root, text="Lowest current price ($)")
price_label.grid(column=2, row=6, sticky=E)

price_box = Listbox(root, width=30, height=1)
price_box.grid(column=3, row=6, sticky=W, pady=20)

# Year box and label

year_label = Label(root, text="Year released")
year_label.grid(column=2, row=7, sticky=E)

year_box = Listbox(root, width=30, height=1)
year_box.grid(column=3, row=7, sticky=W, pady=20)

# Country box and label

country_label = Label(root, text="Country")
country_label.grid(column=2, row=8, sticky=E)

country_box = Listbox(root, width=30, height=1)
country_box.grid(column=3, row=8, sticky=W, pady=20)

# Catalogue number box and label

catno_label = Label(root, text="Catalogue number")
catno_label.grid(column=2, row=9, sticky=E)

catno_box = Listbox(root, width=30, height=1)
catno_box.grid(column=3, row=9, sticky=W, pady=20)

# End of mainloop

root.mainloop()








