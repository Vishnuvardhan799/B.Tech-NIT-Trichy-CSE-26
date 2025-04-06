%{
#include "par.tab.h"
%}

%%
"while" { return WHILE; }
"(" { return LPAREN; }
")" { return RPAREN; }
[a-zA-z][a-zA-Z0-9]* { printf("%s\n", yytext); return ID; }
%%

int yywrap()
{
    return 1;
}