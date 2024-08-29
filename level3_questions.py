level3_questions = [
    {
        "question": "Which command is used to update the package list on Ubuntu?",
        "options": ["sudo apt update", "sudo apt upgrade", "sudo apt install"],
        "answer": "sudo apt update",
        "explanation": "The 'sudo apt update' command updates the package list from the repositories. It ensures that you have the latest information about available packages."
    },
    {
        "question": "How do you upgrade all installed packages to their latest versions on Ubuntu?",
        "options": ["sudo apt upgrade", "sudo apt update", "sudo apt dist-upgrade"],
        "answer": "sudo apt upgrade",
        "explanation": "The 'sudo apt upgrade' command upgrades all installed packages to their latest versions. It installs new versions of packages but does not remove any packages."
    },
    {
        "question": "Which command is used to install a new package on Ubuntu?",
        "options": ["sudo apt install package_name", "sudo apt-get install package_name", "sudo dpkg -i package_name"],
        "answer": "sudo apt install package_name",
        "explanation": "The 'sudo apt install package_name' command installs a new package. It resolves and installs any dependencies required by the package."
    },
    {
        "question": "How do you remove a package and its configuration files on Ubuntu?",
        "options": ["sudo apt purge package_name", "sudo apt remove package_name", "sudo dpkg -r package_name"],
        "answer": "sudo apt purge package_name",
        "explanation": "The 'sudo apt purge package_name' command removes a package along with its configuration files. Use 'sudo apt remove package_name' to remove a package but keep its configuration files."
    },
    {
        "question": "Which command is used to search for a package in the repositories on Ubuntu?",
        "options": ["apt search package_name", "apt-cache search package_name", "dpkg -l package_name"],
        "answer": "apt search package_name",
        "explanation": "The 'apt search package_name' command searches for a package in the repositories. It provides a list of matching packages along with their descriptions."
    },
    {
        "question": "How do you display detailed information about a package on Ubuntu?",
        "options": ["apt show package_name", "apt-cache show package_name", "dpkg -s package_name"],
        "answer": "apt show package_name",
        "explanation": "The 'apt show package_name' command displays detailed information about a package, including its description, dependencies, and version."
    },
    {
        "question": "Which command is used to fix broken dependencies on Ubuntu?",
        "options": ["sudo apt --fix-broken install", "sudo dpkg --configure -a", "sudo apt-get autoremove"],
        "answer": "sudo apt --fix-broken install",
        "explanation": "The 'sudo apt --fix-broken install' command fixes broken dependencies. It installs any missing dependencies required by installed packages."
    },
    {
        "question": "How do you list all installed packages on Ubuntu?",
        "options": ["dpkg -l", "apt list --installed", "apt-cache pkgnames"],
        "answer": "dpkg -l",
        "explanation": "The 'dpkg -l' command lists all installed packages. It provides a detailed list of packages along with their versions and descriptions."
    },
    {
        "question": "Which command is used to upgrade the distribution to a new release on Ubuntu?",
        "options": ["sudo do-release-upgrade", "sudo apt dist-upgrade", "sudo apt upgrade"],
        "answer": "sudo do-release-upgrade",
        "explanation": "The 'sudo do-release-upgrade' command upgrades the distribution to a new release. It handles the entire upgrade process, including updating the package list and installing new packages."
    },
    {
        "question": "How do you open the nano text editor to edit a file?",
        "options": ["nano filename", "vim filename", "gedit filename"],
        "answer": "nano filename",
        "explanation": "The 'nano filename' command opens the nano text editor to edit the specified file. Nano is a simple, user-friendly text editor for the command line."
    },
    {
        "question": "Which command is used to open the vim text editor to edit a file?",
        "options": ["vim filename", "nano filename", "gedit filename"],
        "answer": "vim filename",
        "explanation": "The 'vim filename' command opens the vim text editor to edit the specified file. Vim is a powerful text editor with advanced features for editing text."
    },
    {
        "question": "How do you open the gedit text editor to edit a file?",
        "options": ["gedit filename", "nano filename", "vim filename"],
        "answer": "gedit filename",
        "explanation": "The 'gedit filename' command opens the gedit text editor to edit the specified file. Gedit is a graphical text editor for the GNOME desktop environment."
    },
    {
        "question": "Which command is used to add a new PPA (Personal Package Archive) on Ubuntu?",
        "options": ["sudo add-apt-repository ppa:repository_name", "sudo apt-add-repository ppa:repository_name", "sudo apt-key add ppa:repository_name"],
        "answer": "sudo add-apt-repository ppa:repository_name",
        "explanation": "The 'sudo add-apt-repository ppa:repository_name' command adds a new PPA to the system. PPAs provide additional software packages that are not available in the official repositories."
    },
    {
        "question": "How do you update the package list after adding a new PPA on Ubuntu?",
        "options": ["sudo apt update", "sudo apt upgrade", "sudo apt install"],
        "answer": "sudo apt update",
        "explanation": "The 'sudo apt update' command updates the package list from the repositories, including any newly added PPAs. It ensures that you have the latest information about available packages."
    }
]