import subprocess as sp
from pathlib import Path
from shutil import copytree, rmtree, make_archive
from platform import platform, python_version

PARENT_DIR = Path(__file__).parent

# Delete existing "out" directory
rmtree(PARENT_DIR / "out")

# Copy source addon folder to a subdirectory of "out" directory,
# we copy to a subdirectory because it makes it easier later to ZIP the addon,
# and keep the addon directory in the ZIP (so it gets unzipped correctly by Blender)
copytree(PARENT_DIR / "addon", PARENT_DIR / "out" / "package" / "addon")

# Install requirements to location expected by addon
sp.run(["pip",
        "install",
        "-r",
        PARENT_DIR / "requirements.txt",
        "-t",
        PARENT_DIR / "out" / "package" / "addon" / "extern"])

# Create addon ZIP
zip_filename = f"addon-Python-{python_version()}-{platform()}"
zip_filepath = (PARENT_DIR / "out" / zip_filename).as_posix()
make_archive(zip_filepath, "zip", root_dir=PARENT_DIR / "out" / "package")
