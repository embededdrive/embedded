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

	Node t;
	ioctl(fd, _IO(0, 3), &t);
	printf("Copy to kernel struct!\n");
	printf("struct n : %d\n", (int)t.n);
	printf("struct buf : %s\n", t.buf);

	close(fd);
	return 0;
}