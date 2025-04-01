from itertools import product
import subprocess


if __name__ == "__main__":
    seeds = (2022, 2024, 2026)
    random_rotation_z_ranges = ((-15, 15), (-30, 30), (-60, 60))
    random_offset_ranges = ((-0.1, 0.1), (-0.2, 0.2), (-0.5, 0.5), (-1, 1))
    
    for seed, random_rotation_z_range, random_offset_range in product(seeds, random_rotation_z_ranges, random_offset_ranges):
        command_components = [
            "python",
            "scripts/reinforcement_learning/skrl/train_stochastic_cabinet.py",
            "--seed", str(seed),
            "--random_rotation_z_range", ' '.join(map(str, random_rotation_z_range)),
            "--random_offset_x_range", ' '.join(map(str, random_offset_range)),
            "--random_offset_y_range", ' '.join(map(str, random_offset_range)),
            "--random_offset_z_range", ' '.join(map(str, random_offset_range)),
            "--headless",
        ]
        command = ' '.join(command_components)
        print(f"Running command: {command}")
        subprocess.call(command, shell=True)
