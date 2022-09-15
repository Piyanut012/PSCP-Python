""""Sequence XII"""


def sequencexii():
    """print"""
    num = int(input())
    def first(num):
        """ครึ่งแรก"""
        for i in range(1, num, 1):
            #เลขส่วนหน้า
            for front in range(num+1-i, num, 1):
                print("%02d" % front, end=" ")
            #เลขส่วนกลาง1
            for middle1 in range(num, i-1, -1):
                print("%02d" % middle1, end=" ")
            #เลขส่วนกลาง2
            for middle2 in range(i+1, num+1, 1):
                print("%02d" % middle2, end=" ")
            #เลขส่วนหลัง
            for back in range(num-1, num-i, -1):
                print("%02d" % back, end=" ")
            print()
    first(num)
    #ส่วนกลาง
    for j in range(1, num*2, 1):
        if j < num:
            print("%02d" % j, end=" ")
        else:
            print("%02d" % ((num*2)-j), end=" ")
    print()
    def back(num):
        """ส่วนท้าย"""
        for i in range(1, num, 1):
            #เลขส่วนหน้า
            for front in range(i+1, num, 1):
                print("%02d" % front, end=" ")
            #เลขส่วนกลาง1
            for middle1 in range(num, num-1-i, -1):
                print("%02d" % middle1, end=" ")
            #เลขส่วนกลาง2
            for middle2 in range(num+1-i, num+1, 1):
                print("%02d" % middle2, end=" ")
            #เลขส่วนหลัง
            for back in range(num-1, i, -1):
                print("%02d" % back, end=" ")
            print()
    back(num)

sequencexii()
