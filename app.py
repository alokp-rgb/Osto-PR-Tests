import subprocess


def run(cmd):
    # Run a shell command.
    # TODO: validate input before calling.
    subprocess.call(cmd, shell=True)
