import os.path


class NodeFileStructure:
    def __init__(self, node_path):
        self.node_path = node_path
        self.scripts_path = os.path.join(node_path, "s")
        self.network_path = os.path.join(node_path, "etc/network")
        self.etc_config_name = os.path.join(node_path, "etc/cellframe-node.cfg")
        self.script_defines_name = os.path.join(self.scripts_path, "_defs.sh")

        self.temp_dirs = [os.path.join(node_path, "var/lib/global_db"),
                          os.path.join(node_path, "var/lib/network"),
                          os.path.join(node_path, "var/log")]
        return
