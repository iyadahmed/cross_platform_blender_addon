import subprocess as sp
from pathlib import Path
from platform import platform, python_version
from shutil import copytree, rmtree, make_archive

PARENT_DIR = Path(__file__).parent
OUT_DIR = PARENT_DIR / "out"

# Delete existing "out" directory
if OUT_DIR.exists():
    if OUT_DIR.is_dir():
        rmtree(PARENT_DIR / "out")
    else:
        raise RuntimeError("Output directory exists and it is not a directory, please remove it manually")

# Copy source addon folder to a subdirectory of "out" directory,
# we copy to a subdirectory because it makes it easier later to ZIP the addon,
# and keep the addon directory in the ZIP (so it gets unzipped correctly by Blender)
copytree(PARENT_DIR / "addon", OUT_DIR / "package" / "addon")

# Install requirements to location expected by addon
sp.run(["pip",
        "install",
        "-r",
        PARENT_DIR / "requirements.txt",
        "-t",
        OUT_DIR / "package" / "addon" / "extern"])

# Create addon ZIP
zip_filename = f"addon-Python-{python_version()}-{platform()}"
zip_filepath = (OUT_DIR / zip_filename).as_posix()
make_archive(zip_filepath, "zip", root_dir=OUT_DIR / "package")
