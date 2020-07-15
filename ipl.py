import csv
import matplotlib.pyplot as plt
import numpy as np


def read_file(file):
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        temp = []
        for row in csv_reader:
            temp.append(row)
    return temp


def team_total():
    file = read_file("deliveries.csv")
    line_c = 0
    total_runs = {}
    for row in file:
        if line_c == 0:
            line_c += 1
        else:
            if row[2] not in total_runs:
                total_runs[row[2]] = int(row[17])
            else:
                total_runs[row[2]] += int(row[17])
    list1 = sorted(total_runs.items())
    x, y = zip(*list1)
    plt.figure(figsize=(15, 10))
    plt.barh(x, y, align='center')
    plt.title("Total runs scored by team", fontweight='bold')
    plt.ylabel("Teams", fontweight='bold')
    plt.xlabel("Total Runs", fontweight='bold')
    plt.show()


def rcb_total():
    file = read_file("deliveries.csv")
    line_c = 0
    rcb_batsman = {}
    for row in file:
        if line_c == 0:
            line_c += 1
        else:
            if row[2] == "Royal Challengers Bangalore":
                if row[6] not in rcb_batsman:
                    rcb_batsman[row[6]] = int(row[15])
                else:
                    rcb_batsman[row[6]] += int(row[15])
    list2 = sorted(rcb_batsman.items())
    a, b = zip(*list2)
    plt.figure(figsize=(15, 20))
    plt.bar(a, b)
    plt.title("Top batsman for Royal Challengers Bangalore", fontweight='bold')
    plt.xlabel("Batsman", fontweight='bold')
    plt.ylabel("Total Runs", fontweight='bold')
    plt.xticks(rotation=90)
    plt.show()


def umpire_country():
    file = read_file("umpires.csv")
    line_c = 0
    umpire_list = []
    for row in file:
        if line_c == 0:
            line_c += 1
        else:
            if row[1] == "India":
                continue
            else:
                umpire_list.append(row[1])
    umpire_dict = {}
    for x in umpire_list:
        if x not in umpire_dict:
            umpire_dict[x] = 1
        else:
            umpire_dict[x] += 1
    list5 = sorted(umpire_dict.items())
    u, v = zip(*list5)
    plt.figure(figsize=(15, 10))
    plt.bar(u, v)
    plt.title("Foreign umpire analysis", fontweight='bold')
    plt.xlabel("Country", fontweight='bold')
    plt.ylabel("Number of Umpires", fontweight='bold')
    plt.show()


def by_season():
    file = read_file("matches.csv")
    season = {}
    line_c = 0
    for row in file:
        if line_c == 0:
            line_c += 1
        else:
            if row[1] not in season:
                season[row[1]] = {}
            else:
                if row[4] not in season[row[1]]:
                    season[row[1]][row[4]] = 1
                else:
                    season[row[1]][row[4]] += 1
    teams = ['Gujarat Lions', 'Rising Pune Supergiant',
             'Royal Challengers Bangalore',
             'Kolkata Knight Riders', 'Delhi Daredevils',
             'Sunrisers Hyderabad',
             'Kings XI Punjab', 'Mumbai Indians', 'Chennai Super Kings',
             'Rajasthan Royals', 'Deccan Chargers', 'Pune Warriors',
             'Kochi Tuskers Kerala']
    team_short = ['GL', 'RPS', 'RCB', 'KKR', 'DD', 'SRH', 'KXIP', 'MI', 'CSK',
                  'RR', 'DC', 'PW', 'KTK']
    team_list = []
    for year in sorted(season):
        score = []
        for team in teams:
            score.append(season[year].get(team, 0))
        team_list.append(score)
    barwidth = 0.08
    r1 = np.arange(len(team_list[0]))
    r2 = [x + barwidth for x in r1]
    r3 = [x + barwidth for x in r2]
    r4 = [x + barwidth for x in r3]
    r5 = [x + barwidth for x in r4]
    r6 = [x + barwidth for x in r5]
    r7 = [x + barwidth for x in r6]
    r8 = [x + barwidth for x in r7]
    r9 = [x + barwidth for x in r8]
    r10 = [x + barwidth for x in r9]

    plt.figure(figsize=(15, 10))
    plt.bar(r1, team_list[0], width=barwidth, edgecolor='white',
            label='2008')
    plt.bar(r2, team_list[1], width=barwidth, edgecolor='white',
            label='2009')
    plt.bar(r3, team_list[2], width=barwidth, edgecolor='white',
            label='2010')
    plt.bar(r4, team_list[3], width=barwidth,
            edgecolor='white', label='2011')
    plt.bar(r5, team_list[4], width=barwidth,
            edgecolor='white', label='2012')
    plt.bar(r6, team_list[5], width=barwidth,
            edgecolor='white', label='2013')
    plt.bar(r7, team_list[6], width=barwidth, edgecolor='white',
            label='2014')
    plt.bar(r8, team_list[7], width=barwidth, edgecolor='white',
            label='2015')
    plt.bar(r9, team_list[8], width=barwidth, edgecolor='white',
            label='2016')
    plt.bar(r10, team_list[9], width=barwidth, edgecolor='white',
            label='2017')

    plt.xlabel('group', fontweight='bold')
    plt.ylabel('games played', fontweight='bold')
    plt.title("Games played by teams per season", fontweight='bold')
    plt.xticks([r + barwidth for r in range(len(team_list[0]))], team_short)
    plt.legend()
    plt.show()


def main():
    team_total()

    rcb_total()

    umpire_country()

    by_season()


if __name__ == "__main__":
    main()
