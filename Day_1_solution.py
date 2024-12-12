import requests
left_list = []
right_list = []
filename = "AdventOfCode2024_1_data.txt"
with open(filename, "r") as file:
    for line in file:
        temp = line.split("   ")
        left_list.append(int(temp[0]))
        right_list.append(int(temp[1]))
length_of_rl = len(right_list)
length_of_ll = len(left_list)
if length_of_rl < length_of_ll:
    loop_length = length_of_rl
    loop_1 = right_list.copy()
    loop_2 = left_list.copy()
else:
    loop_length = length_of_ll
    loop_1 = left_list.copy()
    loop_2 = right_list.copy()
leftover_length = abs(length_of_rl - length_of_ll)
distance = 0
while loop_length > 0:
    distance += abs(min(loop_1) - min(loop_2))
    loop_1.remove(min(loop_1))
    loop_2.remove(min(loop_2))
    loop_length -= 1
distance += sum(loop_2)
print("Total Distance Differential is\t:\t" + str(distance))
similarity_score = 0
for i in range(len(left_list)):
    similarity_score += (left_list[i] * right_list.count(left_list[i]))
print("Total Similarity Score is\t:\t" + str(similarity_score))
