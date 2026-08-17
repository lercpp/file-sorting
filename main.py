from pathlib import Path
import shutil

path = Path("test")

categories = {
    "Images": [".jpg",".jpeg",".png",".gif",".webp"],
    "Videos": [".mp4",".avi",".mkv",".mov"],
    "Documents": [".pdf",".docx",".doc",".txt",".xlsx"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Music": [".mp3", ".wav", ".flac"],
    "Programs": [".exe", ".msi"]
}

def get_categoria(extension):
    for category,extensions in categories.items():
        if extension.lower() in extensions:
            return category

    return "Other"


def organze():
    for file in path.iterdir():
        if file.is_dir():
            continue

        category = get_categoria(file.suffix)

        target_folder = path / category
        target_folder.mkdir(exist_ok=True)
        target = target_folder / file.name
        if target.exists():
            print(f"propyshen: {file.name}")
            continue
        shutil.move(file,target)
        print(f"{file.name}->{category}/")

if __name__=="__main__":
    organze()