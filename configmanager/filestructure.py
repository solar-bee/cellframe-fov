import os.path
import shutil


class NodeFileStructure:
    def __init__(self, node_path):
        self.node_path = node_path

        self.files_to_clean = [os.path.join(node_path, "var/lib/global_db"),
                               os.path.join(node_path, "var/lib/network"),
                               os.path.join(node_path, "var/log")]
        self.files_to_backup = [os.path.join(node_path, "etc"),
                                os.path.join(node_path, "var"),
                                os.path.join(node_path, "share"),
                                os.path.join(node_path, "s/_defs.sh")
                                ]
        self.backup_ignore_pattern = shutil.ignore_patterns('node_cli')
        return
