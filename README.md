# Genetic-MicroRTS
This project's main goal is to use the native abstraction and synthesis packages of MicroRTS to create a genetically optimized MircoRTS program.

## Requirements
- Python 3.6 or later
- Java Development Kit (JDK) 8 (MicroRTS requirement)

## Getting Started
To get started using this project you can follow the steps below:
1. Download and compile MicroRTS [here](https://github.com/Farama-Foundation/MicroRTS)
2. Clone this repo into the `ai` folder of your MicroRTS project
3. Run the setup script
    - Linux: `Setup.sh`
    - Windows: `Setup.bat`
4. Run `ScriptGenerator.py` to generate a random legal MicroRTS program in the `Output` directory
    - `python3 ./ScriptGenerator.py`