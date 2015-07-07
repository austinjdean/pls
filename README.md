# pls
Python utility to search Google from the Linux command line

### Installation:

##### Use ant:

`sudo ant install`

##### Removal:

`sudo ant clean`

##### Usage:
`pls [options] [search terms]`

##### Options:
```
-h, --help      show this help message and exit
-d, --debug     Debug flag - print the URL that pls will open
-c, --chrome    Open using Chrome
-f, --firefox   Open using Firefox
-s, --scholar   Search using Google Scholar
-l, --lucky     I'm Feeling Lucky
-i, --images    Search using Google Images
-m, --sass      Increase sass - search using Let Me Google That For You
-y, --youtube   Search using YouTube
-r, --simpsons  Open a randomly selected Simpsons episode
-x, --xkcd      Open a randomly selected xkcd comic
```

##### Notes:
- Search terms do not need to be enclosed in quotes.
- If building with `ant` fails, try using `sudo`.
- Any special characters (`*`, `"`, `$`, etc.) will be consumed by the shell before the script can even get its hands on them. To use these literal characters in a search query, escape them with `\`.

#### To-do list:
- See the [Issues Page](https://github.com/austinjdean/pls/issues)

#### Notes for collaborators:
`git fetch`  
`git checkout develop`  
`git pull`  
- Read up on this branching model: http://nvie.com/posts/a-successful-git-branching-model/
- Most importantly, develop features on branches checked out from `develop`, and merge them back in when they're stable
- Once `develop` is stable, it gets merged with `master` as a new version
- The idea is that `master` will always represent a production-ready state
