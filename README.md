Prerequisites
It is assumed that you are running tests on the Linux operating system.

Possible options includes:

Linux desktop (Mint Cinnamon recommended)
Windows 10/11 + WSL
Windows 10/11 + Virtual machine
Mac OS


WSL setup on Windows
Installation process https://pureinfotech.com/install-windows-subsystem-linux-2-windows-10/
X-server setup to run tests in browser GUI https://gist.github.com/KirillY/bc4253edfd62b27c452d01595d19efce After x-server is set, you might also need to enable AUT_IS_INSIDE_WSL environment variable or similar to set DISPLAY


Installing the necessary libraries

pip install selenium

pip install -U pytest

pip install Faker

pip install requests


Creating a docker image


docker build -t diplom_sergei_klimenkov:local .

Launching the created docker image


docker run diplom_sergei_klimenkov:local /bin/bash -c --reruns 5 "poetry run python -m pytest"
