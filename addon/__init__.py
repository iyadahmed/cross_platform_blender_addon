bl_info = {
    "name": "Cross Platform Addon Example",
    "description": "",
    "author": "Iyad Ahmed (iyadahmed430@gmail.com)",
    "version": (0, 0, 5),
    "blender": (3, 4, 1),
    "location": "",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Scripting",
}

import site
from pathlib import Path

# Add bundled packages directory to import search path
# NOTE: this path has to match the directory where the bundled packages are installed to,
# the path has to be under the addon directory of course
site.addsitedir((Path(__file__).parent / "extern").as_posix())

from scipy.version import version


def register():
    print("SciPy version:", version)


def unregister():
    pass


if __name__ == "__main__":
    register()
