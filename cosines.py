import urllib.request
import math

#create a file to write the downloaded data to
f = open("dl_data.csv", "w")
f.close()

#download the data from the url
url = "http://rapid-hub.org/data/angles_UCI_CS.csv"
urllib.request.urlretrieve(url, "dl_data.csv")

#open the new file for reading
f = open("dl_data.csv", "r")
first = True
for line in f:
    line = line.strip("\n")
    if first:
        splitup = line.split(", ")
        print("{}\t{}\tcosines".format(splitup[0], splitup[1]))
        first = False
    else:
        splitup = line.split(",")
        angle = float(splitup[1])
        cosine = math.cos(angle)
        print("{}\t\t{}\t\t{}".format(splitup[0], splitup[1], cosine))
f.close

