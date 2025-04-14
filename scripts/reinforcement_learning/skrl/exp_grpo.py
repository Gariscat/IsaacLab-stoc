from itertools import product
import subprocess
from argparse import ArgumentParser

parser = ArgumentParser(description="Train an RL agent with skrl.")
parser.add_argument("--group_size", type=int, default=None, help="Group size of GRPO")
args = parser.parse_args()

if __name__ == "__main__":
    seeds = list(range(0, 8))
    
    for seed in seeds:
        
        command_components = [
            "python",
                "scripts/reinforcement_learning/skrl/train.py",
                "--seed", str(seed),
                "--task", "Isaac-Franka-Cabinet-Direct-v0",
                "--algorithm", "GRPO",
                "--group_size", str(args.group_size),
                "--headless",
            ]
        command = ' '.join(command_components)
        print(f"Running command: {command}")
        subprocess.call(command, shell=True)
