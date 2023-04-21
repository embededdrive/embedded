#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/ioctl.h>

int main(){
	int fd = open("/dev/nobrand", O_RDWR);
	if ( fd<0 ){
		printf("ERROR\n");
		close(fd);
		exit(1);
	}

	// Ioctl
	ioctl(fd, 3, 1234);
	ioctl(fd, 4, 9012);
	ioctl(fd, 5, 5678);

	printf("Is it now?\n");

	// Write
	// write(fd, "KFC ZZANG\n", 7);

	// Read
	// char buf[100];
	// read(fd, buf, 100);
	// printf("%s\n", buf);

	close(fd);
	return 0;
}