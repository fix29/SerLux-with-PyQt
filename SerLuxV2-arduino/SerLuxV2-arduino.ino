#include <Servo.h>
Servo srvosaya;
int derajat = 0; //variabel untuk menyimpan nilai 'derajat'
int nilai_ldr = 0; //variabel untuk menyimpan 'nilai_ldr'
int cont1 = 0; //variabel konversi dari data mentah ke Lux
int batasBawah = 350; //var. sebagai baseline bawah
int batasAtas = 550; //var. sebagai baseline atas
int ledku = 8; //led saya terpasang pada pin digital #8

/**************************************************************************/
#define MAX_ADC_READING           1023 //Karena resolusi ADC nya 10bits
#define ADC_REF_VOLTAGE           5.0 //Tegangan pensuplai LDR (4.6V;5.0V)
#define REF_RESISTANCE            5030  // untuk hasil terbaik didapatkan dengan cara mengukurnya
#define LUX_CALC_SCALAR           12518931 //guestimasi dari dataset
#define LUX_CALC_EXPONENT         -1.405 //guestimasi dari dataset
/**************************************************************************/

void setup() // put your setup code here, to run once:
  {
    srvosaya.attach(9);
    pinMode(ledku,OUTPUT);
    Serial.begin(9600);
    srvosaya.write(0);
  }
  
void loop() // put your main code here, to run repeatedly:
  { 
    if(Serial.available()>0)
    {
       derajat = Serial.parseInt();
       nilai_ldr = analogRead(A0);
         
    if (derajat != 0)
      {
       srvosaya.write(derajat);
       map(derajat,0,180,0,255);
      }
    }
    else //led @pin 8 mati dan hidup sesuai persyaratan di bawah
    {
       int nilai_ldr1= analogRead(A0);
        
           if (nilai_ldr1 < batasBawah){
              digitalWrite(ledku, HIGH);
               }
           if (nilai_ldr1 > batasAtas){ 
               digitalWrite(ledku, LOW);
               }
               
//***********Proses tahapan konversi dari data raw A0 ke 'Lux'******************//  
        int   ldrRawData;
        float resistorVoltage, ldrVoltage;
        float ldrResistance;
        float ldrLux;
  
        // Konversi ADC dimulai
        ldrRawData = analogRead(A0);
  
        // RESISTOR VOLTAGE_CONVERSION
        // Konversikan kembali data digital mentah ke voltase yang diukur pada pin analog
        resistorVoltage = (float)ldrRawData / MAX_ADC_READING * ADC_REF_VOLTAGE;

        // Tegangan di LDR adalah suplai 5V dikurangi tegangan resistor 5k
        ldrVoltage = ADC_REF_VOLTAGE - resistorVoltage;
  
         // LDR_RESISTANCE_CONVERSION
        // Resistansi yang dimiliki LDR pada tegangan tertentu  
        ldrResistance = ldrVoltage/resistorVoltage * REF_RESISTANCE;
  
        // LDR_LUX
        // Tahap akhir - Konversi ldrResistance ke ldrLux ->> unit dalam Lux telah didapat (estimasi)
        ldrLux = LUX_CALC_SCALAR * pow(ldrResistance, LUX_CALC_EXPONENT);
        cont1 = ldrLux;
        
    }
  }
