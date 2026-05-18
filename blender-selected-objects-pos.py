import bpy
from os import path as p

selected_objects = bpy.context.selected_objects
output_path = p.join(p.expanduser("~/Desktop"), "objects-data-instanced.txt")

with open(output_path, "w") as output:
    output.write("Name , X , Y , Z, Material\n")

    for obj in selected_objects:
        output.write(f"{obj.active_material.name} , position='{obj.matrix_world.translation[0]}, {obj.matrix_world.translation[2]}, -{obj.matrix_world.translation[1]}' rotation='{obj.rotation_euler[0]},{obj.rotation_euler[2]},{-obj.rotation_euler[1]}'\n scale='{obj.dimensions[0]}, {obj.dimensions[2]}, {-obj.dimensions[1]}'\n")

print(f"Data exported to: {output_path}")