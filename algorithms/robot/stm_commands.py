from typing import List

from path_finding.hybrid_astar import Node
from common.consts import (
    TURNING_RADIUS, 
    DIST_BL,
    DIST_BR,
    DIST_FL,
    DIST_FR
)


def backtracking_smooth_path(
    path: List["Node"]
) -> List[str]:
    if not path:
        return []
    
    merged = []
    for node in path[1:]:
        if not node.d:
            continue
        if merged and can_merge_nodes(merged[-1], node):
            merged[-1].d += node.d
        else:
            merged.append(node.clone())
    return convert_segments_to_commands(merged)        


def _backtracking_smooth_path(
    path: List["Node"]
) -> List[str]:
    if not path:
        return []

    # Initialize the list of contiguous segments of smooth motion
    smooth_segments = []
    # current_segment = []

    # Iterate through the path nodes and group them into segments
    
    current_node = path[-1]

    while current_node.parent:
        prev_node = current_node.parent

        # Check if the current node can be added to the current segment
        if can_merge_nodes(prev_node, current_node):
            current_node.pos = prev_node.pos
            current_node.c_pos = prev_node.c_pos
            current_node.parent = prev_node.parent
    # TODO: Confirm that the node.g is the cost to travel from starting point to node and not from parent node to child node
    # TODO: Do I need to edit the costs of the nodes?
            # current_node.g = prev_node.g
            current_node.d += prev_node.d
        else:
            # If not, start a new segment
            smooth_segments.append(current_node)
            current_node = prev_node

    # Add the last segment to the list
    smooth_segments.append(current_node)

    # Convert segments to motion commands
    motion_commands = convert_segments_to_commands(smooth_segments[::-1])

    return motion_commands

def can_merge_nodes(
    parentNode: Node,
    childNode: Node
) -> bool:
    if not parentNode:
        return False
    # if childNode.v != parentNode.v:
    #     return False
    if childNode.v == parentNode.v and childNode.s == 0 and parentNode.s == 0:
        return True
    return False
    

def convert_segments_to_commands(
    segments: List["Node"]
) -> List[str]:
    
    result = []

    # for segment in segments:
    #     if segment.v == 1:
    #         if segment.s == -1:
    #             result.append("FL"+"{:06.2f}".format((segment.d / (2*DIST_FL[2])) * 180))
    #         elif segment.s == 0:
    #             result.append("FW"+ "{:06.2f}".format(segment.d))
    #         elif segment.s == 1:
    #             result.append("FR"+"{:06.2f}".format((segment.d / (2*DIST_FR[2])) * 180))
    #     elif segment.v == -1:
    #         if segment.s == -1:
    #             result.append("BL"+"{:06.2f}".format((segment.d / (2*DIST_BL[2])) * 180))
    #         elif segment.s == 0:
    #             result.append("BW"+ "{:06.2f}".format(segment.d))
    #         elif segment.s == 1:
    #             result.append("BR"+"{:06.2f}".format((segment.d / (2*DIST_BR[2])) * 180))
    for segment in segments:
        if segment.v == 1:
            if segment.s == -1:
                result.append("left,82,forward,0")
            elif segment.s == 0:
                result.append("center,0,forward," + str(int(segment.d)))
            elif segment.s == 1:
                result.append("right,100,forward,0")
        elif segment.v == -1:
            if segment.s == -1:
                result.append("left,72,reverse,0")
            elif segment.s == 0:
                result.append("center,0,reverse,"+ str(int(segment.d)))
            elif segment.s == 1:
                result.append("right,105,reverse,0")

    resultcombined = []
    n = 0
    for i in range(len(result)):
        string = result[i].split(',')
        if i == 0:
            resultcombined.append(result[i])
            n = 0
        elif string[0] != "center":
            resultcombined.append(result[i])
            n += 1
        else:
            prevstr = resultcombined[n].split(',')
            if string[0] == prevstr[0] and string[2] == prevstr[2]:
                new = string[0]+','+string[1]+','+string[2]+','+str(int(string[3])+int(prevstr[3]))
                resultcombined[n] = new
            else:
                resultcombined.append(result[i])
                n += 1


    return resultcombined


def merge_cmds(cmds: List[List[str]]) -> str:
    s = ''
    for i, seg in enumerate(cmds):
        if not seg:
            continue
        s += ','.join(seg) + '-'

    return s.strip('-')