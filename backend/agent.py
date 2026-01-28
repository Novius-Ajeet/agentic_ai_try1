from langchain import OpenAI

class LangChainAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        self.agent = self.initialize_agent()

    def initialize_agent(self):
        # Initialize the LangChain agent with configurations
        return OpenAI(api_key=self.api_key)

    def run(self, prompt):
        response = self.agent.generate_response(prompt)
        return response

# Example usage
if __name__ == '__main__':
    agent = LangChainAgent(api_key='your-api-key-here')
    result = agent.run('Hello, how can I assist you today?')
    print(result)