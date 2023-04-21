#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ioctl.h>

typedef struct _Node_{
	int lev1;
	int lev2;
} Node;

int main()
{
    int fd = open("/dev/nobrand", O_RDWR);
    if (fd < 0)
    {
        printf("ERROR\n");
		exit(1);
    }

	while(1){	
		Node r;
		ioctl(fd, _IO(0,3), &r);
		printf("BTN1 = %d, BTN2 = %d\n", r.lev1, r.lev2);

		ioctl(fd, _IO(0,4), &r);
		usleep(100 * 1000);
	}
	close(fd);
    return 0;
}

