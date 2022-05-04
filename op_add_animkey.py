import bpy
from bpy.types import Operator
from .define import *
from .op_util import *

class MIO3SK_AnimAddKey(Operator):
    bl_idname = "mio3sk.anim_add"
    bl_label = "Insert"
    bl_description = "Insert a Keyframe"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.type in OBJECT_TYPES

    def execute(self, context):
        shapekey = context.object.active_shape_key
        insert_key(shapekey, 'value')

        object = context.object
        prop_o = object.mio3sksync
        if is_sync_collection(object):
            key_blocks = object.data.shape_keys.key_blocks
            for item in [v for v in prop_o.syncs.objects if has_shapekey(v) and v != object]:
                for item_key in item.data.shape_keys.key_blocks:
                    if shapekey.name in key_blocks:
                        insert_key(item_key, 'value')

        refresh_ui_keyframes()
        return {"FINISHED"}
