'''import multiprocessing
import itertools
import subprocess
from argparse import ArgumentParser

parser = ArgumentParser(description="Train an RL agent with skrl.")
args = parser.parse_args()

def run_training(params):
    seed, select_policy, group_size = params
    command_components = [
        "python",
        "scripts/reinforcement_learning/skrl/train.py",
        "--seed", str(seed),
        "--task", "Isaac-Franka-Cabinet-Direct-v0",
        "--algorithm", "GRPO",
        "--group_size", str(group_size),
        "--select_policy", select_policy,
        "--headless",
    ]
    command = ' '.join(command_components)
    print(f"Running command: {command}")
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error in process with params {params}: {e}")

if __name__ == "__main__":
    seeds = list(range(2015, 2025))
    select_policies = ["random", "advantageous"]
    group_sizes = [8, 16, 32, 64, 128]
    
    param_grid = list(itertools.product(seeds, select_policies, group_sizes))
    
    # num_processes = min(multiprocessing.cpu_count(), len(param_grid))
    num_processes = 1
    print(f"Using {num_processes} processes")
    
    with multiprocessing.Pool(processes=num_processes) as pool:
        pool.map(run_training, param_grid)'''
        
from itertools import product
import subprocess
import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "2"

if __name__ == "__main__":
    x = 2024
    seeds = list(range(x, x+2))
    
    rollouts_s = (128, 256)
    discount_factors = (0.9, 0.99, 0.999, 0.9999)
    
    for seed, rollouts, discount_factor in product(seeds, rollouts_s, discount_factors):
        command_components = [
            "python",
                "scripts/reinforcement_learning/skrl/train.py",
                "--seed", str(seed),
                "--task", "Isaac-Franka-Cabinet-SR-v0",
                "--algorithm", "GRPO",
                "--rollouts", str(rollouts),
                "--discount_factor", str(discount_factor),
                "--headless",
            ]
        command = ' '.join(command_components)
        print(f"Running command: {command}")
        subprocess.call(command, shell=True)
