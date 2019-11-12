# ADC Experiment
import visa
import numpy as np
import time
import serial

# Input v al u e s
com_port = 'COM3'
baud_rate = 9600
awg_address = 'USB0::0x0957::0x1799::MY58100818::INSTR' # AWG Address
awg_volts = np.linspace(0,5,101) # Duty c y c l e v e c t o r (%)
num_points=len(awg_volts)

# Initialize important matrices
ADC_measured=np.zeros(len(awg_volts))
ADC_expected=[int(x/5*1024) for x in awg_volts]

# Initiate communications with and open instruments
rm = visa.ResourceManager()
awg = rm.open_resource(awg_address)

# Place waveform generator in High−Z
awg.write("OUTP:LOAD INF")

# Initialize and open serial communications
arduino = serial.Serial(com_port, baud_rate)
arduino.reset_input_buffer()

# Per form measurements
count=0
for V in awg_volts:
    print("Analyzing Voltage %f" %V)
    awg.write("APPL:DC DEF,DEF,"+str(V))  # AWG output signal
    arduino.reset_input_buffer()
    time.sleep(2)  # Pauses to guarantee a good RPM count
    # Get ADC value from Arduino
    arduino.write(b'1\n')
    #arduino.reset_output_buffer()
    time.sleep(2)
    ADC_measured[count] = float(arduino.readline())
    count += 1

# Close communications
savename=experiment_name+'_data.csv'
arduino.close()
awg.close()
with open(savename,'w') as f:
    f.write( "AWG Voltage, ADC Value Expected, ADC Value Measured\n")
    for val in range (len(awg_volts)):
        f.write( "{vol}, {ADCe}, {ADCm}\n".format (vol=awg_volts[val] ,
                                                    ADCe=ADC_expected [val] ,
                                                    ADCm=ADC_measured [val]))
