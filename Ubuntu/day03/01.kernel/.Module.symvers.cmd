cmd_/home/yong/work/day03/Module.symvers := sed 's/\.ko$$/\.o/' /home/yong/work/day03/modules.order | scripts/mod/modpost -m -a  -o /home/yong/work/day03/Module.symvers -e -i Module.symvers   -T -
