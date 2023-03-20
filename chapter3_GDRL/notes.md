### Balancing immediate and long-term goals

Our goal in a reinforcement learning problem is to maximize the discounted reward by following a plan. But we dont necessary need a plan for a selected state, rather for all possible state (policy).

## State-value function

we want to know the value of every state in a RL learning problem. The expected discounted reward from state s following a policy pi is the state-value function.

$q_\pi (s, a) = \displaystyle\sum_{s',r} p(s', r| s, a) [r + \gamma v_\pi (s')]$