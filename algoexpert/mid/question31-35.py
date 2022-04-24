

def cycleInGraph(edges):
    # Write your code here.
    def bfs(index, edges_, visited):

        edge = edges_[index]
        flag = False
        for idx in edge:
            if flag:
                break
            if idx in visited:
                flag = True
                break
            else:
                visited.add(idx)
                flag = bfs(idx, edges_, visited)
                visited.remove(idx)
        return flag

    for i in range(len(edges)):
        if bfs(i, edges, {i}):
            return True
    return False


def minimumPassesOfMatrix(matrix):
    # Write your code here.
    def check_matrix(ma):
        directions = [[0,1],[0,-1],[1, 0], [-1,0]]
        r = len(ma)
        c = len(ma[0])
        neg_flag = False
        changable_flag = False
        need_changes = []
        for i in range(r):
            for j in range(c):
                if ma[i][j] < 0:
                    neg_flag = True
                    for direction in directions:
                        new_i = i + direction[0]
                        new_j = j + direction[1]
                        if 0 <= new_i < r and 0 <= new_j < c:
                            if ma[new_i][new_j] > 0:
                                changable_flag = True
                                need_changes.append((i,j))
                                break
        for t in need_changes:
            ma[t[0]][t[1]] *= -1
        return neg_flag, changable_flag

    if matrix:
        count = 1
        nf, cf = check_matrix(matrix)
        print(matrix)
        if nf and not cf:
            return -1
        while nf and cf:
            nf, cf = check_matrix(matrix)
            print(matrix)
            count += 1
        return count - 1

    return -1


def taskAssignment(k, tasks):
    # Write your code here.
    tasks = sorted(tasks)

    return [[tasks[i], tasks[2* k - 1]] for i in range(k)]


def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    number_of_cities = len(distances)
    miles_remaining = 0

    index = 0
    miles_remaining_from_index = 0
    for idx in range(1, number_of_cities):
        distance = distances[idx - 1]
        prev_fuel = fuel[idx - 1]
        miles_remaining += prev_fuel * mpg - distance

        if miles_remaining < miles_remaining_from_index:
            index = idx
            miles_remaining_from_index = miles_remaining
    return index

    return -1


if __name__ == '__main__':
    m =[
    [-1, 0, 3],
    [0, -5, -6]
  ]
    print(minimumPassesOfMatrix(m))
    print(m)