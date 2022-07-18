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
| `FLUENTBIT_VERSION` | 1.2.2 | fluent-bit version  |
| `FLUENTBIT_USER` | fluentbit | user for fluentbit |
| `FLUENTBIT_INSTALL_PATH` | /bin/fluent-bit | fluent-bit binary directory|
| `FLUENTBIT_DIR` | /etc/fluent-bit/ | fluent-bit configs directory |
| `FLUENTBIT_MAIN_CONF` | /etc/fluent-bit/fluent-bit.conf | fluent-bit main conf|
| `FLUENTBIT_MAIN_PARSER` | /etc/fluent-bit/parsers.conf | fluent-bit parser file |
| `FLUENTBIT_INITD` | /etc/init.d/fluent-bit | initd directory |
| `FLUENTBIT_SYSTEMD` | /etc/systemd/system/fluent-bit.service | systemd directory |
| `FLUENTBIT_S3_ARTIFACT` | https://s3-us-west-1.amazonaws.com/factual-sysops-artifacts/fluentbit/fluent-bit-{{ fluentbit_version }} | [fluent-bit artifact](https://github.com/Factual/sysops-fluentbit) |

License
-------
MIT