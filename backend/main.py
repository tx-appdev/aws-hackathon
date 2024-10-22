# attempt using: https://github.com/aws-samples/amazon-bedrock-workshop/blob/main/05_Agents/01_create_agent.ipynb

from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3
import logging
import pprint
import json
import pandas as pd
# from agent import invoke_agent_helper
import uuid
logging.basicConfig(format='[%(asctime)s] p%(process)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
bedrock_agent_runtime_client = boto3.client('bedrock-agent-runtime', region_name='us-east-1')
dynamodb = boto3.resource('dynamodb')

def invoke_agent_helper(query, session_id, agent_id, alias_id, enable_trace=False, session_state=None):
    end_session: bool = False
    if not session_state:
        session_state = {}

    # invoke the agent API
    agent_response = bedrock_agent_runtime_client.invoke_agent(
        inputText=query,
        agentId=agent_id,
        agentAliasId=alias_id,
        sessionId=session_id,
        enableTrace=enable_trace,
        endSession=end_session,
        sessionState=session_state
    )
    if enable_trace:
        logger.info(pprint.pprint(agent_response))

    event_stream = agent_response['completion']
    try:
        for event in event_stream:
            if 'chunk' in event:
                data = event['chunk']['bytes']
                if enable_trace:
                    logger.info(f"Final answer ->\n{data.decode('utf8')}")
                agent_answer = data.decode('utf8')
                return agent_answer
                # End event indicates that the request finished successfully
            elif 'trace' in event:
                if enable_trace:
                    logger.info(json.dumps(event['trace'], indent=2))
            else:
                raise Exception("unexpected event.", event)
    except Exception as e:
        raise Exception("unexpected event.", e)

session_id:str = str(uuid.uuid1())
query = "Create a 5 man team"
response = invoke_agent_helper(query, session_id, 'U7CB26MHMI', '6X0BHHM7EZ')

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

@app.route('/chat', methods=['POST'])
def chat():
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

