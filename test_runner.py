# test_runner.py

import sys
import os
import subprocess
from pathlib import Path

def run_tests(script_name: str):
    # Get paths
    code_path = Path('Code') / script_name / f"{script_name}.py"
    data_dir = Path('Data') / script_name

    # Validate script exists
    if not code_path.exists():
        print(f"Error: Script {code_path} not found")
        return

    # Validate data directory exists
    if not data_dir.exists():
        print(f"Error: Data directory {data_dir} not found")
        return

    # Find all test files
    test_files = list(data_dir.glob('*.txt'))
    
    if not test_files:
        print(f"No test files found in {data_dir}")
        return

    # Run each test
    for test_file in test_files:
        print(f"\nRunning test: {test_file.name}")
        print("-" * 40)
        
        with open(test_file, 'r') as f:
            test_data = f.read()
        test_arguments = test_data.split("\n")
        
        run_process = ['python', str(code_path), *test_arguments]
        result = subprocess.run(
            run_process, 
            text=True,
            capture_output=True,
            timeout=30
        )
        
        print("Output:")
        print(result.stdout)
        
        if result.stderr:
            print("Errors:")
            print(result.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test_runner.py <script_name>")
        sys.exit(1)
    
    run_tests(sys.argv[1])