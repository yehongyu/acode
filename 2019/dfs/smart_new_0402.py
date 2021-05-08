# 1. 从file：一行一个keyword，随机sample k个出来，保持先后顺序；
# 2. 有raw-data, 和刚刚随机sample出来的数据，找到samples中的idx


def sample_k(k, file):
    f = open(file, 'r')
    i = 0
    res = [None] * k
    for line in f:
        line = line.strip()
        i += 1
        if i <= k:
            res[i - 1] = line
            continue
        prob = random.randint(1, i)
        if prob <= k:
            res.pop(prob - 1)
            res.append(line)
            # res[prob-1]=line
    f.close()
    return res


def position(raw_data, samples):
    map = {}  # key: raw line, val:[idxs]
    for line in samples: map[line] = []
    for i in range(len(raw_data)):
        line = raw_data[i]
        if line in map: map[line].append(i)
    res = [];
    path = []
    items = [map[line] for line in samples]
    self.dfs(items, res, path)
    return res


def dfs(items, res, path):
    pos = len(path)
    if pos >= len(items):
        res.append(path[0:])
        print(path[0:]);
        return
    min_limit = path[-1] if pos > 0 else -1
    for idx in items[pos]:
        if idx > min_limit:
            path.append(idx)
            self.dfs(items, res, path)
            path.pop(-1)


