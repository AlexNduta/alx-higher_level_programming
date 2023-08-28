#!/usr/bin/python3

if __name__ == "__main__":
    def safe_print_list(my_list=[], x=0):
        try:
            printed_counter = 0
            for item in my_list:
                print(item, end=" ")
                printed_counter += 1
            print()
            return printed_counter
        except Exception:
            return my_list
