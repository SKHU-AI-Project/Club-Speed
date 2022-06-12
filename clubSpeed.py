import math

def speed(file, slow):

    rowData = []
    ballSize = []
    Data_head = []
    indexNum = []
    coor = []

    with open(file, 'r') as f:
        data = f.readlines()

    for i in range(len(data)):
        rowData.append(data[i].split(' ')[:6]) 

    for i in range(len(rowData)):
        if rowData[i][0] == 'golf_ball':
            ballSize.append(int(rowData[i][2]))
            ballSize.append(int(rowData[i][4]))
            break

    realCm = (4.3 * 1.35) / (ballSize[1] - ballSize[0])

    for i in rowData:
        if i[0] == 'golf_head':
            Data_head.append(i)

    for i in range(len(Data_head)):
        if (int(Data_head[i][4])+int(Data_head[i][2]))/2 < (ballSize[1] + ballSize[0])/4:
            indexNum.append(i)
    for i in indexNum:
        Data_head[i] = ''
    for i in range(len(Data_head)):
        if Data_head[i] != '':
            Data_head[i] = ''
        else:
            break
    for i in range(len(Data_head)):
        if Data_head[i] != '':
            cenX = (int(Data_head[i][1])+ int(Data_head[i][3]))/2
            cenY = (int(Data_head[i][2])+ int(Data_head[i][4]))/2
            
            coor.append([cenX, cenY, Data_head[i][-1]])

    middle = round(len(coor)/2)
    km = ((math.sqrt((coor[middle][0]-coor[middle-1][0])**2+(coor[middle][1]-coor[middle-1][1])**2))/realCm)*0.00001
    hour = ((float(coor[middle][2])-float(coor[middle-1][2])))/3600
    kph = round((km/hour)*slow,1)
    mph = round(((km*0.62)/hour)*slow, 1)
    print(str(kph)+' km/h')
    print(str(mph)+' mile/h')

speed('coordinate_and_time_golf_result.txt', 13.3)