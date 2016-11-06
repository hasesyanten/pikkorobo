# -*- coding: utf-8 -*- 

import cv2
import numpy as np

#--------------------------
# detectBallCoordinate
#--------------------------
# 戻り値: ボールのx座標
#
# 引数: [in]  img    入力画像
#
# 説明:
# 入力画像をハフ変換(円検出)してボールのx座標を検出する
# 複数の円が検出された場合は、半径が一番大きい円をボールとみなす
# 円が1つも検出されなかった場合は、引数ball_xに"-1"が格納される
def detectBallCoordinate(img):
	img = cv2.medianBlur(img,5)
	cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

	circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,20,
	                            param1=50,param2=30,minRadius=0,maxRadius=0)

	circles = np.uint16(np.around(circles))

	ball_x = -1
	maxradius = 0

	for i in circles[0,:]:
		if i[2] > maxradius:
			ball_x = i[0]
			maxrauius = i[2]
		
		#円検出画像の生成処理
		#cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
		#cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
	
	#cv2.imwrite('ball1_circle.png',cimg)
	return ball_x

#ロボットの動作
(
    TURN_RIGHT, #右に旋回
    TURN_LEFT,  #左に旋回
    STRAIGHT,   #直進
    TERMINATOR, #ターミネータ
) = range(0, 4)

#--------------------------
# decideRobotOperate
#--------------------------
# 戻り値:ロボット動作の識別子
#
# 引数: [in]  ball_x   ボールのx座標
#       [in]  imgWidth 画像の幅
#       [in]  range_x  「ボールが画像中央にある」と判定する範囲の半分の幅
#
# 説明:
# ball_x が画像左側にある場合は、"左旋回"動作
# ball_x が画像中央にある場合は、"直進"動作
# ball_x が画像右側にある場合は、"右旋回"動作
# ball_x が画像外の座標を示す場合は、ターミネータ(エラー)
def decideRobotOperate(ball_x, imgWidth, range_x):
	ret = TERMINATOR
	imgCenter_x = imgWidth / 2
	if 0 <= ball_x and ball_x < imgCenter_x - range_x:
		ret = TURN_LEFT
	elif imgCenter_x - range_x <= ball_x and ball_x <= imgCenter_x + range_x:
		ret = STRAIGHT
	elif imgCenter_x + range_x <= ball_x and ball_x <= imgWidth:
		ret = TURN_RIGHT
	else:
		ret = TERMINATOR
	return ret
	
#------------------------
# メイン処理
#------------------------

# カメラをキャプチャする
#cap = cv2.VideoCapture(0) # 0はカメラのデバイス番号

#beforeFrameOperate  = -1 #前フレームのロボット命令の識別子
currentFrameOperate = -1 #現フレームのロボット命令の識別子

#while True:
#ret, frame = cap.read()
frame = cv2.imread('ball1.png',0) #暫定的に入力画像を指定している

# ボールのx座標を取得
ball_x = detectBallCoordinate(frame)
print("ball_x: %d" % ball_x)

# 現フレームのロボット命令の識別子を取得
# shape[1] で画像の幅を取得できる
currentFrameOperate = decideRobotOperate(ball_x, frame.shape[1], 10)
print("currentFrameOperate: %d" % currentFrameOperate)

# 前フレームと現フレームのロボット命令の識別子が異なる場合のみ、
# ロボットに指示を送る
#if beforeFrameOperate != currentFrameOperate:
if currentFrameOperate == TURN_RIGHT:
	#右旋回の命令をロボットに送る
	print("右旋回命令 → ロボット")
elif currentFrameOperate == TURN_LEFT:
	#左旋回の命令をロボットに送る
	print("左旋回命令 → ロボット")
elif currentFrameOperate == STRAIGHT:
	#直進の命令をロボットに送る
	print("直進命令 → ロボット")
else:
	print("ボールのx座標が画像範囲外のため、エラー")
	#break

#beforeFrameOperate = currentFrameOperate

# ESCキーが押下されたときに終了
#k = cv2.waitKey(1) # 1msec待つ
#if k == 'a':
#    break

# キャプチャを解放する
#cap.release()
#cv2.destroyAllWindows()
