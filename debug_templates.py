import os
from app import app

print("Templates folder:", app.template_folder)
print("Templates in folder:", os.listdir(app.template_folder))
