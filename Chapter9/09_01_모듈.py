# 내장 모듈
# 파이썬에 기본으로 포함되어 있는 모듈
from math import pi, ceil, ceil as c
print(pi)
print(ceil(2.7))
print(c(2.7))  # alias

# 외부 모듈
# PIP로 설치한 모듈
import pyautogui as pg
pg.moveTo(500, 500, duration=2)