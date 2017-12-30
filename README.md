# Github Trends

The program finds repositories on Github created in the previous week, takes 20 high-starred of them and counts the amount of open issues. 
It outputs the repository name, number of issues and a link to the repo.

# How to launch

The script requires the installed Python interpreter version 3.5

Example of script launch on Linux, Python 3.5:
```
$ python github_trending.py
```

output
```
Name: wechat_jump_game
Issues: 2
Link: https://api.github.com/repos/wangshub/wechat_jump_game

Name: array-explorer
Issues: 2
Link: https://api.github.com/repos/sdras/array-explorer

Name: app-host
Issues: 2
Link: https://api.github.com/repos/pluosi/app-host

Name: PS4-4.05-Kernel-Exploit
Issues: 2
Link: https://api.github.com/repos/Cryptogenic/PS4-4.05-Kernel-Exploit

Name: javascript-tutorial
Issues: 2
Link: https://api.github.com/repos/wangdoc/javascript-tutorial

Name: retrofit2-kotlin-coroutines-adapter
Issues: 2
Link: https://api.github.com/repos/JakeWharton/retrofit2-kotlin-coroutines-adapter


```
Running on Windows is similar.


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
