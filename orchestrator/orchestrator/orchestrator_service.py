import requests

class OrchestratorService:
    def __init__(self):
        self.file_reader_url = 'http://file_reader:5000' # localhost:8000
        self.script_scanner_url = 'http://script_scanner:5000'
        self.script_scientist_url = 'http://script_scientist'
        self.orm = 'http://orm:5000'
        self.data_scientist_url = 'http://data_scientist'
        self.dashboard_url = 'http://dashboard'
        self.script_data = {}
        
    def process_script(self, file_path):
        self.read_file(file_path)
        self.script_data["raw_content"] = self.read_file(file_path)

        # # Step 4: Data science operations
        # ui_data = self.data_science_operations(script)

        # # Step 5: Display in dashboard
        # self.display_in_dashboard(ui_data)

    def read_file(self, file_path):
        response = requests.post(f'{self.file_reader_url}/read', json={'file_path': file_path})
        print(response.json())
        return response.json()  # Assume response contains the script object

    def scan_script(self, script):
        response = requests.post(f'{self.script_scanner_url}/scan', json=script)
        self.script = response.json()  # Assume response contains the updated script object
    
    def add_script(self):
        response = requests.post(f'{self.orm}/add', json=self.script)
        code = response.json()['code']
        if code == 200:
            print("Script stored successfully")
        else:
            print("Error storing script")
        return response.json()

    def analyze_script(self, script):
        response = requests.post(f'{self.script_scientist_url}/analyze', json=script)
        return response.json()  # Assume response contains the further updated script object

    def data_science_operations(self, script):
        response = requests.post(f'{self.data_scientist_url}/process', json=script)
        return response.json()  # Assume response contains the UIData object

    def display_in_dashboard(self, ui_data):
        response = requests.post(f'{self.dashboard_url}/display', json=ui_data)
        return response.json()  # Assume response acknowledges the display

# Example usage
if __name__ == "__main__":
    orchestrator = OrchestratorService()
    orchestrator.process_script(file_path="test_script.html")

