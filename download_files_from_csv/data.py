import csv, sys
import requests
import urllib.request
from urllib.parse import urlparse
import os

datapath = os.path.dirname(os.path.abspath(__file__))
filename = datapath+'/result20180711175556.csv'
with open(filename, newline='') as f:
    next(f)
    reader = csv.reader(f)
    for row in reader:
        print(row[0])

        url = str(row[0])
        print(url)
        file_name = url[url.rfind("/")+1:]

        result = requests.get(url, stream=True)
        if result.status_code == 200:
            image = result.raw.read()
            open(datapath+'/data_downloaded/'+ file_name,"wb").write(image)


                    # urllib.request.urlretrieve("https://"+url,'data_downloaded/'+ file_name )
