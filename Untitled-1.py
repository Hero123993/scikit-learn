
def coin (total_value , coin_10 , coin_5 , coin_1 ):
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);



int pinSpeed_1 = 32;
int pinSpeed_2 = 33;
int pinSpeed_3 = 34;

int state_Speed_1 = 0;
int state_Speed_2 = 0;
int state_Speed_3 = 0;

int coin_10 = 0 ;
int coin_5 = 0 ;
int coin_1 = 0 ;

int oneClink_1 = 0;
int oneClink_2 = 0;
int oneClink_3 = 0;
int coin_total = 0;

int total_value = (coin_1 * 1) + (coin_5 * 5) + (coin_10 * 10);



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Micro Projects TH");

  pinMode(pinSpeed_1, INPUT); 
  pinMode(pinSpeed_2, INPUT); 
  pinMode(pinSpeed_3, INPUT);



  lcd.init();
  lcd.backlight();
  lcd.print("***WELCOME TO***");
  lcd.setCursor(0, 1);
  lcd.print("----2P2K1P1W---- ");
  
 
 delay(10000);



  lcd.clear();

}

void loop() {
  // put your main code here, to run repeatedly:
  state_Speed_1 = digitalRead(pinSpeed_1);
  state_Speed_2 = digitalRead(pinSpeed_2);
  state_Speed_3 = digitalRead(pinSpeed_3);

  Serial.print("state_Speed_1 : "); Serial.println(state_Speed_1);
  Serial.print("state_Speed_2 : "); Serial.println(state_Speed_2);
  Serial.print("state_Speed_3 : "); Serial.println(state_Speed_3);


  if (state_Speed_1 == 1) {
    if (oneClink_1 == 0) {
      oneClink_1 = 1;
      coin_1 ++;
    }
  }
  else if (state_Speed_1 == 0 ) {
    oneClink_1 = 0;
  }



  if (state_Speed_2 == 1) {
    if (oneClink_2 == 0) {
      oneClink_2 = 1;
      coin_5++;
    }
  }
  else if (state_Speed_2 == 0 ) {
    oneClink_2 = 0;
  }



  if (state_Speed_3 == 1) {
    if (oneClink_3 == 0) {
      oneClink_3 = 1;
      coin_10 ++;
    }
  }
  else if (state_Speed_3 == 0 ) {
    oneClink_3 = 0;
  }


coin_total = coin_1 + coin_5 + coin_10;

  Serial.print("coin_1 : "); Serial.println(coin_1);
  Serial.print("coin_5 : "); Serial.println(coin_5);
  Serial.print("coin_10 : "); Serial.println(coin_10);
  Serial.print("Total Coins : "); Serial.println(coin_total);
//
//
  Serial.println("************************************************");
  Serial.println("************************************************");
  Serial.println();


  lcd.setCursor(0, 0);
  lcd.print("c_1 :");
  lcd.print(coin_1);


  lcd.setCursor(9, 0);
  lcd.print("c_5 :");
  lcd.print(coin_5);

  lcd.setCursor(0, 1);
  lcd.print("c_10 :");
  lcd.print(coin_10);

  lcd.setCursor(9, 1);  // ตำแหน่งสำหรับแสดงผลรวม
  lcd.print("ALL:");
  lcd.print(coin_total);
  lcd.print("   ");

  delay(100);

  
}