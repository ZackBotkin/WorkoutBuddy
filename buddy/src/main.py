import argparse
from buddy.config.config import Configs
from buddy.src.io.query_runner import QueryRunner
from buddy.src.interactive.main_menu import MainMenu
from buddy.src.context_manager import ContextManager

def main():

    parser = argparse.ArgumentParser(description= 'default parser')
    parser.add_argument('--config_file', help='the configuration file')
    args = parser.parse_args()

    configs = Configs(args.config_file)

    if configs.get('create_tables_on_start') == True:
        QueryRunner(configs).create_tables()

    context_manager = ContextManager(configs)
    main_menu = MainMenu(context_manager)

    main_menu.main_loop()


if __name__ == '__main__':
    main()
