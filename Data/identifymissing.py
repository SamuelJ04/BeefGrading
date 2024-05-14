import pandas as pd
import os

# this is used to identify

## basically clean the excel file just a tiny bit and then 
## use this after you use the rename script (clean.sh): ensure the images and excel column ID's have the same nomenclature
## modify the folder path, excel path 

def compare_file_and_columns(imgFolderPath, excelPath):
    #load in file names to a tuple
    files = os.listdir(imgFolderPath)
    file_names = [f.split('.')[0] for f in files] # removes file extensions
    #for image_name in file_names:
    #    print(image_name)
    
    #read excel sheet and load it in
    excel_data = pd.read_excel(excelPath)
    #print(excel_data)
    
    excel_ids = excel_data['CarcassId'].astype(str).tolist()
    #for id in excel_ids:
        #print(id)
    
    # identify if there are missing images that do not exist in the excel sheet
    missing_images = set(excel_ids) - set(file_names)
    print ("Excel IDs that do not have a corresponding image:")
    if len(missing_images) == 0:
        print("None!")
    else:
        #prints the list of missing images
        for id in missing_images:
            print(id)
        
    
    #identify missing id numbers for images
    missing_ids = set(file_names) - set(excel_ids)
    print("\nImages that do not have a corresponding excel ID: ")   
    if len(missing_ids) == 0:
        print("None!")
    else:
        #prints the list of missing ids
        for id in missing_ids:
            print(id)
        
# modify here per each case
# excel path and         
folder_path = "CargillDodge072022Plant/Modified Images/"
excel_path = "CargillDodge072022Plant/excel.xlsx"
compare_file_and_columns(folder_path, excel_path)