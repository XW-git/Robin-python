menu = open("menu.txt", "r")
translatedMenu = open("translatedMenu.txt", "w")
X = 0
Period = -1


def ResetVariables():
    global error
    global Line_Has_An_Integer
    global Period
    global Line_Length
    global First_Parenthesis
    global str_line
    global Second_Parenthesis
    str_line = menu.readline()
    error = False
    Line_Has_An_Integer = False
    Period = -1
    Line_Length = len(str_line)
    First_Parenthesis = str_line.find("(")
    Second_Parenthesis = str_line.find(")")


def IsItMaki():
    global name
    global price
    global Line_Length
    Period = str_line.find(".")  ## Checks to see if price is on the same line because that means it has no description
    if Period != -1:
        name = str_line[0:Period - 1]
        price = str_line[Period - 1:Line_Length]
        price = price.strip()
        return True
    else:
        return False


def Checks_If_There_Is_A_Second_Parenthesis():
    global name
    global price
    global str_line
    global Second_Parenthesis
    global description
    if Second_Parenthesis == -1: ## if it can'Line_Has_An_Integer find )
        if not IsItMaki():
            str_line = menu.readline() ## goes to next line to find description
            Second_Parenthesis = str_line.find(")")
            if Second_Parenthesis == -1:
                str_line = menu.readline()
                Second_Parenthesis = str_line.find(")")
                if Second_Parenthesis == -1:
                    str_line = menu.readline()
                    Second_Parenthesis = str_line.find(")")
                else:
                    description3 = str_line[0:Second_Parenthesis + 1]
                    description = (description2 + " " + description3)
            else:
                description3 = str_line[0:Second_Parenthesis+1]
                description = (description2 + " " + description3)

##Main Starts Here

while True:
    ResetVariables()
    if not str_line:  ##This breaks the loop at the end of the file
        break
    name = str_line[0:First_Parenthesis] ##Finds the name in the string and makes a variable with it
    description2 = str_line[First_Parenthesis:Line_Length-1]
    description = str_line[First_Parenthesis:Second_Parenthesis + 1]
    Checks_If_There_Is_A_Second_Parenthesis()

    if Second_Parenthesis != -1: ## Looks For Price
        for character in str_line: ## checks to see if the price in on the line
            if character.isdigit():
                Line_Has_An_Integer = True
        if Line_Has_An_Integer == False: ##goes to the next line for the price
            str_line = menu.readline()
            Line_Length = len(str_line)
            price = str_line[0:Line_Length-1]
        if Line_Has_An_Integer == True:
            Line_Length = len(str_line)
            price = str_line[Second_Parenthesis+1:Line_Length-1]
            price = price.strip()


    if Period != -1:
        translatedMenu.write(name + "<em> " + str(price) + "</em>\n")
    else:
        translatedMenu.write(name + "<em> " + str(price) + "</em> <i>" + description + "</i>\n")

    X = X + 1

