import csv
import string
import json

def deleteFromDictionary(listName, sortedDict):
    keys_to_remove = []
    for key in listName:
        if key in sortedDict:
            keys_to_remove.append(key)
    for key in keys_to_remove:
        del sortedDict[key]

def deleteFindName(userInput, index):
    targetName = userInput.split()[index+1]
    targetName = targetName.replace("’", "")
    targetName = targetName.replace("‘", "")
    for character in string.punctuation:
        targetName = targetName.replace(character, "")
    listName = []
    if userInput.split()[index] == "=":
        for key in sortedDict:
            if sortedDict[key].get("name") == targetName:
                listName.append(key)
    elif userInput.split()[index] == "!=":
        for key in sortedDict:
            if sortedDict[key].get("name") != targetName:
                listName.append(key)
    return listName
def deleteFindLastName(userInput,index):
    targetName = userInput.split()[index+1]
    targetName = targetName.replace("’", '')
    targetName = targetName.replace("‘", '')
    for character in string.punctuation:
        targetName = targetName.replace(character, '')
    listName=[]
    if (userInput.split()[index] == "="):
        for key in sortedDict:
            if (sortedDict.get(key).get('last name') == targetName):
                listName.append(key)
    elif (userInput.split()[index] == "!="):
        for key in sortedDict:
            if (sortedDict.get(key).get('last name') != targetName):
                listName.append(key)
    return listName

def deleteFindGrade(userInput,index):
    grade = userInput.split()[index+1]
    grade = grade.replace("’", '')
    grade = grade.replace("‘", '')
    for character in string.punctuation:
        grade = grade.replace(character, '')
    grade = int(grade)
    listName=[]
    if (userInput.split()[index] == "="):

        for key in sortedDict:
            if (int(sortedDict.get(key).get('grade')) == grade):
                listName.append(key)

    elif (userInput.split()[index] == "!="):
        for key in sortedDict:
            if (int(sortedDict.get(key).get('grade')) != grade):
                listName.append(key)


    elif (userInput.split()[index] == "<") or userInput.split()[index] == "!>":
        for key in sortedDict:
            if (int(sortedDict.get(key).get('grade')) < grade):
                listName.append(key)

    elif (userInput.split()[index] == ">") or userInput.split()[index] == "!<":
        for key in sortedDict:
            if (int(sortedDict.get(key).get('grade')) > grade):
                listName.append(key)
    elif (userInput.split()[index] == "<="):
        for key in sortedDict:
            if (int(sortedDict.get(key).get('grade')) <= grade):
                listName.append(key)
    elif (userInput.split()[index] == ">="):
        for key in sortedDict:
            if (int(sortedDict.get(key).get('grade')) >= grade):
                listName.append(key)
    return listName

def deleteFindId(userInput,index):
    id = userInput.split()[index+1]
    id = id.replace("’", '')
    id = id.replace("‘", '')
    for character in string.punctuation:
        id = id.replace(character, '')
    id = int(id)
    listName=[]
    if (userInput.split()[index] == "="):
        listName.append(id)

    elif (userInput.split()[index] == "!="):
        for key in sortedDict:
            if(int(key)!=id):
                listName.append(key)

    elif (userInput.split()[index] == "<") or userInput.split()[index] == "!>":
        for key in sortedDict:
            if (int(key) < id):
                listName.append(key)
    elif (userInput.split()[index] == ">") or userInput.split()[index] == "!<":
        for key in sortedDict:
            if (int(key) > id):
                listName.append(key)

    elif (userInput.split()[index] == "<="):
        for key in sortedDict:
            if (int(key) <= id):
                listName.append(key)

    elif (userInput.split()[index] == ">="):
        for key in sortedDict:
            if (int(key) >= id):
                listName.append(key)
    return listName

def deleteFindEmail(userInput,index):
    targetEmail = userInput.split()[index+1]
    targetEmail = targetEmail.replace("’", '')
    targetEmail = targetEmail.replace("‘", '')
    targetEmail = targetEmail.replace("'", '')
    targetEmail = targetEmail.replace("'", '')
    targetEmail = targetEmail.replace("\"", '')
    listName=[]
    if (userInput.split()[index] == "="):
        for key in sortedDict:
            if (sortedDict.get(key).get('email') == targetEmail):
                listName.append(key)

    elif (userInput.split()[index] == "!="):
        for key in sortedDict:
            if (sortedDict.get(key).get('email') != targetEmail):
                listName.append(key)
    return listName

