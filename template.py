# Import necessary libraries/modules
import os
from pathlib import Path
import logging

# Configurating logging settings
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

# Logging welcome message
#logging.info("Hello world!")

# List of files/folders to be created 
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynp",
    "app.py",
]

# Iterate over the each file in the list
for filepath in list_of_files:
    # converting the filepath to a path object
    filepath = Path(filepath)
    # Splitting the file path into directory and file name
    file_dir,file_name = os.path.split(filepath)
    # Print the directory
    print(file_dir)

# Check if the file's directory is not exist
    if file_dir!="":
        # create directory if it doesn't exist
        os.makedirs(file_dir, exist_ok=True)    
        logging.info(f"Created directory: {file_dir}")
        #with open(filepath, "w"):
         #   logging.info(f"Created file: {filepath}")
            # Write some content to the file for example purposes
            # with open(filepath, "w") as f:
            #     f.write("This is a sample content")
    # Checking if the file doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"{file_name} already exists:")





