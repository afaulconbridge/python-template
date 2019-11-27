import argparse
import logging

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-config', type=str, help='log configuration file')
    parser.add_argument('--log-level', type=str, help='log level')
    #convert parsed arguments into a dictionary
    args = vars(parser.parse_args())

    if 'log-config' in args and args['log-config'] is not None:
        logging.config.fileConfig(args['log-config'])
        logging.debug("Loaded config {}".format(args['log-config']))

    if 'log-level' in args and args['log-level'] is not None:
        logging.getLogger().setLevel(args['log-level'])
        logging.debug("Set log level to {}".format(args['log-level']))

    # TODO finish


if __name__ == "__main__":
    main()
