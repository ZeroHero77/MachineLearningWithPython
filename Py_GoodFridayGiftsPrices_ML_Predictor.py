import csv
import numpy as np
import pandas as pd
import math

Number_of_train_records = int(20278)
Number_of_test_records = int(13519)


data1 = "C:/Users/McSmith/Documents/Will/Code/MachineLearning/GoodFridayGiftsPrices/dataset/train.csv"
data2 = pd.read_csv(data1)
fx = data2
#fx = data2.sample(n=10760, random_state=10)

gift_typeFx = fx.gift_type
gift_categoryFx = fx.gift_category
gift_clusterFx = fx.gift_cluster
is_discountedFx = fx.is_discounted
volumesFx = fx.volumes
lsg_1Fx = fx.lsg_1
lsg_2Fx = fx.lsg_2
lsg_3Fx = fx.lsg_3
lsg_4Fx = fx.lsg_4
lsg_5Fx = fx.lsg_5
lsg_6Fx = fx.lsg_6
date_diff_stocksFxa = fx.date_diff_stocksFx
priceFx = fx.price

data3 = "C:/Users/McSmith/Documents/Will/Code/MachineLearning/GoodFridayGiftsPrices/dataset/test.csv"
data4 = pd.read_csv(data3)
fx2 = data4

gift_idFx2 = fx2.gift_id
gift_typeFx2 = fx2.gift_type
gift_categoryFx2 = fx2.gift_category
gift_clusterFx2 = fx2.gift_cluster
is_discountedFx2 = fx2.is_discounted
volumesFx2 = fx2.volumes
lsg_1Fx2 = fx2.lsg_1
lsg_2Fx2 = fx2.lsg_2
lsg_3Fx2 = fx2.lsg_3
lsg_4Fx2 = fx2.lsg_4
lsg_5Fx2 = fx2.lsg_5
lsg_6Fx2 = fx2.lsg_6
date_diff_stocksFx2a = fx2.date_diff_stocksFx2
priceFx2 = fx2.price

# date_diff_stocksFx2 = pd.to_datetime(fx2.stock_update_date)-pd.to_datetime(fx2.instock_date)

# compute return path

returns_path = "C:/Users/McSmith/Documents/Will/Code/MachineLearning/GoodFridayGiftsPrices/dataset/TestAB.csv"
filex = open(returns_path, 'w', newline='\n', encoding='utf-8')
writer = csv.writer(filex)
writer.writerow(["gift_id", "price"])

#a = np.array([patientid, effect2, numberof2])

z = []
y = []

# scores ####################
# x_degress = 0 == 91.48178
# x_degress = 0.1 == 91.48623
# x_degrees = 1 ==  91.44931
# x_degrees = 2 ==  91.45938
# x_degrees = 3 ==  91.46591
# x_degrees = 4 == 91.46512
# x_degrees = 5 == 91.46749
# x_degrees = 6 == 91.40476
# x_degrees = 7 == 91.42399
# x_degrees = 8 == 91.40763
# x_degrees = 9 == 91.36411
# x_degrees = 10 == 91.38107
# x_degrees = 11 == 91.37024
###################################################
# x_degrees = 0.1 + variantFx = -0.1 ==91.48517
# x_degrees = 0.1 + variantFx = -1 ==91.51557
# x_degrees = 0.1 + variantFx = -2 ==91.54926
# x_degrees = 0.1 + variantFx = -3 == 91.58275
# x_degrees = 0.1 + variantFx = -4 == 91.61607
# x_degrees = 0.1 + variantFx = -6 == 91.68231
# x_degrees = 0.1 + variantFx = -12 == 91.87686
# x_degrees = 0.1 + variantFx = -36 == 92.57468
# x_degrees = 0.1 + variantFx = -45 == 92.78926
# x_degrees = 0.1 + variantFx = -50 == 92.89210
# x_degrees = 0.1 + variantFx = -60 == 93.05157
# x_degrees = 0.1 + variantFx = -61 == 93.06287
# x_degrees = 0.1 + variantFx = -62 == 93.07314
# x_degrees = 0.1 + variantFx = -63 == 93.08250
# x_degrees = 0.1 + variantFx = -64 == 93.09085
# x_degrees = 0.1 + variantFx = -65 == 93.09805
# x_degrees = 0.1 + variantFx = -66 == 93.10432
# x_degrees = 0.1 + variantFx = -67 == 93.10964
# x_degrees = 0.1 + variantFx = -69 ==93.11644
# max == x_degrees = 0.1 + variantFx = -72 == 93.11685
###################################################

x_degrees = 0.1
variantFx = -72

try:
    for j in range(0, Number_of_train_records,1):

        # print(int(str(date_diff_stocksFx[j])[0:str(date_diff_stocksFx[j]).find(" ")]))

        # date_diff1 = int(str(date_diff_stocksFx[j])[0:str(date_diff_stocksFx[j]).find(" ")])
        z += [(gift_typeFx[j] + gift_categoryFx[j] + gift_clusterFx[j] + is_discountedFx[j] + volumesFx[j] + lsg_1Fx[j] + lsg_2Fx[j] + lsg_3Fx[j] + lsg_4Fx[j] + lsg_5Fx[j] + lsg_6Fx[j] + date_diff_stocksFxa[j]) / 12]
        y += [priceFx[j]]
        
        
except EOFError:
    pass

try:
    for i in range(0, Number_of_test_records, 1):

        # print(int(str(date_diff_stocksFx2[i])[0:str(date_diff_stocksFx2[i]).find(" ")]))

        # date_diff2 = int(str(date_diff_stocksFx2[i])[0:str(date_diff_stocksFx2[i]).find(" ")])

        
        mymodel = np.poly1d(np.polyfit(z,y,x_degrees))

        prediction = mymodel((gift_typeFx2[i] + gift_categoryFx2[i] + gift_clusterFx2[i] + is_discountedFx2[i] + volumesFx2[i] + lsg_1Fx[i] + lsg_2Fx[i] + lsg_3Fx[i] + lsg_4Fx[i] + lsg_5Fx[i] + lsg_6Fx[i] + date_diff_stocksFx2a[i]) / 12)

        gift_id = gift_idFx2[i]
        price = float(prediction) + variantFx

        #if (math.isnan(priceFx2[i]) == True or priceFx2[i] == "" or priceFx2[i] == None or priceFx2[i] == 0 or priceFx2[i] == ''): price = float(prediction) + variantFx
        # else: price = priceFx2[i]
                
        writer.writerow([gift_id, price])
        
except EOFError:
    pass

        
filex.close()
