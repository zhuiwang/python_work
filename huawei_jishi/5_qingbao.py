#!/usr/bin/env python3

while True:
    try:
        s = input()
        s1 = s[::-1]
        f = 0
        # for i in range(1, len(s)+1)[::-1]:
            # if f == 1:
                # break
            # for j in range(len(s)+1-i):
                # ts = s[j:j+1]
                # print(ts)
                # if s1.count(ts) > 0 and ts == ts[::-1]:
                    # print(i)
                    # f = 1
                    # break

        for i in range(len(s)):
            if s == s1:
                print(len(s))
                break
            else:
                s = s[1:]
                s1 = s[::-1]
                print(s)

    except:
        break
