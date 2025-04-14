from itertools import product
import subprocess
from argparse import ArgumentParser

parser = ArgumentParser(description="Train an RL agent with skrl.")
parser.add_argument("--group_size", type=int, default=8, help="Group size of GRPO")
### parser.add_argument("--select_policy", type=str, default="advantageous", help="Policy to select source environment within each group")
args = parser.parse_args()

if __name__ == "__main__":
    seeds = [2022, 2024, 2026]
    
    for seed in seeds:
        for select_policy in ("random", "advantageous",):
            
        
            command_components = [
                "python",
                    "scripts/reinforcement_learning/skrl/train.py",
                    "--seed", str(seed),
                    "--task", "Isaac-Franka-Cabinet-Direct-v0",
                    "--algorithm", "GRPO",
                    "--group_size", str(args.group_size),
                    "--select_policy", select_policy,
                    "--headless",
                ]
            command = ' '.join(command_components)
            print(f"Running command: {command}")
            subprocess.call(command, shell=True)
