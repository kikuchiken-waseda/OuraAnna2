import pandas as pd
import numpy as np
import glob
import os

li = os.listdir('./data/')
#print(li)

for l in li:
    li2 = os.listdir('./data/' +l)
    #print(li2)

    for l2 in li2:

        file = glob.glob('./data/' +l+ '/' +l2+ '/xy/*.xy')
        os.makedirs('./data/' +l+ '/' +l2+ '/xy3', exist_ok=True)

        for m in file:
            # ファイルを読み込む
            f = open(m, 'r')

            # 区切り文字を指定してリスト化
            lst = f.read().split('\n') # 改行コードでリスト化

            data = []
            ind = []
            for i in lst:
                ls = i.split(',')
                #print(ls)
                if ls[0] == "":
                    #print('null')
                    pass
                else:
                    data.append(ls[1:])
                    ind.append(ls[0])

            #col.remove('frm')
            # DataFrame化
            df = pd.DataFrame(data, index=ind)
            print(df)

            # 保存 # ファイル名を決めるために色々条件分岐使ってます
            name = m[-5:-2]
            if '_' in name:
                name = '0' + m[-4:-2]
            else:
                pass
            #print(name)

            df.to_csv('./data/' +l+ '/' +l2+ '/xy3/' +name+ 'csv')

            f.close()
