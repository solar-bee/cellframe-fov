import os.path
from enum import Enum
from shutil import copyfile


class _BackupStyle(Enum):
    POSTFIX_NET_NAME = 0,
    POSTFIX_BAK = 1


def _backup_config_file(net_name, file_name, style):
    if not os.path.exists(file_name):
        print("Config file " + file_name + " does not exist")
        return

    file_name_bak = None
    if style == _BackupStyle.POSTFIX_NET_NAME:
        file_name_bak = file_name + "." + net_name
    elif style == _BackupStyle.POSTFIX_BAK:
        file_name_bak = file_name + ".bak"

    print("Making backup " + file_name + " -> " + file_name_bak)
    copyfile(file_name, file_name_bak)


def _restore_config_file(net_name, file_name, style):
    file_name_bak = None
    if style == _BackupStyle.POSTFIX_NET_NAME:
        file_name_bak = file_name + "." + net_name
    elif style == _BackupStyle.POSTFIX_BAK:
        file_name_bak = file_name + ".bak"

    if not os.path.exists(file_name_bak):
        print("Backup file " + file_name_bak + " does not exist")
        return

    print("Restoring backup " + file_name_bak + " -> " + file_name)
    copyfile(file_name_bak, file_name)


class NetBackupManager:
    def __init__(self, node_file_structure, net_name):
        self.net_name = net_name
        self.node_file_structure = node_file_structure

    def backup(self):
        self._backup_net_config()
        self._backup_etc_config()
        self._backup_script_defines()

    def _backup_net_config(self):
        net_config = os.path.join(self.node_file_structure.network_path, self.net_name + ".cfg")
        _backup_config_file(self.net_name, net_config, _BackupStyle.POSTFIX_BAK)

    def _backup_etc_config(self):
        _backup_config_file(self.net_name, self.node_file_structure.etc_config_name,
                            _BackupStyle.POSTFIX_NET_NAME)

    def _backup_script_defines(self):
        _backup_config_file(self.net_name, self.node_file_structure.script_defines_name,
                            _BackupStyle.POSTFIX_NET_NAME)

    def restore(self):
        self._restore_net_config()
        self._restore_etc_config()
        self._restore_script_defines()

    def _restore_net_config(self):
        net_config = os.path.join(self.node_file_structure.network_path, self.net_name + ".cfg")
        _restore_config_file(self.net_name, net_config, _BackupStyle.POSTFIX_BAK)

    def _restore_etc_config(self):
        _restore_config_file(self.net_name, self.node_file_structure.etc_config_name,
                             _BackupStyle.POSTFIX_NET_NAME)

    def _restore_script_defines(self):
        _restore_config_file(self.net_name, self.node_file_structure.script_defines_name,
                             _BackupStyle.POSTFIX_NET_NAME)
