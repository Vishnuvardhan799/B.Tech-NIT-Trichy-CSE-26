%{
    #include<stdio.h>
    #include<string.h>
%}

%%
if|for|while|else|do|int|"long long"|short|float|double|include|main|return|printf|"<stdio.h>" {printf("keyword %s \n",yytext);}
[_a-zA-Z$][_a-zA-Z0-9]* {
    if(yyleng <= 32){
        printf("identifier %s \n",yytext);
    }
    else{
        printf("Identifier size exceeded the max length\n");
    }
}
[0-9]+ {
    if(yyleng < 10 || (yyleng == 10 && yytext < "2147483648")){
        printf("Numeric value %s \n",yytext);
    }
    else{
        printf("Numeric value exceeded INT_MAX\n");
    }
}
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
