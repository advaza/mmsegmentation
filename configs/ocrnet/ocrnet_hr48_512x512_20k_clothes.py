# Copyright (c) 2019 Lightricks. All rights reserved.
_base_ = "./ocrnet_hr48_512x512_20k_voc12aug.py"
norm_cfg = dict(type="BN", requires_grad=True)
dataset_type = "ClothesDataset"
data_root = "/data"
ann_dir = ["mhp/LV-MHP-v2/masks"]
img_dir = ["mhp/LV-MHP-v2/images"]
model = dict(
    backbone=dict(norm_cfg=norm_cfg,),
    decode_head=[dict(norm_cfg=norm_cfg, num_classes=3,), dict(norm_cfg=norm_cfg, num_classes=3)],
)
data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
    train=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir=img_dir,
        ann_dir=ann_dir,
        split="LV-MHP-v2/splits/train.txt",
    ),
    val=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir=img_dir,
        ann_dir=ann_dir,
        split="LV-MHP-v2/splits/val.txt",
    ),
    test=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir=img_dir,
        ann_dir=ann_dir,
        split="LV-MHP-v2/splits/val.txt",
    ),
)
load_from = "/data/clothes_seg_args/pretrained_models/ocrnet_hr48_512x512_20k_voc12aug/ocrnet_hr48_512x512_20k_voc12aug_20200617_233932-9e82080a.pth"
work_dir = "/cnvrg/output/ocrnet_hr48_512x512_20k_mhp"
gpu_ids = range(1)
