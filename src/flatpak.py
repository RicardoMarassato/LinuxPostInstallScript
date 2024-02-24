import os

flatpak_apps_list = [
    'com.spotify.Client',
    'com.brave.Browser',
    'com.github.micahflee.torbrowser-launcher'
]


def install_flatpak_apps():
    print('Install flatpak apps:')
    print('Beggining installation...')
    try:
        for i in flatpak_apps_list:
            os.system(f'flatpak install -y -v flathub {i}')
    except OSError as err:
        print(err)
