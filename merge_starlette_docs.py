# Download the Starlette docs from GitHub
import os
import requests
import glob
import shutil
from pathlib import Path

# Define paths
STARLETTE_DOCS_PATH = './starlette/docs'
STARLETTE_DOCS = './starlette/docs'
STARLETTE_SRC = './starlette/starlette'
OUTPUT_FILE = 'Starlette-LLM-Docs.md'
CODE_EXAMPLES_DIR = 'starlette_code_examples'

def clone_repository():
    """Clone the Starlette repository if it doesn't exist."""
    if not os.path.exists('starlette'):
        print("Cloning Starlette repository...")
        os.system('git clone https://github.com/encode/starlette.git starlette')
        if not os.path.exists('starlette'):
            print("Error: Failed to clone Starlette repository!")
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

def find_source_file(module_name):
    """Find the source file for a given module name."""
    # Convert module name to file path
    file_path = module_name.replace('.', '/') + '.py'
    full_path = os.path.join(STARLETTE_SRC, file_path)
    
    if os.path.exists(full_path):
        return full_path
    return None

def extract_code_from_source(source_file, start_line, end_line):
    """Extract code from a source file between start and end lines."""
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if start_line <= 0 or end_line > len(lines):
                return None
            return ''.join(lines[start_line-1:end_line])
    except Exception as e:
        print(f"Error reading source file {source_file}: {str(e)}")
        return None

def process_mkdocs_imports(content, code_examples_dir):
    """Process mkdocs imports in the content and extract corresponding source code."""
    lines = content.split('\n')
    processed_lines = []
    example_count = 0
    
    for line in lines:
        if line.startswith('--8<--'):
            # Extract module and line numbers from mkdocs import
            parts = line.strip('--8<--').strip().split(':')
            if len(parts) >= 2:
                module = parts[0].strip()
                line_range = parts[1].strip()
                
                # Parse line range
                if '-' in line_range:
                    start_line, end_line = map(int, line_range.split('-'))
                else:
                    start_line = end_line = int(line_range)
                
                # Find and extract source code
                source_file = find_source_file(module)
                if source_file:
                    code = extract_code_from_source(source_file, start_line, end_line)
                    if code:
                        # Save code to a file
                        example_count += 1
                        code_file = os.path.join(code_examples_dir, f"example_{example_count}.py")
                        with open(code_file, 'w', encoding='utf-8') as f:
                            f.write(code)
                        
                        # Replace mkdocs import with reference to saved code
                        processed_lines.append(f"```python\n# Source: {module} (lines {start_line}-{end_line})\n# Saved as: {os.path.basename(code_file)}\n```")
                        continue
        
        processed_lines.append(line)
    
    return '\n'.join(processed_lines)

def merge_documentation(output_file):
    """Merge markdown documentation and code examples into a single file."""
    print("\nStarting documentation merge process...")
    
    # Get all markdown files
    md_files = get_files_by_extension(STARLETTE_DOCS, '.md')
    
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
        index_file = os.path.join(STARLETTE_DOCS, 'index.md')
        if os.path.exists(index_file):
            print(f"Processing main index: {index_file}")
            with open(index_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
                processed_content = process_mkdocs_imports(content, code_examples_dir)
                outfile.write(processed_content)
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
                            processed_content = process_mkdocs_imports(content, code_examples_dir)
                            
                            # Add relative path as a reference
                            rel_path = os.path.relpath(md_file, STARLETTE_DOCS)
                            outfile.write(f"\n\n## Documentation: {rel_path}\n\n")
                            outfile.write(processed_content)
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
    if not os.path.exists(STARLETTE_DOCS):
        print(f"Error: The Starlette docs folder {STARLETTE_DOCS} does not exist!")
        return
    if not os.path.exists(STARLETTE_SRC):
        print(f"Error: The Starlette source folder {STARLETTE_SRC} does not exist!")
        return
    
    # Create the output file
    output_file = OUTPUT_FILE
    
    # Merge documentation and examples
    merge_documentation(output_file)
    
    print(f"\nSuccessfully merged documentation into {output_file}")
    print(f"Code examples have been saved in the '{CODE_EXAMPLES_DIR}' directory")

if __name__ == "__main__":
    main()


