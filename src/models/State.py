"""
FSM State model
"""

from pydantic import Basemodel
from 

class StateModel(Basemodel):
    """
    _summary_

    Args:
        Basemodel (_type_): _description_
    """
    name: str
    #action: Callable