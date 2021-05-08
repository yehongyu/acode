import random

def self_rand(n):
    return random.randint(0, n-1)

def rand7_using_rand5():
    cnt = 0
    while True:
        cur = self_rand(5) * 5 + self_rand(5)
        cnt += 1
        if cur >= 21: continue
        else: break
    return cur // 3, cnt

def rand3_using_rand5():
    cnt = 0
    while True:
        cur = self_rand(5)
        cnt += 1
        if cur >= 3: continue
        else: break
    return cur, cnt

def rand10_using_rand7():
    cnt = 0
    while True:
        cur = self_rand(7) * 7 + self_rand(7)
        cnt += 1
        if cur >= 40: continue
        else: break
    return cur//4, cnt
def rand10_using_rand5():
    cnt = 0
    while True:
        cur = self_rand(5) * 5 + self_rand(5)
        cnt += 1
        if cur >= 20: continue
        else: break
    return cur//2, cnt



def rand6_using_rand2():
    cnt = 0
    while True:
        cur = self_rand(2) * 4 + self_rand(2) * 2 + self_rand(2)
        cnt += 1
        if cur >= 6: continue
        else: break
    return cur, cnt

def rand01_using_rand01p():
    cnt = 0
    while True:
        a = self_rand(2)
        b = self_rand(2)
        cnt += 1
        if a == b: continue
        else: break
    return a, cnt

def randk_using_rand2(k):
    if k <=2: return None
    bits = 0
    tmp = k-1
    while tmp > 0:
        tmp = tmp >> 1
        bits += 1
    cnt = 0
    while True:
        cur = 0
        for i in range(bits):
            cur = cur * 2 + self_rand(2)
        cnt += 1
        if cur >= k: continue
        else: break
    return cur, cnt

if __name__ == '__main__':
    cnt_map = {}
    total_cnt = 0
    times = 100000
    for i in range(times):
        #cur, cur_cnt = rand7_using_rand5()
        #cur, cur_cnt = rand3_using_rand5()
        #cur, cur_cnt = rand6_using_rand2()
        #cur, cur_cnt = rand10_using_rand5()
        #cur, cur_cnt = rand10_using_rand7()
        #cur, cur_cnt = rand01_using_rand01p()
        cur, cur_cnt = randk_using_rand2(16)
        if cur not in cnt_map:
            cnt_map[cur] = 0
        total_cnt += cur_cnt
        cnt_map[cur] += 1
    print(cnt_map)
    print(total_cnt, total_cnt/times)