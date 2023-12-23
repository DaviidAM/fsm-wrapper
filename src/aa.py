from src.models import Machine, State

machine = Machine(name='machine1', states=[State(name='state1')], initial_state = 'state1')

print(machine)