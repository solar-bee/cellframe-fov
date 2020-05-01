import glob
import os.path
import shutil

from configmanager.backupnet import NetBackupManager


def _strip_config_names(cfg_file_list):
    clean_config_names = []
    for cfg_path in cfg_file_list:
        cfg_path_base = os.path.basename(cfg_path)
        cfg_item_pair = os.path.splitext(cfg_path_base)
        clean_config_names.append(cfg_item_pair[0])
    return clean_config_names


class NetworkListCreator:
    def __init__(self, node_structure):
        self.node_structure = node_structure

    def detect_active_configs(self):
        net_config_list = glob.glob(self.node_structure.network_path + "/*.cfg")
        clean_config_list = _strip_config_names(net_config_list)

        if clean_config_list:
            print("Active configs: " + str(clean_config_list))
        else:
            print("Error detecting current settings.")

        return clean_config_list


class NetConfigManager:
    def __init__(self, node_file_structure):
        self.node_file_structure = node_file_structure

    def backup(self, net_name):
        backup_manager = NetBackupManager(self.node_file_structure, net_name)
        backup_manager.backup()

    def restore(self, net_name):
        backup_manager = NetBackupManager(self.node_file_structure, net_name)
        backup_manager.restore()

    def clear_active_nets(self):
        print("Clearing active nets...")
        delete_file_list = [self.node_file_structure.script_defines_name, self.node_file_structure.etc_config_name]

        active_nets = glob.glob(self.node_file_structure.network_path + "/*.cfg")
        for net_file in active_nets:
            delete_file_list.append(net_file)

        for file in delete_file_list:
            try:
                os.remove(self.node_file_structure.script_defines_name)
            except FileNotFoundError:
                print("File " + file + " not found")

        self.clear_temp_files()

    def clear_temp_files(self):
        print("Clearing temp files...")
        for temp_dir in self.node_file_structure.files_to_clean:
            try:
                shutil.rmtree(temp_dir)
            except FileNotFoundError:
                print("Dir " + temp_dir + " not found")

    def clear_backup(self):
        """TODO:"""
