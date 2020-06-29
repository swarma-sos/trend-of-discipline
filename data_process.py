from pandas import DataFrame as df
import os
import numpy as np
rootdir = r'D:\Users\CHENHAO\Desktop\swarma_sos\trend-of-discipline-master\data_sos'#文献元数据目录
dirlist = os.listdir(rootdir)
metadatas = []
for i in range(len(dirlist)):
    txt_path = os.path.join(rootdir,dirlist[i])
    print(txt_path)
    if os.path.isfile(txt_path):
        fi = open(txt_path,'r',encoding = 'utf-8')#打开元数据
        metatexts=fi.read()
        metatexts=metatexts.split('\n\n')
        for metatext in metatexts:
            metatext = metatext.split('\n')
            metadict = {}
            for metadata in metatext:
                if metadata[0]!=' ':
                    metadict[metadata[:2]] = []
                    metadict[metadata[:2]].append(metadata[3:])
                    temp_key = metadata[:2]
                else:
                    metadict[temp_key].append(metadata[3:])
            metadict.pop('ER')
            metadatas.append(metadict)
        fi.close()
print(len(metadatas))
m=np.array(metadatas)
np.save(r'metadatas.npy',metadatas)
# You can open this npy file with the following codes
# metadatas=np.load(r"D:\Users\CHENHAO\Desktop\swarma_sos\metadatas.npy",allow_pickle=True).item()
