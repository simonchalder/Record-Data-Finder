#Imports

from dotenv import load_dotenv
import os
import time
import discogs_client
from tkinter import *

# Tkinter app window creation

# -------------------------------------------------------------------------------------------

root = Tk() # Create the window widget
root.geometry('700x850') # width and height of app window
root.title("Record Data Finder") # menu bar title

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
    
    for x in artist.releases:
        release_box.insert(1, x) # insert the results of the artist search into the release box
        
def submit(): # Function will be called when the release search button is clicked
    record = d.release(release_input.get()) # release search to discogs API using release number given in release input box
    
    title = record.title # Variable creation for various release fields
    tracklist = record.tracklist
    url = record.url
    formats = record.formats

    try:
        num_for_sale = record.data['num_for_sale']
    except Exception:
        num_for_sale = "N/A"

    try:
        lowest_price = record.data['lowest_price']
    except Exception:
        lowest_price = "N/A"

    try:
        year = record.data['year']
    except Exception:
        year = "N/A"

    try:
        country = record.data['country']
    except Exception:
        country = "N/A"

    try:
        catno = record.data['catno']
    except Exception:
        catno = "N/A"

    # Outputting results to the various release info boxes

    title_box.insert(1, "Title: " + title)
    for x in tracklist:
        tracklist_box.insert(7, x)
    time.sleep(.200)
    url_box.insert(8, "Discogs URL: " + url)
    for y in formats:
        format_box.insert(9, y)
    time.sleep(.200)
    sales_box.insert(2, "Number currently for sale: " + str(num_for_sale))
    price_box.insert(3, "Lowest current price ($): " + str(lowest_price))
    year_box.insert(4, "Released: " + str(year))
    country_box.insert(5, "Country: " + country)
    catno_box.insert(6, "Catalogue No.: " + str(catno))

# -------------------------------------------------------------------------------------------

# Tk Widget creation

# -------------------------------------------------------------------------------------------

# Artist input box

artist_input = Entry(root, width=50)
artist_input.insert(0,"Enter artists name here")
artist_input.pack()

# Artist search button

artist_button = Button(root, text="Submit", padx=20, pady=10, command=clicked)
artist_button.pack()

# Release results box

release_box = Listbox(root, width=90)
release_box.pack()

# Release number input box

release_input = Entry(root, width=50)
release_input.insert(0,"Enter release number")
release_input.pack()

# Release search button

release_button = Button(root, text="Submit", padx=20, pady=10, command=submit)
release_button.pack()

# Title box and label

title_label = Label(root, text="Title")
title_label.pack()

title_box = Listbox(root, width=90, height=1)
title_box.pack()

# Tracklist box and label

tracks_label = Label(root, text="Tracklist")
tracks_label.pack()

tracklist_box = Listbox(root, width=90)
tracklist_box.pack()

# Url box and label

url_label = Label(root, text="Discogs Url")
url_label.pack()

url_box = Listbox(root, width=90, height=1)
url_box.pack()

# Formats box and label

format_label = Label(root, text="Formats")
format_label.pack()

format_box = Listbox(root, width=90, height=3)
format_box.pack()

# Sales box and label

sales_label = Label(root, text="Number currently for sale")
sales_label.pack()

sales_box = Listbox(root, width=90, height=1)
sales_box.pack()

# Price box and label

price_label = Label(root, text="Lowest current price ($)")
price_label.pack()

price_box = Listbox(root, width=90, height=1)
price_box.pack()

# Year box and label

year_label = Label(root, text="Year released")
year_label.pack()

year_box = Listbox(root, width=90, height=1)
year_box.pack()

# Country box and label

country_label = Label(root, text="Country")
country_label.pack()

country_box = Listbox(root, width=90, height=1)
country_box.pack()

# Catalogue number box and label

catno_label = Label(root, text="Catalogue number")
catno_label.pack()

catno_box = Listbox(root, width=90, height=1)
catno_box.pack()

# End of mainloop

root.mainloop()








# # API Call
# d = discogs_client.Client('RecordDataFinder/0.1', user_token=os.environ['USER_TOKEN'])

# #Get user input for artist
# search_term = input("Enter Artist Name: ")

# #Create a results object which contains the results of the artist search
# results = d.search(search_term,type='artist')

# #Createa new variable 'artist_id' and assign it the first result from the artist search
# artist_id = results[0].id

# #Create an 'artist' object which contains all data about the artist
# artist = d.artist(artist_id)

# #Loop through the artist releases and print to the console
# for y in artist.releases:
#     print(y)
#  #User input for the requested release
# release_search = input("Enter Release Code: ")

# #Create a record object with the results of the release search
# record = d.release(release_search)

# #Variable creation for release search results
# title = record.title
# tracklist = record.tracklist
# url = record.url
# formats = record.formats

# #More variables with exception handling as they may not exist in the search results
# try:
#     num_for_sale = record.data['num_for_sale']
# except Exception:
#     num_for_sale = "N/A"

# try:
#     lowest_price = record.data['lowest_price']
# except Exception:
#     lowest_price = "N/A"

# try:
#     year = record.data['year']
# except Exception:
#     year = "N/A"

# try:
#     country = record.data['country']
# except Exception:
#     country = "N/A"

# try:
#     catno = record.data['catno']
# except Exception:
#     catno = "N/A"

# #Print final data to the console

# print("\n******** Record Data Finder **********\n")
# print("Title: " + title)
# print("Discogs URL: " + url)
# print("Formats: ")
# for x in formats:
#     print(x)
# print("Tracklist:")
# for x in tracklist:
#     print(x)
# print("Year: " + str(year))
# print("Country: " + country)
# print("Catalogue No: " + str(catno))
# print("Number for sale: " + str(num_for_sale))
# print("Lowest price ($): " + str(lowest_price))