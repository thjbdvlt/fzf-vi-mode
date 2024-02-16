import configparser

config = configparser.RawConfigParser()
config.optionxform = str
config.read("config")

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
unbind = "unbind({})".format(",".join(keys))
rebind = "rebind({})".format(",".join(keys))
normal = "{}:disable-search+{}".format(modes["escape"], rebind)


def insert_mode(key, action):
    if action is None or action == "":
        suffix = ""
    else:
        suffix = f"+{action}"
    return f"{key}:enable-search+{unbind}{suffix}"


a = [
    ("start", None),
    (modes["insert_before"], None),
    (modes["insert_after"], "forward-char"),
    (modes["insert_end_line"], "end-of-line"),
    (modes["insert_beginning_line"], "beginning-of-line"),
]
b = [insert_mode(i, j) for i, j in a]
insert_bindings = [f"{k}:{v}" for k, v in config['insert'].items()]
allkeys = bind_list + b + [normal] + insert_bindings

with open('export', 'w') as f:
    f.write("--bind='{}'".format(",".join(allkeys)))
