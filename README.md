# renp.ai
AI utils and tools related to AI and the Renpy Engine

# Ren'Py Dialogue and Face Line Extractor to LLM dataset for training Local models

## Description
This Python script is designed to parse Ren'Py script files (`.rpy`) to extract dialogue and face lines. It is particularly useful for processing visual novel scripts written in Ren'Py, enabling writers and developers to easily extract and analyze dialogue and character expressions. The script can handle both individual `.rpy` files and recursively process a directory containing multiple `.rpy` files.

## Features
- **Dialogue and Face Line Extraction**: Extracts both dialogue lines and face expression commands from Ren'Py script files.
- **Include Face Lines Toggle**: Option to include or exclude face lines in the output.
- **Recursive Directory Processing**: Ability to process an entire directory of `.rpy` files recursively.
- **Flexible Output Formatting**: Outputs extracted data in a structured JSON format, suitable for further processing or analysis.
- **Customizable Output**: Provides an option to write output to a specified file or print it to the command line interface (CLI).
- **Filtering Mechanism**: Filters out labels with insufficient content (less than four lines) to ensure meaningful output.

## Usage
The script can be run from the command line and offers several options:

- `--input_dir <path>`: Specify the path to a directory for recursive processing of all `.rpy` files within it.
- `--rpy_file <path>`: Specify the path to a single `.rpy` file for processing.
- `--output <path>`: Specify the path to the output file where the JSON data will be saved. If not provided, the output will be printed to the CLI.
- `--include_face_lines`: Include face expression lines in the output. If not set, only dialogue lines will be extracted.
- `-h`: Display help information about the script's usage and options.

### Example Command
python parser.py --input_dir "path/to/rpy/scripts" --output "output_file.json" --include_face_lines


## Output Format
The output is a JSON array, where each object represents a label from the Ren'Py script. Each object contains:
- `"instruction"`: A generated instruction based on the speakers involved in the dialogue under that label.
- `"input"`: Currently unused, reserved for future enhancements.
- `"output"`: The extracted dialogue and/or face lines formatted in Ren'Py script style.

## Requirements
- Python 3.x
- Ren'Py script files (`.rpy`)

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](#) if you want to contribute.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
joebanks on discord
