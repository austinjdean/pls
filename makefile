install:
	sudo ln -s $(PWD)/pls.py /usr/local/bin/pls

clean:
	sudo rm /usr/local/bin/pls

limited:
	# ensure ~/bin exists
	mkdir -p $(HOME)/bin

	# put symlink to pls in ~/bin
	ln -s $(PWD)/pls.py $(HOME)/bin/pls

limitedClean:
	rm -f $(HOME)/bin/pls
