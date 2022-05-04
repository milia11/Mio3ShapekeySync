import bpy
from .define import *


def is_sync_collection(obj):
    return obj.type in OBJECT_TYPES and obj.mio3sksync.syncs is not None

def has_shapekey(obj):
    return obj.type in OBJECT_TYPES and obj.active_shape_key is not None

def insert_key(data, key, group=None):
    try:
        if group is not None:
            data.keyframe_insert(key, group=group)
        else:
            data.keyframe_insert(key)
    except:
        pass

def refresh_ui_keyframes():
    try:
        for area in bpy.context.screen.areas:
            if area.type in ('TIMELINE', 'GRAPH_EDITOR', 'DOPESHEET_EDITOR'):
                area.tag_redraw()
    except:
        pass

def delete_key(data, key):
    try:
        data.keyframe_delete(key)
    except:
        pass