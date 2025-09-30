import maya.cmds as cmds

def create_primitive(prim_type):
    if prim_type == "cube":
        cmds.polyCube()
    elif prim_type == "sphere":
        cmds.polySphere()
    elif prim_type == "cone":
        cmds.polyCone()
    elif prim_type == "torus":
        cmds.polyTorus()
    elif prim_type == "cylinder":
        cmds.polyCylinder()
    else:
        cmds.warning(f"Unknown primitive type: {prim_type}")
>>>>>>> a904f29 (init repo)

