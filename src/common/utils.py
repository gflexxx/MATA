import matplotlib.pyplot as plt
import networkx as nx

def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def visualize_grid_graph(size_grid, agents, tasks, node_size=180, colors={'agent': 'blue', 'task': 'green', 'empty': 'black'}):
    """
    Visualizes a grid graph with agents and tasks.

    Args:
        size_grid (int): The size of the grid (size_grid x size_grid).
        agents (list): List of agents, each with a position and a name.
        tasks (list): List of tasks, each with a position and a name.
        node_size (int, optional): Size of the nodes in the plot. Defaults to 180.
        colors (dict, optional): Dictionary specifying colors for agents, tasks, and empty cells.
                                  Keys: 'agent', 'task', 'empty'. Defaults to predefined values.

    Raises:
        ValueError: If agents and tasks overlap in positions.

    Returns:
        None
    """
    # Create the grid graph
    G = nx.grid_2d_graph(size_grid, size_grid)
    pos = {(x, y): (y, -x) for x, y in G.nodes()}

    # Initialize node colors and labels
    node_colors = []
    labels = {}

    for node in G.nodes():
        agent = next((agent for agent in agents if agent.position == node), None)
        task = next((task for task in tasks if task.position == node), None)

        if agent and task:
            raise ValueError(f"Conflict at position {node}: Cannot have both agent and task.")

        if agent:
            node_colors.append(colors['agent'])
            labels[node] = agent.agent_name
        elif task:
            node_colors.append(colors['task'])
            labels[node] = task.task_name
        else:
            node_colors.append(colors['empty'])

    # Plot the graph
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, node_size=node_size, node_color=node_colors, with_labels=True,
            labels=labels, font_weight='bold', font_color='white')
    plt.title("Grid Visualization with Agents and Tasks")
    plt.show()
