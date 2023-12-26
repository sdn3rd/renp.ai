# renp.ai
AI utils and tools related to AI and the Renpy Engine

# Ren'Py Dialogue and Face Line Extractor to LLM dataset for training Local models

## Description
This Python script is designed to parse Ren'Py script files (`.rpy`) to extract dialogue and convert it to a local LLM training format to fine-tune your model as a Lora.

## Features
- **Dialogue and Emotion Line Extraction**: Extracts both dialogue lines and face expression commands from Ren'Py script files.
- **Include Face Lines Toggle**: Option to include or exclude face lines in the output, if you do not have emotions in your game.
- **Recursive Directory Processing**: Ability to process an entire directory of `.rpy` files recursively and output to a single flat training file.
- **Customizable Output**: Provides an option to write output to a specified file or print it to the command line interface (CLI).
- **Filtering Mechanism**: Filters out labels with insufficient content (less than four lines) to ensure meaningful output.

## Usage
This script expects that you will be using a local LLM and training a Lora for your game dialogue specifically.

If you do not have `text-generation-webui` installed, please visit: [https://github.com/oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui)

Once you have this installed, I would recommend training against: [https://huggingface.co/georgesung/llama2_7b_chat_uncensored](https://huggingface.co/georgesung/llama2_7b_chat_uncensored)

This has been validated to work, I have not tested anything else. This is literally day 2 of me using LocalLLMs and I just barely read about QLora's give me a break.

The script can be run from the command line and offers several options:

- `--input_dir <path>`: Specify the path to a directory for recursive processing of all `.rpy` files within it.
- `--rpy_file <path>`: Specify the path to a single `.rpy` file for processing.
- `--output <path>`: Specify the path to the output file where the JSON data will be saved. If not provided, the output will be printed to the CLI.
- `--include_face_lines`: Include face expression lines in the output. If not set, only dialogue lines will be extracted.
- `-h`: Display help information about the script's usage and options.

### Example Command

python parser.py --input_dir "path/to/rpy/scripts" --output "output_file.json" --include_face_lines
The include_face_lines flag is for sprite emotions, should you have them in your game. Please update the regex within the script to make this work for your game or do not use this flag.

## Output Format
The output is a JSON array, where each object represents a label from the Ren'Py script. Each object contains:

"instruction": A generated instruction based on the speakers involved in the dialogue under that label.
"input": Currently unused, reserved for future enhancements.
"output": The extracted dialogue and/or face lines formatted in Ren'Py script style.

## Requirements
- Python 3.x
- Ren'Py script files (`.rpy`)

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](#) if you want to contribute.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
joebanks on discord
