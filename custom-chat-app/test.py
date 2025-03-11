import os
from dotenv import load_dotenv, find_dotenv

# Find and load .env file
env_path = find_dotenv()
if not env_path:
    print("Error: .env file not found!")
else:
    print(f".env file found at: {env_path}")
    load_dotenv(env_path)

# Check if the variable is loaded
connection_string = os.getenv("AIPROJECT_CONNECTION_STRING")

if connection_string:
    print("Connection String Loaded:", connection_string)
else:
    print("Error: AIPROJECT_CONNECTION_STRING is not set!")    