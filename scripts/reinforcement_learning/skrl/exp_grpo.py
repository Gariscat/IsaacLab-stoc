from itertools import product
import subprocess


if __name__ == "__main__":
    seeds = list(range(8))
    
    for seed in seeds:
        
        command_components = [
            "python",
                "scripts/reinforcement_learning/skrl/train.py",
                "--seed", str(seed),
                "--task", "Isaac-Franka-Cabinet-Direct-v0",
                "--algorithm", "GRPO",
                "--headless",
            ]
        command = ' '.join(command_components)
        print(f"Running command: {command}")
        subprocess.call(command, shell=True)
