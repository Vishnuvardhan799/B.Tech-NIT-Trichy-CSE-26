%{
#include <stdio.h>
#include <string.h>
%}

%%
"/*"[a-zA-Z0-9 \t\n]+"*/" ;
"//"[a-zA-Z0-9 \t]+ ;
. ECHO;
%%

int main()
{
    yyin = fopen("sample.c","r");
    yyout = fopen("cleaned.c","w");
    yylex();
    fclose(yyout);
    fclose(yyin);
    return 0;
}

int yywrap()
{
    return 1;
}