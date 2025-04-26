from itertools import product
import subprocess
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

if __name__ == "__main__":
    seeds = list(range(0, 4))
    
    for seed in seeds:
        
        command_components = [
            "python",
                "scripts/reinforcement_learning/skrl/train.py",
                "--seed", str(seed),
                "--task", "Isaac-Franka-Cabinet-SR-v0",
                "--algorithm", "PPO",
                "--headless",
            ]
        command = ' '.join(command_components)
        print(f"Running command: {command}")
        subprocess.call(command, shell=True)
