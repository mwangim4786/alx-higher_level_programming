#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) > 0:
        cummulatineNo = 0
        cummulativeDiv = 0
        for eachTuplePair in my_list:
            cummulatineNo += (eachTuplePair[0] * eachTuplePair[1])
            cummulativeDiv += eachTuplePair[1]
        return cummulatineNo / cummulativeDiv
    else:
        return 0
