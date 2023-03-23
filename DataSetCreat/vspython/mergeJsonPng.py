import os
import shutil

def merge_folders(folder1, folder2):
    for item in os.listdir(folder1):
        item_path = os.path.join(folder1, item)
        print(item,item_path)
        if os.path.isdir(item_path):
            if os.path.exists(os.path.join(folder2, item)):
                merge_folders(item_path, os.path.join(folder2, item))
            # else:
            #     shutil.copytree(item_path, os.path.join(folder2, item))
        else:
            if os.path.exists(os.path.join(folder2, item)):
                  try:
                      shutil.copy2(item_path,os.path.join(folder1, item) )
                  except:
                      print("the same")
            else:
                shutil.copy2(item_path, os.path.join(folder2, item))
    return folder1


folder2 = '/Users/lidenghui/vspython/rectangelJson' 
folder1 = '/Users/lidenghui/vspython/rectanglePng'
target_folder = '/Users/lidenghui/vspython'
merged_folder = merge_folders(folder1, folder2)
shutil.copytree(merged_folder, '/Users/lidenghui/vspython/target_folder')


