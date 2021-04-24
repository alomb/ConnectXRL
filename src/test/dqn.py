from src.connectx.constraints import ConstraintType
from src.connectx.dqn import DQN
from src.connectx.environment import ConnectXGymEnv

env = ConnectXGymEnv('random', True)
dqn = DQN(env,
          non_local=True,
          constraint=ConstraintType.LOGIC_PURE)

dqn.training_loop(20000,
                  render_env=False,
                  save_path='../',
                  update_plots_frequency=200)
input('Press to close ...')
