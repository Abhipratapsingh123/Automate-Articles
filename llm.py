from langchain_google_genai import ChatGoogleGenerativeAI
from output_schema import output
from dotenv import load_dotenv


load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
model2 = model1.with_structured_output(output)