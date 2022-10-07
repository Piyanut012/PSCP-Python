"""SecondConverter"""


def main():
    """Input"""
    total_second = int(input())
    second_parallel = int(input())
    min_parallel = int(input())
    hrs_parallel = int(input())

    second = total_second%(second_parallel*min_parallel*hrs_parallel)
    hrs = second//(second_parallel*min_parallel)
    second = second%(second_parallel*min_parallel)
    minute = second//second_parallel
    second = second%second_parallel

    print("%d:%d:%d" % (hrs, minute, second))
main()

