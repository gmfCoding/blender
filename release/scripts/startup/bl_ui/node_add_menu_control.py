# SPDX-License-Identifier: GPL-2.0-or-later
import bpy
from bpy.types import Menu
from bl_ui import node_add_menu
from bpy.app.translations import pgettext_iface as iface_


class NODE_MT_category_CON_EXEC(Menu):
    bl_idname = "NODE_MT_category_CON_EXEC"
    bl_label = "Entry Points"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "ControlNodeFrameExec")
        node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_category_CON_GROUP(Menu):
    bl_idname = "NODE_MT_category_CON_GROUP"
    bl_label = "Group"

    def draw(self, context):
        layout = self.layout
        node_add_menu.draw_node_group_add_menu(context, layout)
        node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_category_CON_LAYOUT(Menu):
    bl_idname = "NODE_MT_category_CON_LAYOUT"
    bl_label = "Layout"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "NodeFrame")
        node_add_menu.add_node_type(layout, "NodeReroute")
        node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_control_node_add_all(Menu):
    bl_idname = "NODE_MT_control_node_add_all"
    bl_label = ""

    def draw(self, _context):
        layout = self.layout
        layout.menu("NODE_MT_category_CON_EXEC")
        layout.menu("NODE_MT_category_CON_GROUP")
        layout.menu("NODE_MT_category_CON_LAYOUT")
        node_add_menu.draw_root_assets(layout)


classes = (
    NODE_MT_control_node_add_all,
    NODE_MT_category_CON_EXEC,
    NODE_MT_category_CON_GROUP,
    NODE_MT_category_CON_LAYOUT,
)

if __name__ == "__main__":  # only for live edit.
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
