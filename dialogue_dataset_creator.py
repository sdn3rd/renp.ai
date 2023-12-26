import re
import argparse
import logging
import json
import os

class RenPyLexer:
    def __init__(self, include_face_lines=False):
        self.label_pattern = re.compile(r'^\s*label\s+([.\w-]+):')
        self.dialogue_pattern = re.compile(r'^\s*(\w+)\s+"(.*?)"(?:\s+id\s+(\w+))?')
        self.menu_pattern = re.compile(r'^\s*(".*?")\s+if\s+.*:$')
        self.face_pattern = re.compile(r'^\s*face\s+(\w+)\s+(.*)') if include_face_lines else None
        self.id_pattern = re.compile(r'\sid\s+(\w+)')
        self.script_structure = {}

    def parse_file(self, lines):
        current_label = None
        dialogue_count = 0
        label_content = []

        for line in lines:
            line = line.rstrip()
            label_match = self.label_pattern.match(line)
            dialogue_match = self.dialogue_pattern.match(line)

            if label_match:
                if current_label and dialogue_count >= 3:
                    self.script_structure[current_label] = label_content

                current_label = label_match.group(1)
                label_content = []
                dialogue_count = 0

            if current_label:
                label_content.append(line)
                if dialogue_match:
                    dialogue_count += 1

        if current_label and dialogue_count >= 3:
            self.script_structure[current_label] = label_content

        return self.script_structure

    def format_elements(self, elements, output_type):
        if output_type == 'rpy':
            return self._format_for_renpy(elements)
        elif output_type == 'llama':
            return self._format_for_llama(elements)
        else:
            return self._format_default(elements)

    def _format_for_renpy(self, elements):
        formatted_output = ""
        for label, content in elements.items():
            formatted_output += f"label {label}:\n"
            formatted_output += "\n".join(content) + "\n"
        return formatted_output

    def _format_for_llama(self, elements):
        output_data = []
        for label, content in elements.items():
            dialogue_lines = [line for line in content if self.dialogue_pattern.match(line)]
            if len(dialogue_lines) >= 3:
                speakers = {self.dialogue_pattern.match(line).group(1) for line in dialogue_lines if self.dialogue_pattern.match(line)}
                instruction = f"Create a dialogue in renpy between {', '.join(speakers)}"
                formatted_output = "\n".join(dialogue_lines)
                output_data.append({"instruction": instruction, "input": "", "output": formatted_output})
        return output_data

    def _format_default(self, elements):
        return json.dumps(elements, indent=4, ensure_ascii=False)

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return lines
    except Exception as e:
        logging.error(f"Error while reading file {file_path}: {e}")
        return []

def read_directory(directory_path, recursive=False):
    file_paths = []
    try:
        if recursive:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    if file.endswith('.rpy'):
                        file_paths.append(os.path.join(root, file))
        else:
            for file in os.listdir(directory_path):
                if file.endswith('.rpy'):
                    file_paths.append(os.path.join(directory_path, file))
    except Exception as e:
        logging.error(f"Error while reading directory {directory_path}: {e}")
    return file_paths

def setup_arg_parser():
    parser = argparse.ArgumentParser(description="Parse and extract elements from a Ren'Py script.")
    parser.add_argument("file", type=str, help="Path to the Ren'Py script file or directory")
    parser.add_argument("--type", type=str, choices=['label', 'dialogue', 'face', 'rpy', 'llama'], help="Type of element to print (label, dialogue, face, rpy, llama)")
    parser.add_argument("--recursive", action="store_true", help="Read files recursively in a directory")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("--output", type=str, help="Path to the output file")
    return parser

def write_output(output, file_path=None):
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(output)
        except Exception as e:
            logging.error(f"Error while writing to file {file_path}: {e}")
    else:
        print(output)

def main():
    parser = setup_arg_parser()
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    all_output = []
    try:
        if os.path.isdir(args.file):
            file_paths = read_directory(args.file, args.recursive)
            for file_path in file_paths:
                lines = read_file(file_path)
                if lines:
                    lexer = RenPyLexer()
                    elements = lexer.parse_file(lines)
                    formatted_output = lexer.format_elements(elements, args.type)
                    all_output.append(formatted_output)
        else:
            lines = read_file(args.file)
            if lines:
                lexer = RenPyLexer()
                elements = lexer.parse_file(lines)
                formatted_output = lexer.format_elements(elements, args.type)
                all_output.append(formatted_output)

        final_output = json.dumps(all_output, indent=4, ensure_ascii=False) if args.type == 'llama' else "\n".join(all_output)
        write_output(final_output, args.output)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
