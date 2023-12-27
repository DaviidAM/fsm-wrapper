"""
FSM State model
"""

from pydantic import BaseModel, Field

from typing import Callable

from .Links import LinksModel

def default_state_action():
    print(f"Executing default action for current state")

class StateModel(BaseModel):
    """
    _summary_

    Args:
        Basemodel (_type_): _description_
    """
    name: str
    action: Callable = Field(
        description="Action to execute in state",
        default=default_state_action
        )
    #links: list[LinksModel]