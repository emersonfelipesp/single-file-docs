import os
import glob
import shutil
from pathlib import Path

# Define paths
PYDANTIC_DOCS_PATH = './pydantic/docs'
PYDANTIC_DOCS = './pydantic/docs'
OUTPUT_FILE = 'Pydantic-LLM-Docs.md'
CODE_EXAMPLES_DIR = 'pydantic_code_examples'

def clone_repository():
    """Clone the Pydantic repository if it doesn't exist."""
    if not os.path.exists('pydantic'):
        print("Cloning Pydantic repository...")
        os.system('git clone https://github.com/pydantic/pydantic.git pydantic')
        if not os.path.exists('pydantic'):
            print("Error: Failed to clone Pydantic repository!")
            return False
    return True

def get_files_by_extension(root_dir, extension):
    """Recursively find all files with given extension in the directory and its subdirectories."""
    files = []
    for root, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(extension):
                full_path = os.path.join(root, filename)
                files.append(full_path)
    return sorted(files)

def get_section_name(file_path):
    """Extract the section name from a file path."""
    parts = file_path.split(os.sep)
    if 'docs' in parts:
        # Get the first directory after 'docs'
        docs_index = parts.index('docs')
        if len(parts) > docs_index + 1:
            return parts[docs_index + 1]
    return None

def copy_code_example(code_path, output_dir):
    """Copy a code example file to the output directory."""
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Copy the file
        shutil.copy2(code_path, output_dir)
        return True
    except Exception as e:
        print(f"Error copying code example {code_path}: {str(e)}")
        return False

def merge_documentation(output_file):
    """Merge markdown documentation and code examples into a single file."""
    print("\nStarting documentation merge process...")
    
    # Get all markdown files
    md_files = get_files_by_extension(PYDANTIC_DOCS, '.md')
    
    print(f"\nFound {len(md_files)} markdown files")
    
    # Group files by section
    sections = {}
    
    # Process markdown files
    for md_file in md_files:
        section = get_section_name(md_file)
        if section not in sections:
            sections[section] = []
        sections[section].append(md_file)
    
    # Create a directory for code examples
    code_examples_dir = os.path.join(os.path.dirname(output_file), CODE_EXAMPLES_DIR)
    os.makedirs(code_examples_dir, exist_ok=True)
    
    # Write the merged documentation
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Write main index first if it exists
        index_file = os.path.join(PYDANTIC_DOCS, 'index.md')
        if os.path.exists(index_file):
            print(f"Processing main index: {index_file}")
            with open(index_file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write("\n\n---\n\n")
        
        # Process each section
        for section, files in sorted(sections.items()):
            if section:
                print(f"\nProcessing section: {section}")
                outfile.write(f"\n\n# {section.replace('-', ' ').title()}\n\n")
                
                # Process markdown files for this section
                for md_file in sorted(files):
                    print(f"Processing documentation: {md_file}")
                    try:
                        with open(md_file, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            
                            # Check for code imports in the markdown
                            if '```python' in content:
                                # Extract code blocks
                                code_blocks = content.split('```python')
                                for i, block in enumerate(code_blocks[1:], 1):
                                    code = block.split('```')[0]
                                    # Save code to a file
                                    code_file = os.path.join(code_examples_dir, f"{os.path.basename(md_file).replace('.md', '')}_example_{i}.py")
                                    with open(code_file, 'w', encoding='utf-8') as code_out:
                                        code_out.write(code)
                            
                            # Add relative path as a reference
                            rel_path = os.path.relpath(md_file, PYDANTIC_DOCS)
                            outfile.write(f"\n\n## Documentation: {rel_path}\n\n")
                            outfile.write(content)
                    except Exception as e:
                        print(f"Error processing {md_file}: {str(e)}")
        
        # Add a section for code examples
        outfile.write("\n\n# Code Examples\n\n")
        outfile.write(f"All code examples have been extracted and saved in the `{CODE_EXAMPLES_DIR}` directory.\n")
        outfile.write("You can find them organized by their corresponding documentation files.\n")

def main():
    # Clone repository if needed
    if not clone_repository():
        return
    
    # Verify directories exist
    if not os.path.exists(PYDANTIC_DOCS):
        print(f"Error: The Pydantic docs folder {PYDANTIC_DOCS} does not exist!")
        return
    
    # Create the output file
    output_file = OUTPUT_FILE
    
    # Merge documentation and examples
    merge_documentation(output_file)
    
    print(f"\nSuccessfully merged documentation into {output_file}")
    print(f"Code examples have been saved in the '{CODE_EXAMPLES_DIR}' directory")

if __name__ == "__main__":
    main()
