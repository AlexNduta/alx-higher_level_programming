#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by zero")
        except TypeError:
            print("wrong type")
        finally:
            return result
