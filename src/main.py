import os
import yaml
import logging
from utils import interactive_visualization, advanced_text_analysis
from logger import setup_logger

def read_config(config_file):
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' not found.")
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    return config

def main():
    config_file = os.path.join(os.path.dirname(__file__), "config.yaml")
    config = read_config(config_file)

    # Set up logger
    log_level = getattr(logging, config.get("settings", {}).get("log_level", "INFO").upper(), logging.INFO)
    setup_logger("root", level = log_level)
    logger = logging.getLogger("root")

    logger.info("Application started")

    try:
        numbers = config["data"].get("numbers", [])
        text = config["data"].get("text", " ")
        operation = config["data"].get("operation", "interactive_visualization")
        chart_type = config["data"].get("chart_type", "scatter")

        if operation == "interactive_visualization":
            interactive_visualization(numbers, chart_type)
            print("Interactive chart created and saved as 'interactive_chart.html'. Open this file in a web browser to view.")
        elif operation == "advanced_text_analysis":
            analysis_results = advanced_text_analysis(text)
            print("Advanced Text Analysis Results:")
            print(f"  Polarity: {analysis_results['polarity']}")
            print(f"  Subjectivity: {analysis_results['subjectivity']}")
            print(f"  Keywords: {', '.join(analysis_results['keywords'])}")
        else:
            logger.error(f"Unsupported operation: {operation}")
            print(f"Unsupported operation: {operation}")

    except Exception as e:
        logger.exception("An error occurred during execution.")
        print(f"An error occurred: {e}")
    finally:
        logger.info("Application finished")

if __name__ == "__main__":
    main()
