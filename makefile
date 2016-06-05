all: index.html
index.html: index.md
	pandoc -s index.md -t revealjs -o index.html --slide-level 2 --highlight-style="zenburn"
