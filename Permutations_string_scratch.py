set_s = input("Enter a string: ")
Length = int(input("Enter the length of the string: "))
count_s = [1]*len(set_s)
f_final = []
def check(count):
    for _ in range(len(count)):
        if(count[_] != 0):
            return _
    return -1
def combinations(s1,count1,final,l):
    global f_final
    position = check(count1)
    count3 = count1[:]
    while(position != -1):
        count2 = count1[:]
        count2[position] -= 1
        count3[position] -= 1
        final.append(s1[position])
        combinations(s1,count2,final[:],l)
        final = final[:-1]
        position = check(count3)
    if(len(final) == l):
        f_final.append(str("".join(final)))
    return
final = []
combinations(set_s,count_s,final[:],Length)
for _ in set(f_final):
    print(_)