def checkconditionition(veriable1,veriable2,condition):
    if condition==">"  and veriable1>veriable2:
        return True
    elif  (condition=="=>" or condition=="!<") and veriable1>=veriable2:
        return True
    elif condition=="<"  and veriable1<veriable2:
        return True
    elif  (condition=="<=" or condition=="!>") and veriable1<=veriable2:
        return True
    elif  condition=="="  and veriable1==veriable2:
        return True
    return False


# main
DICTIONARY = {}
# Read the students.csv file
with open("students.csv", "r") as csvFile:
    csvRead = csv.reader(csvFile, delimiter=";")
    lineCounter = 0

    # Iterate over each row in the CSV file
    for row in csvRead:
        if lineCounter == 0:
            print(f"Column names: {', '.join(row)}")
            lineCounter += 1
            print()
        else:
            # Store the student information in the dictionary
            DICTIONARY[int(row[0])] = {
                "name": row[1],
                "lastname": row[2],
                "email": row[3],
                "grade": row[4],
            }
            lineCounter += 1
    print()

sortedDict = {}  # Create an empty sorted dictionary
# Sort the dictionary by keys
for key in sorted(DICTIONARY.keys()):
    sortedDict[key] = DICTIONARY[key]

# Prompt the user for an SQL command or exit
userInput = input("Enter a sql command or exit:")

