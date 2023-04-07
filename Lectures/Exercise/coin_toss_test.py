# from Lecture.Exercise.my_modules import coin_toss_module

import sys
sys.path.append('my_modules')
import coin_toss_module

for i in range(10):
    print(coin_toss_module.coin_toss())