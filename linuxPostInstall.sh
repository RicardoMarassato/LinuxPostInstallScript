#!/usr/bin/env bash

exec_start=`date +%s`

URL_GOOGLE_CHROME="https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
URL_INSOMNIA="https://updates.insomnia.rest/downloads/ubuntu/latest?&app=com.insomnia.app&source=website"
URL_DBEAVER="https://dbeaver.io/files/dbeaver-ce_latest_amd64.deb"
URL_VSCODE="https://code.visualstudio.com/docs/?dv=linux64_deb"
URL_MINECRAFT="https://launcher.mojang.com/download/Minecraft.deb"
URL_DISCORD="https://discord.com/api/download?platform=linux&format=deb"
URL_WARSAW="https://guardiao.itau.com.br/warsaw/warsaw_setup_64.deb"
URL_TEAMS="https://go.microsoft.com/fwlink/p/?LinkID=2112886&clcid=0x416&culture=pt-br&country=BR"
URL_ARDUINO="https://downloads.arduino.cc/arduino-1.8.13-linux64.tar.xz"
URL_JMETER="https://downloads.apache.org//jmeter/binaries/apache-jmeter-5.4.1.tgz"
URL_NETEXTENDER="https://software.sonicwall.com/NetExtender/NetExtender.Linux-10.2.824.x86_64.tgz"

APPS_PATH="$HOME/Downloads/apps"

APT_APPS=(
	git
  nodejs
	openjdk-14-jre-headless
	gimp
	vlc
	gnome-tweaks
	clipit
	notepadqq
	snapd
	flatpak
  virtualbox
	filezilla
  flameshot
	vim
	neofetch
	gparted
	qbittorrent
	remmina
	remmina-plugin-vnc
)

echo "Execution started!"
echo
echo "Removing apt locks"
sudo rm /var/lib/dpkg/lock-frontend
sudo rm /var/cache/apt/archives/lock
echo

echo "Updating apt"
sudo apt update -y
echo

echo "Downloading external apps"
mkdir 	"$APPS_PATH"
wget -c "$URL_GOOGLE_CHROME"     -P "$APPS_PATH"
wget -c "$URL_INSOMNIA"          -P "$APPS_PATH"
wget -c "$URL_DBEAVER"         	 -P "$APPS_PATH"
wget -c "$URL_VSCODE"         	 -P "$APPS_PATH"
wget -c "$URL_MINECRAFT"         -P "$APPS_PATH"
wget -c "$URL_DISCORD"         	 -P "$APPS_PATH"
wget -c "$URL_WARSAW"         	 -P "$APPS_PATH"
wget -c "$URL_TEAMS"         	   -P "$APPS_PATH"
wget -c "$URL_ARDUINO"         	 -P "$APPS_PATH"
wget -c "$URL_JMETER"         	 -P "$APPS_PATH"
wget -c "$URL_NETEXTENDER"       -P "$APPS_PATH"
echo

echo "Installing downloaded .deb apps"
sudo dpkg -i $APPS_PATH/*.deb
echo

echo "Extracting downloaded compacted files"
sudo tar -xvf $APPS_PATH/*.tar.xz
sudo tar -xvf $APPS_PATH/*.tgz
echo

echo "Installing apt apps"
for app_name in ${APT_APPS[@]}; do
  if ! dpkg -l | grep -q $app_name; then
    apt install "$app_name" -y
  else
    echo "Installed -> $app_name"
  fi
done
echo

echo "Configuring GIT"
echo "Please type git user.name and press Enter to continue"
read git_user_name
echo "Please type git user.email and press Enter to continue"
read git_user_email
git config --global user.name "$git_user_name"
git config --global user.email $git_user_email
git config --global core.editor "vim"
echo "GIT configured"
echo

echo "Flatpak apps installation"
sudo apt install gnome-software-plugin-flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub com.obsproject.Studio -y
flatpak install flathub org.kde.kdenlive -y
echo

echo "Snap apps installation"
sudo snap install spotify
sudo snap install telegram-desktop
echo

echo "Finishing installation and cleaning"
sudo apt update && sudo apt dist-upgrade -y
flatpak update
sudo apt autoclean
sudo apt autoremove -y
echo

echo "Execution finished!"
exec_end=`date +%s`
runtime=$((exec_end-exec_start))
echo "Execution time $runtime seconds"
echo

echo "Do you wish to reboot your system now?"
read -p "Continue? (Y/N): " user_answer && [[ $user_answer == [yY] ]] || exit 1
echo "Rebooting system!"
reboot
