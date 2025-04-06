%{
#include <stdio.h>
%}

%%
"+" {printf("\t(Addition operator)%s\t",yytext);}
"-" {printf("\t(Subtraction operator)%s\t",yytext);}
"/" {printf("\t(Division operator)%s\t",yytext);}
"*" {printf("\t(Multiplication operator)%s\t",yytext);}
. ECHO;
%%

int main()
{
    printf("\nEnter the string : ");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}