import os
import maya.cmds as cmds
from importlib import reload
import grig.build.buildPart as gnPart

mp = 'D:/Repos/vfx-collections/MayaAutoRigging/assets/ray/model/ray_model.mb'
gp = 'D:/Repos/vfx-collections/MayaAutoRigging/assets/ray/guides/ray_guides.mb'

import grig.build.buildPart as gnPart
reload(gnPart)

cmds.file(new=True, f=True)
root = gnPart.build_module(module_type='root', side='Cn', part='root', global_shape='gnomon', model_path=mp, guide_path=gp)
cmds.viewFit('perspShape', fitFactor=1, all=True, animate=True)
hip = gnPart.build_module(module_type='hip', side='Cn', part='hip', guide_list=['Hips'], ctrl_scale=20, offset_hip=-0.5)
chest = gnPart.build_module(module_type='chest', side='Cn', part='chest', guide_list=['Spine2'], ctrl_scale=20)
spine = gnPart.build_module(module_type='spine', side='Cn', part='spine', guide_list=['Hips', 'Spine', 'Spine1', 'Spine2'], ctrl_scale=1)
neck = gnPart.build_module(module_type='neck', side='Cn', part='neck', guide_list=['Neck', 'Neck1', 'Head'], ctrl_scale=1)
head = gnPart.build_module(module_type='head', side='Cn', part='head', guide_list=['Head'], ctrl_scale=5)

for s in ['Lf', 'Rt']:
    if s == 'Lf':
        fs = 'Left'
    else:
        fs = 'Right'
    arm = gnPart.build_module(module_type='bipedLimb', side=s, part='arm', guide_list=[fs + 'Arm', fs + 'ForeArm', fs + 'Hand'], offset_pv=30, ctrl_scale=15)
    leg = gnPart.build_module(module_type='bipedLimb', side=s, part='leg', guide_list=[fs + 'UpLeg', fs + 'Leg', fs + 'Foot'], offset_pv=60, ctrl_scale=10)
    clav = gnPart.build_module(module_type='clavicle', side=s, part='clavicle', guide_list=[fs + 'Shoulder', fs + 'Arm'], local_orient=True, ctrl_scale=9)
    hand = gnPart.build_module(module_type='hand', side=s, part='hand', guide_list=[fs + 'Hand'], ctrl_scale=8)
    foot = gnPart.build_module(module_type='foot', side=s, part='foot', guide_list=[fs + 'Foot', fs + 'ToeBase', fs + 'Toe_End'], ctrl_scale=10, 
                               toe_piv=fs + 'ToePiv', heel_piv=fs + 'HeelPiv', in_piv=fs + 'In', out_piv=fs + 'Out')
    pinky = gnPart.build_module(module_type='finger', side=s, part='pinky', guide_list=[fs + 'HandPinky1', fs + 'HandPinky2', fs + 'HandPinky3', fs + 'HandPinky4'], ctrl_scale=2)
    ring = gnPart.build_module(module_type='finger', side=s, part='ring', guide_list=[fs + 'HandRing1', fs + 'HandRing2', fs + 'HandRing3', fs + 'HandRing4'], ctrl_scale=2)
    middle = gnPart.build_module(module_type='finger', side=s, part='middle', guide_list=[fs + 'HandMiddle1', fs + 'HandMiddle2', fs + 'HandMiddle3', fs + 'HandMiddle4'], ctrl_scale=2)
    index = gnPart.build_module(module_type='finger', side=s, part='index', guide_list=[fs + 'HandIndex1', fs + 'HandIndex2', fs + 'HandIndex3', fs + 'HandIndex4'], ctrl_scale=2)
    thumb = gnPart.build_module(module_type='finger', side=s, part='thumb', guide_list=[fs + 'HandThumb1', fs + 'HandThumb2', fs + 'HandThumb3', fs + 'HandThumb4'], ctrl_scale=2)



import grig.post.finalize as gnFinalize
import grig.post.dataIO.controls as ctrlIO
import grig.post.dataIO.weights as weightIO
reload(weightIO)
reload(gnFinalize)

gnFinalize.finalize_rig()

# read data
ctrlIO.read_controls('D:/Repos/vfx-collections/MayaAutoRigging/assets/ray/control_data/control_curves.json')
#weightIO.read_skin('D:/Repos/vfx-collections/MayaAutoRigging/assets/ray/weight_data/')

