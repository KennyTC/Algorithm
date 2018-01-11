# 1.
from datetime import datetime
import operator


def NextClosetTime(timestr):
    time = timestr.replace(":", "")
    num = set(time)
    hournum, minutenum = GenerateNumber(num)
    timediffset = {}
    for i in hournum:
        for j in minutenum:
            timenum = str(i + ":" + j)
            a = datetime.strptime(timenum, "%H:%M")
            b = datetime.strptime(timestr, "%H:%M")
            # timedifferent = datetime.strptime(timenum) -
            timedifferent = a - b
            if timedifferent.total_seconds() > 0:
                timediffset[timedifferent.total_seconds()] = a
    orderedtimediffset = sorted(timediffset)
    return timediffset[orderedtimediffset[0]].time()


def GenerateNumber(num):
    hour = []
    minute = []
    for i in num:
        for j in num:
            number = str(i + j)
            if int(number) < 60:
                minute.append(number)
            if int(number) < 24:
                hour.append(number)
    return hour, minute
# Khong giai quyet dc thoi gian gan nhat la ngay hom sau
###############################################################################
# 2. simulate the clock.

def NextClosetTime2(time):
    cur = 60 * int(time[:2]) + int(time[3:])
    print("cur=", cur)
    allowed = {int(x) for x in time if x != ':'}
    while True:
        cur = (cur + 1) % (24 * 60)
        print("cur=(cur + 1) % (24 * 60)",cur)
        if all(digit in allowed for block in divmod(cur, 60) for digit in divmod(block, 10)):# divmod(a,b)=(a//b,a%b)
            return "{:02d}:{:02d}".format(*divmod(cur, 60))

# Ta sử dụng % để xử lý khi một số nào đó vượt quá một ngưỡng mà quay lại số ban đầu. VD. 1%12 = 13%12 =1.
# Lợi dụng điều này, ta sẽ đặt 12 là ngưỡng. Một variable tăng dần, nếu >12 thì coi như quay lại là 1.

#print(NextClosetTime2("19:34"))
print(NextClosetTime2("13:59"))
