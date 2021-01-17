config_template="""
[global]
name=fio-rand-RW
filename=/media/ubuntu/disk2/fio-rand-RW
rw=randrw
rwmixread=<rwmixread>
rwmixwrite=<rwmixwrite>
bs=<bs>
direct=1
numjobs=4
time_based
runtime=60

[file1]
size=24G
ioengine=libaio
iodepth=80
"""
for bs in ['4k','8k','16k']:
  for read_ratio in [0,30,100]:
    rwmixread = str(read_ratio)
    rwmixwrite = str(100-read_ratio)
    config_out = config_template.replace("<bs>",bs).replace("<rwmixread>",rwmixread).replace("<rwmixwrite>",rwmixwrite)
    config_out_file = open("fio-" + bs + "-"+ "r" + rwmixread + "-" + "w" + rwmixwrite+".fio","w")
    config_out_file.write(config_out)
    config_out_file.close()
