import pylxd
import subprocess
import sys

client = pylxd.Client()


def exec_shell_command(cmd, log=True):
    proc = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    try:
        while True:
            # バッファから1行読み込む.
            line = proc.stdout.readline()
            if log:
                sys.stdout.write(line.decode('utf-8'))

            # バッファが空 + プロセス終了.
            if not line and proc.poll() is not None:
                break
    except BaseException:
        pass

    proc.kill()
    return proc.returncode


def launch_machine(hostname, image):
    temp = ["lxc", "launch", image, hostname]
    if exec_shell_command(" ".join(temp)) == 0:
        return True
    else:
        return False


def network_test_machine(hostname):
    print("Network Waiting...")
    for i in range(100):
        temp = ["lxc", "exec", hostname, "--"] + ["ping", "-c", "1", "8.8.8.8"]
        if exec_shell_command(" ".join(temp), log=False) == 0:
            print("Network Available!")
            return True
    print("Network Not available")
    return False


def stop_machine(hostname):
    temp = ["lxc", "stop", hostname]
    if exec_shell_command(" ".join(temp)) == 0:
        return True
    else:
        return False


def delete_machine(hostname):
    temp = ["lxc", "delete", hostname]
    if exec_shell_command(" ".join(temp)) == 0:
        return True
    else:
        return False


def exec_command(hostname, cmd):

    if exec_container_command(hostname, cmd, log=True) == 0:
        return True
    else:
        return False


def copy_command(hostname, source, dist):
    temp = ["lxc", "file", "push", source, hostname + "/" + dist]
    if exec_shell_command(" ".join(temp)) == 0:
        return True
    else:
        return False


def get_machine(hostname):
    machine = None
    try:
        machine = client.containers.get(hostname)
    except pylxd.exceptions.NotFound:
        pass
    try:
        machine = client.virtual_machines.get(hostname)
    except pylxd.exceptions.NotFound:
        pass
    return machine


def exec_container_command(hostname, cmd, log=True):
    machine = get_machine(hostname)
    if machine is None:
        raise Exception("マシンが見つかりません")

    proc = machine.execute(cmd)
    sys.stdout.write(proc[1])
    return proc[0]
