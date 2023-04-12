
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
		printf("유효하지 않은 숫자입니다");

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
			printf("테스트 셸 매뉴얼\n\n");
			printf("write \n");
			printf("    write LBA주소 4바이트값\n");
			printf("    * ex) write 3 0xABCDABCD\n");
			printf("    * LBA 주소는 0 - 99 사이입니다.\n");
			printf("    * 반드시 0xAAAAAAAA 형식의 16진수 10글자로 입력합니다.\n");
			printf("    * 결과는 nand.txt 에 기록됩니다.\n");
			printf("\n");
			printf("read \n");
			printf("    read LBA주소\n");
			printf("    ex) write 4\n");
			printf("    * 결과는 result.txt 에 작성됩니다.\n");
			printf("\n");
			printf("fullwrite \n");
			printf("    fullwrite\n");
			printf("    * nand.txt 의 모든 값을 0xABCDFFFF 로 변경합니다.\n");
			printf("\n");
			printf("fullread \n");
			printf("    fullread\n");
			printf("    * nand.txt 의 모든 LBA 에 대해 read 수행 후, 셸에 모든 LBA 값을 출력합니다.\n");
			printf("\n");
			printf("testapp1 \n");
			printf("    testapp1 \n");
			printf("    * fullwrite 수행 후 fullread 수행합니다\n");
			printf("\n");
			printf("testapp2 \n");
			printf("    testapp2 \n");
			printf("    * 0 ~ 5 번 LBA 에 0xAAAABBBB 값으로 총 30번 Write를 수행합니다.\n");
			printf("    * 0 ~ 5 번 LBA 에 0x12345678 값으로 1 회 Over Write를 수행합니다.\n");
			printf("    * 0 ~ 5 번 LBA Read 했을 때 정상적으로 값이 읽히는지 확인합니다.\n");
			printf("\n");
			printf("exit 명령어 입력 시 이 프로그램은 종료됩니다.");
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