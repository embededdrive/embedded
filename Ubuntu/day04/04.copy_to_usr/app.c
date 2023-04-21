#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/ioctl.h>

char buf[30];

int main(){
	int fd = open("/dev/nobrand", O_RDWR);
	if ( fd<0 ){
		printf("ERROR\n");
		close(fd);
		exit(1);
	}

	ioctl(fd, _IO(0, 3), buf);
	printf("%s\n", buf);

	close(fd);
	return 0;
}