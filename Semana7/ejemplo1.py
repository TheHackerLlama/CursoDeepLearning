# https://github.com/openai/gym/wiki/CartPole-v0

import gym
env = gym.make('CartPole-v0')
env.reset()

# Tomamos 1000 pasos
for _ in range(1000):
    env.render()

    # Tomamos una acción aleatoria
    action = env.action_space.sample()

    # Ejecutamos acción
    env.step(action)