import zipfile
import pathlib

def make_archive(filepaths, dir):
    zip_path = pathlib.Path(dir, 'Compress.zip')
    with zipfile.ZipFile(zip_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["Note1.txt", "Note2.txt"], dir="Test_cmp")