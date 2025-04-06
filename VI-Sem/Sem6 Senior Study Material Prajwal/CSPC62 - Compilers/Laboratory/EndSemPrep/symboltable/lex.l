%{
#include "par.tab.h"
extern char * yylval;
int x=0;
%}
%%
"int" {x++;return INT;}
"float" {x++;return FLOAT;}
"char" {x++; return CHAR;}
"double" {x++;return DOUBLE;}
[a-z]+ {yylval=yytext;if(x>0) {return ID;} return 0;}
"," return C;
[\n] return NL;
";" {x--;return SE;}
%%