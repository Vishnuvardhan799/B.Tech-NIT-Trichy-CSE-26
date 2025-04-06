%{
#include<stdio.h>
#include<string.h>
int err_no=0,fl=0,i=0,j=0,type[100];
char symbol[100][100],temp[100];
%}
%token ID NL SE C INT FLOAT CHAR DOUBLE
%%
START:S1 NL {return;}
;
S1:S NL S1
|
S NL
;
S: INT L1 E
|
FLOAT L2 E
|
CHAR L3 E
|
DOUBLE L4 E
|
INT L1 E S
|
FLOAT L2 E S
| 
CHAR L3 E S
| 
DOUBLE L4 E S
|
L1:L1 C ID{strcpy(temp,(char *)$3); insert(0);}
|ID{strcpy(temp,(char *)$1); insert(0);}
;
L2:L2 C ID{strcpy(temp,(char *)$3); insert(1);}
|ID{strcpy(temp,(char *)$1); insert(1);}
;
L3:L3 C ID{strcpy(temp,(char *)$3); insert(2);}
|ID{strcpy(temp,(char *)$1); insert(2);}
;
L4:L4 C ID{strcpy(temp,(char *)$3); insert(3);}
|ID{strcpy(temp,(char *)$1); insert(3);}
;
E:SE
;
%%
void yyerror(const char *str) {printf("error");}
int yywrap(){return 1;}
main()
{
yyparse();
if(err_no==0)
{
for(j=0;j<i;j++)
{
if(type[j]==0) printf("INT-");
if(type[j]==1) printf("FLOAT-");
if(type[j]==2) printf("CHAR-");
if(type[j]==3) printf("DOUBLE-");
printf("%sn",symbol[j]);
}
}
}
void insert(int type1)
{
fl=0;
 for(j=0;j<i;j++)
if(strcmp(temp,symbol[j])==0)
{
if(type[i]==type1) printf("Redeclaration of variable");
else {printf("Multiple Declaration of Variable");err_no=1;}
fl=1;
}
if(fl==0)
{
type[i]=type1;
strcpy(symbol[i],temp);
i++;
}
}