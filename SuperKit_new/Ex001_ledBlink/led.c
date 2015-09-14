# include <wiringPi.h>
# include <stdio.h>

# define LedPin	0
int main(void)
{
	if(wiringPiSetup() == -1) {
		printf("setup wiringPi failed");
		return 1;
	}

	pinMode(LedPin, OUTPUT);

	while(1){
		digitalWrite(LedPin, LOW);
		printf("led ON\n");
		delay(50);
		digitalWrite(LedPin, HIGH);
		printf("lef OFF\n");
		delay(500);
	}
	return 0;
}

