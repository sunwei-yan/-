#include ".\CORE\STC8Ax_REG.H"
sbit PWM=P2^1;  //定义给舵机信号线接的I/O口
void UartInit(void)		//9600bps@11.0592MHz
{
	SCON = 0x50;		//8位数据,可变波特率
	AUXR |= 0x40;		//定时器时钟1T模式
	AUXR &= 0xFE;		//串口1选择定时器1为波特率发生器
	TMOD &= 0x0F;		//设置定时器模式
	TL1 = 0xE0;		//设置定时初始值
	TH1 = 0xFE;		//设置定时初始值
	ET1 = 0;		//禁止定时器%d中断
	TR1 = 1;		//定时器1开始计时
}
void send(char dat){
SBUF=dat;
while(!TI){
	TI=0;
}
}

void dalay(int ms){
	int i=0,j=0;
	for (i=0;i<5000;i++){
		for (j=0;j<ms;j++);
	}
}
void Delay(unsigned char i)   //12MHz 延时函数  
{
    unsigned char a,b;        //该段延时函数Delay(1)=0.5ms
    for(;i>0;i--)
      for(b=71;b>0;b--)
        for(a=2;a>0;a--);
}
void zero(void) //0度 子程序
{   
        PWM=1;
        Delay(1);       //高电平 Delay(1)=0.5ms。因为周期为20ms，所以低电平就是19.5ms 
        PWM=0;
        Delay(39);      //低电平 Delay(39)=19.5ms
}
void three(void) //135度 子程序
{
        PWM=1;
        Delay(4);       //高电平 Delay(4)=2ms
        PWM=0;
        Delay(36);      //低电平 18ms
}

sbit l1=P0^4;
sbit l2=P0^5;
sbit l3=P0^6;
sbit l4=P0^7;
sbit k1=P1^0;
sbit key=P5^1;
int flag=1;
void main(){
	
//	P_SW1 &=0x0f;
//	P_SW1 |=0x80;
	P0M0=0;
	P0M1=0;
P2M0=0;
P2M1=0; 
	UartInit();

	 if(SBUF=='1')   //按键接P3^1口。如果按键按下
		{
		  Delay(20);   
			 if(SBUF=='1'){three();  //如果按键按下，调用舵机90度子程序，实现转动90度。
l2=0;			 }    
             
		}
 
		 else         //否则
		    zero();   //舵机为0度
    }
	
	


//	
//RI = 0;//清除接收中断标志位	
//	SBUF = '6';//将接收到的数据放回发送缓存器
//	while(!TI);//等待发送数据完成
//	TI = 0;//清除发送中断标志位
//	
