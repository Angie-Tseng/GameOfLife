#  [X-Village Python Programming (挑戰題)](https://hackmd.io/Oy66r5PkSNC7xoHbhZkwug?view)

## 模組說明
### ```main.py```
執行用模組
### ```gameoflife.py```
生命遊戲的主模組，包含以下method:
| <center>method</center> | <center>description</center> |
| --- | --- |
| ＿init＿(w=60, h=23) | 初始化世界地圖 |
| initialize\(p=1\) |初始化地圖的生命狀態<br><blockquote>p=1: Glider<br> p=2: Lightweight<br>p=3: pulsar<br>p=4~100: 數字為生命(cell)佔地圖的百分比</blockquote> |
| proceed(t) | 展示世界地圖 t 個世代的生命狀態，每秒刷新一次 | 
| display() | 顯示世界地圖 |
### ```map.py```
針對特定初始化世界地圖(p=1~3)的模組，包含以下method:
| <center>method</center> | <center>description</center> |
| --- | --- |
| ＿init＿(w,h) | 初始化世界地圖 |
| glider() | 將glider放置在地圖中央 |
| lightweight() | 將lightweight放置在地圖中央 |
| pulsar() | 將pulsar放置在地圖中央 |


## 執行結果
1. ```python3 main.py```
![](https://imgur.com/9J63EI0.png)
    

2.  ```python main.py --width=60 --height=23 --pattern=2 --generation=100```
![](https://imgur.com/vNPxT9z.gif)
