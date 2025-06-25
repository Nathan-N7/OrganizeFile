import os
import mimetypes
import shutil

my_bot = os.path.basename(__file__)

for file in os.listdir():
    if file == my_bot:
        continue
    
    path = os.path.join(os.getcwd(), file)
    if os.path.isfile(path):
        type_mime, _ = mimetypes.guess_type(path)

        if (type_mime and type_mime.startswith("text")) or (type_mime == None):
            os.makedirs("text", exist_ok=True)
            text = os.path.join(os.getcwd(), "text")
            shutil.move(path, text)

        elif file.endswith((".png", ".jpg", ".jpeg", ".webp", ".gif")):
            os.makedirs("image", exist_ok=True)
            image = os.path.join(os.getcwd(), "image")
            shutil.move(path, image)

        elif file.endswith((".pdf", ".doc", ".docx")):
            os.makedirs("document", exist_ok=True)
            document = os.path.join(os.getcwd(), "document")
            shutil.move(path, document)

        else:
            print (f"{file}: nao identificado")