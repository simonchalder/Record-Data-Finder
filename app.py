from dotenv import load_dotenv
import os
import discogs_client

d = discogs_client.Client('RecordDataFinder/0.1', user_token="ebrELjhwzwbrWOcmGapdIrSpFRAyFwDMXrvgydzF")

results = d.search('Physical Graffiti', type='release')
print(dir(results[0].artists[0]))
print(results[0].artists[0])
print(results[0].labels[0])
print(results[0].formats[0])
for x in results[0].tracklist:
    print(x)