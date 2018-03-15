# Install https://github.com/keras-rl/keras-rl

import numpy as np
import gym

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

from rl.agents.cem import CEMAgent
from rl.memory import EpisodeParameterMemory

ENV_NAME = 'CartPole-v0'

# Conseguimos ammbiente
env = gym.make(ENV_NAME)
np.random.seed(123)
env.seed(123)

# Conseguimos el espacio de las acciones y las dimensiones del espacio de observaciones
nb_actions = env.action_space.n
obs_dim = env.observation_space.shape[0]

#  Red neuronal más compleja
model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('softmax'))

print(model.summary())

# Configuramos y compilamos agente. S
memory = EpisodeParameterMemory(limit=1000, window_length=1)

cem = CEMAgent(model=model, nb_actions=nb_actions, memory=memory,
               batch_size=50, nb_steps_warmup=2000, train_interval=50, elite_frac=0.05)
cem.compile()

# Visualizamos el entrenamiento.
cem.fit(env, nb_steps=100000, visualize=False, verbose=2)

# Guardamos mejores pesos
cem.save_weights('cem_{}_params.h5f'.format(ENV_NAME), overwrite=True)

# Evaluamos 5 pisodios
cem.test(env, nb_episodes=5, visualize=True)