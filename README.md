# pls
Python utility to search Google from the Linux command line

### Dependencies:

- Python 2.x
- Make (only for installation/removal)

### Installation:

##### Use make:

`make install`

##### Removal:

`make clean`

##### Installation Notes:

- Updating `pls` (i.e. pulling the latest into your local `pls` directory) does not require reinstallation
- Relocating your local `pls` directory does - the symlink needs to point to the new location
	- This can be done with `make clean install`

### Usage:
`pls [options] [search terms]`

### Options:
```
-h, --help            show this help message and exit
-d, --debug           Print the target URL instead of opening it
-w [WORD [WORD ...]], --word [WORD [WORD ...]]
                      Show syllable segmentation, pronunciation, and
                      definition of WORD in the terminal
-l, --lucky           I'm Feeling Lucky
-t, --temperature     Get a brief summary of local temperature and sky
                      conditions
-W, --wiki            Get results from Wikipedia
-F, --force           Force pls to attempt to open in browser
-c, --chrome          Open using Chrome
-f, --firefox         Open using Firefox
-T, --text            Display results in the terminal instead of showing
                      them in browser
-i, --images          Search using Google Images
-S, --scholar         Search using Google Scholar
-n, --news            Search using Google News
-m, --maps            Search using Google Maps
-v, --video           Search using Google Video
-s SITE, --site SITE  Search a specific website
-L, --sass            Increase sass - open "Let Me Google That For You" URL
-C, --curious         Open a random fact from Google
-r, --simpsons        Open a randomly selected Simpsons episode
-x, --xkcd            Open a randomly selected xkcd comic
```

#### Notes:
- Search terms do not need to be enclosed in quotes
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
