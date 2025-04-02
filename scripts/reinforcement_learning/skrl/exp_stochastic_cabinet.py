from itertools import product
import subprocess


if __name__ == "__main__":
    seeds = (2022, 2026)
    random_rotation_z_ranges = ((-15, 15), (-30, 30), (-60, 60))
    random_offset_ranges = ((-0.25, 0.25), (-0.5, 0.5), (-1, 1))
    
    for add_rot_to_obs in (True, False):
        for seed, random_rotation_z_range, random_offset_range in product(seeds, random_rotation_z_ranges, random_offset_ranges):
            random_offset_y_range = random_offset_range
            
            # Avoid model collision
            random_offset_x_range = (random_offset_range[0], min(random_offset_range[1], 0))
            random_offset_z_range = (max(random_offset_range[0], 0), random_offset_range[1])
            
            command_components = [
                "python",
                "scripts/reinforcement_learning/skrl/train_stochastic_cabinet.py",
                "--seed", str(seed),
                "--random_rotation_z_range", ' '.join(map(str, random_rotation_z_range)),
                "--random_offset_x_range", ' '.join(map(str, random_offset_x_range)),
                "--random_offset_y_range", ' '.join(map(str, random_offset_y_range)),
                "--random_offset_z_range", ' '.join(map(str, random_offset_z_range)),
                "--headless",
            ]
            if add_rot_to_obs:
                command_components.append("--add_rot_to_obs")
                
            command = ' '.join(command_components)
            print(f"Running command: {command}")
            subprocess.call(command, shell=True)
