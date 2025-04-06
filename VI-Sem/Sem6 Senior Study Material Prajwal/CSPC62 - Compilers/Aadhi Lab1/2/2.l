%{
#include <stdio.h>
%}

%%
if|for|while|else|do|int|"long long"|short|float|double|include|main|return|printf|"<stdio.h>" {printf("\n%s is a keyword.",yytext);}
[a-zA-Z_][a-zA-Z0-9_]+ {
    if(yyleng > 32)  {
        printf("\n%s is too long for an identifier.\n",yytext);
        printf("Change and try again\n");
        return -1;
    }
    else {
        printf("\n%s is an valid identifier.", yytext);
    }
}
. {printf("%s",yytext);}
%%

int main()
{
    yyin = fopen("sample.c","r");
    yylex();
    fclose(yyin);
    return 0;
}

int yywrap()
{
    return 1;
}