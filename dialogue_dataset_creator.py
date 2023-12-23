import re
import argparse

def extract_dialogue_and_face_lines(file_path):
    data = {}
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            current_label = None
            dialogue_face_pattern = re.compile(r'(\w+)\s+"(.*?)"|face\s+(\w+)\s+(.*)')

            for index, line in enumerate(lines):
                label_match = re.match(r'label\s+(\w+):', line)
                dialogue_face_match = dialogue_face_pattern.search(line)

                if label_match:
                    current_label = label_match.group(1)
                    data[current_label] = []

                elif dialogue_face_match and current_label:
                    speaker_or_command, dialogue, face_character, face_expression = dialogue_face_match.groups()
                    if speaker_or_command:
                        # It's a dialogue line
                        data[current_label].append(f'    {speaker_or_command} "{dialogue}"')
                    else:
                        # It's a face line
                        data[current_label].append(f'    face {face_character} {face_expression}')

    except Exception as e:
        print(f"Error reading file: {str(e)}")

    return data

def output_data(data, output_file=None):
    formatted_data = [f'label {label}:\n' + '\n'.join(lines) + '\n\n' for label, lines in data.items()]
    formatted_output = '\n'.join(formatted_data)

    if output_file:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(formatted_output)
    else:
        print(formatted_output)

def main():
    parser = argparse.ArgumentParser(description="Extract and format dialogue and face lines from a Ren'Py script.")
    parser.add_argument("rpy_file", type=str, help="Path to the Ren'Py script file")
    parser.add_argument("--output", type=str, help="Path to output file")

    args = parser.parse_args()
    rpy_file_path = args.rpy_file
    output_file = args.output if args.output else None

    data = extract_dialogue_and_face_lines(rpy_file_path)
    output_data(data, output_file)

if __name__ == "__main__":
    main()
