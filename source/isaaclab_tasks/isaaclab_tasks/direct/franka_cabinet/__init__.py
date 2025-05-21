# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause
"""
Franka-Cabinet environment.
"""

import gymnasium as gym

from . import agents

##
# Register Gym environments.
##

gym.register(
    id="Isaac-Franka-Cabinet-Direct-v0",
    entry_point=f"{__name__}.franka_cabinet_env:FrankaCabinetEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.franka_cabinet_env:FrankaCabinetEnvCfg",
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:FrankaCabinetPPORunnerCfg",
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_ppo_cfg.yaml",
        "skrl_grpo_cfg_entry_point": f"{agents.__name__}:skrl_grpo_cfg.yaml"
    },
)

gym.register(
    id="Isaac-Franka-Stochastic-Cabinet-v0",
    entry_point=f"{__name__}.franka_cabinet_stochastic_env:FrankaCabinetStochasticEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.franka_cabinet_stochastic_env:FrankaCabinetStochasticEnvCfg",
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:FrankaCabinetPPORunnerCfg",
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_ppo_stochastic_env_cfg.yaml",
    },
)

gym.register(
    id="Isaac-Franka-Cabinet-SR-v0",
    entry_point=f"{__name__}.franka_cabinet_sparse_reward_env:FrankaCabinetSREnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.franka_cabinet_sparse_reward_env:FrankaCabinetSREnvCfg",
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_ppo_sr_cfg.yaml",
        "skrl_grpo_cfg_entry_point": f"{agents.__name__}:skrl_grpo_sr_cfg.yaml"
    },
)

gym.register(
    id="Isaac-Franka-Cabinet-Multi-Cab-v0",
    entry_point=f"{__name__}.franka_cabinet_multi_cab_env:FrankaCabinetMultiCabEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.franka_cabinet_multi_cab_env:FrankaCabinetMultiCabEnvCfg",
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_ppo_mc_cfg.yaml",
        "skrl_grpo_cfg_entry_point": f"{agents.__name__}:skrl_grpo_mc_cfg.yaml"
    },
)