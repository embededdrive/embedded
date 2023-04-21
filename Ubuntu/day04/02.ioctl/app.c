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

	int n;
	while(1) {
		scanf("%d", &n);
		int ret = ioctl(fd, _IO(0, n), 0);
		if (ret < 0) {
			printf("command invalid!\n");
			break;
		}
	}

	close(fd);
	return 0;
}