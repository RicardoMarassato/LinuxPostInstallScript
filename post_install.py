import os
import time


apt_apps_list = [
    'flameshot',
    'tmux',
    'qbittorrent',
    'vlc',
    'vim',
    'git',
    'docker.io',
    'neofetch',
    'virtualbox',
    'gparted',
    'filezilla',
    'remmina',
    'remmina-plugin-vnc',
    'clipit',
    'nodejs'
]


debian_apps_list = [
    'https://discord.com/api/download?platform=linux&format=deb',
    'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb',
    'https://guardiao.itau.com.br/warsaw/warsaw_setup_64.deb',
    'https://dbeaver.io/files/dbeaver-ce_latest_amd64.deb'
]


flatpak_apps_list = [
    'com.spotify.Client',
    'com.brave.Browser',
    'com.github.micahflee.torbrowser-launcher'
]


def install_apt_apps(apt_apps):
    print('Install apt apps:')
    print('Removing apt locks...')
    os.system('sudo rm -rf /var/lib/dpkg/lock-frontend')
    os.system('sudo rm -rf /var/cache/apt/archives/lock')
    print('Updating apt...')
    os.system('sudo apt-get update')
    print('Beggining installation...')
    for i in apt_apps:
        print(f'Installing -> {i}')
        os.system(f'sudo apt-get install -y {i}')
    print()


def install_debian_apps(debian_apps):
    print('Install debian apps:')
    print('Downloading packages...')
    try:
        os.mkdir('temp')
        for i in debian_apps:
            os.system(f'sudo wget {i} -P temp')
        print('Beggining installation...')
        os.system('sudo dpkg -i temp/*.deb')
    except OSError as err:
        print(err)


def install_flatpak_apps(flatpak_apps):
    print('Install flatpak apps:')
    print('Beggining installation...')
    try:
        for i in flatpak_apps:
            os.system(f'flatpak install -y -v flathub {i}')
    except OSError as err:
        print(err)


def finish_actions():
    print("Cleaning...")
    try:
        os.system("apt autoclean -y")
        os.system("apt autoremove -y")
        os.system("sudo rm -rf temp/")
        print("Execution finished!")
    except OSError as err:
        print(err)


def main():
    print('Linux post install script!\n')
    install_apt_apps(apt_apps_list)
    install_debian_apps(debian_apps_list)
    install_flatpak_apps(flatpak_apps_list)
    finish_actions()


if __name__ == '__main__':
    main()
