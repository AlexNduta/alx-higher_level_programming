#!/usr/bin/python3
if __name__ == "__main__":
    # import our provided file
    import hidden_4
    # loop through the whole file to check for characters begining with "__"
    for string in dir(hidden_4):
        if string[:2] != "__":
            print(f"{:s}".format(s))
