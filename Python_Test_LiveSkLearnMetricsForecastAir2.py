import numpy
from sklearn.metrics import r2_score
import csv

# import statistics as st
# import math
# import random

holiday = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 4, 1, 1, 5, 6, 7, 8, 9, 10, 11, 2, 3, 4, 5, 6, 12, 7, 8, 9, 10, 11, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10, 11, 11, 2, 3, 4, 5, 5, 6, 12, 12, 7]
air = [121, 178, 113, 20, 281, 23, 184, 167, 119, 161, 243, 150, 128, 18, 186, 58, 158, 166, 101, 179, 93, 57, 226, 86, 52, 273, 72, 254, 129, 271, 259, 61, 286, 151, 260, 234, 162, 65, 250, 173, 142, 90, 144, 143, 211, 207, 115, 253, 242, 220, 210, 174, 79, 148, 252, 190, 192, 59, 134, 240, 12, 182, 284, 228, 149, 36, 205, 261, 257, 163, 219, 31, 28, 110, 171, 97, 46, 180, 269, 280, 264, 77, 114, 67, 196, 13, 294, 26, 246, 33, 125, 247, 297, 299, 170, 213, 49, 63, 98, 144, 11, 106, 133, 194, 200, 224, 230, 208, 183, 215, 76, 87, 51, 73, 99, 16, 272, 131, 22, 29, 263, 95, 189, 70, 105, 229, 103, 71, 249, 199, 155, 19, 139, 69, 82, 248, 188, 204, 108, 279, 85, 75, 42, 278, 39, 35, 132, 152, 154, 14, 153, 122, 285, 187, 147, 227, 177, 289, 231, 181, 268, 265, 256, 214, 117, 130, 270, 116, 298, 287, 91, 225, 245, 295, 216, 43, 217, 195, 156, 123, 104, 244, 282, 27, 40, 202, 55, 266, 89, 276, 165, 96, 251, 41, 290, 30, 102, 107, 159, 60, 206, 53, 293, 237, 197, 66, 198, 47, 238, 140, 44, 255, 233, 34, 118, 275, 24, 291, 78, 56, 141, 235, 127, 135, 236, 94, 239, 120, 64, 21, 164, 274, 172, 62, 145, 146, 100, 32, 48, 137, 176, 54, 241, 109, 160, 81, 223, 138, 212, 157, 112, 88, 25, 68, 203, 221, 169, 267, 232, 191, 175, 222, 111, 50, 84, 262, 288, 74, 83, 10, 193, 38, 124, 126, 209, 15, 136, 80, 258, 201, 296, 17, 218, 45, 283, 37, 185, 92, 119, 292, 242, 168, 277, 87, 260, 82, 153, 236, 85, 155, 201, 145, 154, 14, 192, 293, 269, 223, 286, 132, 212, 113, 131, 73, 229, 13, 273, 145, 109, 136, 47, 291, 196, 241, 104, 104, 78, 188, 287, 146, 260, 144, 67]

path = "test.csv"
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)  # the first line is the header
data = []

print('date_time', 'air_pollution_index')

for row in reader:
    # row = ['date_time', 'is_holiday', 'humidity', 'wind_speed', 'wind_direction', 'visibility_in_miles', 'dew_point', 'temperature', 'rain_p_h', 'snow_p_h', 'clouds_all', 'weather_type', 'traffic_volume', 'air_pollution_index']
    date_time = str(row[0])
    is_holiday = str(row[1]).replace('None','1').replace('Columbus Day','2').replace('Veterans Day', '3').replace('Thanksgiving Day', '4').replace('Christmas Day', '5').replace('New Years Day', '6').replace('Washingtons Birthday', '7').replace('Memorial Day', '8').replace('Independence Day','9').replace('State Fair','10').replace('Labor Day', '11').replace('Martin Luther King Jr Day', '12').replace('','0')
    humidity = float(row[2])
    wind_speed = float(row[3])
    wind_direction = float(row[4])
    visibility_in_miles = float(row[5])
    dew_point = float(row[6])
    temperature = float(row[7])
    rain_p_h = float(row[8])
    snow_p_h = float(row[9])
    clouds_all = int(row[10])
    weather_type = str(row[11])
    traffic_volume = float(row[12])
       

    x = [date_time, is_holiday, humidity, wind_speed, wind_direction, visibility_in_miles, dew_point, temperature, rain_p_h, snow_p_h, clouds_all, weather_type, traffic_volume]

    data.append(x)

# compute return path

returns_path = "returnsTestFinal.csv"
filex = open(returns_path, 'w', newline='\n', encoding='utf-8')
writer = csv.writer(filex)
writer.writerow(["date_time", "air_pollution_index"])


'''

0.01 = 91.51466
0.02 = 91.51466
0.10 = 91.51466
0.30 = 91.51466
0.50 = 91.51466
0.70 = 91.51466
0.80 = 91.51466
0.90 = 91.51466
0.99 = 
1 = 91.27225
1.01 = 91.27225
1.02 = 91.27225
1.03 = 91.27225
1.10 = 91.27225
1.20 = 91.27225
1.30 = 91.27225
1.40 = 91.27225
1.50 = 91.27225
1.60 = 91.27225
1.70 = 91.27225
1.80 = 91.27225
1.90 = 91.27225
1.99 = 91.27225
2 = 79.08985
3 = 0
4 = 0
5 = 0
6 = 0 
7 = 0 
8 = 0 
9 = 0 
10 = 0 
11 = 0


'''


x_mean = 0.50


for i in range(0, len(data), 1):
    dataFx = data[i]
    date_time = str(dataFx[0]) 
    is_holiday = int(dataFx[1])
    
    mymodel = numpy.poly1d(numpy.polyfit(holiday, air, x_mean))    

    air_pollution_index = int(mymodel(is_holiday))

    #print(date_time, air_pollution_index)
    writer.writerow([date_time, air_pollution_index])
filex.close()
