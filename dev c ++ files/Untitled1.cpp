#include<iostream>
using namespace std;
int main()
{
	int year;
	cout<<"enter thne year :";
	cin>>year;
	if(year%4==0&&year%100!=0||year%400==0)
	{
		cout<<"yes it is lep year ";
	}
	else
	{
		cout<<"not a leap year ";
	}
	return 0;
}
