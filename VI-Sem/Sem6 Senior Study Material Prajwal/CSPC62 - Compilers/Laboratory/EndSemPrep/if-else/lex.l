%{
#include "par.tab.h"
%}

%%
"if" { return IF; }
"else" { return ELSE; }
"(" { return LPAREN; }
")" { return RPAREN; }
[a-zA-z][a-zA-z0-9]* { printf("%s\n", yytext); return ID; }
.   ;
%%

int yywrap()
{
    return 1;
}