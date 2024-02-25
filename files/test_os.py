import os

images_extentions = [".jpeg", ".jpg", ".png", ".gif"]
doc_extentions = [".doc", ".docx", ".pdf", ".txt"]
archives_extentions = [".zip", ".rar"]


base_path = r"C:\Users\LENOVO X13\Desktop"
dest_path  = r"C:\Users\LENOVO X13\Desktop\CleanedUp"

entries = os.scandir(base_path)
#os.path.splitext()

for entry in entries:
    #print("entry:", entry.name)
    original_path_entry = os.path.join(base_path, entry.name)
    dest_path_entry = os.path.join(dest_path, entry.name)
    if os.path.isfile(entry):
        extention = os.path.splitext(entry.name)[1]
        #print("file extension is:", os.path.splitext(entry.name)[1])
        if extention in images_extentions:
            # move to Images 
            pass
        # os.renames(original_path_entry, dest_path_entry)



#def__init__(self, *args):
 #   self.speed = args[0]
  #  self.color = args[1]



