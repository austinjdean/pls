# go
Python utility to search Google from the Linux command line

### Installation:

(Tentatively using ant - might go with Ryan's install scripts)

##### Use ant:

`sudo ant install`

##### Removal:

`sudo ant clean`

##### Usage:  
`go [options] [search terms]`

##### Options:
`-c: open using Chrome`  
`-f: open using Firefox`  
`-h, --help: display usage information and exit`

##### Notes:
- search terms do not need to be enclosed in quotes.
- if building with `ant` fails, try using `sudo`.

#### To-do list:
- (?) switch window focus to newly created browser session
- (?) use Ryan's scripts instead of ant to install
