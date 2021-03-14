#Imports

from dotenv import load_dotenv
import os
import discogs_client

# API Call
d = discogs_client.Client('RecordDataFinder/0.1', user_token=os.environ['USER_TOKEN'])

#Get user input for artist
search_term = input("Enter Artist Name: ")

#Create a results object which contains the results of the artist search
results = d.search(search_term,type='artist')

#Createa new variable 'artist_id' and assign it the first result from the artist search
artist_id = results[0].id

#Create an 'artist' object which contains all data about the artist
artist = d.artist(artist_id)

#Loop through the artist releases and print to the console
for y in artist.releases:
    print(y)
 #User input for the requested release
release_search = input("Enter Release Code: ")

#Create a record object with the results of the release search
record = d.release(release_search)

#Variable creation for release search results
title = record.title
tracklist = record.tracklist
url = record.url
formats = record.formats

#More variables with exception handling as they may not exist in the search results
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

#Print final data to the console

print("\n******** Record Data Finder **********\n")
print("Title: " + title)
print("Discogs URL: " + url)
print("Formats: ")
for x in formats:
    print(x)
print("Tracklist:")
for x in tracklist:
    print(x)
print("Year: " + str(year))
print("Country: " + country)
print("Catalogue No: " + str(catno))
print("Number for sale: " + str(num_for_sale))
print("Lowest price ($): " + str(lowest_price))