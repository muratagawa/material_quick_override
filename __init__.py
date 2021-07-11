import bpy
from bpy.types import Panel, Operator

bl_info = {
    "name": "Material Quick Override",
    "author": "Kei MURATAGAWA",
    "description": "Converts a material added by library override to a local material.",
    "blender": (2, 93, 0),
    "version": (0, 1, 0),
    "location": "Material Properties",
    "warning": "",
    "category": "Material",
    "wiki_url": "https://github.com/muratagawa/material_quick_override/",
    "tracker_url": "https://github.com/muratagawa/material_quick_override/issues",
}


class MQO_OT_override_single(Operator):
    bl_idname = "object.material_quick_override_single"
    bl_label = "Active Only"
    bl_description = "Make the active material local."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        index = context.object.active_material_index

        # Skip if not library linked material
        if context.object.material_slots[index].material.library is None:
            self.report({'INFO'}, "This material is not linked with library override. Skipped.")
            return {'FINISHED'}

        new_mat = context.object.active_material.copy()
        context.object.material_slots[index].link = 'OBJECT'
        context.object.material_slots[index].material = new_mat

        self.report({'INFO'}, "Material overwritten.")
        return {'FINISHED'}


class MQO_OT_override_all(Operator):
    bl_idname = "object.material_quick_override_all"
    bl_label = "All"
    bl_description = "Make all materials in list local."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for name, slot in context.object.material_slots.items():
            print(slot)

            # Skip if not library linked material
            if slot.material.library is None:
                self.report({'INFO'}, "'%s' is not linked with library override. Skipped." %(name))
                continue

            new_mat = slot.material.copy()
            slot.link = 'OBJECT'
            slot.material = new_mat

            self.report({'INFO'}, "Material '%s' overwritten." %(name))

        return {'FINISHED'}


class MQO_PT_override(Panel):
    """Creates a Panel in the Material properties window"""
    bl_label = "Material Quick Override"
    bl_idname = "MATERIAL_PT_quickmatoverride"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"
    bl_parent_id = "EEVEE_MATERIAL_PT_context_material"

    def draw(self, context):
        row = self.layout.row()
        row.operator(MQO_OT_override_single.bl_idname)
        row.operator(MQO_OT_override_all.bl_idname)


classes = (
    MQO_PT_override,
    MQO_OT_override_single,
    MQO_OT_override_all
)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
