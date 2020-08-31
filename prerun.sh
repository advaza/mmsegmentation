#!/usr/bin/env bash

apt-get update && apt-get install -y git libglib2.0-0 libsm6 libxrender-dev libxext6 libgl1-mesa-glx && apt-get clean  && rm -rf /var/lib/apt/lists/* && pip install -e . && pip install ipywidgets && jupyter nbextension enable --py widgetsnbextension


