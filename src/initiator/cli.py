import argparse


def run_cli():
    arg_parser = setup_argparser()
    args = arg_parser.parse_args()
    args_dict = vars(args)

    print(args_dict)
    gen_cli = args_dict.get("cli")
 

def setup_argparser():

    parser = argparse.ArgumentParser(description='Keep your computer awake.')
    parser.add_argument('--cli', type=bool, default=True,
                    help='Number of seconds between keep-alive actions')

    args = parser.parse_args()

    return parser