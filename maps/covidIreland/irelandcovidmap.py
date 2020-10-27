import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use("dark_background")

irelandcovid = gpd.read_file("Covid19_LEACases_Mapped-shp/Covid19_LEACases_Mapped.shp")

cases = pd.read_csv("Covid19_LEACases_Mapped.csv")

#pd.set_option('display.max_columns', None)


cases = irelandcovid['C19_P14_T']

for i in range(0,len(cases)):
    try:
        cases[i] = float(cases[i])
    except:
        cases[i] = 3.0

fig = plt.figure()
ax1 = fig.add_subplot(111)

irelandcovid.plot(ax=ax1,column=cases,cmap='Blues')
cbar = plt.cm.ScalarMappable(cmap='Blues',
                           norm=plt.Normalize(
                               vmin=min(cases), vmax=max(cases)))

ax1.axis('off')

cbar = fig.colorbar(cbar)

plt.show()
