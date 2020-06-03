menu = open("menu.txt", "r")
translatedMenu = open("translatedMenu.txt", "w")
Period = -1


def ResetVariables():
    global error
    global LineHasAInteger
    global Period
    global z
    global x
    global str_line
    global SecondParenthesis
    str_line = menu.readline()
    error = False
    LineHasAInteger = False
    Period = -1
    z = len(str_line)
    x = str_line.find("(")
    SecondParenthesis = str_line.find(")")


def IsItMaki():
    global name
    global price
    global z
    Period = str_line.find(".")  ## Checks to see if price is on the same line because that means it has no description
    if Period != -1:
        name = str_line[0:Period - 1]
        price = str_line[Period - 1:z]
        price = price.strip()
        return True
    else:
        return False


def ChecksIfThereIsASecondParenthesis():
    global name
    global price
    global str_line
    global SecondParenthesis
    global description
    if SecondParenthesis == -1: ## if it can'LineHasAInteger find )
        if not IsItMaki():
            str_line = menu.readline() ## goes to next line to find description
            SecondParenthesis = str_line.find(")")
            if SecondParenthesis == -1:
                str_line = menu.readline()
                SecondParenthesis = str_line.find(")")
                if SecondParenthesis == -1:
                    str_line = menu.readline()
                    SecondParenthesis = str_line.find(")")
                else:
                    description3 = str_line[0:SecondParenthesis + 1]
                    description = (description2 + " " + description3)
            else:
                description3 = str_line[0:SecondParenthesis+1]
                description = (description2 + " " + description3)

while True:
    ResetVariables()
    if not str_line:  ##This breaks the loop at the end of the file
        break
    name = str_line[0:x] ##Finds the name in the string and makes a variable with it
    description2 = str_line[x:z-1]
    description = str_line[x:SecondParenthesis + 1]
    ChecksIfThereIsASecondParenthesis()

    if SecondParenthesis != -1: ## Looks For Price
        for character in str_line: ## checks to see if the price in on the line
            if character.isdigit():
                LineHasAInteger = True
        if LineHasAInteger == False: ##goes to the next line for the price
            str_line = menu.readline()
            z = len(str_line)
            price = str_line[0:z-1]
        if LineHasAInteger == True:
            z = len(str_line)
            price = str_line[SecondParenthesis+1:z-1]
            price = price.strip()


    if Period != -1:
            translatedMenu.write(name + "<em> " + str(price) + "</em>\n")
    else:
            translatedMenu.write(name + "<em> " + str(price) + "</em> <i>" + description + "</i>\n")

