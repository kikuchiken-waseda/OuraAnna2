import pandas as pd
import glob
import cv2
import os

def draw_trac(filename, png_folder, show=False):
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

        # 点を描画
        im2 = cv2.circle(im, (x,y), 1, color=(255, 255, 0), thickness=2)
        # 軌跡を描画
        if i==0:
            pass
        else:
            for a in range(0, i):
                x1 = int(X[a])
                y1 = int(Y[a])
                x2 = int(X[a+1])
                y2 = int(Y[a+1])
                im2 = cv2.line(im2, (x1,y1), (x2,y2), color=(255, 255, 0), thickness=2, lineType=cv2.LINE_8, shift=0)

        # 画像の表示
        if show:
            cv2.namedWindow('image', cv2.WINDOW_NORMAL)
            cv2.imshow('image', im2)
            cv2.waitKey(0)
            #cv2.destroyAllWindow()

        i += 1

    return im2

if __name__ == '__main__':

    li = glob.glob('./xlsx/*.xlsx')
    for l in li:
        src = './png'+ l[6:-5]
        im = draw_trac(l, src, show=False)

        # 保存
        result_folder = 'result'
        os.makedirs('./' +result_folder, exist_ok=True)
        cv2.imwrite('./' +result_folder+ '/' +l[7:-5]+ '.png', im)
