import random
import time
from tokenize import tokenize

import mesop as me
import mesop.labs as mel


from langchain_community.llms import CTransformers
from langchain.prompts import PromptTemplate

llm = CTransformers(model="openhermes-2.5-mistral-7b.Q4_K_M.gguf", model_type= "llama", tokenize=1000)

def response(question, llm):
    
    template = """Question: {question}

    Answer:"""

    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm_chain = prompt | llm

    response = llm_chain.invoke(question)

    return response


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/chat",
  title="Opehnermes chat",
)
def page():
  mel.chat(transform, title="Openhermes chat", bot_user="Bot")


def transform(input: str, history: list[mel.ChatMessage]):
  # for line in random.sample(LINES, random.randint(3, len(LINES) - 1)):
  #   time.sleep(0.3)
    res = response(input, llm)
    print(res)
    yield res