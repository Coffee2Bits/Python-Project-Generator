if sys.argv[0].endswith("__main__.py"):
    sys.argv[0] = "coffee"

if __name__ == "__main__":
    from aac import cli

    cli.run_cli()