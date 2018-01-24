SRC=$(wildcard mds/*.md)
OBJS=$(SRC:mds/%.md=pages/%.html)

all: $(OBJS)


pages/%.html: mds/%.md
	pandoc -s --reference-links  -r markdown_github -t html $? -o $@



# This entry allows you to type " make clean " to get rid of
# all object and module files
clean:
	 rm -f -r f_{files,modd}* lib/*.o lib/*.mod *.M *.d V*.inc *.vo  V*.f *.dbg album F.err
