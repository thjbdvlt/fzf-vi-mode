import configparser
import argparse
from string import ascii_letters, punctuation


def read_config():
    """read config file"""
    config = configparser.RawConfigParser()
    config.optionxform = str
    config.read("config")
    return config


def insert_mode(key, action):
    if action is None or action == "":
        suffix = ""
    else:
        suffix = f"+{action}"
    return f"{key}:enable-search+{unbind}{suffix}"


def parse_script_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-I",
        "--no-ignore",
        action="store_true",
        help="does not add '[key]:ignore' for ascii_letters not specified in config file.",
        default=False
    )
    parser.add_argument(
        "-o",
        "--output",
        action="store",
        help="filpath for output. default to ./export",
        default="./export",
    )
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_script_args()
    fp = args.output

    config = read_config()

    modes = config["mode"]
    bindings = config["normal"]

    bind_list = [f"{k}:{v}" for k, v in bindings.items()]
    insert_keys = [
        modes[i]
        for i in [
            "insert_before",
            "insert_after",
            "insert_end_line",
            "insert_beginning_line",
        ]
    ]

    keys = list(bindings.keys()) + insert_keys

    if args.no_ignore is False:
        signs = ascii_letters + "?!."
        ignored = [i for i in signs if i not in keys]
        ignored = set(signs).difference(keys)
        keys = set(keys)
        keys.update(signs)
        bind_ignored = [f"{i}:ignore" for i in ignored]
    else:
        ignored = []

    unbind = "unbind({})".format(",".join(keys))
    rebind = "rebind({})".format(",".join(keys))
    normal = "{}:disable-search+{}".format(modes["escape"], rebind)

    a = [
        ("start", None),
        (modes["insert_before"], None),
        (modes["insert_after"], "forward-char"),
        (modes["insert_end_line"], "end-of-line"),
        (modes["insert_beginning_line"], "beginning-of-line"),
    ]
    b = [insert_mode(i, j) for i, j in a]
    insert_bindings = [
        f"{k}:{v}" for k, v in config["insert"].items()
    ]
    allkeys = (
        bind_list + b + [normal] + insert_bindings + bind_ignored
    )

    with open(fp, "w") as f:
        f.write("--bind='{}'".format(",".join(allkeys)))
