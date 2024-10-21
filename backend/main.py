
import boto3
import json
from langchain_aws import BedrockEmbeddings
from langchain_community.vectorstores import FAISS
import pandas as pd

bedrock = boto3.client(service_name="bedrock-runtime")
# body = json.dumps({
#   "max_tokens": 256,
#   "messages": [{"role": "user", "content": "Hello, world"}],
#   "anthropic_version": "bedrock-2023-05-31"
# })

df = pd.read_csv('./backend/vct.csv')
# sentences = df['sentences_column_name'].tolist() # don't really know what this is for
data = df.values.tolist()

embeddings = BedrockEmbeddings(
    client="bedrock_runtime",
    model_id="amazon.titan-embed-text-v1",  # Titan embedding model for text
)

print(data)
local_vector_store = FAISS.from_texts(data, embeddings) #df repleaced "sentences"

def retrieve_context(query):
    # Perform a similarity search using FAISS
    docs = local_vector_store.similarity_search(query)
    
    # Combine the retrieved documents into a single context string
    context = ""
    for doc in docs:
        context += doc.page_content + "\n"
    
    return context


def construct_prompt(query, context):
    prompt = f"""Use the following context to answer the question:

    {context}

    Question: {query}
    Answer:"""
    
    return prompt


def call_claude_model(prompt):
    prompt_config = {
        "prompt": prompt,
        "max_tokens_to_sample": 4096,
        "temperature": 0.5,
        "top_k": 250,
        "top_p": 0.5,
        "stop_sequences": [],  # Optional stop sequences to control output
    }
    
    body = json.dumps(prompt_config)
    
    # Use the Claude model ID from Anthropic
    model_id = "anthropic.claude-3-haiku-20240307-v1:0"  # Or "anthropic.haiku" depending on the version
    accept = "application/json"
    contentType = "application/json"
    
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept=accept,
        contentType=contentType
    )
    
    response_body = json.loads(response.get("body").read())
    
    return response_body.get("completion")


# response = bedrock.invoke_model(body=body, modelId="anthropic.claude-3-haiku-20240307-v1:0")
# response_body = json.loads(response.get("body").read())
# print(response_body.get("content"))
