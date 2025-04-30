import os
import glob
from pathlib import Path

# Global variables for the FastAPI folders
DOCS_SRC = '/opt/fastapi/docs_src'
DOCS_MD = '/opt/fastapi/docs/en/docs'

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
    if 'docs_src' in parts:
        return parts[parts.index('docs_src') + 1]
    elif 'docs' in parts:
        # Handle special directories
        if 'tutorial' in parts:
            return parts[parts.index('tutorial') + 1] if len(parts) > parts.index('tutorial') + 1 else 'tutorial'
        return parts[parts.index('docs') + 1]
    return None

def merge_documentation(output_file):
    """Merge markdown documentation and Python examples into a single file."""
    print("\nStarting documentation merge process...")
    
    # Get all markdown and Python files
    md_files = get_files_by_extension(DOCS_MD, '.md')
    py_files = get_files_by_extension(DOCS_SRC, '.py')
    
    print(f"\nFound {len(md_files)} markdown files and {len(py_files)} Python examples")
    
    # Group files by section
    sections = {}
    
    # Process markdown files
    for md_file in md_files:
        section = get_section_name(md_file)
        if section not in sections:
            sections[section] = {'md': [], 'py': []}
        sections[section]['md'].append(md_file)
    
    # Process Python files
    for py_file in py_files:
        section = get_section_name(py_file)
        if section not in sections:
            sections[section] = {'md': [], 'py': []}
        sections[section]['py'].append(py_file)
    
    # Write the merged documentation
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Write main index first if it exists
        index_file = os.path.join(DOCS_MD, 'index.md')
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
                for md_file in sorted(files['md']):
                    print(f"Processing documentation: {md_file}")
                    try:
                        with open(md_file, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            # Add relative path as a reference
                            rel_path = os.path.relpath(md_file, DOCS_MD)
                            outfile.write(f"\n\n## Documentation: {rel_path}\n\n")
                            outfile.write(content)
                    except Exception as e:
                        print(f"Error processing {md_file}: {str(e)}")
                
                # Process Python examples for this section
                if files['py']:
                    outfile.write("\n\n### Code Examples\n\n")
                    for py_file in sorted(files['py']):
                        print(f"Processing example: {py_file}")
                        try:
                            with open(py_file, 'r', encoding='utf-8') as infile:
                                content = infile.read()
                                # Add relative path as a reference
                                rel_path = os.path.relpath(py_file, DOCS_SRC)
                                outfile.write(f"\n\n#### Example: {rel_path}\n\n")
                                outfile.write("```python\n")
                                outfile.write(content)
                                outfile.write("\n```\n")
                        except Exception as e:
                            print(f"Error processing {py_file}: {str(e)}")

def main():
    # Verify directories exist
    if not os.path.exists(DOCS_SRC):
        print(f"Error: The docs_src folder {DOCS_SRC} does not exist!")
        return
    if not os.path.exists(DOCS_MD):
        print(f"Error: The docs folder {DOCS_MD} does not exist!")
        return
    
    # Create the output file
    output_file = "FastAPI-LLM-Docs.md"
    
    # Merge documentation and examples
    merge_documentation(output_file)
    
    print(f"\nSuccessfully merged documentation into {output_file}")

if __name__ == "__main__":
    main()


