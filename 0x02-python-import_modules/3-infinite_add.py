#!/usr/bin/python3
#make the code exutable only on shell
if __name__ == "__main__":
    import sys

    total_sum = 0
    #loop through the argumnents list
    for argument in sys.argv[1:]:
        total_sum = total_sum + int(argument) #sum up the arguments
    print(total_sum)
