from models import MachineModel, StateModel
from time import sleep

machine = MachineModel(name='machine1', states=[StateModel(name='state1')], initial_state = 'state1')

print(machine)

model = StateModel(name="bbb")
model.action()

def state_action():
    sleep(3)


