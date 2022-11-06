/* SPDX-License-Identifier: GPL-2.0-or-later */

#include "BKE_mesh.h"

#include "UI_interface.h"
#include "UI_resources.h"

#include "node_control_util.hh"

namespace blender::nodes::node_con_every_frame_cc {
NODE_STORAGE_FUNCS(NodeControlFrameExec)
static void node_declare(NodeDeclarationBuilder &b)
{
  b.add_output<decl::Int>(N_("FrameExec"));
}

}  // namespace blender::nodes::node_con_every_frame_cc

void register_node_type_con_every_frame()
{
  namespace file_ns = blender::nodes::node_con_every_frame_cc;

  static bNodeType ntype;
  //NODE_CLASS_ATTRIBUTE
  con_node_type_base(&ntype, CON_NODE_FRAME_EXEC, "FrameExec", NODE_CLASS_CONTROL);
  ntype.declare = file_ns::node_declare;

  nodeRegisterType(&ntype);
}
