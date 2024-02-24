from apt     import install_apt_apps
from deb     import install_debian_apps
from flatpak import install_flatpak_apps
from actions import finish_actions

def main():
    print('Linux post install script!\n')
    install_apt_apps()
    install_debian_apps()
    install_flatpak_apps()
    finish_actions()


if __name__ == '__main__':
    main()
