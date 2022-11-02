# Begin by importing pandas and matplotlib modules for Dataframe calculations and visualization

import pandas as pd
import matplotlib.pyplot as plt

# Using formatted date, concatenates Google search for news article

def googler(date):
    return (str(date) + " fire Louisville Kentucky")

# Visualizer plotting injury count over injury dates, setting up labels

def visualizer(x, y):
    plt.plot(x, y, marker = "^", linestyle = "None")
    plt.xlabel("Date of Incident")
    plt.ylabel("Fire Injuries per Incident")
    plt.title("Documented Fire Incidents in Louisville, Kentucky from 2005 to 2016")
    plt.grid(True)
    plt.show()

# Reads in CSV, converts injuryDate to datetime, concatenating dates for Google searches
# into written text file, selecting only incidents involving more than one
# fire injury, then calls visualization

def main():
    df = pd.read_csv("assets/fireInjuries.csv")
    injuryDate = pd.to_datetime(df["Injury_Date"], errors = "coerce")
    totalInjuries = df["Total_Injuries"]

    searches = open("googleSearches.txt", "w")
    count = 0
    for line in injuryDate:
        if df["Total_Injuries"][count] > 1:
            print(googler(line.strftime("%Y-%m-%d")))
            searches.writelines(googler(line.strftime("%Y-%m-%d")))
        count += 1
    searches.close()

    visualizer(injuryDate, totalInjuries)

# Calls the main program into existence

main()