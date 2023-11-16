import subprocess
import sys

from xas_standards_backend import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "xas_standards_backend", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
