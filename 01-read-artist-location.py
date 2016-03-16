import pandas as pd

inCSV = '/Users/danielmsheehan/Dropbox/GIS/Data/Commercial/spotify/data/artist_location.txt'

df = pd.read_csv(inCSV, sep='<SEP>', header=None)

df.columns = ['id','lat','lng','bandname','loc'] 

print df.head(100)

df.to_csv('/Users/danielmsheehan/Dropbox/GIS/Data/Commercial/spotify/data/artist_location.csv', index=False)