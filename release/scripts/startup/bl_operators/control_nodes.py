# SPDX-License-Identifier: GPL-2.0-or-later

import bpy
from bpy.types import Operator

from bpy.app.translations import pgettext_data as data_


def control_node_group_empty_new():
    group = bpy.data.node_groups.new(data_("Control Nodes"), 'ControlNodeTree')
    # CHRIS_TODO: NodeSocketControl what is it? Is it the socket type? Then it should be something like NodeSocketExecute
    print(data_("Control Nodes"))
    group.inputs.new('NodeSocketGeometry', data_("Control"))
    group.outputs.new('NodeSocketGeometry', data_("Control"))
    input_node = group.nodes.new('NodeGroupInput')
    output_node = group.nodes.new('NodeGroupOutput')
    output_node.is_active_output = True

    input_node.select = False
    output_node.select = False

    input_node.location.x = -200 - input_node.width
    output_node.location.x = 200

    group.links.new(output_node.inputs[0], input_node.outputs[0])

    return group


def control_modifier_poll(context):
    ob = context.object

    # Test object support for control node modifier
    if not ob or ob.type not in {'MESH', 'POINTCLOUD', 'VOLUME', 'CURVE', 'FONT', 'CURVES'}:
        return False

    return True


class NewControlNodesModifier(Operator):
    """Create a new modifier with a new control node group"""

    bl_idname = "node.new_control_nodes_modifier"
    bl_label = "New Control Node Modifier"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return control_modifier_poll(context)

    def execute(self, context):
        modifier = context.object.modifiers.new(data_("ControlNodes"), "CONTROLNODES")

        if not modifier:
            return {'CANCELLED'}

        group = control_node_group_empty_new()
        modifier.node_group = group

        return {'FINISHED'}


class NewControlNodeTreeAssign(Operator):
    """Create a new control node group and assign it to the active modifier"""

    bl_idname = "node.new_control_node_group_assign"
    bl_label = "Assign New Control Node Group"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return control_modifier_poll(context)

    def execute(self, context):
        if context.area.type == 'PROPERTIES':
            modifier = context.modifier
        else:
            modifier = context.object.modifiers.active

        if not modifier:
            return {'CANCELLED'}

        group = control_node_group_empty_new()
        modifier.node_group = group

        return {'FINISHED'}


classes = (
    NewControlNodesModifier,
    NewControlNodeTreeAssign,
)
