n = 6
direction = [(2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2)]
startPoint=(0,0)
init = [[0 for j in range(n)] for i in range(n)]
def nextOk(point, i):
    nextp = (point[0] + direction[i][0], point[1] + direction[i][1])
    if 0 <= nextp[0] < n and 0 <= nextp[1] < n and init[nextp[0]][nextp[1]] == 0:
        return True, nextp
    else:
        return False, point

def test(point, count):
    if count > n * n:
        return True
    for i in range(8):
        ok, nextp = nextOk(point, i)
        if ok:
            init[nextp[0]][nextp[1]] = count
            result = test(nextp, count + 1)
            if result:
                return True
            else:
                init[nextp[0]][nextp[1]] = 0
    return False

init[startPoint[0]][startPoint[1]]=1
test(startPoint,2)
for i in range(n):
    print init[i]

    n 几维 * 几维
    direction 八个方向的坐标
    startPoint 起始点的坐标
    init 初始化棋盘[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    nextOk
    下一步是否可行（这一坐标的八个方向进行判断，直到找到符合条件的方向）
    test
    每一次先判断下一步是否超过总步数，记录符合条件的方向是第几步，然后递归（重复调用test）记录每一步的坐标，当下一步数不满总步数并且
    不能继续走时，回溯（回到有别的方向选择）
