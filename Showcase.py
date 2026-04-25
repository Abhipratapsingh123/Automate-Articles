from IPython.display import Image
from agent import workflow  



Image(workflow.get_graph().draw_mermaid_png())