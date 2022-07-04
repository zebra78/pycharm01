import subprocess

# exit_code = subprocess.call('./practice.sh')
# print(exit_code)
file = 'stale_process.txt'
# exit_code = subprocess.call("../resources/stale_clean_sh.sh, " + file)
exit_code = subprocess.check_call("../resources/stale_clean_sh.sh %s" % file, shell=True)
print(exit_code)