while userInput.lower() != "exit": # Continue until the user chooses to exit
    if userInput.split()[0] == "SELECT":
        selected = {}
        for key in sortedDict: # Iterate over the sorted dictionary
            keyValue = sortedDict[key]
            conjunction = userInput.split()[8]  # Get the conjunction (AND / OR)

            # Check the conditions based on the user input
            if userInput.split()[5] == "grade" :
                compareFirst = int(userInput.split()[7])
                first_value_at_hand = int(keyValue[userInput.split()[5]])
            elif userInput.split()[5] == "id":
                compareFirst = int(userInput.split()[7])
                first_value_at_hand = key
            else:
                compareFirst = userInput.split()[7]
                compareFirst = compareFirst.replace('‘', '')
                compareFirst = compareFirst.replace('’', '')
                compareFirst = compareFirst.replace("'", "")
                first_value_at_hand = keyValue[userInput.split()[5]]
            if len(userInput.split())!=11:
                if userInput.split()[9] == "grade" :
                    secondition_value_to_compare = int(userInput.split()[11])
                    secondition_value_at_hand = int(keyValue[userInput.split()[9]])
                elif userInput.split()[9] == "id":
                    secondition_value_to_compare = int(userInput.split()[11])
                    secondition_value_at_hand = key
                else:
                    secondition_value_to_compare = userInput.split()[11]
                    secondition_value_to_compare = secondition_value_to_compare.replace('‘', '')
                    secondition_value_to_compare = secondition_value_to_compare.replace('’', '')
                    secondition_value_to_compare = secondition_value_to_compare.replace("'", "")
                    secondition_value_at_hand = keyValue[userInput.split()[9]]

            #                    0      1   2       3       4     5  6  7  8    9  10   11    12  13  14
            # userInput = "SELECT name,lastname FROM STUDENTS WHERE grade!<40 ORDERED BY ASC"
            con1 = checkconditionition(first_value_at_hand, compareFirst, userInput.split()[6])
            if len(userInput.split())==11:
                con2=True
            else :
                con2 = checkconditionition(secondition_value_at_hand, secondition_value_to_compare, userInput.split()[10])
            # Dict[int(row[0])] = {'name': row[1], 'last name': row[2], 'email': row[3], 'grade': row[4]}
            addDict = False # Flag to determine if the row should be added to the selected dictionary

            # Evaluate the conditions based on the conjunction

            if len(userInput.split())==11:
                addDict = con1
            else :
                if userInput.split()[8] == "AND" and (con1 and con2):
                    addDict = True
                elif userInput.split()[8] == "OR" and (con1 or con2):
                    addDict = True
            # Add the row to the selected dictionary if conditions are met

            if addDict:

                if userInput.split()[1].lower() == "all":
                    selected[key] = keyValue
                else:
                    a = userInput.split()[1]
                    values = {}
                    for i in a.split(","):
                        if i=="id":
                            values["id"]=key
                        else:
                            values[i] = keyValue[i]

                    selected[key] = values

        ordered_selected = {}

        if len(userInput.split()) == 11:
            if userInput.split()[10] == "DSC":
                for key in sorted(selected.keys(), reverse=True):
                    ordered_selected[key] = selected[key]

            else:
                ordered_selected = selected
        else:

            if userInput.split()[14] == "DSC":
                for key in sorted(selected.keys(), reverse=True):
                    ordered_selected[key] = selected[key]

            else:
                ordered_selected = selected

        print("selected and sorted")
        print(ordered_selected)
    elif userInput.split()[0] == "INSERT":
        if userInput.split()[1] == "INTO" and userInput.split()[2] == "STUDENT" and userInput.split()[3].split("(")[0]=="VALUES":
            values=userInput.split()[3].split("(")[1].split(",")
            if len(values) == 5:
                if sortedDict.get(int(values[0])):
                    print("This id has been taken")
                else:
                    DICTIONARY[int(values[0])] = {'name': values[1], 'lastname': values[2], 'email': values[3], 'grade': values[4]}
                    sortedDict[int(values[0])] = DICTIONARY[int(values[0])]
            else:
                print("Invalid ")

        else:
            print("INVALID")
    elif userInput.split()[0] == "DELETE":
        if userInput.split()[1] == "FROM" and userInput.split()[2] == "STUDENT" and userInput.split()[3] == "WHERE":
            strAndOr=""
            listOfWords = []
            for key in range(4,len(userInput.split())):
                listOfWords.append(userInput.split()[key])
            listName = []
            while len(listOfWords) != 0:
                firstKey=listOfWords.pop(0)
                if (firstKey == "name"):
                    str1 = ""
                    for words in listOfWords:
                        str1 += words+" "
                    if(strAndOr=="or" or strAndOr==""):
                        listName += deleteFindName(str1, 0)
                    elif(strAndOr=="and"):
                        listNew = deleteFindName(str1, 0)
                        listName = set(listName) & set(listNew)
                    listOfWords.pop(0)
                    listOfWords.pop(0)
                elif (firstKey == "grade"):
                    str1 = ""
                    for words in listOfWords:
                        str1 += words + " "
                    if (strAndOr == "or" or strAndOr == ""):
                        listName += deleteFindGrade(str1, 0)

                    elif (strAndOr == "and"):
                        listNew = deleteFindGrade(str1, 0)
                        listName = set(listName) & set(listNew)
                    listOfWords.pop(0)
                    listOfWords.pop(0)
                elif (firstKey == "id"):
                    str1 = ""
                    for words in listOfWords:
                        str1 += words + " "
                    if (strAndOr == "or" or strAndOr == ""):
                        listName += deleteFindId(str1, 0)
                    elif (strAndOr == "and"):
                        listNew = deleteFindId(str1, 0)
                        listName = set(listName) & set(listNew)
                    listOfWords.pop(0)
                    listOfWords.pop(0)

                elif (firstKey == "email"):

                    str1 = ""
                    for words in listOfWords:
                        str1 += words + " "
                    if (strAndOr == "or" or strAndOr == ""):
                        listName += deleteFindEmail(str1, 0)
                    elif (strAndOr == "and"):
                        listNew = deleteFindEmail(str1, 0)
                        listName = set(listName) & set(listNew)
                    listOfWords.pop(0)
                    listOfWords.pop(0)

                elif firstKey == "last" and listOfWords[0]=="name":
                    str1 = ""
                    for words in listOfWords:
                        str1 += words + " "
                    if (strAndOr == "or" or strAndOr == ""):
                        listName += deleteFindLastName(str1,0)
                    elif (strAndOr == "and"):
                        listNew = deleteFindLastName(str1,1)
                        listName = set(listName) & set(listNew)

                    listOfWords.pop(0)
                    listOfWords.pop(0)
                    listOfWords.pop(0)
                if(len(listOfWords)!=0):
                    strAndOr=listOfWords.pop(0).lower()
            deleteFromDictionary(listName,sortedDict)

        else:
            print("INVALID input")
    else:
        print("INVALID input")
    userInput = input("Enter a SQL query or exit:")
with open("sample.json", "w") as outfile:
    json.dump(DICTIONARY, outfile, indent=2)
