#include <linux/module.h>
#include <linux/fs.h>
#include <linux/uaccess.h>

#define NOD_MAJOR 100
#define NOD_NAME "nobrand"

MODULE_LICENSE("GPL");

typedef struct _Node_ {
	char n;
	char buf[100];
} Node;

static int nobrand_open(struct inode *inode, struct file *filp){
	printk( KERN_INFO "welcome\n");
	return 0;
}
static int nobrand_release(struct inode *inode, struct file *filp){
	printk( KERN_INFO "release\n");
	return 0;
}

static ssize_t nobrand_read(struct file *flip, char *buf, size_t count, loff_t *ppos)
{
	buf[0] = 'H';
	buf[1] = 'I';
	buf[2] = '\0';
	return count;
}

static ssize_t nobrand_write(struct file *flip, const char *buf, size_t count, loff_t *ppos)
{
	printk(KERN_INFO "app msg : %s\n", buf);
	return count;
}

static long nobrand_ioctl(struct file *flip, unsigned int cmd, unsigned long arg){
	Node t = {20, "Kernel Struct"};
	int ret;
	void *p = (void *)(arg);
	switch (cmd)
	{
		case _IO(0, 3):
			printk(KERN_INFO "Copy to user struct!");
			ret = copy_to_user(p, &t, sizeof(Node));
			printk(KERN_ALERT "Complete!");
			break;
	}
	return 0;
}

static struct file_operations fops = {
	.open = nobrand_open,
	.release = nobrand_release,
	.read = nobrand_read,
	.write = nobrand_write,
	.unlocked_ioctl = nobrand_ioctl,
};

static int nobrand_init(void){
	if( register_chrdev(NOD_MAJOR, NOD_NAME, &fops) < 0) {
		printk("INIT FAIL\n");
	}
	printk( KERN_INFO "hi\n" );
	return 0;
}

static void nobrand_exit(void){
	unregister_chrdev(NOD_MAJOR, NOD_NAME);
	printk( KERN_INFO "bye\n");
}

module_init(nobrand_init);
module_exit(nobrand_exit);

