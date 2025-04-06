%{
#include <stdio.h>
#include <stdlib.h>
extern int yylex();
extern int yyparse();
extern FILE* yyin;
void yyerror(const char*);

#define YYSTYPE YYSTYPE
#define YYDEBUG 1

typedef struct {
    char* str;
} YYSTYPE;

%}

%token IF ELSE LPAREN RPAREN SEMICOLON IDENTIFIER

%%

program :
        | program statement
        ;

statement : if_statement
          | other_statement
          ;

if_statement : IF LPAREN condition RPAREN statement
             | IF LPAREN condition RPAREN statement ELSE statement
             ;

other_statement : IDENTIFIER SEMICOLON
                ;

condition : IDENTIFIER
          ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Syntax Error: %s\n", s);
}

int main() {
    FILE* input_file = fopen("sample.c", "r");
    yyin = input_file;
    yyparse();
    fclose(input_file);
    return 0;
}
