from collections import deque

step = [[-1, 0], [1, 0], [0, -1], [0, 1]]


# Nhập dữ liệu.
def enter():
    m, n = map(int, input().split())

    a = [[] for _ in range(m + 1)]
    for i in range(1, m + 1):
        a[i] = [0] + [int(j) for j in input().split()]

    x1, y1, x2, y2 = map(int, input().split())

    return m, n, a, x1, y1, x2, y2


# Kiểm tra một ô có hợp lệ để đi vào không.
def is_valid(x, y, m, n, dp, a):
    return 1 <= x <= m and 1 <= y <= n and dp[x][y] == 0 and a[x][y] == 0


# Loang trên ma trận.
def solution(m, n, a, x1, y1, x2, y2):
    qu = deque(())
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    trace = [[(0, 0)] * (n + 1) for _ in range(m + 1)]
    dp[x1][y1] = 1
    qu.append((x1, y1))

    while len(qu) > 0:
        cur = qu[0]
        qu.popleft()

        if cur[0] == x2 and cur[1] == y2:
            break

        for i in range(4):
            next_x, next_y = cur[0] + step[i][0], cur[1] + step[i][1]

            if is_valid(next_x, next_y, m, n, dp, a):
                dp[next_x][next_y] = dp[cur[0]][cur[1]] + 1
                trace[next_x][next_y] = cur
                qu.append((next_x, next_y))

    if not dp[x2][y2]:
        return -1, 0, 0
    else:
        path = []
        cell = (x2, y2)
        while cell[0] != 0 and cell[1] != 0:
            path.append(cell)
            cell = trace[cell[0]][cell[1]]

        return 1, dp[x2][y2], path


# Xử lý các trường hợp bài toán.
def main():
    m, n, a, x1, y1, x2, y2 = enter()
    res, minimum_distance, path = solution(m, n, a, x1, y1, x2, y2)

    if res == -1:
        print(-1)
    else:
        print(minimum_distance)

        for i in range(len(path) - 1, -1, -1):
            print(path[i][0], path[i][1])


if __name__ == '__main__':
    main()
