from pydantic import BaseModel, Field


class output(BaseModel):
    feedback:str = Field(description='Detailed feedback for the essay')
    score:int = Field(description='Score out of 10',ge=0,le=10)



    