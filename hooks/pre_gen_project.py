import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_error(message):
    print(bcolors.FAIL + message + bcolors.END)

if __name__ == "__main__":
    extras_example = '{{ cookiecutter.extras_example }}' == "True"
    extras_app = '{{ cookiecutter.extras_app }}' == "True"
    bootstrap = '{{ cookiecutter.bootstrap }}' == "True"
    login_required_middleware = '{{ cookiecutter.login_required_middleware }}' == "True"
    custom_accounts = '{{ cookiecutter.custom_accounts }}' == "True"

    if(extras_app and not bootstrap):
        print_error("You cannot use extras_app without bootstrap")
        sys.exit(1)

    if(extras_example and not extras_app):
        print_error("You cannot use extras_example without extras_app")
        sys.exit(1)

    if(login_required_middleware and not custom_accounts):
        print_error("You cannot use login_required_middleware without custom_accounts")
        sys.exit(1)