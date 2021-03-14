#Imports

from dotenv import load_dotenv
import os
import discogs_client

# API Call
d = discogs_client.Client('RecordDataFinder/0.1', user_token=os.environ['USER_TOKEN'])

search_term = input("Enter Artist Name: ")

results = d.search(search_term,type='artist')

artist_id = results[0].id

artist = d.artist(artist_id)
for y in artist.releases:
    print(y)

release_search = input("Enter Release Code: ")
record = d.release(release_search)

title = record.title
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

print(catno)