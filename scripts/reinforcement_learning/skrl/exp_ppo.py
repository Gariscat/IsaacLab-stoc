from itertools import product
import subprocess


if __name__ == "__main__":
    seeds = list(range(0, 4))
    
    for seed in seeds:
        
        command_components = [
            "python",
                "scripts/reinforcement_learning/skrl/train.py",
                "--seed", str(seed),
                "--task", "Isaac-Ant-Direct-v0",
                "--algorithm", "GRPO",
                "--headless",
            ]
        command = ' '.join(command_components)
        print(f"Running command: {command}")
        subprocess.call(command, shell=True)
