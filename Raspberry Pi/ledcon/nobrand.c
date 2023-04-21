#include <linux/module.h>
#include <linux/fs.h>
#include <asm/io.h>
#include <linux/gpio.h>
#include <linux/uaccess.h>

#define NOD_MAJOR 100
#define NOD_NAME "nobrand"

MODULE_LICENSE("GPL");

typedef struct _Node_{
	int lev1;
	int lev2;
} Node;

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

static void led1on(void){
	gpio_set_value(23,1);
	printk(KERN_INFO "led on\n");
}
static void led1off(void){
	gpio_set_value(23,0);
	printk(KERN_INFO "led off\n");
}

static void led2on(void){
	gpio_set_value(18,1);
	printk(KERN_INFO "led on\n");
}
static void led2off(void){
	gpio_set_value(18,0);
	printk(KERN_INFO "led off\n");
}

int lev1, lev2;
int ret1, ret2;
static long nobrand_ioctl(struct file *filp, unsigned int cmd, unsigned long arg){
	Node t = {0, 0}, r;
	int ret;
	void *p = (void *)(arg);

	switch(cmd){
		case _IO(0,3):
			lev1 = gpio_get_value(3);
			lev2 = gpio_get_value(2);
			printk(KERN_INFO "btn1 = %d, btn2 = %d\n", lev1, lev2);
			t.lev1 = lev1;
			t.lev2 = lev2;

			printk(KERN_INFO "Copy to user struct!");
			ret = copy_to_user(p, &t, sizeof(Node));
			printk(KERN_ALERT "Complete!");
			break;
		case _IO(0,4):
			printk(KERN_INFO "Copy from user struct!");
			ret = copy_from_user( &r, p, sizeof(Node));
			printk(KERN_ALERT "led1 = %d, led2 = %d\n", r.lev1, r.lev2);
			
			if (!r.lev1)
				led1on();
			else
				led1off();
			if (!r.lev2)
				led2on();
			else
				led2off();
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
	gpio_request(23,"LED");
	gpio_direction_output(23,0);

	gpio_request(2,"BTN");
	gpio_direction_input(2);
	gpio_request(3,"BTN");
	gpio_direction_input(3);

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
	gpio_free(23);
	gpio_free(2);
	gpio_free(3);

	unregister_chrdev(NOD_MAJOR, NOD_NAME);
    printk(KERN_INFO "bye\n");
}

module_init(nobrand_init);
module_exit(nobrand_exit);

