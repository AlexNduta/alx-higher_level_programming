#!/usr/bin/python3

if __name__ == "__main__":
    def safe_print_list(my_list=[], x=0):
        try:
            printed_counter = 0
            remaining_to_print = x
            for item in my_list:
                if remaining_to_print > 0:
                    print(item, end=" ")
                    printed_counter += 1
                else:
                    break

            print()
            return printed_counter
        except Exception:
            return printed_counter
