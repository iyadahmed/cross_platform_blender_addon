A template/example of a Blender addon that uses packages from pip, and can be packaged for different platforms

- run `package.py` script to create the addon zip under "out" directory,
this also installs requirements from `requirements.txt` into the addon itself (under a directory named "extern" inside the addon)
`site.addsitedir` is used in the addon's `__init__.py` to make bundled packages importable
you may want to install the same requirements in your Python environment to enable intellisense while developing your addon

- the package script will produce a ZIP that is tied to the OS and Python version that was used the run the script,
so the resultant ZIP will only work on Blender versions with same OS and Python version,
you can install different python versions using `conda` or any other method

- GitHub actions can be used to automate the release for different platforms (the repo includes such GitHub action)

it is a good idea to split resulting ZIP for each platform for two reasons:
1) It keeps the addon size smaller, especially if you are using large packages like SciPy
2) Installing pip packages for platforms different than running system is tricky, doable but not pretty

P.S Apple M1 hopefully will be supported by GitHub hosted runners soon <https://github.com/github/roadmap/issues/528>,
you can host a GitHub action runner on an Apple M1 that you have access to for the time being
