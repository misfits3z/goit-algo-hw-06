import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()
DG = nx.DiGraph(G)

DG.add_nodes_from(["Hanna", "Dmytro", "Viki", "Mariia", "Roman", "Mykhailo"])
DG.add_weighted_edges_from([("Hanna", "Dmytro", 3), ("Hanna", "Viki", 2), ("Hanna", "Mariia", 5),
                            ("Dmytro", "Viki", 1), ("Dmytro", "Mykhailo", 4), ("Roman", "Viki", 2),
                            ("Viki", "Dmytro", 1),("Hanna","Roman", 3)])


# Візуалізація графа
pos = nx.spring_layout(DG)
nx.draw(DG, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, font_weight='bold', edge_color='gray', arrows=True)
edge_labels = {(u, v): d['weight'] for u, v, d in DG.edges(data=True) if 'weight' in d}
nx.draw_networkx_edge_labels(DG, pos, edge_labels=edge_labels)
plt.title("Соціальна мережа")
plt.show()


# Аналіз характеристик графа
num_nodes = DG.number_of_nodes()
num_edges = DG.number_of_edges()
average_degree = sum(dict(DG.degree()).values()) / num_nodes

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Середній ступінь вершин: {average_degree}")
print("")

# Алгоритм Дейкстри
shortest_paths = nx.single_source_dijkstra_path(DG, source="Hanna")
shortest_path_lengths = nx.single_source_dijkstra_path_length(DG, source="Hanna")

print(f"Довжини найкоротших шляхів: {shortest_path_lengths}")
print(f"Найкоротші шляхи від Hanna до інших вершин:")
for node, distance in shortest_paths.items():
    print(f"{node}: {distance}")
print("")


# алгоритм DFS
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    result = [vertex]  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            result += dfs_recursive(graph, neighbor, visited)
    return result

dfs_result = dfs_recursive(DG, "Hanna")
print("DFS Result:", dfs_result)


# алгоритм BFS
def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    result = [] #створюємо пустий список result, де зберігаємо результати обходу графа
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            queue.extend(set(graph.neighbors(vertex)) - visited)
    return result

bfs_result = bfs_recursive(DG, deque(["Hanna"]))
print("BFS Result:", bfs_result)
