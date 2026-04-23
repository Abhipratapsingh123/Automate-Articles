from langgraph import StateGraph,START,END
from typing import TypedDict,Annotated
from pydantic import BaseModel, Field


class EvalState(TypedDict):
    essay:str
    format_feedback:str
    language_feedback:str
    spelling_feedback:str
    grammar_feedback:str








   