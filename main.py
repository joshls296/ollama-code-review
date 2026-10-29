from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

app = FastAPI()

# Allow React frontend on localhost:5173 to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeSnippet(BaseModel):
    language: str
    code: str

@app.post("/api/review")
async def review_code(snippet: CodeSnippet):
    llm = ChatOllama(model="codellama", temperature=0)

    prompt = PromptTemplate.from_template(
        "Analyze the following {language} code for bugs, security risks, and optimization opportunities:\n\n{code}"
    )

    chain = prompt | llm
    response = chain.invoke({"language": snippet.language, "code": snippet.code})

    return {"analysis": response.content}