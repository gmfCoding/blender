/* SPDX-License-Identifier: GPL-2.0-or-later */

#pragma once


#include "BKE_node.h"

#ifdef __cplusplus
extern "C" {
#endif


extern struct bNodeTreeType *ntreeType_Control;

void register_node_tree_type_con(void);

void register_node_type_con_group(void);
void register_node_type_con_custom_group(bNodeType *ntype);

void register_node_type_con_every_frame(void);

#ifdef __cplusplus
}
#endif
