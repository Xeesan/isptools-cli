# ⚡ ISP Tools (`isptools-cli`)

[![PyPI version](https://badge.fury.io/py/isptools-cli.svg)](https://badge.fury.io/py/isptools-cli)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A fast, interactive, and beautifully designed CLI utility tailored specifically for ISP Network Engineers. Built by Xeesan.

## ✨ Features

- **Interactive Menu UI**: No need to memorize commands! Just type `isptools` to launch the menu.
- **Subnet Calculator**: Instantly calculate network, broadcast, netmask, and usable IP ranges from any CIDR block.
- **MAC Vendor Lookup**: Quickly identify the hardware vendor (OUI) for any MAC address.
- **Public IP Checker**: Fetch your current WAN IP, ISP Name (ASN), and geolocation data.

---

## 🚀 Installation

You can install this tool globally on any OS (Windows, Linux, macOS) using `pip`:

```bash
pip install isptools-cli
```

### ⚠️ Troubleshooting Windows Installation

If you are on Windows and see a yellow warning like this during installation:
> *WARNING: The script isptools.exe is installed in 'C:\Users\...\Scripts' which is not on PATH.*

**How to fix it:**
1. Copy the folder path mentioned in the warning.
2. Search for **"Environment Variables"** in your Windows Start Menu.
3. Click "Edit the system environment variables" -> "Environment Variables" button.
4. Under "User variables", find `Path`, select it, and click Edit.
5. Click New, paste the folder path you copied, and hit OK.
6. **Restart your terminal.** You can now use the `isptools` command from anywhere!

---

## 💻 Usage

The fastest way to use the tool is via the interactive menu. Simply open your terminal and type:

```bash
isptools
```

This will launch the branded interactive menu where you can easily select tools by pressing `1`, `2`, or `3`.

### ⚡ Power User Commands

If you prefer to bypass the menu, you can pass arguments directly. This is great for scripting or rapid use:

```bash
# Calculate subnet details instantly
isptools subnet 192.168.1.0/24

# Look up a MAC address vendor directly
isptools mac D4:CA:6D:12:34:56

# Check your public IP and ISP info directly
isptools myip
```

## 🛠️ Upgrading

To grab the newest features in the future, just run:

```bash
pip install --upgrade isptools-cli
```
