# midi-to-51
MIDI文件转51单片机代码

https://www.bilibili.com/video/BV1fh411k7oW#reply4052668545

需要安装python3，可能需要某个版本的.net运行库

还是不行就试试管理员下运行：

```
pip install argparse csv
```

或者把错误信息发在issue里


## 使用方法：

把midi文件拖到midi_to_51.bat上，然后把生成的beep.h拖到keil文件夹中，替换里面的文件，确认一下单片机型号正确，具体可以看main.c注释，编译keil工程，烧录到单片机。

## 如果不能正确播放：

如果数组是空的，可能是音轨选择错误。删除midi_to_51.bat第三行，然后再把midi拖上去，用记事本打开生成的out.csv文件

0, 0, Header, 1, 2, 480

1, 0, Start_track

1, 0, Title_t, "new"

1, 0, Tempo, 600000

1, 0, Time_signature, 4, 2, 24, 8

1, 0, End_track

2, 0, Start_track

2, 0, Title_t, "MIDI"

2, 0, Note_on_c, 0, 76, 64

2, 0, Program_c, 0, 80

2, 0, Control_c, 0, 0, 0

2, 80, Note_off_c, 0, 76, 0

2, 120, Note_on_c, 0, 76, 64

2, 200, Note_off_c, 0, 76, 0

2, 360, Note_on_c, 0, 76, 64

第一列就是音轨信息，可以一个一个试带有Note_on_c的音轨

有些midi文件开头可能有一段空白，如果想去掉，到生成的beep.h里删除数组开头的第一个 'S',___

如果声音很奇怪，可能是音轨选错了，也可能是单片机频率变了，或者换了其它型号的单片机。我用的是STC15W104，理论上STC12应该不用改，看一下手册吧。

## 定时器初值计算：

如果换了晶振频率（我用的是12M），需要用freq2timer重新计算初值：

修改freq2timer.py第一行，改成自己的晶振频率（单位：Hz）

当前目录命令行输入python freq2timer.py，把生成的note.h拖入keil文件夹。

## 已知问题：

只支持单音轨，可以在python代码中的选择，一般是第二个

同一时间不能出现两个以上音符，不然声音会乱
