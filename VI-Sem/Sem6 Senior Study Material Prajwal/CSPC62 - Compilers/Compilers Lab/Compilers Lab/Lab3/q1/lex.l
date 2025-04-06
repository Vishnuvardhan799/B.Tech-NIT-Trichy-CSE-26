%{
#include "y.tab.h"
%}

%%
"if"            { return IF; }
"else"          { return ELSE; }
"("             { return LPAREN; }
")"             { return RPAREN; }
";"             { return SEMICOLON; }
[a-zA-Z][a-zA-Z0-9]*    { return IDENTIFIER; }
[ \t\n]         ; /* Ignore whitespace */
.               { return yytext[0]; }

%%

int yywrap() {
    return 1;
}
