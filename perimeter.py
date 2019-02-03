file_name = input('Which data file do you want to use? ')
with open(file_name) as f:
    content = f.readlines()
content_clean = []
for i in content:
    temp = i.strip('\n')
    content_clean.append(temp)
content_list = []
temp_int_list = []
for i in content_clean:
    temp = i.split()
    for j in temp:
        j = int(j)
        temp_int_list.append(j)
    content_list.append(temp_int_list)
    temp_int_list = []

perimeters = []
for i in content_list:
    perimeter = 0
    p1 = [i[0], i[1]]
    p2 = [i[0], i[3]]
    p3 = [i[2], i[3]]
    p4 = [i[2], i[1]]
    #from p1 to p2
    for j in range(p1[1], p2[1]):
            perimeter += 1
    for j in range(p2[0], p3[0]):
            perimeter += 1
    for j in range(p3[1], p4[1], -1):
            perimeter += 1
    for j in range(p4[0], p1[0], -1):
            perimeter += 1
    perimeters.append(perimeter)

for i in range(len(content_list)):
    for j in [content_list[i][0], content_list[i][2]]:
        for k in range(content_list[i][1], content_list[i][3]+1):
             for m in content_list:
                 if m != content_list[i]:
                    if j > m[0] and j < m[2] and k > m[1] and k < m[3]:
                            perimeters[i] -= 1
                            break
                    elif (j == m[0] or j == m[2]) and (k > m[1] and k < m[3]):
                            perimeters[i] -= 0.5
                            break
                    elif (k == m[1] or k == m[3]) and (j > m[0] and j < m[2]):
                            perimeters[i] -= 0.5
                            break
                    else:
                        pass
    for k in [content_list[i][1], content_list[i][3]]:
        for j in range(content_list[i][0]+1, content_list[i][2]):
             for n in content_list:
                 if n != content_list[i]:
                     if j > n[0] and j < n[2] and k > n[1] and k < n[3]:
                            perimeters[i] -= 1
                            break
                     elif (j == n[0] or j == n[2]) and (k > n[1] and k < n[3]):
                            perimeters[i] -= 0.5
                            break
                     elif (k == n[1] or k == n[3]) and (j > n[0] and j < n[2]):
                            perimeters[i] -= 0.5
                            break
                     else:
                         pass
print('The perimeter is: {}'.format(int(sum(perimeters))))         
            
