%{
    #include <stdio.h>
    #include <string.h>
%}

%%
if | for | while | else | do | int | long | short | float | double | include | main | return | printf | "<stdio.h>" { printf("Keyword %s encountered.\n", yytext); }
[_a-zA-Z$][_a-zA-Z0-9]* {
    if (yyleng <= 32) printf("Identifier %s encountered.\n", yytext);
    else printf("Identifier exceeded the maximum length.\n");
}
[0-9]+ {
    if (yyleng <= 10 || (yyleng == 10 && yytext < "2147483648")) printf("Numeric value is $s.\n", yytext);
    else printf("Numeric value exceeded INT_MAX.\n");
}
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