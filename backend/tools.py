# Agent Tools for Processing and Handling Requests

class Agent:
    def __init__(self, name):
        self.name = name
    
    def process_request(self, request):
        # Code to process the request
        print(f"Processing request: {request}")

    def handle_response(self, response):
        # Code to handle the response
        print(f"Handling response: {response}")

# Example usage:
agent = Agent("RequestHandler")
agent.process_request("Sample Request")
agent.handle_response("Sample Response")
