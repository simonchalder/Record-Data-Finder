from dotenv import load_dotenv
import os
import discogs_client
print('USER_TOKEN' in os.environ)
d = discogs_client.Client('RecordDataFinder/0.1', user_token=os.environ['USER_TOKEN'])

results = d.search('Physical Graffiti', type='release')
#print(dir(results[0].artists[0]))
print(results[0].artists[0])
print(results[0].labels[0])
print(results[0].formats[0])
for x in results[0].tracklist:
    print(x)
print(results[0].data['num_for_sale'])
print(results[0].data['lowest_price'])
print(results[0].data['year'])
print(results[0].data['country'])

#for y in results:
#    print(y)