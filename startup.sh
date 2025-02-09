#!/bin/bash
set -e

echo "Installing dependencies..."
sudo apt-get update
sudo apt-get install -y wget curl unzip

echo "Installing Google Chrome..."
wget -q -O google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -y ./google-chrome.deb
rm google-chrome.deb

echo "Google Chrome installed successfully!"
