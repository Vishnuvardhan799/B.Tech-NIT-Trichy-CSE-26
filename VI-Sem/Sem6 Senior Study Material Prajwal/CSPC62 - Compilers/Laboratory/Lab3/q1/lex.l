%{
#include "y.tab.h"
%}

%%
"if"            { return IF; }
"else"          {return ELSE; }
"("             { return LPAREN; }
")"             { return RPAREN; }
[a-zA-Z][a-zA-Z0-9]*    { printf("%s\n",yytext);return ID; }
.               ;

%%

int yywrap() {
    return 1;
}
