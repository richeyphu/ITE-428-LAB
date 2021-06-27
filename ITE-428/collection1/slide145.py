import statistics


# def count_above_avg(data):
#     avg = statistics.mean(data)
#     count = 0
#     for i in data:
#         if i > avg:
#             count += 1
#     return count
#
#
# def count_below_avg(data):
#     avg = statistics.mean(data)
#     count = 0
#     for i in data:
#         if i < avg:
#             count += 1
#     return count
#
#
# def count_equal_to_avg(data):
#     avg = statistics.mean(data)
#     count = 0
#     for i in data:
#         if i == avg:
#             count += 1
#     return count


def count_avg(data):
    avg = statistics.mean(data)
    a = b = c = 0
    for i in data:
        if i > avg:
            a += 1
        elif i < avg:
            b += 1
        else:
            c += 1
    return a, b, c


weight = (62.5, 78, 50, 42, 84, 65.5, 48, 53.5, 43)
print("Maximum weight of 9 persons = {}".format(max(weight)))
print("Minimum weight of 9 persons = {}".format(min(weight)))
print("Average weight of 9 persons = {:.2f}".format(statistics.mean(weight)))

# print("No. of weight above average\t= {}".format(count_above_avg(weight)))
# print("No. of weight below average\t= {}".format(count_below_avg(weight)))
# print("No. of weight equal to average\t= {}".format(count_equal_to_avg(weight)))
calavg = count_avg(weight)
print("No. of weight above average\t= {}".format(calavg[0]))
print("No. of weight below average\t= {}".format(calavg[1]))
print("No. of weight equal to average\t= {}".format(calavg[2]))
