class Graph:
    def __init__(self, my_dict, centers=[], cycle = []):
        self.my_dict = my_dict
        self.centers = centers
        self.cycle = cycle

    def DFS(self):
        node = 0
        visited = [node]
        stack = [node]
        # пока стек не пуст
        while stack:
            node = stack[-1]
            #Сохраняем вершину предка
            if (len(stack) >= 2):
                temp1 = stack.pop()
                papa = stack.pop()
                stack.append(papa)
                stack.append(temp1)
            if node not in visited:
                visited.append(node)
            remove_from_stack = True
            for next in self.my_dict[node]:
                if next not in visited:
                    stack.append(next)

                    remove_from_stack = False
                    break
                elif (len(stack) > 2) and  (next in stack) and (papa != next):
                    # В стиле стека достаем вершины
                    cycle = []
                    tempstack = []
                    tempstack = stack.copy()
                    while tempstack[-1] != next :
                        cycle.append(tempstack.pop())
                    cycle.append(next)
                    cycle.reverse()
                    counter = 0

                    for j in self.centers:
                        if j in cycle:
                            counter += 1
                    if counter <= 2:
                        self.cycle = cycle

            if remove_from_stack:
                stack.pop()
        return 'not found cycle'

    def BFS(self, a):
        n = len(self.my_dict)  # узнаем количество вершин
        used = [False] * n  # инициализируем список, в котором хранится состояние каждой вершины
        q = []  # инициализируем очередь
        q_start = 0  # индекс первого элемента очереди
        q.append(a)  # добавляем в очередь стартовую вершину
        used[a] = True  # и помечаем её, как просмотренную
        d = [0] * n
        while q_start < len(q):
            v = q[q_start]  # выбираем первую в очереди вершину
            q_start += 1  # удаляем её
            # проходимся по всем смежным вершинам от текущей, добавляем в очередь  помечаем, как просмотренные
            for i in self.my_dict[v]:
                if (used[i] == False):
                    q.append(i)
                    used[i] = True
                    d[i] = d[v] + 1
        return max(d)

    def find_nodes(self):
        nodes = []
        for i in self.my_dict:
            nodes.append(self.BFS(i))
        ans = []
        for i in range(len(nodes)):
            if nodes[i] == min(nodes):
                ans.append(i)
        self.centers = ans




