"""
Created on Thu Oct  4 10:32:30 2018

@author: benjamin.o.larking
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Where our data is
csv_path="C:\\Users\\benjamin.o.larking\\Documents\\GitHubProjects\\Python\\DataScience\\DataSets\\artwork_data.csv"

csv_df = pd.read_csv(csv_path)

# Count how many of each acquisition years. Pandas has a basic plot function
acquisition_years = csv_df.groupby('acquisitionYear').size()
acquisition_years.plot()


# Option to tweek some params for our figure
rcParams.update({'figure.autolayout' : True, 
                 'axes.titlepad' : 20 })

# Master figure with a subplot with 1 row and 1 column. The thrid 1 means we want to place out axxes in position 1
fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
acquisition_years.plot(ax=subplot)
fig.show()

# More Advanced Figure / Plot
# Add Axis 
fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
acquisition_years.plot(ax=subplot)
subplot.set_xlabel("Acquisition Year")
subplot.set_ylabel("Artworks Aquired")
fig.show()

# Increase Granularity
fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
# Rotate ticks 45 degrees 
acquisition_years.plot(ax=subplot, rot=45)
subplot.set_xlabel("Acquisition Year")
subplot.set_ylabel("Artworks Aquired")
# We want 40 ticks on the x axis 
subplot.locator_params(nbins=40, axis='x')
fig.show()


title_font = {
        'family' : 'source sans pro',
        'color' : 'darkblue',
        'weight' : 'normal', 
        'size' : 20
        }

labels_font = {
        'family' : 'consolas',
        'color' : 'darkred',
        'weight' : 'normal', 
        'size' : 16
        }

# Change to Log Scale, add a grid and set title / fonts
fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
# Rotate ticks 45 degrees and scale the y axis using log
acquisition_years.plot(ax=subplot, rot=45, logy=True, grid=True)
subplot.set_xlabel("Acquisition Year", fontdict=labels_font, labelpad=10)
subplot.set_ylabel("Artworks Aquired", fontdict=labels_font)
# We want 40 ticks on the x axis 
subplot.locator_params(nbins=40, axis='x')
subplot.set_title("Tate Gallery Acquisitions", fontdict=title_font)
fig.show()

# Saving Figures
fig.savefig("plot.png")
fig.savefig('plot.svg', format='svg')
