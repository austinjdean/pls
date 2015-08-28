# pls
Python utility to search Google from the Linux command line

### Dependencies:

- Python 2.x
- Ant (only for installation/removal)

### Installation:

##### Use ant:

`sudo ant install`

##### Removal:

`sudo ant clean`

##### Installation Notes:

- Updating `pls` (i.e. pulling the latest into your local `pls` directory) does not require reinstallation
- Relocating your local `pls` directory does - the symlink needs to point to the new location
	- This can be done with `sudo ant clean install`

### Usage:
`pls [options] [search terms]`

### Options:
```
-h, --help            show this help message and exit
-d, --debug           Print the target URL instead of opening it
-F, --force           Force pls to attempt to open in browser
-c, --chrome          Open using Chrome
-f, --firefox         Open using Firefox
-t, --text            Display results in the terminal instead of showing
                      them in browser
-w WORD, --word WORD  Show syllable segmentation, pronunciation, and
                      definition of WORD in the terminal
-l, --lucky           I'm Feeling Lucky
-i, --images          Search using Google Images
-S, --scholar         Search using Google Scholar
-n, --news            Search using Google News
-m, --maps            Search using Google Maps
-v, --video           Search using Google Video
-s SITE, --site SITE  Search a specific website
-L, --sass            Increase sass - open "Let Me Google That For You" URL
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
