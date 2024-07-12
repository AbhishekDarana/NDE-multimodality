""" Abhishek Darana- Script to convert data to COCO format json"""

import json

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

# Example data
images = [
    {"id": 1, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_1_formatted_data\\data0_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    {"id": 2, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_1_formatted_data\\data1_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    {"id": 3, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_1_formatted_data\\data2_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    # {"id": 4, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_1_formatted_data\\data3_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    # {"id": 5, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_1_formatted_data\\data4_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    # {"id": 6, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_2_formatted_data\\data0_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    # {"id": 7, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_2_formatted_data\\data1_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    # {"id": 8, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_2_formatted_data\\data2_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    # {"id": 9, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_2_formatted_data\\data3_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    # {"id": 10, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_3_formatted_data\\data0_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    # {"id": 11, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_3_formatted_data\\data1_unmarked.jpg" , "license":1, "date_captured": "2024-07-10"},
    # {"id": 12, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_3_formatted_data\\data2_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    # {"id": 13, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_3_formatted_data\\data3_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    # {"id": 14, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_4_formatted_data\\data0_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    # {"id": 15, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_4_formatted_data\\data1_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    # {"id": 16, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_4_formatted_data\\data2_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"},
    # {"id": 17, "width": 1500, "height": 1200, "file_name": "C:\\Users\\Abhishek\\Documents\\Summer_research\\CHARISMA-main\\ground-penetrating-radar\\Rebar mapping\\data\\GPR_zone_4_formatted_data\\data3_unmarked.jpg", "license": 1, "date_captured": "2024-07-10"}
]

annotations = [
    {"id": 1, "image_id": 1, "category_id": 1, "bbox": [134,5, 0, 0], "area": 1, "segmentation": [[134,5]], "iscrowd": 0},
    {"id": 2, "image_id": 1, "category_id": 1, "bbox": [28,5, 0, 0], "area": 1, "segmentation": [[28,5]], "iscrowd": 0},
    {"id": 3, "image_id": 1, "category_id": 1, "bbox": [106,5, 0, 0], "area": 1, "segmentation": [[106,5]], "iscrowd": 0},
    {"id": 4, "image_id": 1, "category_id": 1, "bbox": [38,7, 0, 0], "area": 1, "segmentation": [[38,7]], "iscrowd": 0},
    {"id": 5, "image_id": 1, "category_id": 1, "bbox": [92,7, 0, 0], "area": 1, "segmentation": [[92,7]], "iscrowd": 0},
    {"id": 6, "image_id": 1, "category_id": 1, "bbox": [53,5, 0, 0], "area": 1, "segmentation": [[53,5]], "iscrowd": 0},
    {"id": 7, "image_id": 1, "category_id": 1, "bbox": [79,4, 0, 0], "area": 1, "segmentation": [[79,4]], "iscrowd": 0},
    {"id": 8, "image_id": 1, "category_id": 1, "bbox": [4,5, 0, 0], "area": 1, "segmentation": [[4,5]], "iscrowd": 0},
    {"id": 9, "image_id": 1, "category_id": 1, "bbox": [16,7, 0, 0], "area": 1, "segmentation": [[16,7]], "iscrowd": 0},
    {"id": 10, "image_id": 1, "category_id": 1, "bbox": [120,7, 0, 0], "area": 1, "segmentation": [[120,7]], "iscrowd": 0},
    {"id": 11, "image_id": 1, "category_id": 1, "bbox": [64, 7, 0, 0], "area": 1, "segmentation": [[64, 7]], "iscrowd": 0},
    {"id": 12, "image_id": 2, "category_id": 1, "bbox": [83,7, 0, 0], "area": 1, "segmentation": [[83,7]], "iscrowd": 0},
    {"id": 13, "image_id": 2, "category_id": 1, "bbox": [42,5, 0, 0], "area": 1, "segmentation": [[42,5]], "iscrowd": 0},
    {"id": 14, "image_id": 2, "category_id": 1, "bbox": [106,7, 0, 0], "area": 1, "segmentation": [[106,7]], "iscrowd": 0},
    {"id": 15, "image_id": 2, "category_id": 1, "bbox": [int(16.10925105),int(5.18675373), 0, 0], "area": 1, "segmentation": [[int(16.10925105),int(5.18675373)]], "iscrowd": 0},
    {"id": 16, "image_id": 2, "category_id": 1, "bbox": [ int(75.03543731),int(5.16949861), 0, 0], "area": 1, "segmentation": [[int(75.03543731),int(5.16949861)]], "iscrowd": 0},
    {"id": 17, "image_id": 2, "category_id": 1, "bbox": [int(129.76444838),int(5.16407674), 0, 0], "area": 1, "segmentation": [[int(129.76444838),int(5.16407674)]], "iscrowd": 0},
    {"id": 18, "image_id": 2, "category_id": 1, "bbox": [ int(35.18949539),int(7.24895406), 0, 0], "area": 1, "segmentation": [[int(35.18949539),int(7.24895406)]], "iscrowd": 0},
    {"id": 19,"image_id": 2, "category_id": 1, "bbox": [int(130.96025816),int(7.25714651), 0, 0], "area": 1, "segmentation": [[int(130.96025816),int(7.25714651)]], "iscrowd": 0},
    {"id": 20, "image_id": 2, "category_id": 1, "bbox": [ int(11.41331068),int(7.21494188), 0, 0], "area": 1, "segmentation": [[int(11.41331068),int(7.21494188)]], "iscrowd": 0},
    {"id": 21, "image_id": 2, "category_id": 1, "bbox": [ int(58.95252926),int(7.13072557), 0, 0], "area": 1, "segmentation": [[int(58.95252926),int(7.13072557)]], "iscrowd": 0},
    {"id": 22   , "image_id": 2, "category_id": 1, "bbox": [int(103.13114287),int(5.17898088), 0, 0], "area": 1, "segmentation": [[int(103.13114287),int(5.17898088)]], "iscrowd": 0},
    {"id": 23, "image_id": 3, "category_id": 1, "bbox": [int(12.72730672),int(6.7916171), 0, 0], "area": 1, "segmentation": [[int(12.72730672),int(6.7916171)]], "iscrowd": 0},
    {"id": 24, "image_id": 3, "category_id": 1, "bbox": [int(72.91782141),int(4.93301811), 0, 0], "area": 1, "segmentation": [[int(72.91782141),int(4.93301811)]], "iscrowd": 0},
    {"id": 25, "image_id": 3, "category_id": 1, "bbox": [int(129.15879455),int(7.6905102), 0, 0], "area": 1, "segmentation": [[int(129.15879455),int(7.6905102)]], "iscrowd": 0},
    {"id": 26, "image_id": 3, "category_id": 1, "bbox": [int(53.3975225),int(5.36808932), 0, 0], "area": 1, "segmentation": [[int(53.3975225),int(5.36808932)]], "iscrowd": 0},
    {"id": 27, "image_id": 3, "category_id": 1, "bbox": [int(103.809074),int(7.0711704), 0, 0], "area": 1, "segmentation": [[int(103.809074),int(7.0711704)]], "iscrowd": 0},
    {"id": 28, "image_id": 3, "category_id": 1, "bbox": [int(125.54480138),int(5.03877314), 0, 0], "area": 1, "segmentation": [[int(125.54480138),int(5.03877314)]], "iscrowd": 0},
    {"id": 29, "image_id": 3, "category_id": 1, "bbox": [int(75.17196512),int(7.02491508), 0, 0], "area": 1, "segmentation": [[int(75.17196512),int(7.02491508)]], "iscrowd": 0},
    {"id": 30, "image_id": 3, "category_id": 1, "bbox": [int(9.92198389),int(5.11354303), 0, 0], "area": 1, "segmentation": [[int(9.92198389),int(5.11354303)]], "iscrowd": 0},
    {"id": 31, "image_id": 3, "category_id": 1, "bbox": [int(40.86959632),int(7.68570166), 0, 0], "area": 1, "segmentation": [[int(40.86959632),int(7.68570166)]], "iscrowd": 0},
    {"id": 32, "image_id": 3, "category_id": 1, "bbox": [int(94.31836705),int(4.91926933), 0, 0], "area": 1, "segmentation": [[int(94.31836705),int(4.91926933)]], "iscrowd": 0},
    {"id": 33   , "image_id": 3, "category_id": 1, "bbox": [int(29.57292833),int(5.38388564), 0, 0], "area": 1, "segmentation": [[int(29.57292833),int(5.38388564)]], "iscrowd": 0}
    # {"id": 4, "image_id": 4, "category_id": 1, "bbox": [100, 200, 0, 0], "area": 1, "segmentation": [[]], "iscrowd": 0},
    # {"id": 5, "image_id": 5, "category_id": 1, "bbox": [100, 200, 0, 0], "area": 1, "segmentation": [[]], "iscrowd": 0},
    # {"id": 6, "image_id": 6, "category_id": 1, "bbox": [100, 200, 0, 0], "area": 1, "segmentation": [[]], "iscrowd": 0},
    # {"id": 7, "image_id": 7, "category_id": 1, "bbox": [100, 200, 0, 0], "area": 1, "segmentation": [[]], "iscrowd": 0},
    # {"id": 8, "image_id": 8, "category_id": 1, "bbox": [100, 200, 0, 0], "area": 1, "segmentation": [[]], "iscrowd": 0},
    # {"id": 9, "image_id": 9, "category_id": 1, "bbox": [100, 200, 0, 0], "area": 1, "segmentation": [[]], "iscrowd": 0},
    # {"id": 10, "image_id": 10, "category_id": 1, "bbox": [100, 200, 0, 0], "area": 1, "segmentation": [[]], "iscrowd": 0},
    # {"id": 11, "image_id": 11, "category_id": 1, "bbox": [100, 200, 0, 0], "area": 1, "segmentation": [[]], "iscrowd": 0},
    # {"id": 12, "image_id": 12, "category_id": 1, "bbox": [100, 200, 0, 0], "area": 1, "segmentation": [[]], "iscrowd": 0},
    # {"id": 13, "image_id": 13, "category_id": 1, "bbox": [100, 200, 0, 0], "area": 1, "segmentation": [[]], "iscrowd": 0},
    # {"id": 14, "image_id": 14, "category_id": 1, "bbox": [100, 200, 0, 0], "area": 1, "segmentation": [[]], "iscrowd": 0},
    # {"id": 15, "image_id": 15, "category_id": 1, "bbox": [100, 200, 0, 0], "area": 1, "segmentation": [[]], "iscrowd": 0},
    # {"id": 16, "image_id": 16, "category_id": 1, "bbox": [100, 200, 0, 0], "area": 1, "segmentation": [[]], "iscrowd": 0},
    # {"id": 17, "image_id": 17, "category_id": 1, "bbox": [100, 200, 0,  0], "area": 1, "segmentation": [[]], "iscrowd": 0}
]

categories = [
    {"id": 1, "name": "Rebar", "supercategory": "Overlay"}
]

# Adding data to coco_format
coco_format['images'].extend(images)
coco_format['annotations'].extend(annotations)
coco_format['categories'].extend(categories)

# Saving to a JSON file
with open('coco_dataset.json', 'w') as f:
    json.dump(coco_format, f, indent=4)
