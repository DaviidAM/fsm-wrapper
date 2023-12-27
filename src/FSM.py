from models import MachineModel, StateModel

class FSM:

    _fsm: MachineModel
    _current_state: str

    def __init__(
            self, fsm: MachineModel
            ):
        """
        FSM constructor

        Args:
            name (str): FSM name
            states (list[StateModel]): List of states inside FSM
            initial_state (str): Initial state name
            links (dict): Dict with FSM events and states transitions
        """
        self._fsm = fsm
        print(f"Starting FSM {self._fsm.name}")
        self._current_state = self._fsm.initial_state
        print(f"Initial state is {self._current_state}")



