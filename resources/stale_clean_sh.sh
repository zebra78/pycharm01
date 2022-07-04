#!/usr/bin/bash

echo "Hello, World!"
echo "Hello, World 2 !"
# exit 1
echo "Script name is: $0"
stale_file=$1
echo "File passed is: $stale_file"
for stale_line in $(cat $stale_file);
do
  echo "in stale.sh loop"
  echo "$stale_line";
done
# touch ~/stale_clean_log.log
exit 0


