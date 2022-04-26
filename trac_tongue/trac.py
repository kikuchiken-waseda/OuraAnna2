import pandas as pd
import glob
import cv2
import os

def draw_trac(filename, png_folder, show=False, mode=0):
    # Excelファイルの読み込み
    df = pd.read_excel(filename, sheet_name='points')

    # データを抽出
    X = df['x']
    Y = df['y']

    # 画像の読み込み
    files = glob.glob(png_folder +'/*.png')
    i = 0

    # 1枚ずつ処理
    for file in files:
        im = cv2.imread(file)
        # 対応点の座標を取得
        x = int(X[i])
        y = int(Y[i])

        # 軌跡を描画
        if mode == 0: ## 舌接触前後両方
            col = (0, 255, 255)
            if i==0:
                im2 = cv2.circle(im, (x,y), 1, color=col, thickness=2)
            else:
                if i <= 3: #舌接触前
                    for a in range(0, i):
                        x1 = int(X[a])
                        y1 = int(Y[a])
                        x2 = int(X[a+1])
                        y2 = int(Y[a+1])
                        im2 = cv2.line(im, (x1,y1), (x2,y2), color=col, thickness=2, lineType=cv2.LINE_8, shift=0)
                else: #舌接触後
                    for a in range(0, 3):
                        x1 = int(X[a])
                        y1 = int(Y[a])
                        x2 = int(X[a+1])
                        y2 = int(Y[a+1])
                        im2 = cv2.line(im, (x1,y1), (x2,y2), color=col, thickness=2, lineType=cv2.LINE_8, shift=0)
                    for a in range(3, i):
                        col = (255, 255, 0)
                        x1 = int(X[a])
                        y1 = int(Y[a])
                        x2 = int(X[a+1])
                        y2 = int(Y[a+1])
                        im2 = cv2.line(im, (x1,y1), (x2,y2), color=col, thickness=2, lineType=cv2.LINE_8, shift=0)
        elif mode == 1: ## 舌接触後のみ
            col = (255, 255, 0)
            if i <= 3:
                im2 = im
            elif i == 4:
                im2 = cv2.circle(im, (x,y), 1, color=col, thickness=2)
            else:
                for a in range(3, i):
                    x1 = int(X[a])
                    y1 = int(Y[a])
                    x2 = int(X[a+1])
                    y2 = int(Y[a+1])
                    im2 = cv2.line(im, (x1,y1), (x2,y2), color=col, thickness=2, lineType=cv2.LINE_8, shift=0)
        else: ## 舌接触前のみ
            col = (0, 255, 255)
            if i == 0:
                im2 = cv2.circle(im, (x,y), 1, color=col, thickness=2)
            elif i <= 3 and i > 0:
                for a in range(0, i):
                    x1 = int(X[a])
                    y1 = int(Y[a])
                    x2 = int(X[a+1])
                    y2 = int(Y[a+1])
                    im2 = cv2.line(im, (x1,y1), (x2,y2), color=col, thickness=2, lineType=cv2.LINE_8, shift=0)
            else:
                im2 = im

        # 画像の表示
        if show:
            cv2.namedWindow(filename[7:-5], cv2.WINDOW_NORMAL)
            cv2.imshow(filename[7:-5], im2)
            cv2.waitKey(0)
            #cv2.destroyAllWindow()

        i += 1

    return im2

if __name__ == '__main__':

    li = glob.glob('./xlsx/*.xlsx')
    for l in li:
        src = './png'+ l[6:-5]
        im = draw_trac(l, src, show=True)

        # 保存
        result_folder = 'result'
        os.makedirs('./' +result_folder, exist_ok=True)
        cv2.imwrite('./' +result_folder+ '/' +l[7:-5]+ '.png', im)
