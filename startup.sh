#!/bin/bash
set -e

echo "Installing dependencies..."
sudo apt-get update
sudo apt-get install -y wget curl unzip

echo "Installing Google Chrome..."
wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i /tmp/chrome.deb || sudo apt-get -fy install
rm /tmp/chrome.deb

echo "Verifying Chrome installation..."
if command -v google-chrome-stable; then
    echo "Chrome installed successfully!"
else
    echo "Chrome installation failed!"
    exit 1
fi
