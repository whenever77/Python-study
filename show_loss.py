# -*- coding: utf-8 -*-
"""
Created on 2017-12-20
@author: whenever77
ubuntu 14

在训练过程中显示loss图像并进行保存

loss文件格式如下（每行一个值）：
4.578215
3.984914
……
3.718668

使用以下命令运行：
python show_loss.py  '/home/data/pytorch_out/'

png保存形式为 loss_month_day_hours_minutes.png

"""

import matplotlib.pyplot as plt
import numpy as np
import os
import time
import sys


# dir 为训练目录，即loss.txt所在目录，直接修改为所需路径即可
dir = "/home/data/pytorch_out/"


# 如读入有参数，即sys.argv[1]有值
if len(sys.argv) >= 2:
    try:
        print("--------------------------------")
        print(sys.argv[1].split('/')[-2])
        print("--------------------------------")
        dir = sys.argv[1]
    except BaseException as e:
        print('error:\t')
        print(e)
else:
    print("--------------------------------")
    print(dir.split('/')[-2])
    print("--------------------------------")

	
	
# 读取loss的路径
path = os.path.join(dir, 'loss.txt')

# 利用时间作为画图后缀。可在训练过程中随时记录loss图像
time_tmp = list(time.localtime())[1:5]
time_now = "_".join(str(i) for i in time_tmp)

# 如路径有误，print error
try:
    dataloss = np.loadtxt(path)
    plt.plot(dataloss)
    save_path = str(dir) + 'loss_' + str(time_now) + '.png'
    plt.savefig(save_path)
    plt.show()
except BaseException as e:
    # print("--------------------------------")
    print('error:\t')
    print(e)

