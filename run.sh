# Install necessary dependencies
pip3 install -r requirements.txt

# Download NLTK data required for TextBlob
python3 -m textblob.download_corpora

# Run the application
python3 src/main.py
