import json
import boto3
import uuid

# Setup bedrock
client = boto3.client(
    service_name="bedrock-agent-runtime",
    region_name="us-east-1",
)

input_text = "Hello, please enter the information to create a VALORANT Team"

agent_alias_id = 'ALP9UYMYI9'

agent_id = '2P7SZ0COP0'

session_id = str(uuid.uuid4())  # Generate a unique session ID

response = client.invoke_agent(
    agentAliasId=agent_alias_id,
    agentId=agent_id,
    enableTrace=False,
    endSession=False,# can set either to true if needed
    inputText= input_text,
    # memoryId='string',
    sessionId=session_id,
    sessionState={
        # 'files': [
        #     {
        #         'name': 'example.txt',
        #         'source': {
        #             'byteContent': {
        #                 'data': b'byte content here',
        #                 'mediaType': 'text/plain'
        #             },
        #             # Choose one of these based on your source type
        #             # 's3Location': {
        #             #     'uri': 's3://your-bucket/path/to/file'
        #             # },
        #             'sourceType': 'BYTE_CONTENT'  # or 'S3'
        #         },
        #         'useCase': 'CHAT'  # or 'CODE_INTERPRETER'
        #     },
        # ],
        'invocationId': str(uuid.uuid4()),
        'knowledgeBaseConfigurations': [
            {
                'knowledgeBaseId': '1SIQMDIMHZ',
                'retrievalConfiguration': 
                {
                    'vectorSearchConfiguration': {
                        'filter': {
                            'equals': {
                                'key': 'category',
                                'value': 'science'
                            }
                            # 'andAll': [
                            #     {'... recursive ...'},
                            # ],
                            # 'equals': {
                            #     'key': 'string',
                            #     'value': {...}|[...]|123|123.4|'string'|True|None
                            # },
                            # 'greaterThan': {
                            #     'key': 'string',
                            #     'value': {...}|[...]|123|123.4|'string'|True|None
                            # },
                            # 'greaterThanOrEquals': {
                            #     'key': 'string',
                            #     'value': {...}|[...]|123|123.4|'string'|True|None
                            # },
                            # 'in': {
                            #     'key': 'string',
                            #     'value': {...}|[...]|123|123.4|'string'|True|None
                            # },
                            # 'lessThan': {
                            #     'key': 'string',
                            #     'value': {...}|[...]|123|123.4|'string'|True|None
                            # },
                            # 'lessThanOrEquals': {
                            #     'key': 'string',
                            #     'value': {...}|[...]|123|123.4|'string'|True|None
                            # },
                            # 'listContains': {
                            #     'key': 'string',
                            #     'value': {...}|[...]|123|123.4|'string'|True|None
                            # },
                            # 'notEquals': {
                            #     'key': 'string',
                            #     'value': {...}|[...]|123|123.4|'string'|True|None
                            # },
                            # 'notIn': {
                            #     'key': 'string',
                            #     'value': {...}|[...]|123|123.4|'string'|True|None
                            # },
                            # 'orAll': [
                            #     {'... recursive ...'},
                            # ],
                            # 'startsWith': {
                            #     'key': 'string',
                            #     'value': {...}|[...]|123|123.4|'string'|True|None
                            # },
                            # 'stringContains': {
                            #     'key': 'string',
                            #     'value': {...}|[...]|123|123.4|'string'|True|None
                            # }
                        },
                        'numberOfResults': 10,
                        'overrideSearchType': 'SEMANTIC' # or "HYBRID"
                    }
                }
            },
        ],
        'promptSessionAttributes': {
            'string': 'string'
        },
        'returnControlInvocationResults': [
            {
                'apiResult': {
                    'actionGroup': 'string',
                    'apiPath': 'string',
                    'confirmationState': 'CONFIRM', # or DENY
                    'httpMethod': 'string',
                    'httpStatusCode': 123,
                    'responseBody': {
                        'string': {
                            'body': 'string'
                        }
                    },
                    'responseState': 'FAILURE'# or 'REPROMPT'
                },
                # 'functionResult': {
                #     'actionGroup': 'string',
                #     'confirmationState': 'CONFIRM', # |'DENY'
                #     'function': 'string',
                #     'responseBody': {
                #         'string': {
                #             'body': 'string'
                #         }
                #     },
                #     'responseState': 'FAILURE'# |'REPROMPT'
                # }
            },
        ],
        'sessionAttributes': {
            'string': 'string'
        }
    }
)

print(response.get("body").read())
response_body = json.loads(response.get("body").read())
print(response_body.get("completion"))