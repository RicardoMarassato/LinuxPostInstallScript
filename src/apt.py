import os

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


def install_apt_apps():
    print('Install apt apps:')
    print('Removing apt locks...')
    os.system('rm -rf /var/lib/dpkg/lock-frontend')
    os.system('rm -rf /var/cache/apt/archives/lock')
    print('Updating apt...')
    os.system('apt-get update')
    print('Beggining installation...')
    for i in apt_apps_list:
        print(f'Installing -> {i}')
        os.system(f'apt-get install -y {i}')
    print()
