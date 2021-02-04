//单片机型号：STC15w104
//晶振频率：12MHz
//如果更换型号或晶振频率不同请用stcisp重新生成Delay40ms函数
//如果修改了晶振频率请修改freq2timer.py第一行定义的晶振频率(单位：Hz)并执行，然后把生成的tone.h文件复制到keil文件夹
#include <STC89C5xRC.H>
#include "beep.h"
#include "tone.h"

sbit BEEP = P3^5;													//输出端口,对应T0CLKO，防止蜂鸣器关闭后消耗电流
sfr WAKE_CLKO = 0x8f;               //wakeup and clock output control register
unsigned int t0tmp;
#define beep(tone) TL0 = tonetofreq[tone];TH0 = tonetofreq[tone] >>8

void Delay40ms(unsigned char tm)		//@12.000MHz STC15w104，STCISP生成的只能延时固定时间，需要增加一个while循环
{
	++tm;
	while(--tm)
	{
		unsigned char i, j, k;

	i = 2;
	j = 211;
	k = 231;
	do
	{
		do
		{
			while (--k);
		} while (--j);
	} while (--i);
	}
}

void play(unsigned char *table)
{
	unsigned int pos = 0;
	while(1)
	{
		BEEP = 0;
		if(table[pos] == 'B')
		{
			TR0 = 1;
			beep(table[pos+1]);
			Delay40ms(table[pos+2]);
			TR0 = 0;
			BEEP = 0;
			BEEP = 0;
			BEEP = 0;
			pos += 3;
			
		}
		else if(table[pos] == 'S')
		{
			TR0 = 0;
			BEEP = 0;
			BEEP = 0;
			BEEP = 0;
			Delay40ms(table[pos+1]);
			pos += 2;
			BEEP = 0;
			BEEP = 0;
			BEEP = 0;
		}
		else if(table[pos] == 'T')
		{
			TR0 = 0;
			BEEP = 0;
			BEEP = 0;
			BEEP = 0;
			return;
		}
		else return;
	}
}

void main()
{
	AUXR &= 0x7F;		//定时器时钟12T模式
	TMOD = 0;
	TR0 = 0;
  WAKE_CLKO = 0x01;               //enable timer0 clock output
	EA = 1;
	play(beeptable);
	while(1);
}
