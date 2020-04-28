import shutil
import os

node_path = os.path.abspath("/opt/cellframe-node/")
destination_dir = "cellframe-fov"
destination_path = os.path.join(node_path, destination_dir)
deploy_module_list = ['configmanager']

print("Target path: " + destination_path)
for module in deploy_module_list:
    print("Deploying " + module + "...")
    module_path = os.path.join(destination_path, module)
    try:
        shutil.rmtree(module_path)
    except FileNotFoundError:
        pass

    shutil.copytree(module, module_path)
