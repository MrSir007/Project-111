import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as pgo
import plotly.figure_factory as pff
import statistics
import random

getData = pd.read_csv("medium_data.csv")
readingtimeList = getData["reading_time"].tolist()

def findMean (counter) :
  getSample = []
  for i in range (0,30) :
    index = random.randint(0,len(readingtimeList)-1)
    value = readingtimeList[index]
    getSample.append(value)
  global meanFind 
  meanFind = statistics.mean(getSample)
  return meanFind

meanlist = []
for i in range (0,100) :
  meanFind = findMean(100)
  meanlist.append(meanFind)
meanMeanlist = statistics.mean(meanlist)
sdMeanlist = statistics.stdev(meanlist)

def graph () :
  graph = px.scatter(meanlist)
  graph.show()

sd1S, sd1E = meanMeanlist - sdMeanlist, meanMeanlist + sdMeanlist
sd2S, sd2E = meanMeanlist - 2*sdMeanlist, meanMeanlist + 2*sdMeanlist
sd3S, sd3E = meanMeanlist - 3*sdMeanlist, meanMeanlist + 3*sdMeanlist

distribution = pff.create_distplot([meanlist], ["student marks"], show_hist=False)
distribution.add_trace(pgo.Scatter(x=[meanMeanlist, meanMeanlist], y=[0, 0.17], mode="lines", name="MEAN"))
distribution.add_trace(pgo.Scatter(x=[meanFind, meanFind], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO USED THE APP"))
distribution.add_trace(pgo.Scatter(x=[sd1S, sd1E], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
distribution.add_trace(pgo.Scatter(x=[sd2S, sd2E], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
distribution.add_trace(pgo.Scatter(x=[sd3S, sd3E], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
distribution.show()

zscore = (meanFind - meanMeanlist) / sdMeanlist
print(zscore)