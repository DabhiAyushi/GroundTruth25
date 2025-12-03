import zipfile
import os

def create_zip(files, output_name="ad_creatives.zip"):
    with zipfile.ZipFile(output_name, "w") as zipf:
        for file in files:
            if file is None:
                continue
            zipf.write(file)
            os.remove(file)
    return output_name