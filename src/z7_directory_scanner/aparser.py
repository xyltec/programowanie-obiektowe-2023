import argparse


def setup_arg_parser() -> argparse.Namespace:
    _parser = argparse.ArgumentParser()
    _parser.add_argument('--start_dir',
                         help='Actual start directory.',
                         type=str, required=True)

    _parser.add_argument('--workers',
                         help="Number of processes to launch in parallel.",
                         type=int, default=10)

    _parser.add_argument('--verbose', '-v', action='count', default=0)

    args = _parser.parse_args()
    if args.verbose == 1:
        # WARN is default
        print(1)
    elif args.verbose >= 2:
        print('>=2')

    return args


if __name__ == '__main__':
    args = setup_arg_parser()
    print(args.workers)
