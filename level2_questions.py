level2_questions = [
    {
        "question": "Which command displays the kernel version?",
        "options": ["uname -r", "ls -l", "df -h"],
        "answer": "uname -r",
        "explanation": "The 'uname' command with the '-r' option shows the kernel release. You can use 'uname -a' to display all system information at once."
    },
    {
        "question": "How do you check disk usage?",
        "options": ["free -h", "df -h", "du -sh"],
        "answer": "df -h",
        "explanation": "The 'df' command shows disk space usage. The '-h' option makes the output human-readable. You can also use 'df -i' to check inode usage instead of block usage."
    },
    {
        "question": "Which command shows system uptime?",
        "options": ["uptime", "top -n 1", "time -p"],
        "answer": "uptime",
        "explanation": "The 'uptime' command shows how long the system has been running, along with the current time, number of users, and load averages."
    },
    {
        "question": "How do you find files by name?",
        "options": ["locate -i", "whereis -b", "which -a"],
        "answer": "locate -i",
        "explanation": "The 'locate' command quickly finds files by name. The '-i' option makes the search case-insensitive. For real-time searches, use the 'find' command."
    },
    {
        "question": "Which command is used to monitor system resources in real-time?",
        "options": ["top", "ps aux", "free -m"],
        "answer": "top",
        "explanation": "The 'top' command provides a dynamic real-time view of system processes and resource usage. It's interactive and can be customized to show different information."
    },
    {
        "question": "How do you compress a file using gzip?",
        "options": ["gzip file.txt", "zip -r file.zip file.txt", "compress -v file.txt"],
        "answer": "gzip file.txt",
        "explanation": "The 'gzip' command compresses files. It replaces the original file with a compressed version having a .gz extension. Use 'gunzip' to decompress."
    },
    {
        "question": "Which command is used to schedule tasks to run at specific times?",
        "options": ["cron", "at -f", "batch -d"],
        "answer": "cron",
        "explanation": "The 'cron' daemon is used to schedule recurring tasks. You can edit cron jobs using 'crontab -e'. For one-time scheduled tasks, use the 'at' command."
    },
    {
        "question": "How do you view the contents of a file without opening it entirely?",
        "options": ["less", "more -d", "cat -n"],
        "answer": "less",
        "explanation": "The 'less' command allows you to view file contents page by page. It's more feature-rich than 'more' and allows backward navigation."
    },
    {
        "question": "Which command is used to create a symbolic link?",
        "options": ["ln -s", "link -s", "symlink -f"],
        "answer": "ln -s",
        "explanation": "The 'ln' command with the '-s' option creates a symbolic link. Symbolic links can point to directories and can span file systems, unlike hard links."
    },
    {
        "question": "How do you check the size of a directory and its subdirectories?",
        "options": ["du -sh", "ls -lh", "df -h"],
        "answer": "du -sh",
        "explanation": "The 'du' command with '-sh' options shows the total size of a directory in human-readable format. Use 'du -sh *' to see sizes of all items in the current directory."
    },
    {
        "question": "Which command is used to change file ownership?",
        "options": ["chown user:group", "chmod 755", "chgrp group"],
        "answer": "chown user:group",
        "explanation": "The 'chown' command changes file ownership. It can change both user and group ownership. Use 'chgrp' to change only the group ownership."
    },
    {
        "question": "How do you search for a pattern in files recursively?",
        "options": ["grep -r pattern", "find -name pattern", "locate -r pattern"],
        "answer": "grep -r pattern",
        "explanation": "The 'grep' command with the '-r' option searches for a pattern recursively in all files under the specified directory. It's a powerful tool for searching through code or logs."
    },
    {
        "question": "Which command shows network connections and their status?",
        "options": ["netstat -tuln", "ifconfig -a", "route -n"],
        "answer": "netstat -tuln",
        "explanation": "The 'netstat' command displays network connections, routing tables, interface statistics, masquerade connections, and multicast memberships. The '-tuln' options show TCP and UDP listening ports and addresses in numeric form."
    }
]