""""Sequence X"""

def sequencex():
    """print"""
    num = int(input())
    for i in range(1, num*2, 1):
        # บรรทัด 1-num
        if i <= num:
            # print space
            for space in range(num, 1, -1):
                if space > i:
                    print("  ", end=' ')
            # เลขโซนหน้า
            for num_front in range(1, num+1, 1):
                if num_front <= i:
                    print("%02d" % num_front, end=' ')
            # เลขโซนหลัง
            for num_back in range(i-1, 0, -1):
                print("%02d" % num_back, end=' ')
            # บรรทัดหลัง num
        else:
            # print space
            for space in range(1, num, 1):
                if space <= i%num:
                    print("  ", end=' ')
            # เลขโซนหน้า
            for num_front in range(1, num - i%num, 1):
                print("%02d" % num_front, end=' ')
            # เลขโซนหลัง
            for num_back in range(num - i%num, 0, -1):
                print("%02d" % num_back, end=' ')
        print()
sequencex()
