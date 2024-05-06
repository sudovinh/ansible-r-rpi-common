# r-rpi-common

[![CI](https://github.com/sudovinh/ansible-r-rpi-common/actions/workflows/ansible-lints.yml/badge.svg?branch=main)](https://github.com/sudovinh/ansible-r-rpi-common/actions/workflows/ansible-lints.yml)

Role for initial Raspberry Pi setup

- set timezone
- enable ntp and ssh
- install packages and remove bloatware packages
- setup new users/admins
- configure raspberry default configs
- setup raspberry motd
- disable pi ssh/login

based of from:
https://github.com/glennklockwood/rpi-ansible
https://github.com/willshersystems/ansible-users

### Requirements
------------
- Ansible Core >= 2.11.12

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
| `disable_pi_user` | `false`  | disable default pi ssh login (recommend to enable gui or have another user created before enabling it) and pi login|
| `users_default_shell` | `/bin/bash` | user's default shell |
| `users_create_homedirs` | `false` | Create home dirs for new user |
| `users_default_home` | `/user` | Create parent home directory |
| `users_per_user_groups` | `false` | Create groups for users with the same name as the users group |
| `users_manage_admin_sudoers` | `false` | If true, create a sudoers entry for the admin group allow root access. |
| `users_admin_uses_ansible` | `false` | If true, assume the admin group is also used to run Ansible jobs |
| `users_admin_sudo_password` | `false` | If set to true, require a password for sudo, false to not require a password |
| `users_admin_group` | `sudo` | users admin group |
| `users_default_password` | `!` | user default password |

### Example
-----------
```
# Rasp Common Variables
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
disable_pi_user: False # run first then enable after verifying new user login/ssh works
users_manage_admin_sudoers: True

# User Variables
users:
- username: {username}
  comment: main pi user
  is_admin: yes
  groups: 
    - '{{ users_admin_group }}' # add to `sudo` group
  pubkey: {ssh public key}
  uid: {user id}
  gid: {group id}
  system: true
  password: !vault |
          {use ansible-vault to encrypt your user password}
users_groups:
  - groupname: logger
    gid: 150
    system: true

additionalusers:
  - username: svc-logger
    comment: for logging
    uid: 151
    gid: 151
    home: /var/lib/logger
    shell: /bin/bash
    system: true
```

License
-------
MIT
