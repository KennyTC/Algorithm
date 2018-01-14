# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
# Example 1:
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller

# Simulate the clock.

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
