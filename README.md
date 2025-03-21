# ElliShape

[![PyPI version](https://badge.fury.io/py/ElliShape.svg)](https://badge.fury.io/py/ElliShape)

A graphical user interface tool for shape analysis using Elliptic Fourier Descriptors (EFD). 

Additionally, we provide a command-line version 'ellishape_cli' of the software tool for batch processing. (https://github.com/wpwupingwp/ellishape_cli)

## Description
A user-friendly software designed to offer improved contour extraction, efficient EFDs calculation, and complete EFD normalization across all basic contour transformations.

## Installation

#### Preparation Steps:
Option 1. Install Conda (if not already installed):
    - Download Anaconda from the official website:
      https://www.anaconda.com/
    - Follow the installation instructions for your operating system

Option 2. Install Python (if not using Conda):
    - Download Python 3.8 or later from the official website: https://www.python.org/downloads/ 
    - Follow the installation instructions and ensure you select the option to add Python to your system PATH

#### Installation and Usage with Conda:
1. Open the Anaconda Prompt 
2. Create a Conda environment with Python 3.8:
    ```Anaconda Prompt
    conda create -n ElliShape python=3.8
    ```
3. Activate the environment:
    ```Anaconda Prompt
    conda activate ElliShape
    ```
4. Install the ElliShape package:
    ```Anaconda Prompt
    pip install ElliShape
    ```
4. Download the required model weight files:
    ```Anaconda Prompt
    python path/to/download_pth.py
    ```
5. Run ElliShape:
    ```Anaconda Prompt
    ElliShape
    ```

#### Installation and Usage with Python Environment (Requires Python >= 3.8):
1. Open the Command Prompt
2. Install the ElliShape package:
    ```cmd
    pip install ElliShape
    ```
3. Download the required model weight files:
    ```cmd
    python path/to/download_pth.py
    ```
4. Run ElliShape:
    ```cmd
    ElliShape
    ```

#### Notes:
- Ensure your environment meets the Python version requirements.
- The model weight files are essential for running ElliShape. Make sure to download them before using the software.
- For detailed documentation and troubleshooting, refer to the official website or contact support.






