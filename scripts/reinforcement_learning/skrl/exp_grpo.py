import multiprocessing
from itertools import product
import subprocess
import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "2"
import argparse
from typing import Dict

parser = argparse.ArgumentParser()
parser.add_argument(
    "--comment",
    type=str,
    default="",
)
args = parser.parse_args()

def run_training(params: Dict):
    gpu = params["gpu_id"]
    command_components = [
        f"CUDA_VISIBLE_DEVICES={gpu} python",
        "scripts/reinforcement_learning/skrl/train.py",
        "--seed", str(seed),
        "--task", "Isaac-Franka-Cabinet-SR-v0",
        "--algorithm", "GRPO",
        f"--comment {params['comment']}" if params.get('comment') else "",
        f"--rollouts {params['rollouts']}" if params.get('rollouts') else "",
        f"--group_size {params['group_size']}" if params.get('group_size') else "",
        f"--discount_factor {params['discount_factor']}" if params.get('discount_factor') else "",
        "--headless",
    ]
    command = ' '.join(command_components)
    print(f"Running command: {command}")
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error in process with params {params}: {e}")

if __name__ == "__main__":
    x = 0
    seeds = list(range(x, x+2))
    available_gpus = (1, 2, 3, 4,)
    rollouts_s = (128, 256)
    discount_factors = (0.99, 0.999, 0.9999)
    group_sizes = (8, 32, 128, 512)
    
    exp_params = []
    idx = 0
    for seed, rollouts, discount_factor, group_size in product(seeds, rollouts_s, discount_factors, group_sizes):
        '''command_components = [
            "python",
                "scripts/reinforcement_learning/skrl/train.py",
                "--seed", str(seed),
                "--task", "Isaac-Franka-Cabinet-SR-v0",
                "--algorithm", "GRPO",
                
                "--headless",
            ]'''
        exp_params += [{
            "gpu_id": available_gpus[idx],
            "comment": args.comment,
            "rollouts": rollouts,
            "discount_factor": discount_factor,
            "group_size": group_size
        }]
        idx = (idx + 1) % len(available_gpus)
        '''command = ' '.join(command_components)
        print(f"Running command: {command}")
        subprocess.call(command, shell=True)'''
        
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(run_training, exp_params)
