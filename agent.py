from langgraph.graph import StateGraph,START,END
from nodes import evaluate_language,evaluate_format,evaluate_grammar
from state import EvalState

# defining workflow
graph = StateGraph(EvalState)

graph.add_node("language", evaluate_language)
graph.add_node("format", evaluate_format)
graph.add_node("grammar", evaluate_grammar)


# definging edges
graph.add_edge(START,"language")
graph.add_edge("language","format")
graph.add_edge("format","grammar")
graph.add_edge("grammar",END)


workflow = graph.compile()




















   