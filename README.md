# SSH Brute-Force

Just a simple SSH brute-force script I created today as part of the HackTheBox machine I'm currently rooting.
Tested against an OpenSSH 7.9 server with no issues; as this script was more for personal use I haven't tested it thoroughly.

It's nothing special; it served me well (it did what I wanted it to do, anyhow!)

Python pwntools is a minimum requirement for running this script.

Please note: most establishments hosting an SSH server would have protection in place to prevent this script from being of any use (for instance, blocking a specific IP after X number of login attempts for Y minutes)- if this is the case you will need to further improve the script (perhaps a timeout before repeating the attempt if the connection is refused.)

Hope you enjoy my noobery ^-^

--C-Cracks

linkedin.com/in/courtney-evans99

UPDATE: You can now execute a line of commands upon successful authentication to the server and view the result of the provided command.
