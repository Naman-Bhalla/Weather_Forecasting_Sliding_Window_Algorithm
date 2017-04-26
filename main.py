# author : naman-bhalla
# title : Weather Forecasting Using Sliding Window Algorithm
# for more details :- https://www.hindawi.com/journals/isrn/2013/156540/

from scipy.spatial import distance
#-------------- TEST ONLY
#import random
#-------------- TEST ONLY

def enter_data(year):
    if year == "present":
        slots = 7
    elif year == "last":
        slots = 14

    data_list = []

    for num in range(slots):

        value = []

        for slot in range(4):

            if slot == 0:
                quantity = "max_temp"
            elif slot == 1:
                quantity = "min_temp"
            elif slot == 2:
                quantity = "humidity"
            elif slot == 3:
                quantity = "rainfall"

            print("Please enter the", quantity, "for day",str(num + 1), "for", year, "year:- ")

            #-------------- TEST ONLY
            ##print(data)
            #-------------- TEST ONLY

            data = int(input())
            value.append(data)

        data_list.append(value)

    return data_list

def create_sliding_windows():
    sliding_windows = []

    for num in range(8):
        value = data_past_year[num: num + 7]
        sliding_windows.append(value)

    return sliding_windows

def calculate_mean(array):
    ans = (sum(array) / len(array))
    return ans

def each_sliding_windows_dist():
    dic = {}
    lis = []
    iter_a = 0
    iter_b = 0
    while iter_a < 8:
        while iter_b < 7:
            entries = data_past_slidingWindow[iter_a][iter_b]
            value = data_present_year[iter_b]
            dist = distance.euclidean(entries, value)
            lis.append(dist)
            iter_b += 1
        lis_mean = calculate_mean(lis)
        dic[iter_a] = lis_mean
        lis = []
        iter_b = 0
        iter_a += 1
    return dic

def min_value_dic(dic):
    v = list(dic.values())
    k = list(dic.keys())
    return k[v.index(min(v))]


def variation():
    var = []
    ans = 0
    for iter_up in range(4):
        for iter_l in range(6):
            ans += (closest_sliding_window[iter_l + 1][iter_up] - closest_sliding_window[iter_l][iter_up])
        for iter_n in range(6):
            ans += (data_present_year[iter_n + 1][iter_up] - data_present_year[iter_n][iter_up])
        val = ans / 12
        var.append(val)
        ans = 0
    return var

def prediction():
    pred = []
    for i in range(4):
        val = 0
        val = data_present_year[6][i] + variation[i]
        pred.append(val)
    return pred

data_past_year = enter_data("last")
data_present_year = enter_data("present")
data_past_slidingWindow = create_sliding_windows()
sliding_dist_dic = each_sliding_windows_dist()
min_distance_sliding_index = min_value_dic(sliding_dist_dic)
closest_sliding_window = data_past_slidingWindow[min_distance_sliding_index]
variation = variation()
prediction = prediction()

#-------------- TEST ONLY
#print(data_past_year)
#print(data_present_year)
#print(data_past_slidingWindow)
#print(sliding_dist_dic)
#print(min_distance_sliding_index)
#print(closest_sliding_window)
#print(variation)
#print(prediction)
#-------------- TEST ONLY

print("Predicted Maximum Temperature for Tomorrow :-", prediction[0])
print("Predicted Minimum Temperature for Tomorrow :-", prediction[1])
print("Predicted Humidity for Tomorrow :-", prediction[2])
print("Predicted Rainfall for Tomorrow :-", prediction[3])