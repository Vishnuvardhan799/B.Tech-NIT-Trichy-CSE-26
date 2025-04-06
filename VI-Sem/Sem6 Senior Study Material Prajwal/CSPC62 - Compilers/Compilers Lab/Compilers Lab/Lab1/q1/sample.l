%{
#include <stdio.h>
#include <string.h>
%}

%%
\n?"/*"(.|\n)*"*/"\n ;
"//".*\n ;
[ ]+ {fprintf(yyout," ");}
[\t]+ {fprintf(yyout,"\t");}
[\n]+ {fprintf(yyout,"\n");}

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