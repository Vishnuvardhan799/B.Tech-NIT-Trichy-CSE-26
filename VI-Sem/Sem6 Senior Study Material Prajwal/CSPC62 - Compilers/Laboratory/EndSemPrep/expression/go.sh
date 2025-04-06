flex lex.l
bison -d par.y
gcc lex.yy.c par.tab.c -o file
./file