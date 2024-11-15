from cbaa.initialize_experiment import initialize_experiment
from cbaa.cbaa_algorithm import run_cbaa_experiment
import numpy as np

def run():
    # Initialize experiment parameters
    size_grid = 5
    n_agents = 10
    n_tasks = 4
    seed = 42
    grid, agents, tasks = initialize_experiment(size_grid, n_agents, n_tasks, seed)

    # Define the communication graph (for simplicity, using a fully connected graph)
    communication_graph = np.ones((n_agents, n_agents)) 

    # Run the CBAA experiment
    assignments = run_cbaa_experiment(agents, communication_graph)
    print("Final task assignments:", assignments)

if __name__ == "__main__":
    run()
