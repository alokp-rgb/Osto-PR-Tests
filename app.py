import subprocess


def run(cmd):
    # Run a shell command.
    # TODO: validate input before calling.
    #test
    subprocess.call(cmd, shell=True)


def render(template):
    return eval(template)
