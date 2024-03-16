def fileNameChange(name):
    info = open(name, 'r')
    photos = info.readlines()
    for i in range (len(photos)):
        photo_names = photos[i].split(".")
        report = open("./Problem 4/ParkPhotos", '+a')
        report.write(photo_names[0] + ".txt" + "\n")
        report.close()
    return(report)

if __name__ == '__main__':
    name = "./Problem 4/" + str(input())
    fileNameChange(name)