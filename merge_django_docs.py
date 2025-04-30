import os
import glob
import shutil
from pathlib import Path

# Define paths
DJANGO_DOCS_PATH = './django/docs'
DJANGO_SRC = './django/django'
OUTPUT_FILE = 'Django-LLM-Docs.md'
CODE_EXAMPLES_DIR = 'django_code_examples'

def clone_repository():
    """Clone the Django repository if it doesn't exist."""
    if not os.path.exists('django'):
        print("Cloning Django repository...")
        os.system('git clone https://github.com/django/django.git django')
        if not os.path.exists('django'):
            print("Error: Failed to clone Django repository!")
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
    full_path = os.path.join(DJANGO_SRC, file_path)
    
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

def process_code_blocks(content, code_examples_dir):
    """Process code blocks in the content and extract them to separate files."""
    lines = content.split('\n')
    processed_lines = []
    example_count = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('```python'):
            # Start of a code block
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code_lines.append(lines[i])
                i += 1
            
            if code_lines:
                # Save code to a file
                example_count += 1
                code_file = os.path.join(code_examples_dir, f"example_{example_count}.py")
                with open(code_file, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(code_lines))
                
                # Replace code block with reference
                processed_lines.append(f"```python\n# Code example saved as: {os.path.basename(code_file)}\n```")
            i += 1
        else:
            processed_lines.append(line)
            i += 1
    
    return '\n'.join(processed_lines)

def merge_documentation(output_file):
    """Merge markdown documentation and code examples into a single file."""
    print("\nStarting documentation merge process...")
    
    # Get all markdown files
    md_files = get_files_by_extension(DJANGO_DOCS_PATH, '.txt')  # Django uses .txt for docs
    
    print(f"\nFound {len(md_files)} documentation files")
    
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
        index_file = os.path.join(DJANGO_DOCS_PATH, 'index.txt')
        if os.path.exists(index_file):
            print(f"Processing main index: {index_file}")
            with open(index_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
                processed_content = process_code_blocks(content, code_examples_dir)
                outfile.write(processed_content)
                outfile.write("\n\n---\n\n")
        
        # Process each section
        for section, files in sorted(sections.items()):
            if section:
                print(f"\nProcessing section: {section}")
                outfile.write(f"\n\n# {section.replace('-', ' ').title()}\n\n")
                
                # Process documentation files for this section
                for md_file in sorted(files):
                    print(f"Processing documentation: {md_file}")
                    try:
                        with open(md_file, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            processed_content = process_code_blocks(content, code_examples_dir)
                            
                            # Add relative path as a reference
                            rel_path = os.path.relpath(md_file, DJANGO_DOCS_PATH)
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
    if not os.path.exists(DJANGO_DOCS_PATH):
        print(f"Error: The Django docs folder {DJANGO_DOCS_PATH} does not exist!")
        return
    if not os.path.exists(DJANGO_SRC):
        print(f"Error: The Django source folder {DJANGO_SRC} does not exist!")
        return
    
    # Create the output file
    output_file = OUTPUT_FILE
    
    # Merge documentation and examples
    merge_documentation(output_file)
    
    print(f"\nSuccessfully merged documentation into {output_file}")
    print(f"Code examples have been saved in the '{CODE_EXAMPLES_DIR}' directory")

if __name__ == "__main__":
    main()
