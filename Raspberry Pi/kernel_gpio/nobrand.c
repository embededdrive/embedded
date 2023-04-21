#include <linux/module.h>
#include <linux/fs.h>
#include <asm/io.h>
#include <linux/gpio.h>

#define NOD_MAJOR 100
#define NOD_NAME "nobrand"

MODULE_LICENSE("GPL");

static int nobrand_open(struct inode *inode, struct file *filp)
{
    printk(KERN_INFO "welcome\n");
    return 0;
}

static int nobrand_release(struct inode *inode, struct file *filp)
{
    printk(KERN_INFO "release\n");
    return 0;
}

static void ledon(void){
	gpio_set_value(18,1);
	printk(KERN_INFO "led on\n");
}
static void ledoff(void){
	gpio_set_value(18,0);
	printk(KERN_INFO "led off\n");
}

int lev;
int ret;
static long nobrand_ioctl(struct file *filp, unsigned int cmd, unsigned long arg){
	switch(cmd){
		case _IO(0,3):
			ledon();
			break;
		case _IO(0,4):
			ledoff();
			break;
		case _IO(0,5):
			lev = gpio_get_value(2);
			printk(KERN_INFO "btn = %d\n", lev);
			ret = copy_to_user((void*)arg, &lev, sizeof(int));
			break;
	}
	return 0;
}

static struct file_operations fops = {
    .open = nobrand_open,
    .release = nobrand_release,
	.unlocked_ioctl = nobrand_ioctl,
};

static int nobrand_init(void)
{
	gpio_request(18,"LED");
	gpio_direction_output(18,0);

	gpio_request(2,"BTN");
	gpio_direction_input(2);

    if (register_chrdev(NOD_MAJOR, NOD_NAME, &fops) < 0)
    {
        printk("INIT FALE\n");
    }
	
    printk(KERN_INFO "hi\n");
    return 0;
}

static void nobrand_exit(void)
{
	gpio_free(18);
	gpio_free(2);

	unregister_chrdev(NOD_MAJOR, NOD_NAME);
    printk(KERN_INFO "bye\n");
}

module_init(nobrand_init);
module_exit(nobrand_exit);

