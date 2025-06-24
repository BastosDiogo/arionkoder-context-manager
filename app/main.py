from services.logs import Logging
from context_manager import ContextManager

def connect_mock():
    Logging().info("Conecting to mock...")
    return {"status": "connected"}

def disconnect_mock(resource):
    Logging().info(f"Disconecting to: {resource}")

def run():
    with ContextManager("MockAPI", connect_mock, disconnect_mock) as resource:
        Logging().info(f"Using resource: {resource["status"]}")

    # Simulating error
    try:
        with ContextManager("ErrorAPI", connect_mock, disconnect_mock):
            raise RuntimeError("Simulating error")
    except RuntimeError:
        Logging().error("Error successfully captured")

    # Context Manager
    with ContextManager("API1", connect_mock, disconnect_mock) as r1:
        with ContextManager("API2", connect_mock, disconnect_mock) as r2:
            Logging().info("Using nested resources")

if __name__ == "__main__":
    run()
