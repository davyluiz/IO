import os


def get_directory():
    SYSTEM_DRIVE = os.environ['SYSTEMDRIVE']
    PC_NAME = os.environ['COMPUTERNAME']
    USER_PATH = os.path.expanduser('~')
    CURRENT_PATH = os.getcwd()

    print(f"Letra do disco do sistema: {SYSTEM_DRIVE}")
    print(f"Nome da máquina: {PC_NAME}")
    print(f"Diretório do usuário: {USER_PATH}")
    print(f"Diretório atual: {CURRENT_PATH}")


def inicialize():
    pass


if __name__ == '__main__':
    get_directory()
