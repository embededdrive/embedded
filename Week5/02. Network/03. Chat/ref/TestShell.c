
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int isValid(char str[20])
{
	if (strlen(str) != 10)
		return 0;

	int flag = 0;

	for (int i = 0; i < 10; i++)
	{
		if (i == 1)
			continue;

		if (str[i] >= '0' && str[i] <= '9')
			flag = 1;

		if (str[i] >= 'A' && str[i] <= 'F')
			flag = 1;
	}

	return flag;
}

	int line;
	char input[20];
void write() {



	if (!isValid(input))
		printf("��ȿ���� ���� �����Դϴ�");

	char command[100];

	sprintf(command, "ssdProject.exe W %d %s", line, input);

	system(command);
}
void read() {


	char command[100];

	sprintf(command, "ssdProject.exe R %d", line);

	system(command);
}
int main()
{
	while (1)
	{
		printf("SHELL > ");

		char cmd[10];

		scanf("%s", cmd);

		if (strcmp(cmd, "write") == 0)
		{
			scanf("%d", &line);

			scanf("%s", input);

			write();
		}
		else if (strcmp(cmd, "read") == 0)
		{
			scanf("%d", &line);

			read();
		}
		else if (strcmp("help", cmd) == 0) {
			printf("\n\n");
			printf("�׽�Ʈ �� �Ŵ���\n\n");
			printf("write \n");
			printf("    write LBA�ּ� 4����Ʈ��\n");
			printf("    * ex) write 3 0xABCDABCD\n");
			printf("    * LBA �ּҴ� 0 - 99 �����Դϴ�.\n");
			printf("    * �ݵ�� 0xAAAAAAAA ������ 16���� 10���ڷ� �Է��մϴ�.\n");
			printf("    * ����� nand.txt �� ��ϵ˴ϴ�.\n");
			printf("\n");
			printf("read \n");
			printf("    read LBA�ּ�\n");
			printf("    ex) write 4\n");
			printf("    * ����� result.txt �� �ۼ��˴ϴ�.\n");
			printf("\n");
			printf("fullwrite \n");
			printf("    fullwrite\n");
			printf("    * nand.txt �� ��� ���� 0xABCDFFFF �� �����մϴ�.\n");
			printf("\n");
			printf("fullread \n");
			printf("    fullread\n");
			printf("    * nand.txt �� ��� LBA �� ���� read ���� ��, �п� ��� LBA ���� ����մϴ�.\n");
			printf("\n");
			printf("testapp1 \n");
			printf("    testapp1 \n");
			printf("    * fullwrite ���� �� fullread �����մϴ�\n");
			printf("\n");
			printf("testapp2 \n");
			printf("    testapp2 \n");
			printf("    * 0 ~ 5 �� LBA �� 0xAAAABBBB ������ �� 30�� Write�� �����մϴ�.\n");
			printf("    * 0 ~ 5 �� LBA �� 0x12345678 ������ 1 ȸ Over Write�� �����մϴ�.\n");
			printf("    * 0 ~ 5 �� LBA Read ���� �� ���������� ���� �������� Ȯ���մϴ�.\n");
			printf("\n");
			printf("exit ��ɾ� �Է� �� �� ���α׷��� ����˴ϴ�.");
			printf("\n\n");

		}
		else if (strcmp("fullwrite", cmd) == 0) {
			system("ssdProject.exe w 12");
		}
		else if (strcmp("fullread", cmd) == 0) {
			system("ssdProject.exe r 12");
		}
		else if (strcmp("testapp1", cmd) == 0) {
			//fullwrite
			system("ssdProject.exe w 12");
			//fullread
			system("ssdProject.exe r 12");
		}
		else if (strcmp("testapp2", cmd) == 0) {

			strcpy(input, "0xAAAABBBB");
			for (int j = 0; j < 30; j++) {
				for (int i = 0; i <= 5; i++) {
					line = i;
					write();
				}
			}
			strcpy(input, "0x12345678");
			for (int i = 0; i <= 5; i++) {
				line = i;
				write();
			}
			
			for (int i = 0; i <= 5; i++) {
				line = i;
				read();
			}
		}
		else if (strcmp("exit", cmd) == 0) {
			printf("END");
			break;
		}
		else {
			printf("INVALID COMMAND\N");
		}
	}

	return 0;
}