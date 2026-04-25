from typing import TypedDict, Annotated
import operator 


class EvalState(TypedDict):
    article:str
    language_feedback:str
    format_feedback:str
    grammar_feedback:str
    individual_scores:Annotated[list[int],operator.add] # reducer