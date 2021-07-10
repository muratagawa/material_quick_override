# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from bpy.types import Panel, Operator

bl_info = {
    "name": "Material Quick Override",
    "author": "Kei MURATAGAWA",
    "description": "",
    "blender": (2, 93, 0),
    "version": (0, 0, 1),
    "location": "Material Properties",
    "warning": "",
    "category": "Material"
    # "wiki_url": "https://github.com/muratagawa/dimensions-per-keyframe/",
    # "tracker_url": "https://github.com/muratagawa/dimensions-per-keyframe/issues",
}


class MQO_OT_override(Operator):
    bl_idname = "object.material_quick_override"
    bl_label = "Override Material"
    bl_description = "Override active material to be unique."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("Hello World")
        return {'FINISHED'}


class MQO_PT_override(Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Quick Material Override"
    bl_idname = "OBJECT_PT_quickmatoverride"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"
    bl_parent_id = "EEVEE_MATERIAL_PT_context_material"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator(MQO_OT_override.bl_idname)


# bpy.context.object.active_material_index = 0
# bpy.context.object.material_slots[1].link = 'OBJECT'
# bpy.ops.material.new()

# Skip if not library linked material
# bpy.data.materials["kosode"].is_library_indirect

# bpy.data.object["Tomoe.Body"].active_material_index

def register():
    bpy.utils.register_class(MQO_PT_override)
    bpy.utils.register_class(MQO_OT_override)


def unregister():
    bpy.utils.unregister_class(MQO_PT_override)
    bpy.utils.unregister_class(MQO_OT_override)


if __name__ == "__main__":
    register()
