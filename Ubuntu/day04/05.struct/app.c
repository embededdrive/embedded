#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/ioctl.h>

typedef struct _Node_ {
	char n;
	char buf[100];
} Node;

int main(){
	int fd = open("/dev/nobrand", O_RDWR);
	if ( fd<0 ){
		printf("ERROR\n");
		close(fd);
		exit(1);
	}

	Node t = {10, "STRUCT MESSAGE!"};
	ioctl(fd, _IO(0, 3), &t);
	printf("struct complete\n");

	close(fd);
	return 0;
}