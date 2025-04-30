# Download the Starlette docs from GitHub
import os
import requests
import glob
from pathlib import Path

# Issue the git clone command
os.system('git clone https://github.com/encode/starlette.git .')

# Define the path to the Starlette docs folder
STARLETTE_DOCS_PATH = './starlette/docs'

# Global variable for the Starlette docs folder
STARLETTE_DOCS = './starlette/docs'

# Define the path to the output file
OUTPUT_FILE = 'Starlette-LLM-Docs.md'

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

def merge_documentation(output_file):
    """Merge markdown documentation into a single file."""
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
    
    # Write the merged documentation
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Write main index first if it exists
        index_file = os.path.join(STARLETTE_DOCS, 'index.md')
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
                            # Add relative path as a reference
                            rel_path = os.path.relpath(md_file, STARLETTE_DOCS)
                            outfile.write(f"\n\n## Documentation: {rel_path}\n\n")
                            outfile.write(content)
                    except Exception as e:
                        print(f"Error processing {md_file}: {str(e)}")

def main():
    # Verify directory exists
    if not os.path.exists(STARLETTE_DOCS):
        print(f"Error: The Starlette docs folder {STARLETTE_DOCS} does not exist!")
        return
    
    # Create the output file
    output_file = OUTPUT_FILE
    
    # Merge documentation
    merge_documentation(output_file)
    
    print(f"\nSuccessfully merged documentation into {output_file}")

if __name__ == "__main__":
    main()


