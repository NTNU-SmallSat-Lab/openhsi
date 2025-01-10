import os
from openhsi.capture import *
from openhsi.cameras import IDSCamera

json_path= '/home/ubuntu/Documents/openhsi/nbs/assets/cam_settings_ids.json'
with IDSCamera(n_lines=5, 
                 processing_lvl = -1,
                 json_path = json_path) as cam:
    cam.collect()
    
    fig = cam.show(hist_eq=True)
    
