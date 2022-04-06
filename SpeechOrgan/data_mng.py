import pandas as pd
import numpy as np
import glob
import os

li = os.listdir('./data/')
#print(li)

for l in li:
    file = glob.glob('./data/' +l+ '/xy/*.xy')

    os.makedirs('./data/' +l+ '/xy2', exist_ok=True)

    for m in file:
        # ファイルを読み込む
        f = open(m, 'r')

        # 区切り文字を指定してリスト化
        lst = f.read().split('\n') # 改行コードでリスト化

        data = []
        ind = []
        count = 0
        for i in lst:
            ls = i.split(',')
            #print(ls)
            if ls[0] == "":
                #print('null')
                pass
            else:
                if count == 0:
                    col = ls
                else:
                    data.append(ls[1:])
                    ind.append(ls[0])
            count += 1

        col.remove('frm')
        # DataFrame化
        df = pd.DataFrame(data, columns=col, index=ind)

        # 保存 # ファイル名を決めるために色々条件分岐使ってます
        name = m[-8:-2]
        if 's' in name:
            if name.find('.') - name.find('_') != 3:
                name = name[1:]
            else:
                pass
        else:
            name = 's' + name
        #print(name)

        df.to_csv('./data/' +l+ '/xy2/' +name+ 'csv')

        f.close()
