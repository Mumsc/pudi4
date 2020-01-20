# include <iostream.h>
 #include <conio.h>
void main ()
{
int i ;
float delta, com, coeff = 0.1;
struct input
{
float val,out,wo, wi;
int top;
int s[3];
}
cout<<"\n Enter the i/p value to target o/p"<<"\t";
for (i=0; i<3 ; i++)
cin>>s[i],val>>s[i],top);
i = 0;
do{
if (i =  = 0)
{
W0 = -1.0;  W1 = -0.3;
}else
{
W0 =  del [i - 1], W0 ;
W1 =  del [i - 1] , Wi ;
}
del [i]. aop = w0 + (wi * del [i]. val);
del [i].out = del [i]. aop);
delta = (top - del [i]. out) * del [i].out * (1 - del [i].out);
corr = coeff * delta * del [i].[out];
del [i].w0 = w1 + corr;
del [i]. w1 = w1 + corr; i++;
}
While ( i ! = 3)
cout<< "VALUEâ"<"Target"<<"Actual"<<"w0"<<"w1"<<"\n";
for (i=0; i=3; i++)
{
cout<< s [i].val<< s[i].top<<s[i].out << s[i]. w0<< s[i]. w1;
cout<< "\n";
}
getch ();
}
