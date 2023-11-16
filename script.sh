#!/bin/bash


commit_recent=$(git log -n 1 --pretty=format:%H "origin/master")
url=$(git remote get-url "origin")

for c in "$(git ls-remote -h $url)"; do
	hash_ref=$(echo $c | awk '{print $1}')
	echo $hash_ref
	if test "$hash_ref" == "$commit_recent" 
	then
		echo "new matching commit detected; update server"
		git pull
		# when server is up add commands to get it to restart or smth
	else
		echo "no new commits"
	fi
	
done
