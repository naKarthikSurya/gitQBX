# settings.py
import os

# Load environment variables
A = os.getenv('a')
B = os.getenv('b')
C = os.getenv('c')
D = os.getenv('d')
E = os.getenv('e')

def get_env_settings():
    return {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "E": E
    }
def get_attribute(attr):
    env_settings = get_env_settings()
    return env_settings.get(attr, "Not Set")
