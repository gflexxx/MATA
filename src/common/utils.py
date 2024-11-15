import matplotlib.pyplot as plt
import networkx as nx

def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def visualize_grid_graph(size_grid, agents, tasks):
    G = nx.grid_2d_graph(size_grid, size_grid)
    pos = {(x, y): (y, -x) for x, y in G.nodes()}

    node_colors = []
    labels = {}

    for node in G.nodes():
        agent = next((agent for agent in agents if agent.position == node), None)
        task = next((task for task in tasks if task.position == node), None)

        if agent:
            node_colors.append('blue')
            labels[node] = agent.agent_name
        elif task:
            node_colors.append('green')
            labels[node] = task.task_name
        else:
            node_colors.append('black')

    plt.figure(figsize=(5, 5))
    nx.draw(G, pos, node_size=180, node_color=node_colors, with_labels=True, labels=labels, font_weight='bold', font_color='white')
    plt.title("Grid Visualization with Agents and Tasks")
    plt.show()
