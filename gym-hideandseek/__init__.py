from gym.envs.registration import register

register(
    id='hideandseek-v0',
    entry_point='gym_hideandseek.envs:hideandseekEnv',
)
register(
    id='hideandseek-extrahard-v0',
    entry_point='gym_hideandseek.envs:hideandseekExtraHardEnv',
)