import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import mplcursors

style.use("dark_background")
irelandcovid = gpd.read_file("Covid19_LEACases_Mapped-shp/Covid19_LEACases_Mapped.shp")
cases = pd.read_csv("Covid19_LEACases_Mapped.csv")

pd.set_option('display.max_columns', None)
cases = irelandcovid['C19_P14_T']
populations = irelandcovid['Pop2016']

for i in range(0,len(cases)):
    try:
        cases[i] = float(cases[i])
        #print("POPULATION:",irelandcovid["Pop2016"][i],irelandcovid['ENGLISH'][i],":",cases[i])
        #EVIDENT CORRELATION BETWEEN POPULATION AND CASES
    except:
        cases[i] = 1

figcorr = plt.figure()
figcorr.suptitle("Correlation between population of a location and recorded Covid19 cases")
axcorr = figcorr.add_subplot(111)

plt.scatter(populations,cases)

mplcursors.cursor(axcorr).connect(
    "add", lambda sel: sel.annotation.set_text(
        irelandcovid["ENGLISH"][sel.target.index]))
figmap = plt.figure()
axmap = figmap.add_subplot(111)
figmap.suptitle("Covid19 cases around ireland")
irelandcovid.plot(ax=axmap,column=cases,cmap='Blues')

cbar = plt.cm.ScalarMappable(cmap='Blues',norm=plt.Normalize(vmin=min(cases), vmax=max(cases)))
axmap.axis('off')
cbar = figmap.colorbar(cbar)

plt.show()
