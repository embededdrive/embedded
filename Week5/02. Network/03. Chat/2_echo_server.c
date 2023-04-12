#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>

// 서비스할 포트 미리 정해둠
const char *PORT = "12345";

// file descriptor
// 소켓도 파일
// 파일에 쓰기 = 송신
// 파일을 읽기 = 수신

int server_sock;
int client_sock;

// exit(0) 정상적인 종료
// exit(1) 에러가 있는 경우 종료
// socket close
void interrupt(int arg)
{
	printf("\nYou typed Ctrl + C\n");
	printf("Bye\n");

	close(client_sock);
	close(server_sock);
	exit(1);
}

void removeEnterChar(char *buf)
{
	int len = strlen(buf);
	for (int i = len - 1; i >= 0; i--)
	{
		if (buf[i] == '\n')
			buf[i] = '\0';
		break;
	}
}

int main()
{
	// Ctrl + C 누를 경우 안전종료
	signal(SIGINT, interrupt);


	// 1) 소켓 생성
	// sys/socket.h 함수
	// PF_INET : IPv4
	// SOCK_STREAM : TCP
	// 다른 타입 (TCP / IP 1가지 뿐이므로 0)
	// TCP / IP로 소켓 생성
	server_sock = socket(PF_INET, SOCK_STREAM, 0);
	if (server_sock == -1)
	{
		printf("ERROR :: 1_Socket Create Error\n");
		exit(1);
	}

	// 소켓 옵션설정
	// 종료 시 3분 정도 동일한 포트 배정 불가 에러 해결
	int optval = 1;
	setsockopt(server_sock, SOL_SOCKET, SO_REUSEADDR, (void *)&optval, sizeof(optval));

	// 주소 설정
	// sockaddr_in 구조체 변수 server_addr 초기화
	// AF_INET : IPv4
	// Host TO Network, Long
	// INADDR : 현재 서버내 IP
	// host(빅 / 리틀) ==> 네트워크(빅)
	// Host TO Network, Short
	// 포트
	// host(빅 / 리틀) ==> 네트워크(빅)
	struct sockaddr_in server_addr = {0};
	server_addr.sin_family = AF_INET;
	server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
	server_addr.sin_port = htons(atoi(PORT));

	// 2) 소켓에 주소 할당
	// kernel이 이해할 수 있도록 구조체 형변환
	if (bind(server_sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1)
	{
		printf("ERROR :: 2_bind Error\n");
		exit(1);
	}

	// 3) 클라이언트 연결 요청 대기
	// 대기열 생성
	// 메모리와 CPU에 의하여 결정
	if (listen(server_sock, 5) == -1)
	{
		printf("ERROR :: 3_listen Error");
		exit(1);
	}

	client_sock = 0;
	struct sockaddr_in client_addr = {0};
	socklen_t client_addr_len = sizeof(client_addr);

	while (1)
	{
		// 새로운 클라이언트를 위해 초기화
		memset(&client_addr, 0, sizeof(client_addr));

		// 정보를 받음
		// 4) 클라이언트 연결 승인
		client_sock = accept(server_sock, (struct sockaddr *)&client_addr, &client_addr_len);
		if (client_sock == -1)
		{
			printf("ERROR :: 4_accept Error\n");
			break;
		}

		// read & write
		char buf[100];
		while (1)
		{
			memset(buf, 0, 100);
			// 5) 통신
			// read : 수신
			int len = read(client_sock, buf, 99);

			// 개행문자 '\n' 삭제
			removeEnterChar(buf);

			// client 와 연결이 끊어졌을 때 클라이언트 종료
			if (len == 0)
			{
				printf("INFO :: Disconnect with client... BYE\n");
				break;
			}

			// client 에서 exit 입력했을 때 클라이언트 종료
			if (!strcmp("exit", buf))
			{
				printf("INFO :: Client want close... BYE\n");
				break;
			}
			// write : 송신
			write(client_sock, buf, strlen(buf));
		}
		// 6) 클라이언트 소켓 close
		close(client_sock);
	}
	// 6) 서버 소켓 close
	close(server_sock);
	return 0;
}
