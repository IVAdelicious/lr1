class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        # Добавляем ребро от node к neighbor
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def bfs(self, start_node):
        # Обход в ширину (Breadth-First Search)
        visited = set()  # Множество для отслеживания посещенных узлов
        queue = [start_node]  # Очередь для обхода

        visited.add(start_node)

        while queue:
            node = queue.pop(0)
            print(node, end=" ")  # Вывод текущего узла

            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

    def dfs(self, start_node):
        # Обход в глубину (Depth-First Search)
        visited = set()  # Множество для отслеживания посещенных узлов
        self._dfs_recursive(start_node, visited)

    def _dfs_recursive(self, node, visited):
        # Рекурсивная функция для обхода в глубину
        visited.add(node)
        print(node, end=" ")  # Вывод текущего узла

        if node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    self._dfs_recursive(neighbor, visited)

# Пример использования
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')

print("BFS (Обход в ширину):")
graph.bfs('A')  # Начинаем обход в ширину с узла 'A'
print("\nDFS (Обход в глубину):")
graph.dfs('A')  # Начинаем обход в глубину с узла 'A'
