import statistics as st
import csv
import math
import random

train_troops_mobilized_to_defcon_level_1 = st.NormalDist.from_samples([748000, 765600, 792000, 800800, 809600, 814000, 818400, 827200, 836000, 840400, 844800, 853600, 862400, 871200, 875600, 880000, 888800, 897600, 906400, 915200, 924000, 932800, 941600, 959200, 968000, 976800, 985600, 994400, 1003200, 1012000, 1020800, 1029600, 1038400, 1047200, 1056000, 1064800, 1073600, 1082400, 1091200, 1100000, 1108800, 1126400, 1135200])

train_troops_mobilized_to_defcon_level_2 =st.NormalDist.from_samples([739200, 748000, 765600, 774400, 792000, 796400, 800800, 809600, 812533.3333, 814000, 818400, 827200, 836000, 840400, 841866.6667, 844800, 853600, 862400, 871200, 875600, 880000, 882933.3333, 888800, 897600, 906400, 915200, 924000, 928400, 932800, 941600, 946000, 950400, 959200, 968000, 976800, 985600, 994400, 1003200, 1012000, 1020800, 1029600, 1038400, 1047200, 1051600, 1056000, 1064800, 1073600, 1082400, 1091200, 1100000, 1108800, 1117600, 1126400, 1135200, 1144000, 1152800, 1170400, 1193866.667, 1196800, 1232000, 1311200])

train_troops_mobilized_to_defcon_level_3 =st.NormalDist.from_samples([739200, 765600, 774400, 792000, 800800, 809600, 812533.3333, 814000, 818400, 827200, 836000, 840400, 841866.6667, 844800, 853600, 862400, 871200, 875600, 880000, 888800, 897600, 906400, 915200, 924000, 928400, 932800, 941600, 946000, 950400, 959200, 968000, 973866.6667, 976800, 985600, 994400, 1003200, 1012000, 1020800, 1029600, 1038400, 1047200, 1051600, 1056000, 1064800, 1073600, 1082400, 1091200, 1100000, 1108800, 1117600, 1126400, 1135200, 1144000, 1152800, 1170400, 1179200, 1188000, 1193866.667, 1196800, 1232000])

train_troops_mobilized_to_defcon_level_4 = st.NormalDist.from_samples([792000, 800800, 809600, 818400, 827200, 836000, 844800, 853600, 862400, 871200, 875600, 880000, 888800, 897600, 906400, 915200, 924000, 928400, 932800, 941600, 946000, 950400, 959200, 968000, 973866.6667, 976800, 985600, 994400, 1003200, 1012000, 1020800, 1029600, 1038400, 1047200, 1051600, 1056000, 1064800, 1073600, 1082400, 1091200, 1100000, 1108800, 1117600, 1126400, 1135200, 1144000, 1152800, 1161600, 1170400, 1179200, 1188000, 1193866.667, 1196800, 1232000, 1311200])

train_troops_mobilized_to_defcon_level_5 = st.NormalDist.from_samples([792000, 809600, 818400, 836000, 844800, 853600, 862400, 871200, 880000, 888800, 897600, 924000, 932800, 941600, 959200, 968000, 976800, 985600, 994400, 1012000, 1020800, 1029600, 1038400, 1056000, 1073600, 1082400, 1091200, 1100000, 1108800, 1117600, 1126400, 1135200, 1144000, 1179200, 1188000, 1196800, 1232000, 1311200])

path = "test.csv"
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)  # the first line is the header
data = []

print('ID', 'DEFCON_Level')

for row in reader:
    # row = ['Allied_Nations', 'Diplomatic_Meetings_Set', 'Percent_Of_Forces_Mobilized', 'Hostile_Nations', 'Active_Threats', 'Inactive_Threats', 'Citizen_Fear_Index', 'Closest_Threat_Distance(km)', 'Aircraft_Carriers_Responding', 'Troops_Mobilized(thousands)', 'ID', 'DEFCON_Level']
    Allied_Nations = float(row[0])
    Diplomatic_Meetings_Set = float(row[1])
    Percent_Of_Forces_Mobilized = float(row[2])
    Hostile_Nations = float(row[3])
    Active_Threats = float(row[4])
    Inactive_Threats = float(row[5])
    Citizen_Fear_Index = float(row[6])
    Closest_Threat_Distance = float(row[7])
    Aircraft_Carriers_Responding = float(row[8])
    Troops_Mobilized = float(row[9])
    ID = int(row[10])
    DEFCON_Level = int(row[11])

    x = [Allied_Nations, Diplomatic_Meetings_Set, Percent_Of_Forces_Mobilized, Hostile_Nations, Active_Threats, Inactive_Threats, Citizen_Fear_Index, Closest_Threat_Distance, Aircraft_Carriers_Responding, Troops_Mobilized, ID, DEFCON_Level]

    data.append(x)

# compute return path

returns_path = "returnsTestFinal.csv"
filex = open(returns_path, 'w', newline='\n', encoding='utf-8')
writer = csv.writer(filex)
writer.writerow(["ID", "DEFCON_Level"])


