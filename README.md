# 2022 인공지능 기말과제 3팀

### 🎃 팀원소개
* 박 결 👑
* 강준혁
* 허지영
* 이승헌

* * *

### 프로젝트 소개
Title: MSFC (**Measure Speed For Club**)

```
저희 프로젝트는 인공지능을 이용하여 골프채의 속도를 측정하는 서비스입니다.
darknet YOLOv3를 사용하여 골프채를 인식하고 스윙 동작에서 클럽헤드의 좌표를 통한
계산으로 속도를 측정하였습니다.
```

### USAGE
```
# -*- coding: utf-8 -*-
"""MSFC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MVsvHKhLyEP8SFAYjNZZxfmvC8uwQC9g
"""

!git clone https://github.com/SKHU-AI-Project/Club-Speed.git #our git

# Commented out IPython magic to ensure Python compatibility.
# %cd darknet

!make

!wget —no-check-certificate 'https://docs.google.com/uc?export=download&id=1CFlxbIKTiNlC5jURSMV87KB7IhgfPlyp' -O golf_custom_10000.weights

!wget —no-check-certificate 'https://docs.google.com/uc?export=download&id=1c2ebtK5_4V5yvcflYA98H30Og4Mw1StH' -O test.mp4

!./darknet detector demo golf_cfg/golf_custom.data golf_cfg/golf_custom.cfg golf_custom_10000.weights -dont_show ./test.mp4 -i 0 -out_filename ./results.avi
```

### 사용 기술
- 📖 웹 크롤링
  - Github: <https://github.com/YoongiKim/AutoCrawler>

- 🔥 유튜브 사진 추출
  - Github: <https://github.com/yt-dlp/yt-dlp> (동영상 다운로드)
  - Github: <https://github.com/sga8/Video2Image> (image 분리)

- 🛠 Labeling
  - Github: <https://github.com/tzutalin/labelImg>

- 👾 darknet YOLOv3
  - 출처: [medium 블로그 링크](https://medium.com/@quangnhatnguyenle/how-to-train-yolov3-on-google-colab-to-detect-custom-objects-e-g-gun-detection-d3a1ee43eda1)
  - Github: <https://github.com/AlexeyAB/darknet>
 
 * * *

### 좌표추출
<img src="https://user-images.githubusercontent.com/51286325/172812835-f0d7620d-06f2-4b4d-83b5-5e501af51934.png" width="200px" height="400px" alt="lastOne"></img>
<img src="https://user-images.githubusercontent.com/51286325/172813467-2f0ce6c9-197f-4b33-bbf0-12804a8f279a.png" width="200px" height="400px" alt="lastTwo"></img>
<img src="https://user-images.githubusercontent.com/51286325/172813614-c4ae315d-a596-4a16-880a-356e8bd3ea00.png" width="200px" height="400px" alt="lastThree"></img>
<img src="https://user-images.githubusercontent.com/51286325/172816524-d6b7b96c-100d-4f37-80d8-e5a35d795cbe.gif" width="200px" height="400px" alt="lastFour"></img>
