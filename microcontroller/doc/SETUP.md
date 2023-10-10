# OS, Wireless & Library Setup

## Getting Started

We will be working on this together!
<br>

### 1. Installing OS

- Format the Micro SD card to FAT32 format to be compatible with Raspberry Pi 4 Model B.

  - For Mac OS, use the disk utility to erase the card and rename it 'boot'. <br>

- Head over to [Raspberry Pi Official Website](https://www.raspberrypi.com/software/operating-systems/) and download **Raspberry Pi OS Lite** and its imager **Raspberry Pi Imager**.
  - Use the Raspberry Pi Imager to flash the Micro SD card with our downloaded Raspberry Pi OS Lite

### 2. Wireless Setup (Headless Mode)

- Create a file named `wpa_supplicant.conf` and copy the code

```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="wifi name"
    psk="wifi password"
}
```

- Create a file named `ssh` with **no** extension and leave it blank. This will enable SSH on Raspberry Pi.
- Move both `wpa_supplicant.conf` and `ssh` to MicroSD card 'boot'.

### 3. Python Installation
