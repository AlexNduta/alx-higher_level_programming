#!/usr/bin/python3

def search_replace(my_list, search, replace):

    def replace_element(element):
        # if the element is equal to search value, replace with value
        return replace if element == search else element

    # Apply the replaced element to each element
    replaced_list = list(map(replace_element, my_list))
    return replaced_list
