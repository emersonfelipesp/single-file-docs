import os
from pathlib import Path

# Define input and output files
INPUT_FILES = [
    'FastAPI-LLM-Docs.md',
    'Pydantic-LLM-Docs.md',
    'Starlette-LLM-Docs.md'
]
OUTPUT_FILE = 'FastAPI-Pydantic-Starlette-LLM-Docs.md'

def merge_documentation():
    """Merge all documentation files into a single unified file."""
    print("\nStarting documentation merge process...")
    
    # Check if all input files exist
    missing_files = [f for f in INPUT_FILES if not os.path.exists(f)]
    if missing_files:
        print(f"Error: The following files are missing: {', '.join(missing_files)}")
        return False
    
    # Create the output file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        # Write the main title
        outfile.write("# FastAPI, Pydantic, and Starlette Documentation\n\n")
        outfile.write("This document combines the documentation for FastAPI, Pydantic, and Starlette.\n\n")
        outfile.write("---\n\n")
        
        # Process each input file
        for input_file in INPUT_FILES:
            # Extract framework name from filename
            framework = input_file.split('-')[0]
            
            # Write framework section header
            outfile.write(f"# {framework} Documentation\n\n")
            
            # Read and write the content
            try:
                with open(input_file, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    
                    # Skip the title if it exists
                    if content.startswith('# '):
                        content = content[content.find('\n')+1:]
                    
                    outfile.write(content)
                    outfile.write("\n\n---\n\n")
                
                print(f"Successfully processed {input_file}")
            except Exception as e:
                print(f"Error processing {input_file}: {str(e)}")
                return False
    
    return True

def main():
    # Merge documentation
    if merge_documentation():
        print(f"\nSuccessfully merged documentation into {OUTPUT_FILE}")
    else:
        print("\nFailed to merge documentation")

if __name__ == "__main__":
    main() 