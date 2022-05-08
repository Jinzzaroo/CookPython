aa = []
hap = 0
for i in range (0,4):
    aa.append(0)
    aa[i] = int(input(str(i+1) + "번째 숫자 :"))
    hap += aa[i]


print("합계 ==> %d" % hap)
