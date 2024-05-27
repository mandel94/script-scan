import requests

class OrchestratorService:
    def __init__(self):
        self.file_reader_url = 'http://file-reader:5000' # localhost:8000
        self.script_scanner_url = 'http://script-scanner:5000'
        self.script_scientist_url = 'http://script-scientist'
        self.data_scientist_url = 'http://data-scientist'
        self.dashboard_url = 'http://dashboard'
        
    def process_script(self, file_path):
        # Step 1: Read file content
        script = self.read_file(file_path)
        print("READ OUTPUT: ", script)
        # Print the script to see the structure
        print(script)
        # # Step 2: Scan script
        script = self.scan_script(script)
        print("SCAN OUTPUT: ", script)
        
        # # Step 3: Analyze script
        # script = self.analyze_script(script)
        
        # # Step 4: Data science operations
        # ui_data = self.data_science_operations(script)
        
        # # Step 5: Display in dashboard
        # self.display_in_dashboard(ui_data)

    def read_file(self, file_path):
        response = requests.post(f'{self.file_reader_url}/read', json={'file_path': file_path})
        print("ORCHESTRATOR: read_file executed", response.json())
        return response.json()

    def scan_script(self, script):
        response = requests.post(f'{self.script_scanner_url}/scan', json=script)
        return response.json()  # Assume response contains the updated script object

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
    # orchestrator = OrchestratorService()
    # orchestrator.process_script('/path/to/script/file.txt')
    # Change so that the orchestrator takes the file path as an argument from the command line
    import sys
    orchestrator = OrchestratorService()
    orchestrator.process_script(file_path="test_script.html")
    # orchestrator.process_script(sys.argv[1])

