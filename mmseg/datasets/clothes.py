# Copyright (c) 2019 Lightricks. All rights reserved.
import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class ClothesDataset(CustomDataset):
    CLASSES = ("background", "bottom", "top")
    PALETTE = [[128, 128, 128], [129, 127, 38], [120, 69, 125]]

    def __init__(self, split, **kwargs):
        super(ClothesDataset, self).__init__(
            img_suffix=".jpg", seg_map_suffix=".png", split=split, **kwargs
        )
        assert osp.exists(self.img_dir) and self.split is not None
