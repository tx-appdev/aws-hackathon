# attempt using: https://github.com/aws-samples/amazon-bedrock-workshop/blob/main/05_Agents/01_create_agent.ipynb

import json
import boto3
import uuid

import time
# import boto3
import logging
# import ipywidgets as widgets
# import uuid

from agent import create_agent_role, create_lambda_role
from agent import create_dynamodb, create_lambda, invoke_agent_helper
# Setup bedrock
s3_client = boto3.client('s3')
sts_client = boto3.client('sts')
session = boto3.session.Session()
region = session.region_name
account_id = sts_client.get_caller_identity()["Account"]
bedrock_agent_client = boto3.client('bedrock-agent')
bedrock_agent_runtime_client = boto3.client('bedrock-agent-runtime')
logging.basicConfig(format='[%(asctime)s] p%(process)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
region, account_id

input_text = "Hello, please enter the information to create a VALORANT Team"

alias_id = 'ALP9UYMYI9'

agent_id = '2P7SZ0COP0'

session_id = str(uuid.uuid4())  # Generate a unique session ID

# session_id:str = str(uuid.uuid1())
# query = "Hi, I am Anna. I want to create a booking for 2 people, at 8pm on the 5th of May 2024."
response = invoke_agent_helper(input_text, session_id, agent_id, alias_id)
print(response)

# response = client.invoke_agent(
#     agentAliasId=agent_alias_id,
#     agentId=agent_id,
#     enableTrace=False,
#     endSession=False,# can set either to true if needed
#     inputText= input_text,
#     # memoryId='string',
#     sessionId=session_id,
#     sessionState={
#         # 'files': [
#         #     {
#         #         'name': 'example.txt',
#         #         'source': {
#         #             'byteContent': {
#         #                 'data': b'byte content here',
#         #                 'mediaType': 'text/plain'
#         #             },
#         #             # Choose one of these based on your source type
#         #             # 's3Location': {
#         #             #     'uri': 's3://your-bucket/path/to/file'
#         #             # },
#         #             'sourceType': 'BYTE_CONTENT'  # or 'S3'
#         #         },
#         #         'useCase': 'CHAT'  # or 'CODE_INTERPRETER'
#         #     },
#         # ],
#         'invocationId': str(uuid.uuid4()),
#         'knowledgeBaseConfigurations': [
#             {
#                 'knowledgeBaseId': '1SIQMDIMHZ',
#                 'retrievalConfiguration': 
#                 {
#                     'vectorSearchConfiguration': {
#                         'filter': {
#                             'equals': {
#                                 'key': 'category',
#                                 'value': 'science'
#                             }
#                             # 'andAll': [
#                             #     {'... recursive ...'},
#                             # ],
#                             # 'equals': {
#                             #     'key': 'string',
#                             #     'value': {...}|[...]|123|123.4|'string'|True|None
#                             # },
#                             # 'greaterThan': {
#                             #     'key': 'string',
#                             #     'value': {...}|[...]|123|123.4|'string'|True|None
#                             # },
#                             # 'greaterThanOrEquals': {
#                             #     'key': 'string',
#                             #     'value': {...}|[...]|123|123.4|'string'|True|None
#                             # },
#                             # 'in': {
#                             #     'key': 'string',
#                             #     'value': {...}|[...]|123|123.4|'string'|True|None
#                             # },
#                             # 'lessThan': {
#                             #     'key': 'string',
#                             #     'value': {...}|[...]|123|123.4|'string'|True|None
#                             # },
#                             # 'lessThanOrEquals': {
#                             #     'key': 'string',
#                             #     'value': {...}|[...]|123|123.4|'string'|True|None
#                             # },
#                             # 'listContains': {
#                             #     'key': 'string',
#                             #     'value': {...}|[...]|123|123.4|'string'|True|None
#                             # },
#                             # 'notEquals': {
#                             #     'key': 'string',
#                             #     'value': {...}|[...]|123|123.4|'string'|True|None
#                             # },
#                             # 'notIn': {
#                             #     'key': 'string',
#                             #     'value': {...}|[...]|123|123.4|'string'|True|None
#                             # },
#                             # 'orAll': [
#                             #     {'... recursive ...'},
#                             # ],
#                             # 'startsWith': {
#                             #     'key': 'string',
#                             #     'value': {...}|[...]|123|123.4|'string'|True|None
#                             # },
#                             # 'stringContains': {
#                             #     'key': 'string',
#                             #     'value': {...}|[...]|123|123.4|'string'|True|None
#                             # }
#                         },
#                         'numberOfResults': 10,
#                         'overrideSearchType': 'SEMANTIC' # or "HYBRID"
#                     }
#                 }
#             },
#         ],
#         'promptSessionAttributes': {
#             'string': 'string'
#         },
#         'returnControlInvocationResults': [
#             {
#                 'apiResult': {
#                     'actionGroup': 'string',
#                     'apiPath': 'string',
#                     'confirmationState': 'CONFIRM', # or DENY
#                     'httpMethod': 'string',
#                     'httpStatusCode': 123,
#                     'responseBody': {
#                         'string': {
#                             'body': 'string'
#                         }
#                     },
#                     'responseState': 'FAILURE'# or 'REPROMPT'
#                 },
#                 # 'functionResult': {
#                 #     'actionGroup': 'string',
#                 #     'confirmationState': 'CONFIRM', # |'DENY'
#                 #     'function': 'string',
#                 #     'responseBody': {
#                 #         'string': {
#                 #             'body': 'string'
#                 #         }
#                 #     },
#                 #     'responseState': 'FAILURE'# |'REPROMPT'
#                 # }
#             },
#         ],
#         'sessionAttributes': {
#             'string': 'string'
#         }
#     }
# )