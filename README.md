# goo
Python utility to search Google from the Linux command line

### Installation:

(Tentatively using ant - might use Ryan's install scripts)

##### Use ant:

`sudo ant install`

##### Removal:

`sudo ant clean`

##### Usage:
`goo [options] [search terms]`

##### Options:
`-c: open using Chrome`  
`-f: open using Firefox`  
`-h, --help: display usage information and exit`

##### Notes:
- search terms do not need to be enclosed in quotes.
- if building with `ant` fails, try using `sudo`.
- Any special characters (`*`, `"`, `$`, etc...) will be consumed by the shell before the script can even get its hands on them. To use these litreal characters in a search query, escape them with `\`.

#### To-do list:
- (?) switch window focus to newly created browser session
- (?) use Ryan's scripts instead of ant to install
