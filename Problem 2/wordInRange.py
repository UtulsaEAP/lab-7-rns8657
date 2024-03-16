def wordInRange(name, lower_range, upper_range):
    names = open(name, 'r')
    words = names.readlines()
    for i in range (len(words)):
        if (words[i].strip("\n") <= upper_range and words[i].strip("\n") >= lower_range):
            print(str(words[i].strip("\n")) + " - in range")
        else:
            print(str(words[i].strip("\n")) + " - not in range" )
    

    return
if __name__ == '__main__':
    name = input()
    lower_range = input()
    upper_range = input()

    wordInRange(name, lower_range, upper_range)