import gym
env = gym.make('CartPole-v0')

# Hacemos 20 pruebas
for i_episode in range(20):
	# Reseteamos para cada prueba
    observation = env.reset()

    # Hacemos 100 pasos o hasta que terminemos
    for t in range(100):
        env.render()

        # Elegimos acción aleatoria
        action = env.action_space.sample()

        # Sacamos información del ambiente
        observation, reward, done, info = env.step(action)

        # Si terminamos, cerramos
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break