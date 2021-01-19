#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""

def get_greatest(number_list):
    #greatest_number = max(number_list)
    greatest_number = number_list[0]
    for n in number_list:
        if n > greatest_number:
            greatest_number = n
    return greatest_number


def get_smallest(number_list):
    #smallest_number = min(number_list)
    smallest_number = number_list[0]
    for n in number_list:
        if n < smallest_number:
            smallest_number = n
    return smallest_number


def get_mean(number_list):
    sum = 0
    for n in number_list:
        sum += n
    mean = sum / len(number_list)
    return mean


def get_median(number_list):
    l = len(number_list)
    number_list.sort() # 리스트 정렬
    if l % 2 == 1: # 홀수개일때
        median = number_list[l//2] # 가운데 값 반환
    else: #짝수개일때
        median = (number_list[l//2 - 1] + number_list[l//2]) / 2 # 가운데 두 값의 평균 반환
    return median
