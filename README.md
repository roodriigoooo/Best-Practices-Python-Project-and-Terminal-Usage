
# Python Project with Terminal Usage: Best Practices

## Overview
This project is a Python application demonstrating best practices in project structure, code organization, configuration management, script execution and unit testing. The application also showcases some advanced functionalities:
- **Interactive Data Visualization**: Generates interactive charts (scatter or line plots) that can be viewed in a web browser. 
- **Advanced Text Analysis**: Performs sentiment analysis and keyword extraction using basic NLP techniques. 
- **Enhanced Logging**: Implements a custom logging system that logs to both the console and a JSON file, including detailed metadata. 

## Project Structure
```bash
python_project/
|--src/
|  |--main.py
|  |--utils.py
|  |--config.yaml
|  |--logger.py
|--tests/
|  |--test_utils.py
|--run.sh
|--README.md
|--requirements.txt
```

## Setup and Installation
### Prerequisites
- **Python 3.6 or higher**
- **pip** (Python package installer)
- **Git** (optional, for cloning repository)

### Clone the Repository
You can clone the repository using Git:
```bash
git clone https://github.com/rodrigosastre/python_best_practices_project.git
```
Or download the ZIP file from GitHub and extract it.
 
### Navigate to the Project Directory
```bash
cd python_best_practices_project
```
### (Optional) Create and Activate a Virtual Environment
I recommend to use a virtual environvent (venv) to manage dependencies. 
```bash
python3 -m venv venv
source venv/bin/activate # "venv\Scripts\activate" on Windows
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
**Note**: The requirements.txt file includes all necessary packages:
- PyYAML
- Plotly
- Pandas
- TextBlob
- scikit-learn
Also, download the NLTK data required by TextBlob:
```bash
python -m textblob.download_corpora
```
## How to Run the Project
### Ensure run.sh Has Execution Permissions
```bash
chmod +x run.sh
```
### Run the Application Using the Shell Script
```bash
./run.sh
```
This script will:
- Install the necessary dependencies (if not already installed).
- Download necessary NLTK data for TextBlob. 
- Run the application. 

### Running the Application Manually
Alternatively, the application can also be ran manually:
```bash
python src/main.py
```

## Customization
### Modify Configuration
The application's behavior is controlled via the config.yaml file located in the src/ directory. 
```yaml
settings:
	log_level: "INFO"

data:
	numbers: [12,45,23,67,34,89]
	text: "Python is a programming language with a nice community and many useful libraries."
	operation: "advanced_text_analysis" # Options: "interactive_visualization", "advanced_text_analysis"
	chart_type: "scatter" # Options: "scatter", "line"
```
**Available Configuration Options**
- settings.log_level: Sets the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
- data.numbers: A list of numbers for data visualization. 
- data.text: A text string for advanced text analysis. 
- data.operation: The operation to perform:
	- "interactive_visualization": Generates an interactive chart. 
	- "advanced_text_analysis": Performs sentiment analysis and keyword extraction. 
- data.chart_type: Type of chart for visualization ("scatter" or "line").

### Example: Changing the Operation to Interactive Visualization
Edit the config.yaml file:
```yaml
operation: "interactive_visualization"
chart_type: "line"
```
## How Each File Works
```
src/
```
- __init__.py: Indicates that src is a Python package. 
- main.py: The main module orchestrating the application. Reads configurations, sets up logging, and calls utils.py functions. 
- utils.py: Contains core functionality:
	- interactive_visualization(numbers, chart_type): Creates an interactive chart using Plotly.
	- advanced_text_analysis(text): Performs sentiment analysis and keyword extraction. 
- config.yaml: Configuration file to customize the application's behavior. 
- logger.py: Sets up a custom logging system that logs messages to both the console and a JSON file (app_logs.json), including detailed metadata. 

```
tests/
```
- __init__.py: Indicates that tests is Python package. 
- test_utils.py: Contains unit tests for the functions in utils.py using the unittest framework. 

### Root Directory 
- run.sh: A shell script to run the application, ensures all dependencies and necessary data are installed.
- README.md: Documentation for the project (this file). 
- requirements.txt: Lists all Python dependencies required by the project. 

## How to Run the Tests
### Navigate to the Project Directory
Ensure you are in the project's root directory:
```bash
cd python_best_practices_project
```
### Run the Unit Tests
Use the following command to run all tests:
```bash
python -m unittest discover tests
```
This command will: 
- Discover all test modules in the tests/ directory.
- Execute the tests and report results. 

## Expected Output
You should see output similar to:
```markdown
......
----------------------------------------------------------------------
Ran 6 tests in 0.1234s

OK
```

## Logging
The application uses a custom logging system that logs messages to both the console and a JSON file (app_logs.json) with metadata including:
- Timestamp
- Thread name
- Logger name
- Log level
- Message
- Function name
- Line number

### Adjusting the Logging Level
Modify the log_level in config.yaml:
```yaml
log_level: "DEBUG"
```
Available levels:
- DEBUG: Detailed information, typically used when diagnosing problems. 
- INFO: Confirmation that things are working as intended.
- WARNING: An indication that something went wrong. 
- ERROR: Due to a more serious problem, the software was unable to perform a given function. 
- CRITICAL: A serious error, indicating that the program itself may be unable to continue running.  

## Error Handling 
The application includes robust error handling to manage:
- Invalid or missing configurations. 
- Unsupported operations. 
- Empty or invalid input data. 
Errors are logged with detailed information and are also displayed to the user. 

## Dependencies
The project relies on the following Python packages:
- PyYAML: For parsing YAML configuration files. 
- Plotly: For creating interactive visualizations. 
- Pandas: For data manipulation. 
- TextBlob: For text processing and sentiment analysis. 
- Scikit-learn: For keyword extraction using TF-IDF. 
- NLTK: Required by TextBlob for NLP. 

Install all dependencies using:
```bash
pip install -r requirements.txt
python -m textblob.download_corpora

## Additional Information
### Viewing the Interactive Charts
After running an interactive visualization, an HTML file named interactive_chart.html will be generated in the project root directoy. 
- Open this file in a web browser to view the chart. 
- The chart supports features like zooming, panning and hover information. 

## License
This project is licensed under the MIT License. 

## Conclusion
The aim of this project is mainly to demonstrate a less straight-forward version of a project that is well-structured, well modularized, robust in error handling and testing, comprehensive in logging and documented clearly.  
