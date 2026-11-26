from pathlib import Path
#current working directory
root = Path(".")

#Folder
folders = [
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "uploads",
    "tests",
]

# File
files = [
    "app/main.py",
    "requirements.txt"
    "ingest_sample_kb.py",
    "run.py",
    ".env",
]
#Create folder
for folder in folders:
    (root/folder).mkdir(parents=True,exist_ok=True)

#Create file
for file in files:
    (root/file).touch(exist_ok=True)

print("sucessfully create a project structure")
