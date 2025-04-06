%{
    #include<stdio.h>
    #include<string.h>
%}
%%
">" {printf("Greater Than >\n");}
"<" {printf("Lesser Than <\n");}
"=" {printf("assigning =\n");}
"+" {printf("Addition +\n");}
"-" {printf("Subtraction -\n");}
"/" {printf("Division /\n");}
"*" {printf("Multiplication *\n");}
"%" {printf("Modulo %%\n");}
"!=" {printf("Not equal !=\n");}
"==" {printf("Comparision ==\n");}
">=" {printf("Greater Than equals to >=\n");}
"<=" {printf("Greater Than equals to <=\n");}
. ;
%%
int yywrap(){
    return 1;
}
int main(){
    yyin = fopen("sample.c","r");
    yylex();
    fclose(yyin);
    return 0;
}