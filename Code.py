import RPi.GPIO as io
from smbus2 import SMBus 
from time import sleep

io.setwarnings(False)

io.setmode(io.BCM)

def init_pins( mux_Select_pins, i2c_mux_rst_pin, mod_sel_pins, output_pins ):

    for i in mux_Select_pins:
        io.setup(i,io.OUT)

    for i in mod_sel_pins:
        io.setup(i,io.OUT)

    for i in output_pins:
        io.setup(i,io.OUT)
    return 0

def select_module(mod_num):
    write_data = [0,0,0]
    if mod_num == 1:
        write_data = [0,0,0]
    elif mod_num == 2:
        write_data = [0,0,1]
    elif mod_num == 3:
        write_data = [0,1,0]
    elif mod_num == 4:
        write_data = [0,1,1]
    elif mod_num == 5:
        write_data = [1,0,0]
    elif mod_num == 6:
        write_data = [1,0,1]
    elif mod_num == 7:
        write_data = [1,1,0]
    elif mod_num == 8:
        write_data = [1,1,1]

    for i in range (0,3):
        print(type(mod_sel_pins[i]))
        io.output(mod_sel_pins[i],write_data[i])
    
    bus.write_byte(0x70, 1 << (mod_num-1))

    return 0

def select_mux(mux_num):

    A0 = 0X40
    A1 = 0X41
    A2 = 0X42

    if mux_num == 1:
        bus.write_byte( 0x48, A0 )
    elif mux_num == 2:
        bus.write_byte( 0x48, A1 )
    elif mux_num == 3:
        bus.write_byte( 0x48, A2 )

    return 0

def select_sensor(sensor_num):
    write_data = [0,0,0,0]
    if sensor_num == 1:
        write_data = [0,0,0,0]
    elif sensor_num == 2:
        write_data = [0,0,0,1]
    elif sensor_num == 3:
        write_data = [0,0,1,0]
    elif sensor_num == 4:
        write_data = [0,0,1,1]
    elif sensor_num == 5:
        write_data = [0,1,0,0]
    elif sensor_num == 6:
        write_data = [0,1,0,1]
    elif sensor_num == 7:
        write_data = [0,1,1,0]
    elif sensor_num == 8:
        write_data = [0,1,1,1]
    elif sensor_num == 9:
        write_data = [1,0,0,0]
    elif sensor_num == 10:
        write_data = [1,0,0,1]
    elif sensor_num == 11:
        write_data = [1,0,1,0]
    elif sensor_num == 12:
        write_data = [1,0,1,1]
    elif sensor_num == 13:
        write_data = [1,1,0,0]
    elif sensor_num == 14:
        write_data = [1,1,0,1]
    elif sensor_num == 15:
        write_data = [1,1,1,0]
    elif sensor_num == 16:
        write_data = [1,1,1,1]
    
    for i in range (0,4):
        io.OUTPUT(mod_sel_pins[i],write_data[i])
    
    return 0

def read_sensor_data():
    value = bus.read_byte(0x48)
    return value

def output(out, output_pins):
    io.OUTPUT(outpout_pins[3],0)
    sleep(0.000000050)
    io.OUTPUT(outpout_pins[1],1)
    sleep(0.000000050)
    io.OUTPUT(outpout_pins[1],0)
    sleep(0.000000050)
    while(data!=0):
        data = 0b01 & out
        io.OUTPUT(outpout_pins[0],data)
        io.OUTPUT(outpout_pins[2],1)
        sleep(0.000000100)
        io.OUTPUT(outpout_pins[2],0)
        sleep(0.000000100)
        out = out >> 1
    io.OUTPUT(outpout_pins[3],1)
    sleep(0.000000050)
    return 

mux_Select_pins = [13,6,5,0]
i2c_mux_rst_pin = 4
mod_sel_pins = {22,27,17}
outpout_pins = {14,15,18,23}

init_pins( mux_Select_pins, i2c_mux_rst_pin, mod_sel_pins, output_pins ) #Initialize pins
bus = SMBus(1) #Initialize I2C
select_module(1) #Select the module
select_sensor(1) #Select from which sensor we need input
select_mux(1) #Select from which mux we need the input using ADC Input Selection
value = read_sensor_data() #Read data from selected sensor

out = 0b01
output(out,outpout_pins)
