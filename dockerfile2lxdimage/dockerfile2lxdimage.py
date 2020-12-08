import dockerfile
import pprint
import shlex
import random
import string
import re
import sub.lxdcontroller as lxdcontroller


def randomname(n):
    randlst = [
        random.choice(
            string.ascii_letters) for i in range(n)]
    return ''.join(randlst)


def convert(filepath):
    entry_cmd = {"entrypoint": "", "cmd": ""}

    hostname = "building-" + randomname(10)
    for command in dockerfile.parse_file(filepath):
        if command.cmd == "from":
            pass
            #from_command_lxd(hostname, command.value)

        elif command.cmd == "run":
            pass
            #run_command_lxd(hostname, command.value)

        elif command.cmd == "copy":
            pass
            #copy_command_lxd(hostname, command.value)

        elif command.cmd == "env":
            pass
            #env_command_lxd(hostname, command.value)

        elif command.cmd == "volume":
            volume_command_lxd(hostname, command.value)

        elif command.cmd == "entrypoint":
            entry_cmd["entrypoint"] = command.value
            entry_cmd["entrypoint_json"] = command.json

        elif command.cmd == "cmd":
            entry_cmd["cmd"] = command.value
            entry_cmd["cmd_json"] = command.json

        else:
            print(command.cmd)
    lxdcontroller.stop_machine(hostname)
    lxdcontroller.delete_machine(hostname)

    make_startup_command(entry_cmd)


def from_command_lxd(hostname, value):
    image = "images:" + value[0].split(":")[0]
    try:
        image += "/" + value[0].split(":")[1]
    except BaseException:
        raise BaseException("バージョン(数字ベース)が指定されていません")
    if lxdcontroller.launch_machine(hostname, image):
        pass
    else:
        raise BaseException("FROMで指定できるのはディストリビューションとバージョン(数字ベース)のみです")
    lxdcontroller.network_test_machine(hostname)


def run_command_lxd(hostname, value):
    pass
    cmd = shlex.split(value[0])
    if lxdcontroller.exec_command(hostname, cmd):
        pass
    else:
        print(cmd)
        raise BaseException("起動失敗？")


def copy_command_lxd(hostname, value):
    pass
    try:
        lxdcontroller.copy_command(hostname, value[0], value[1])
    except BaseException:
        raise BaseException("COPYの記述エラー")


def env_command_lxd(hostname, value):
    pass
    #lxdcontroller.exec_command(hostname, ["printenv"])
    lxdcontroller.exec_command(
        hostname, [
            "\"echo " + value[0] + "=" + value[1] + ">>" + "/etc/profile\""])
    #lxdcontroller.exec_command(hostname, ["printenv"])
    print((value))


def volume_command_lxd(hostname, value):
    pass
    # print(shlex.split(value[0]))


def make_startup_command(value):
    print(value)
    command = ""
    if value["entrypoint"] == "":
        pass
    elif value["entrypoint_json"]:
        for i in value["entrypoint"]:
            command += i + " "
    else:
        command += "/bin/sh -c " + value["entrypoint"][0] + " "

    if value["cmd"] == "":
        pass
    elif value["cmd_json"]:
        for i in value["cmd"]:
            command += i + " "
        pass
    else:
        command += "/bin/sh -c " + value["cmd"][0] + " "
    print(command)
    pass


if __name__ == "__main__":
    pass

    convert('./dockerfile_test')
