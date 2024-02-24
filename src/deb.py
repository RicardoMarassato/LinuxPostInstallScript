import os

debian_apps_list = [
    'https://discord.com/api/download?platform=linux&format=deb',
    'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb',
    'https://guardiao.itau.com.br/warsaw/warsaw_setup_64.deb',
    'https://dbeaver.io/files/dbeaver-ce_latest_amd64.deb'
]


def install_debian_apps():
    print('Install debian apps:')
    print('Downloading packages...')
    try:
        os.mkdir('temp')
        for i in debian_apps_list:
            os.system(f'wget {i} -P temp')
        print('Beggining installation...')
        os.system('dpkg -i temp/*.deb')
    except OSError as err:
        print(err)
