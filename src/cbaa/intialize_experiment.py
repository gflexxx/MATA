from common.utils import visualize_grid_graph
def initialize_experiment(size_grid, n_agents, n_tasks, seed=42):

    random.seed(seed)
    np.random.seed(seed)

    all_locations = [(i, j) for i in range(size_grid) for j in range(size_grid)]
    random_positions = random.sample(all_locations, n_agents + n_tasks)

    agent_positions = random_positions[:n_agents]
    task_positions = random_positions[n_agents:]

    agents_data = [{'agent_id': i, 'position': agent_positions[i]} for i in range(n_agents)]
    tasks_data = [{'task_id': i, 'position': task_positions[i]} for i in range(n_tasks)]

    tasks = [Task(task_id=task_data['task_id'], position=task_data['position']) for task_data in tasks_data]
    agents = [Agent(position=agent_data['position'], id=agent_data['agent_id'], tasks=tasks) for agent_data in agents_data]

    visualize_grid_graph(size_grid, agents, tasks)

    grid = np.full((size_grid, size_grid), -1)
    for agent in agents:
        grid[agent.position] = agent.id
    for task in tasks:
        grid[task.position] = task.task_id

    return grid, agents, tasks
