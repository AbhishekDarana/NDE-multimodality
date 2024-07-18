"""Author- Abhishek Darana- 07/18/2024 - Have initially eveloped dataset_filler.py but was dependent most of structure and could break files. This version involves 
another config file which is a safe bet and easy to use for multiple models."""
import sys
import ast
import configparser
import datetime
import os
if(len(sys.argv)!=2):
    print("Give a config file  or location create a config file to input images and annotations")
    config_file=input()
else:
    config_file=sys.argv[1]

config = configparser.ConfigParser()

if not config_file.endswith(".ini"):
    x = datetime.datetime.now()
    ini_dateformat_file=x.strftime("%Y_%b_%d_%H_%M_%S_")+"config.ini"
    config_file=os.path.join(os.path.dirname(config_file),ini_dateformat_file)
    # print("yeeees",config_file)
    config['DATA'] = {'images': [], 'annotations': []}
    with open(config_file, 'w') as conf:
        config.write(conf)

dataset_config = configparser.ConfigParser()
dataset_config.read(config_file)
list_dataset_images=ast.literal_eval(dataset_config["DATA"]['images'])
if(len(list_dataset_images)!=0):
    print(list_dataset_images)
    img_id=list_dataset_images[-1]["id"]+1
else:
    img_id=1
list_dataset_annotations=ast.literal_eval(dataset_config['DATA']['annotations'])
if(len(list_dataset_annotations)!=0):
    id=list_dataset_annotations[-1]["id"]+1
else:
    id=1
print("Start inputting the data file for dataset json")

try:
    while True:
        user_input=input()
        if user_input.startswith('"') and user_input.endswith('"'):
            user_input=user_input[1:-1]
        dir_name=os.path.dirname(user_input)
        basename=os.path.basename(user_input)
        if(basename.endswith(".ini")):
            ini_name=basename
            data_name=basename.split(".")[0]+"_unmarked.jpg"
            if not os.path.exists(os.path.join(dir_name,data_name)):
                print("No data file for the given config file. Therefore,discarded")
                continue
        else:
            data_name=basename
            ini_name=basename.split(".")[0]+".ini"
            if not os.path.exists(os.path.join(dir_name,ini_name)):
                print("No config file for the given data file. Therefore,discarded")
                continue

        
        list_dataset_images.append({"id": img_id, "width": 1500, "height": 1200, "file_name": os.path.join(dir_name,data_name), "license": 1, "date_captured": "2024-07-10"})
        
        ini_config=configparser.ConfigParser()
        ini_config.read(os.path.join(dir_name,ini_name))
        stringer=ini_config['CENTERS']['points']
        splitter=stringer[1:-1].split("[")
        # splitter=splitter.split("]")
        for i in splitter[1:]:
            split2=i.split("]")[0]
            space_split=split2.split(" ")
            while '' in space_split:
                space_split.remove('')        
            list_dataset_annotations.append({"id": id, "image_id": img_id, "category_id": 1, "bbox": [int(float(space_split[0])),int(float(space_split[1])), 0, 0], "area": 1, "segmentation": [[int(float(space_split[0])),int(float(space_split[1]))]], "iscrowd": 0})
            id+=1
        img_id+=1
        print(list_dataset_annotations)
        print(list_dataset_images)

except KeyboardInterrupt:
    # with open("COCO_formatter.py", "a") as file:
    #     for i in extension:
    #         file.write(f"{i},\n")
    config = configparser.ConfigParser()

    config['DATA'] = {'images': str(list_dataset_images).replace("},","},\n"), 'annotations': str(list_dataset_annotations).replace("},","},\n")}
    with open(config_file, 'w') as conf:
        config.write(conf)
    print("\nProgram terminated by user")
    