'''
26.4%
DEFCON_1 = 0.10
DEFCON_2 = 0.33
DEFCON_3 = 0.33
DEFCON_4 = 0.12
DEFCON_5 = 0.12

26.0%
DEFCON_1 = 0.10
DEFCON_2 = 0.32
DEFCON_3 = 0.32
DEFCON_4 = 0.13
DEFCON_5 = 0.13

25.8%
DEFCON_1 = 0.10
DEFCON_2 = 0.31
DEFCON_3 = 0.31
DEFCON_4 = 0.14
DEFCON_5 = 0.14

24.9%
DEFCON_1 = 0.10
DEFCON_2 = 0.30
DEFCON_3 = 0.30
DEFCON_4 = 0.15
DEFCON_5 = 0.15


23.3%
DEFCON_1 = 0.12
DEFCON_2 = 0.30
DEFCON_3 = 0.30
DEFCON_4 = 0.14
DEFCON_5 = 0.14

23.1%
DEFCON_1 = 0.14
DEFCON_2 = 0.29
DEFCON_3 = 0.29
DEFCON_4 = 0.14
DEFCON_5 = 0.14

23.4%
DEFCON_1 = 0.16
DEFCON_2 = 0.28
DEFCON_3 = 0.28
DEFCON_4 = 0.14
DEFCON_5 = 0.14

25.1%
DEFCON_1 = 0.18
DEFCON_2 = 0.27
DEFCON_3 = 0.27
DEFCON_4 = 0.14
DEFCON_5 = 0.14

42.51311
DEFCON_1 = 0.20
DEFCON_2 = 0.26
DEFCON_3 = 0.26
DEFCON_4 = 0.14
DEFCON_5 = 0.14

42.57597
DEFCON_1 = 0.18
DEFCON_2 = 0.27
DEFCON_3 = 0.27
DEFCON_4 = 0.12
DEFCON_5 = 0.16

21.42802
DEFCON_1 = 0.22
DEFCON_2 = 0.25
DEFCON_3 = 0.25
DEFCON_4 = 0.14
DEFCON_5 = 0.14

10.65602
DEFCON_1 = 0.24
DEFCON_2 = 0.24
DEFCON_3 = 0.24
DEFCON_4 = 0.14
DEFCON_5 = 0.14

23.51644
DEFCON_1 = 0.20  # set
DEFCON_2 = 0.24
DEFCON_3 = 0.28
DEFCON_4 = 0.14  # set
DEFCON_5 = 0.14  # set



'''


# 43.73471 - my record


'''

42.57597
DEFCON_1 = 0.18
DEFCON_2 = 0.27
DEFCON_3 = 0.27
DEFCON_4 = 0.12
DEFCON_5 = 0.16

42.58167%
DEFCON_1 = 0.19  # set
DEFCON_2 = 0.27
DEFCON_3 = 0.27
DEFCON_4 = 0.12  # set
DEFCON_5 = 0.15  # set

# 42.31141%
DEFCON_1 = 0.20  # set
DEFCON_2 = 0.30  # set
DEFCON_3 = 0.30  # set
DEFCON_4 = 0.10  # set  
DEFCON_5 = 0.10  # set

# 42.58846%
DEFCON_1 = 0.10  # set
DEFCON_2 = 0.30  # set
DEFCON_3 = 0.30  # set
DEFCON_4 = 0.10  # set  
DEFCON_5 = 0.20  # set

'''

# 42.58846%
DEFCON_1 = 0.10  # set
DEFCON_2 = 0.30  # set
DEFCON_3 = 0.30  # set
DEFCON_4 = 0.10  # set  
DEFCON_5 = 0.20  # set


for i in range(0, len(data), 1):
    dataFx = data[i]
    Troops_Mobilized = dataFx[9] 
    ID = dataFx[10]
    DEFCON_Level = dataFx[11]

    posterior_DEFCON_1 = (DEFCON_1 * train_troops_mobilized_to_defcon_level_1.pdf(Troops_Mobilized))
    posterior_DEFCON_2 = (DEFCON_2 * train_troops_mobilized_to_defcon_level_2.pdf(Troops_Mobilized))
    posterior_DEFCON_3 = (DEFCON_3 * train_troops_mobilized_to_defcon_level_3.pdf(Troops_Mobilized))
    posterior_DEFCON_4 = (DEFCON_4 * train_troops_mobilized_to_defcon_level_4.pdf(Troops_Mobilized))
    posterior_DEFCON_5 = (DEFCON_5 * train_troops_mobilized_to_defcon_level_5.pdf(Troops_Mobilized))


    posterior_DEFCON_1 = float(posterior_DEFCON_1)
    posterior_DEFCON_2 = float(posterior_DEFCON_2)
    posterior_DEFCON_3 = float(posterior_DEFCON_3)
    posterior_DEFCON_4 = float(posterior_DEFCON_4)
    posterior_DEFCON_5 = float(posterior_DEFCON_5)
    d1 = [posterior_DEFCON_2, posterior_DEFCON_3, posterior_DEFCON_4, posterior_DEFCON_5]
    d2 = [posterior_DEFCON_1, posterior_DEFCON_3, posterior_DEFCON_4, posterior_DEFCON_5]
    d3 = [posterior_DEFCON_1, posterior_DEFCON_2, posterior_DEFCON_4, posterior_DEFCON_5]
    d4 = [posterior_DEFCON_1, posterior_DEFCON_2, posterior_DEFCON_3, posterior_DEFCON_5]
    d5 = [posterior_DEFCON_1, posterior_DEFCON_2, posterior_DEFCON_3, posterior_DEFCON_4]

    if all(d <= posterior_DEFCON_1 for d in d1):
                          DEFCON_Level = 1
    elif all(e <= posterior_DEFCON_2 for e in d2):
                          DEFCON_Level = 2
    elif all(f <= posterior_DEFCON_3 for f in d3):
                          DEFCON_Level = 3
    elif all(g <= posterior_DEFCON_4 for g in d4):
                          DEFCON_Level = 4
    elif all(h <= posterior_DEFCON_5 for h in d5):
                          DEFCON_Level = 5
    else:
        DEFCON_Level = 0

    #print(ID, posterior_DEFCON_1, posterior_DEFCON_2, posterior_DEFCON_3, posterior_DEFCON_4, posterior_DEFCON_5)
    #print(ID, DEFCON_Level)
    writer.writerow([ID, DEFCON_Level])
filex.close()
