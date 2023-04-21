#include <fcntl.h>
#include <sys/ioctl.h>

int init()
{
    int fd = open("/dev/nobrand", O_RDWR);
    return fd;
}

void ledon(int fd)
{
    ioctl(fd, _IO(0, 3), 0);
}

void ledoff(int fd)
{
    ioctl(fd, _IO(0, 4), 0);
}

void finalization(int fd)
{
    close(fd);
}
