import sys
from agents.pipeline import process_file_pipeline

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        return

    file_path = sys.argv[1]
    try:
        output = process_file_pipeline(file_path)
        print(f" Report generated: {output}")
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    main()
