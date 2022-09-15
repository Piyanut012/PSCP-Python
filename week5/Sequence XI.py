""""Sequence XI"""

def sequencexi():
    """print"""
    num = int(input())
    #ครึ่งแรก
    for i in range(1, num, 1):
        #เลขส่วนหน้า
        for front in range(1, i+1, 1):
            print("%02d" % front, end=" ")
        #เลขส่วนกลาง
        for middle in range(1, (num*2)-(i*2)):
            print("%02d" % i, end=" ")
            middle = middle + 1
        #เลขส่วนหลัง
        for back in range(i, 0, -1):
            print("%02d" % back, end=" ")
        print()
    #ส่วนกลาง
    for j in range(1, num*2, 1):
        if j < num:
            print("%02d" % j, end=" ")
        else:
            print("%02d" % ((num*2)-j), end=" ")
    print()
    #ส่วนท้าย
    for i in range(1, num, 1):
        #เลขส่วนหน้า
        for front in range(1, num+1-i, 1):
            print("%02d" % front, end=" ")
        #เลขส่วนกลาง
        for middle in range(1, i*2):
            print("%02d" % (num - i), end=" ")
            middle = middle + 1
        #เลขส่วนหลัง
        for back in range(num-i, 0, -1):
            print("%02d" % back, end=" ")
        print()
sequencexi()
