import json
import boto3
from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.vectorstores import FAISS

# Setup bedrock
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
)

sentences = [
    # Pets
    "Your dog is so cute.",
    "How cute your dog is!",
    "You have such a cute dog!",
    # Cities in the US
    "New York City is the place where I work.",
    "I work in New York City.",
    # Color
    "What color do you like the most?",
    "What is your favourite color?",
]


def agent_prompt_format(prompt: str) -> str:
    # Add headers to start and end of prompt
    return "\n\nHuman: " + prompt + "\n\nAssistant:"


# Call the Bedrock agent instead of directly calling the Claude model
def call_bedrock_agent(prompt):
    prompt_config = {
        "prompt": agent_prompt_format(prompt),
        "max_tokens_to_sample": 4096,
        "temperature": 0.5,
        "top_k": 250,
        "top_p": 0.5,
        "stop_sequences": [],
    }

    body = json.dumps(prompt_config)

    # Use the agent's model ID instead of a base model like Claude
    agent_model_id = "your_bedrock_agent_id"  # Replace this with your Bedrock agent ID
    accept = "application/json"
    contentType = "application/json"

    response = bedrock_runtime.invoke_model(
        body=body, modelId=agent_model_id, accept=accept, contentType=contentType
    )
    response_body = json.loads(response.get("body").read())

    results = response_body.get("completion")
    return results


# Function to set up RAG (retrieve-augmented generation)
def rag_setup(query):
    # Embed the sentences using Bedrock embeddings
    embeddings = BedrockEmbeddings(
        client=bedrock_runtime,
        model_id="amazon.titan-embed-text-v1",  # Titan model for embeddings
    )

    # Create a local FAISS vector store
    local_vector_store = FAISS.from_texts(sentences, embeddings)

    # Perform similarity search to get relevant context
    docs = local_vector_store.similarity_search(query)
    context = ""

    # Compile the retrieved context
    for doc in docs:
        context += doc.page_content

    # Construct the prompt with the retrieved context
    prompt = f"""Use the following pieces of context to answer the question at the end.

    {context}

    Question: {query}
    Answer:"""

    # Call the Bedrock agent instead of a specific base model
    return call_bedrock_agent(prompt)


# Query to test the agent with RAG
query = "What type of pet do I have?"
print(query)
print(rag_setup(query))
