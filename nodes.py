from state import EvalState
from llm import model2 as structured_model


# language check node function
def evaluate_language(state:EvalState):
    prompt =f'Evaluate the language quality of the following article and provide a feedback and assign a score out of 10 \n {state['article']}'
    output = structured_model.invoke(prompt)
    
    return{'language_feedback':output.feedback,'individual_scores':[output.score]}

#  format check node function
def evaluate_format(state:EvalState):
    prompt =f'Evaluate the format quality of the following article and provide a feedback and assign a score out of 10 \n {state['article']}'
    output = structured_model.invoke(prompt)
    
    return{'format_feedback':output.feedback,'individual_scores':[output.score]}

#  grammar check node function
def evaluate_grammar(state:EvalState):
    prompt =f'Evaluate the grammar quality of the following article and provide a feedback and assign a score out of 10 \n {state['article']}'
    output = structured_model.invoke(prompt)
    
    return{'grammar_feedback':output.feedback,'individual_scores':[output.score]}


