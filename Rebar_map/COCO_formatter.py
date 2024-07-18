"""Author- Abhishek Darana-07/18/2024- Have modified dataset formatter as it has been a huge workload to modify, created filler2.py file that helps setting up data into the json file."""
import json
import configparser
import sys
import ast
if(len(sys.argv)!=2):
    print("Give a config file  for labels")
    config_file=input()
else:
    config_file=sys.argv[1]

coco_format = {
    "info": {
        "description": "Example Dataset",
        "url": "http://example.com",
        "version": "1.0",
        "year": 2024,
        "contributor": "Your Name",
        "date_created": "2024-07-12"
    },
    "licenses": [
        {
            "id": 1,
            "name": "Example License",
            "url": "http://example.com/license"
        }
    ],
    "images": [],
    "annotations": [],
    "categories": []
}

config = configparser.ConfigParser()
config.read(config_file)
# Example data
images = ast.literal_eval(config['DATA']['images'])
annotations = ast.literal_eval(config['DATA']['annotations'])

categories = [
    {"id": 1, "name": "Rebar", "supercategory": "Overlay"}
]


if __name__=="__main__":
    # Adding data to coco_format
    coco_format['images'].extend(images)
    coco_format['annotations'].extend(annotations)
    coco_format['categories'].extend(categories)

    # Saving to a JSON file
    with open('coco_dataset.json', 'w') as f:
        json.dump(coco_format, f, indent=4)


    
    

    
    


