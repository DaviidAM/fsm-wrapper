"""
FSM Links model
"""

from pydantic import BaseModel 

class LinksModel(BaseModel):
    """
    _summary_

    Args:
        Basemodel (_type_): _description_
    """
    event: str
    next_state: str