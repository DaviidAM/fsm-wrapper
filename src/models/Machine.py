"""
FSM Machine model
"""

from pydantic import BaseModel, Field

from .State import StateModel


class MachineModel(BaseModel):
    """
    _summary_

    Args:
        Basemodel (_type_): _description_
    """
    name: str
    states: list[StateModel]
    initial_state: str
    next_event: str | None = None
    links: dict = Field(
        description = "links to implement transitions between states using events",
        default = {}, 
        )



