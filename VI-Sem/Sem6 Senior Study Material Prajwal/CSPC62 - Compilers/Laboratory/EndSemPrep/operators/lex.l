%{
#include<stdio.h>
#include<string.h>
%}

%%
">" { printf("Grester Than >\n"); }
">=" { printf("Greater Than or Equal To >=\n"); }
"<" { printf("Lesser Than or Equal To <=\n"); }
"<=" { printf("Lesser Than <\n"); }
"=" { printf("Assigning =\n"); }
"+" { printf("Addition +\n"); }
"-" { printf("Subtraction -\n"); }
"*" { printf("Multiplication *\n"); }
"/" { printf("Division /\n"); }
"%" { printf("Modulo %%\n"); }
"!=" { printf("Not Equal To !=\n"); }
"==" { printf("Comparision ==\n"); }
. ;
%%

int yywrap()
{
    return 1;
}

int main()
{
    yyin = fopen("sample.c", "r");
    yylex();
    fclose(yyin);
    return 0;
}