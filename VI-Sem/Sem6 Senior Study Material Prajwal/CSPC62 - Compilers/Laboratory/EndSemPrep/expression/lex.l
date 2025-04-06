%{
#include <stdio.h>
#include <stdlib.h>
#include "par.tab.h"
extern int yylval;
%}

%%
[a-zA-Z][a-zA-Z0-9]* { return ID; }
[0-9]+ { yylval = atoi(yytext); return NUM; }
[\t] {;}
[\n] { return 0; }
. { return yytext[0]; }
%%