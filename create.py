import sys
from pathlib import Path

def create(name: str):
    code_dir = Path('Code') / name
    data_dir = Path('Data') / name
    script_file = code_dir / f"{name}.py"
    base_code = Path('Code') / 'BaseCode.py'
    
    try:
        template = base_code.read_text()
        code_dir.mkdir(parents=True, exist_ok=False)
        data_dir.mkdir(parents=True, exist_ok=False)
        script_file.write_text(template)
        
        print(f"Created:")
        print(f"- Code Directory: {code_dir}")
        print(f"- Test Data Directory: {data_dir}")
        print(f"- Script file created: {script_file}")
        
    except FileExistsError:
        print("Error: Solution structure already exists")
    except FileNotFoundError:
        print("Error: base code was not found")
    except Exception as e:
        print(f"Error creating solution structure: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create.py <solution_name>")
        sys.exit(1)
    
    create(sys.argv[1])