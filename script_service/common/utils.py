from dotenv import load_dotenv, find_dotenv

def get_env_path():
    return find_dotenv(filename='.env')