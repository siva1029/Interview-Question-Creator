import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')
#logging.info("Hello world!")

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

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir,file_name = os.path.split(filepath)
    print(file_dir)

    if file_dir!="":
        os.makedirs(file_dir, exist_ok=True)    
        logging.info(f"Created directory: {file_dir}")
        #with open(filepath, "w"):
         #   logging.info(f"Created file: {filepath}")
            # Write some content to the file for example purposes
            # with open(filepath, "w") as f:
            #     f.write("This is a sample content")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"{file_name} already exists:")



