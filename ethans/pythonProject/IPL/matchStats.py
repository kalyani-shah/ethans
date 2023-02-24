import csv
infile = open(r'./../IPL/matches.csv')

def showTeams():
    print('''===Select a team===
1. Sunrisers Hyderabad
2. Rising Pune Supergiant
3. Kolkata Knight Riders
4. Chennai Super Kings
5. Rajasthan Royals
6. Royal Challengers Bangalore
7. Mumbai Indians
8. Kings XI Punjab
9. Deccan Chargers
10. Kochi Tuskers Kerala''')

    team = int(input('enter a team name:'))

    if team ==1:
        return'Sunrisers Hyderabad'
    elif team==2:
        return'Rising Pune Supergiant'
    elif team==3:
        return'Kolkata Knight Riders'
    elif team==4:
        return'Chennai Super Kings'
    elif team==5:
        return'Rajasthan Royals'
    elif team==6:
        return'Royal Challengers Bangalore'
    elif team==7:
        return'Mumbai Indians'
    elif team==8:
        return'Kings XI Punjab'
    elif team==9:
        return'Deccan Chargers'
    elif team==10:
        return'Kochi Tuskers Kerala'
    else:
        print('!!! ENTER TEAM NUMBER CORRECTLY !!!','\n')
        return showTeams()


def tossWin(a):
    listToss=['a','b']
    listToss[0]=0
    listToss[1]=0

    csvobj=csv.DictReader(infile)
    infile.seek(0)
    for each in csvobj:
        if a in each['TEAM1'] or a in each['TEAM2']:
            listToss[0] += 1
        if a in each['TOSS_WINNER']:
            listToss[1]+=1
    return listToss

def yearWise_WonPlayed(b):
    csvobj=csv.DictReader(infile)
    infile.seek(0)
    l1=[]
    l2=[]
    for each in csvobj:
        if b in each['TEAM1'] or b in each['TEAM2']:
            l1.append(each['SEASON'])
            l2=list(set(l1))
    count=0
    for each in csvobj:
        if b in each['TEAM1'] or b in each['TEAM2']:
            if b in each['l2']:
                count+=1
    return l2































