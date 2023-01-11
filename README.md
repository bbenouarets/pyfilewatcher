![Logo](https://github.com/bbenouarets/pyfilewatcher/blob/main/.smartizer/logo.png?raw=true) 
<div style="font-size: 2.5em; text-align: center;">pyFileWatcher</div>

<div style="font-weight: light; text-align: center; margin-bottom: 40px;">A library for monitoring files and directories for changes</div>

The python package for monitoring files and directories provides a fast and efficient way to detect changes to files and directories. It is particularly small and resource-efficient, making it ideal for use in environments with limited resources.
The package is also easy to integrate and can be effortlessly incorporated into existing projects. It provides icomprehensive documentation to get you started.
Overall, our Python package for monitoring files and directories is a powerful and reliable choice for anyone who wants to monitor changes to files and directories.

![Download Badge](https://img.shields.io/github/downloads/bbenouarets/pyfilewatcher/total?style=for-the-badge) ![Last commit badge](https://img.shields.io/github/last-commit/bbenouarets/pyfilewatcher?color=%231BCBF2&style=for-the-badge) ![Issues Badges](https://img.shields.io/github/issues/bbenouarets/pyfilewatcher?style=for-the-badge)

## Installation

### pip

```bash
python3 -m pip install --user pyfilewatcher
```

### Manual

Download the folder from `https://github.com/bbenouarets/pyfilewatcher/tree/main/src/pyfilewatcher` and copy it into your project into the folder `modules`.
Then you can import the package via `from modules.pyfilewatcher import Observer`.

## Example

### pip installation

```python
from pyfilewatcher import Observer

locations = [
    "test"
]

observer = Observer()
observer.watch(locs=locations)
```

### Manual installation

```python
from modules.pyfilewatcher import Observer

locations = [
    "test"
]

observer = Observer()
observer.watch(locs=locations)
```

## Handler

- [x] Log file
- [x] MySQL database
- [ ] HTTP Endpoint (e.g. API)