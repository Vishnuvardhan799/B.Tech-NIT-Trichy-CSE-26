%{
#include "y.tab.h"
%}

%%
"while"            { return WHILE; }
"("             { return LPAREN; }
")"             { return RPAREN; }
[a-zA-Z][a-zA-Z0-9]*    { printf("%s\n",yytext);return ID; }
.               ;

%%

int yywrap() {
    return 1;
}
