from detectron2.data.datasets import register_coco_instances
register_coco_instances("surgery_train", {}, "/home/lahen/detectron2/AdelaiDet/data/coco/annotations/instances_train2017.json", "/home/lahen/detectron2/AdelaiDet/data/coco/train2017")
# register_coco_instances("surgery_val", {}, "//home/lishuo/data_maker_videoC/data/annotations/instances_val2017.json", "/home/lahen/SOLO/data/coco/val2017")
# register_coco_instances("surgery_test", {}, "/home/lahen/SOLO/data/coco/annotations/instances_test2017.json", "/home/lahen/SOLO/data/coco/test2017")

from detectron2.data import MetadataCatalog
MetadataCatalog.get("surgery_train").thing_classes = ['Cerebellum','CN8', 'CN5',
             'CN7', 'SCA',  'AICA',
             'SuperiorPetrosalVein', 'Vein', 'Brainstem',
             'Suction', 'Bipolar',
             'Forcep', 'BluntProbe',
             'Drill', 'Kerrison',
             'Cottonoid', 'Scissors',
             'Unknown']
# MetadataCatalog.get("surgery_val").thing_classes = ['nonsegmented', 'artery', 'blood', 'spinalcord', 'bluntprobe', 'scissor']