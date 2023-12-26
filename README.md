# Ren'Py Script Parser

This Python script is designed to parse Ren'Py script files (`.rpy`) and extract various elements from them, including labels, dialogues, and more. It offers flexibility in choosing the type of element to extract and can process individual files or entire directories of Ren'Py scripts.

## Features

- Extracts labels, dialogues, and other elements from Ren'Py script files.
- Supports parsing of individual files or entire directories (recursively if desired).
- Option to specify the type of element to extract (label, dialogue, face, etc.).
- Output can be saved to a file or printed to the command line.

## Pre-requisites
- A high technical level of competance
- Python 3.x
- Ren'Py script files (`.rpy`)
- text-generation-webu - [https://github.com/oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui)
- a model to train against - [https://huggingface.co/georgesung/llama2_7b_chat_uncensored](https://huggingface.co/georgesung/llama2_7b_chat_uncensored)

## Usage
1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or download the `renpy_script_parser.py` script.
3. Open a terminal or command prompt and navigate to the directory containing `renpy_script_parser.py`.
4. Run the script with the desired options. Here are some example commands:
   - To extract labels from a single Ren'Py script file and print the output:
     ```shell
     python renpy_script_parser.py /path/to/script.rpy --type label
     ```
   - To extract dialogues from all Ren'Py script files in a directory (recursively) and save the output to a file:
     ```shell
     python renpy_script_parser.py /path/to/scripts_directory --type dialogue --recursive --output output.json
     ```
   - To extract face expressions from a single script file and print the output:
     ```shell
     python renpy_script_parser.py /path/to/script.rpy --type face
     ```
5. View the extracted elements in the specified output file or in the terminal, depending on your chosen options.

## Options
- `--type`: Specify the type of element to extract (label, dialogue, face, rpy, llama).
- `--recursive`: Read files recursively in a directory (only applicable when processing directories).
- `--verbose`: Enable verbose logging for debugging (optional).
- `--output`: Specify the path to the output file (optional).

## Example Output
The script provides output in the chosen format, which can be JSON or plain text. Here's an example of JSON output:

```json
[
    "label start:",
    "    $ player_name = \"John\"",
    "    ' This is a comment",
    "",
    "label intro:",
    "    ' Introduction dialogue",
    "    ' More dialogue here",
    "",
    "label end:",
    "    ' Ending dialogue",
    "    ' Goodbye!"
]
```

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](#) if you want to contribute.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
joebanks on discord
