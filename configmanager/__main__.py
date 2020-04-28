import os.path
import argparse

from configmanager.filestructure import NodeFileStructure
from configmanager.netmanager import NetConfigManager

node_path = os.path.abspath("/opt/cellframe-node/")


def _process_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--action', help="performs specified action",
                        choices=['clean', 'backup', 'restore'], required=True)
    parser.add_argument('-n', '--network', help="specify network")

    return parser


def main():
    parser = _process_args()
    args = parser.parse_args()

    node_file_structure = NodeFileStructure(node_path)
    config_manager = NetConfigManager(node_file_structure)

    if args.action == 'clear':
        config_manager.clear_active_nets()
    elif args.action == 'backup':
        if args.network is None:
            raise ValueError("Error: net name is empty")
        config_manager.backup(args.network)
    elif args.action == 'restore':
        if args.network is None:
            raise ValueError("Error: net name is empty")
        config_manager.restore(args.network)


if __name__ == "__main__":
    main()


