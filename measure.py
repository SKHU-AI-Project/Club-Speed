import math


# 리스트에서 작은 y값 2개 반환
def extractSamllY(headInfoList):
    
    yPointSort = []

    for headInfo in headInfoList:
        yPointSort.append(int(headInfo[4]))

    # y좌표 리스트 복사
    copyYPointSort = sorted(yPointSort)

    # 작은 수 2개
    smallYOne = copyYPointSort[0]
    smallYTwo = copyYPointSort[1]

    # 인덱스 반환
    indexOne = yPointSort.index(smallYOne)
    indexTwo = yPointSort.index(smallYTwo)

    return (indexOne, indexTwo)
    

# 좌표값이 담긴 파일과 해당 동영상의 fps
def measure(file, slow):

    headInfoList = []
    ballInfoList = []


    # 입력받은 파일에서 데이터 불러오기
    with open(file, 'r') as data:
        info = data.readlines()

    for pixelInfo in info:
        point = pixelInfo.split(' ')

        # 각자 객체의 리스트에 좌표값 저장
        if point[0] == 'golf_head':
            headInfoList.append(point)

        if point[0] == 'golf_ball':
            ballInfoList.append(point)

    # 픽셀거리와 실제거리의 차이를 보정하기 위한 값 계산
    correctionConstant = 4.3 / (int(ballInfoList[0][3]) - int(ballInfoList[0][1]))

    # 헤드의 가장 작은 y값 두 개 값을 구함
    smallOne, smallTwo = extractSamllY(headInfoList)
    headInfoOne = headInfoList[smallOne]
    headInfoTwo = headInfoList[smallTwo]

    # 픽셀 길이 계산 후 실제 거리 반환
    distance = math.dist([int(headInfoOne[1]), int(headInfoOne[2])], [int(headInfoTwo[1]), int(headInfoTwo[2])])
    realDistance = distance * correctionConstant * 0.00001

    # 시간 계산 후 동영상의 배속 적용
    time = (float(headInfoOne[5]) - float(headInfoTwo[5])) / 3600

    # 속도 = 거리 / 시간
    speed = realDistance / time * slow

    return speed
    

print(str(measure('coordinate_and_time.txt', 6))[:4] + "km/h")