#include<stdio.h>

int main()
{
	//�������
	int item;
	float price;
	int date_f,date_m,date_l;
	char date[5];
	//��������
	printf("Enter item number: ");
	scanf("%d",&item);
	printf("Enter unit price: ");
	scanf("%f", &price);
	setbuf(stdin,NULL);           //��ջ���������
	printf("Enter purchase date(mm/dd/yyyy): ");
	//getchar();
	scanf("%d/%d/%d",&date_f,&date_m,&date_l);
	//scanf("%d/%d/%d",&date_f,&date_m,&date_l);
	date[0] = itoa(date_f);
	date[1] = '/';
	date[2] = date_m;
	date[3] =  '/';
	date[4] = date_l;
	//�������
	printf("Item\tUnit\tPurchase\n");
	printf("\tPrice\tDate\n");
	printf("%d\t$%4.2f\t%s\n",item,price,date);
	return 0;
}
