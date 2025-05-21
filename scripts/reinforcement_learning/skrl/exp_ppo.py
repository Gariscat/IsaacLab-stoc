from itertools import product
import subprocess
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--comment",
    type=str,
    default="",
)
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()

if __name__ == "__main__":
    x = 0
    seeds = list(range(x, x+3))
    
    for seed in seeds:
        
        command_components = [
            "python",
                "scripts/reinforcement_learning/skrl/train.py",
                "--seed", str(seed),
                "--task", "Isaac-Franka-Cabinet-SR-v0",
                "--algorithm", "PPO",
                "--comment", args.comment,
                "--headless",
                "--debug" if args.debug else "",
            ]
        command = ' '.join(command_components)
        print(f"Running command: {command}")
        subprocess.call(command, shell=True)
