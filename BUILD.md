# How build game?

## Python

Setup **PyInstaller** for build to executable file.

```bash
pip3 install pyinstaller        # Default
sudo pip3 install pypyinstaller # For sudo
```

## Optimization

You can remove unnecessary elements from the engine before compilation to make it lighter, for example, folders such as **icons**.

## Libraries

Downolad binary for your OS [glfw](https://www.glfw.org/download.html)

## Compiling

```bash
# With console:
pyinstaller --noconfirm --onedir --console --name "YOUR PROJECT NAME"  "YOUR PYTHON FILE PATH"
# Without console
pyinstaller --noconfirm --onedir --windowed --name "YOUR PROJECT NAME"  "YOUR PYTHON FILE PATH"
```

## End steps

Place the binary file you downloaded into the folder containing the executable file, and you're ready to use it.
