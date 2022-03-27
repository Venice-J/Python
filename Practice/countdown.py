import time

h = int(input('請輸入小時：'))
m = int(input('請輸入分鐘：'))
s = int(input('請輸入秒:'))

def countdown( hour , min , sec ):
    while True:
        timeformat = '{:02d}:{:02d}:{:02d}'.format(hour,min,sec)
        print(timeformat , end='\r')
        time.sleep(1)

        if sec != 0:
            sec -= 1
        elif sec == 0 and min != 0 :
            min -= 1 
            sec = 59
        elif min == 0 and hour != 0 :
            hour -= 1
            min = 59
            sec = 59
        elif hour == 0 and min == 0 and sec == 0 :
            print('TimesUp')
            break

if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
    print('\n倒數計時開始')
    countdown(h,m,s)
else:
    print('時間輸入錯誤!!!')