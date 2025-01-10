import os
from openhsi.capture import *
from openhsi.cameras import IDSCamera
import time

json_path= '/home/ubuntu/Documents/openhsi/capture_continuous_ids_settings.json'

    
with IDSCamera(n_lines=10, 
        processing_lvl = -1,
        json_path = json_path) as cam:
        cam.collect()


#cam.save(save_dir="/home/ubuntu/OpenHSIcubes")
# Define the bands for RGB channels (adjust indices based on your wavelength calibration)
rgb_bands = {
    'r': 30,  # Index for the red channel
    'g': 20,  # Index for the green channel
    'b': 10   # Index for the blue channel
}


cam.save(
    save_dir="/home/ubuntu/OpenHSIcubes",
    prefix='experiment1_',
    #rgb_bands=rgb_bands,
    #robust=True
)
fig = cam.show(plot_lib="matplotlib", robust=True)

