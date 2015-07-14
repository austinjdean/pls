# pls
Python utility to search Google from the Linux command line

### Dependencies:

- Python 2.x
- ant (only for installation/removal)

### Installation:

##### Use ant:

`sudo ant install`

##### Removal:

`sudo ant clean`

### Usage:
`pls [options] [search terms]`

### Options:
```
-h, --help            show this help message and exit
-d, --debug           Debug flag - print the URL that pls will open
-c, --chrome          Open using Chrome
-f, --firefox         Open using Firefox
-l, --lucky           I'm Feeling Lucky
-i, --images          Search using Google Images
-S, --scholar         Search using Google Scholar
-n, --news            Search using Google News
-m, --maps            Search using Google Maps
-v, --video           Search using Google Video
-s SITE, --site SITE  Search a specific website
-L, --sass            Increase sass - search using Let Me Google That For
                      You
-r, --simpsons        Open a randomly selected Simpsons episode
-x, --xkcd            Open a randomly selected xkcd comic
```

#### Notes:
- Search terms do not need to be enclosed in quotes
- If building with `ant` fails, try using `sudo`
- Any special characters (`*`, `"`, `$`, etc.) will be consumed by the shell before the script can even get its hands on them. To use these literal characters in a search query, escape them with `\`

#### To-do list:
- See the [Issues Page](https://github.com/austinjdean/pls/issues)

#### Notes for collaborators:
`git fetch`  
`git checkout develop`  
`git pull`  
- Read up on this branching model: http://nvie.com/posts/a-successful-git-branching-model/
- Most importantly, develop features on your local `develop` branch, and push your changes to the remote when they're stable
- Once `develop` is stable, it gets merged into `master` as a new version
- The idea is that `master` will always represent a production-ready state
