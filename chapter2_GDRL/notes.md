### A complex world

Complex sequential decision under  uncertainty. I do not know what will happen, but based on what I have observed in this world I am making the best possible decision to my ultimate goal.

What if I aligned my life and make the best possible actions I can conceptualize?

## Components of reinforcement learning

- agent:
    This is the decision maker. 
- environment
    The environment is simply the representation of a problem

# Learning cycle

The Agent acts on the environment by performing Action, the environment transition to a new state in condition with the action taken by the agent and in return generates a reward and a new observation which is fed to the agent.

The aim is to learn what sequential set of action will lead to the most possible reward?

// Evaluative Feedback simply means the requirements to for the Agent to "evaluate" the actions taken and determine which was the optimal action and which was also sub-optimal without direct feedback from the environment.

# Markov Property

The probability of the next state given the current state and an action is same as the probability of next state given every all previous states and actions.

# Discounted Return

G_t = R_t_1 + gmma * R_t_2 + ... 
G_t = R_t_1 + gmma * G_t_1