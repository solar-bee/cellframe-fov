import os.path
import shutil

def _entirely_replace_dir(src, dest, ignore_pat):
    if not os.path.exists(src):
        print("Source file/dir " + src + " does not exist")
        return

    if os.path.exists(dest):
        if os.path.isdir(dest):
            print(f"Removing old backup dir {dest}...")
            shutil.rmtree(dest)
        else:
            print(f"Removing old backup file {dest}...")
            os.remove(dest)

    print(f"Making backup {src} -> {dest}...")

    if os.path.isdir(src):
        shutil.copytree(src, dest, ignore=ignore_pat)
    else:
        shutil.copyfile(src, dest)


class NetBackupManager:
    def __init__(self, node_file_structure, net_name):
        self.net_name = net_name
        self.node_file_structure = node_file_structure

    def backup(self):
        print(f"Making backup for net {self.net_name}")
        for entity in self.node_file_structure.files_to_backup:
            file_name_bak = entity + "." + self.net_name
            _entirely_replace_dir(entity, file_name_bak, ignore_pat=self.node_file_structure.backup_ignore_pattern)

    def restore(self):
        print(f"Restoring backup for net {self.net_name}")
        for entity in self.node_file_structure.files_to_backup:
            file_name_bak = entity + "." + self.net_name
            _entirely_replace_dir(file_name_bak, entity, ignore_pat=None)
