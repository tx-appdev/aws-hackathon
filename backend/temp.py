import json
import boto3
import uuid

# Setup bedrock
client = boto3.client(
    service_name="bedrock-agent-runtime",
    region_name="us-east-1",
) 

input_text = "Hello, please enter the information to create a VALORANT Team"


def invoke_agent(self, agent_id, agent_alias_id, session_id, prompt):
        """
        Sends a prompt for the agent to process and respond to.

        :param agent_id: The unique identifier of the agent to use.
        :param agent_alias_id: The alias of the agent to use.
        :param session_id: The unique identifier of the session. Use the same value across requests
                           to continue the same conversation.
        :param prompt: The prompt that you want Claude to complete.
        :return: Inference response from the model.
        """

        # try:
            # Note: The execution time depends on the foundation model, complexity of the agent,
            # and the length of the prompt. In some cases, it can take up to a minute or more to
            # generate a response.
        response = self.invoke_agent(
                agentId=agent_id,
                agentAliasId=agent_alias_id,
                sessionId=session_id,
                inputText=prompt,
            )

        completion = ""

        for event in response.get("completion"):
                chunk = event["chunk"]
                completion = completion + chunk["bytes"].decode()

        # except ClientError as e:
        #     logger.error(f"Couldn't invoke agent. {e}")
        #     raise

        return completion


print(invoke_agent(client, agent_id = '2P7SZ0COP0', agent_alias_id='ALP9UYMYI9', session_id=str(uuid.uuid4()), prompt=input_text))