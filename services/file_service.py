def clear(file_name):
    f = open(file_name, "w")
    f.write("")
    f.close()

#
# list is a list of strings
# separator is any special character to separate items with spaces between f.e ' | '
#
def append_to_bulk(file_name, list, separator):
    f = open(file_name, "a")
    to_append = ""
    for item_index in range(len(list)):
        if item_index < len(list) - 1:
            to_append += str(list[item_index]) + separator
        else:
            to_append += str(list[item_index])
    
    f.write(to_append)
    f.write('\n')

