xw

import re  # do you still need this? 

menu = open("menu.txt", "r")
translatedMenu = open("translatedMenu.txt", "w")
X = 0
p = -1

    if x == -1:
        translatedMenu.write("Format Error\n")
        error = True
    if y == -1:
        translatedMenu.write("Format Error\n")
        error == True
    if error == False:
        if p != -1:
            translatedMenu.write(name + "<em> " + str(price) + "</em>\n")
        else:
            translatedMenu.write(name + "<em> " + str(price) + "</em> <i>" + description + "</i>\n")
    X = X + 1

    ##name = re.search("[(]$", str_line)
    ##print(name.start)
##Calamari of the East <em> 6.75</em> <i>(lightly breaded Calamari)</i>
