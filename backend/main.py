import boto3
import json
import os
from botocore.exceptions import BotoCoreError, ClientError
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

def initialize_bedrock_client():
    """
    Initialize the Amazon Bedrock client using Boto3.

    Returns:
        boto3.client: Bedrock client object.
    """
    try:
        bedrock_client = boto3.client(
            'bedrock',
            region_name=os.getenv('AWS_DEFAULT_REGION', 'us-east-1')  # Replace with your preferred region if different
        )
        print("Successfully initialized Bedrock client.")
        return bedrock_client
    except Exception as e:
        print(f"Error initializing Bedrock client: {e}")
        return None

def list_bedrock_models(client):
    """
    List available foundation models in Amazon Bedrock.

    Args:
        client (boto3.client): Bedrock client object.
    """
    try:
        response = client.list_foundation_models()
        models = response.get('foundationModelSummaries', [])
        if not models:
            print("No foundation models found.")
            return
        print("\nAvailable Foundation Models:")
        for model in models:
            model_name = model.get('modelName', 'N/A')
            provider = model.get('provider', 'N/A')
            print(f" - Model Name: {model_name}, Provider: {provider}")
    except ClientError as e:
        print(f"AWS ClientError: {e.response['Error']['Message']}")
    except BotoCoreError as e:
        print(f"BotoCoreError: {str(e)}")
    except Exception as e:
        print(f"Unexpected error while listing models: {str(e)}")

def generate_text(client, model_id, prompt, max_tokens=100):
    """
    Generate text using a specified foundation model in Amazon Bedrock.

    Args:
        client (boto3.client): Bedrock client object.
        model_id (str): The identifier of the foundation model to use.
        prompt (str): The input text prompt for generation.
        max_tokens (int): Maximum number of tokens to generate.

    Returns:
        str: Generated text or None if an error occurred.
    """
    try:
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps({
                "prompt": prompt,
                "maxTokens": max_tokens
            }),
            contentType='application/json'
        )
        
        # Read and parse the response body
        response_body = response['body'].read()
        response_json = json.loads(response_body)
        generated_text = response_json.get('generatedText', '')
        return generated_text
    except ClientError as e:
        print(f"AWS ClientError: {e.response['Error']['Message']}")
    except BotoCoreError as e:
        print(f"BotoCoreError: {str(e)}")
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
    except Exception as e:
        print(f"Unexpected error while generating text: {str(e)}")
    return None

def main():
    """
    Main function to execute Bedrock operations:
    1. Initialize Bedrock client.
    2. List available foundation models.
    3. Generate text using a selected model.
    """
    # Initialize Bedrock client
    bedrock_client = initialize_bedrock_client()
    if not bedrock_client:
        print("Failed to initialize Bedrock client. Exiting.")
        return

    # List available models
    list_bedrock_models(bedrock_client)

    # Prompt user for model selection and input
    model_id = input("\nEnter the Model ID you want to use (e.g., 'anthropic.claude-v1'): ").strip()
    if not model_id:
        print("No Model ID provided. Exiting.")
        return

    prompt = input("Enter your prompt for text generation: ").strip()
    if not prompt:
        print("No prompt provided. Exiting.")
        return

    # Generate text
    print("\nGenerating text...")
    generated = generate_text(bedrock_client, model_id, prompt)
    if generated:
        print("\n--- Generated Text ---")
        print(generated)
    else:
        print("Failed to generate text.")

if __name__ == "__main__":
    main()