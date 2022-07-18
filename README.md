# r-rpi-common

Role for initial Raspberry Pi setup

### Requirements
------------
- Ansible Core >= 2.11.12
- Molecule >= 3.4.0

### Variables
--------------
All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `required_packages` | [here](defaults/main.yml) | packages to be installed |
| `enable_gui` | `false` | enable gui in raspberry pi |
| `enable_autologin` | `false`  | enable autologin in raspberry pi |
| `enable_bootwait` | `true`  | enable wait on network on boot |
| `enable_bootsplash` | `false`  | enable boot splash on startup |
| `enable_camera` | `false`  | enable camera |
| `enable_vnc` | `false`  | enable vnc|
| `enable_spi` | `false`  | enable spi |
| `enable_i2c` | `false`  | enable i2c bus pins |
| `enable_serial` | `false`  | enable serial console |
| `enable_serial_hw` | `false`  | enable serial hw |
| `enable_onewire` | `false`  | enable onewire communication bus |
| `enable_rgpio` | `false`  | enable general-purpose Input/Output pins |
| `disable_pi_ssh_login` | `false`  | disable default pi ssh login (recommend to enable gui or have another user created before eanbling it) |

| `users_default_shell` | `/bin/bash` | user's default shell |
| `users_create_homedirs` | `yes` | Create home dirs for new user |
| `users_default_home` | `/user` | Create parent home directory |
| `users_per_user_groups` | `yes` | Create groups for users with the same name as the users group |
| `users_manage_admin_sudoers` | `yes` | If true, create a sudoers entry for the admin group allow root access. |
| `users_admin_uses_ansible` | `yes` | If true, assume the admin group is also used to run Ansible jobs |
| `users_admin_sudo_password` | `false` | If set to true, require a password for sudo, false to not require a password |
| `users_admin_group` | `sudo` | users admin group |
| `users_default_password` | `!` | user default password |

### Example
-----------
```
users:
- username: rickmorty
  comment: rick morty
  is_admin: yes
  sshkey: {SSH PUB KEY}
  uid: 1024
  gid: 1024

enable_gui: False
enable_autologin: False
enable_bootwait: True
enable_bootsplash: False
enable_camera: False
enable_vnc: False
enable_spi: False
enable_i2c: False
enable_serial: False
enable_serial_hw: False
enable_onewire: False
enable_rgpio: False
disable_pi_ssh_login: False
```

License
-------
MIT
