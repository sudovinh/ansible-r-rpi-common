
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


print("test")
# def test_java_runs_successfully(host):
#     java_ran = host.run("java -version")

#     assert java_ran.rc == 0
#     # java prints to stderr not stdout?
#     assert 'openjdk version "1.8.0_222' in java_ran.stderr
