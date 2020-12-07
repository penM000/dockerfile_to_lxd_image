import dockerfile
import pprint
import shlex
import pylxd

client = pylxd.Client()


def convert(filepath):
    for command in dockerfile.parse_file(filepath):
        if command.cmd == "from":
            from_command_lxd(command.value)

        elif command.cmd == "run":
            run_command_lxd(command.value)

        elif command.cmd == "copy":
            copy_command_lxd(command.value)

        elif command.cmd == "env":
            env_command_lxd(command.value)

        elif command.cmd == "volume":
            volume_command_lxd(command.value)

        elif command.cmd == "entrypoint":
            entrypoint_command_lxd(command.value)

        elif command.cmd == "cmd":
            cmd_command_lxd(command.value)

        else:
            print(command.cmd)


def from_command_lxd(value):
    pass
    # print(value[0])


def run_command_lxd(value):
    pass

    # print(shlex.split(value[0]))


def copy_command_lxd(value):
    pass
    # print(shlex.split(value[0]))


def env_command_lxd(value):
    pass
    # print(shlex.split(value[0]))


def volume_command_lxd(value):
    pass
    # print(shlex.split(value[0]))


def entrypoint_command_lxd(value):
    pass
    # print(shlex.split(value[0]))


def cmd_command_lxd(value):
    pass
    # print(shlex.split(value[0]))


if __name__ == "__main__":
    pass
    print(client.images.all())
    convert('./dockerfile_test')
