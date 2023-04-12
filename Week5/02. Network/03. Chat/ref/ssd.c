#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {


	if (argc == 1)
	{
		return 0;
	}

	char cmd = argv[1][0];

	int line = atoi(argv[2]);


	FILE *fp;
	if (cmd == 'W')
	{
		char input[20];

		strcpy(input, argv[3]);

		int inputLen = strlen(input);

		input[inputLen] = '\n';
		input[inputLen + 1] = '\0';

		//printf("input : %s\n", input);


		fp = fopen("nand.txt", "r");

		char buf[100][12];

		for (int i = 0; i < 100; i++)
		{
			fgets(buf[i], 12, fp);
			//printf("buf %d : %s", i, buf[i]);
		}

		fclose(fp);

		fp = fopen("nand.txt", "w");

		for (int i = 0; i < 100; i++)
		{
			if (i == line)
			{
				fputs(input, fp);
			}
			else {
				fputs(buf[i], fp);
			}
		}

		fclose(fp);

		// fputs(input, fp);
	}
	else if (cmd == 'R')
	{
		fp = fopen("nand.txt", "r");

		char target[12];

		for (int i = 0; i <= line; i++)
		{
			fgets(target, 12, fp);

		}

		fclose(fp);

		fp = fopen("result.txt", "w");

		fputs(target, fp);

		fclose(fp);
	}
	else if (cmd == 'w')
	{
		fp = fopen("nand.txt", "w");

		for (int i = 0; i < 100; i++)
		{
			fputs("0xABCDFFFF\n", fp);
		}

		fclose(fp);
	}
	else if (cmd == 'r')
	{
		fp = fopen("nand.txt", "r");

		char target[12];

		for (int i = 0; i <= 100; i++)
		{
			fgets(target, 12, fp);

			printf("%s", target);

		}

		fclose(fp);
	}

	// system("cls");

	return 0;
}