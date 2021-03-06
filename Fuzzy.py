import math

print('Implement Fuzzy logic')

#input
input_temperature     = input('Temperture     = ')
input_humidity        = input('Humidity       = ')
input_Soil_moisture   = input('Soil moisture  = ')
input_Light_intesity  = input('Light intesity = ')

#store input to variable
temp     = int(input_temperature)
humidity = int(input_humidity)
soil     = int(input_Soil_moisture)
light    = float(input_Light_intesity)

#Implement Linguistic variable
#Temperature
if(temp <= 25):
    temp_cool = 1
    temp_warm = 0
    temp_hot = 0
elif(temp < 50):
    temp_cool = (50 - temp) / (50) 
    temp_warm = (temp) / (50)
    temp_hot = 0
elif(temp == 50):
    temp_cool = 0
    temp_warm = 1
    temp_hot = 0
elif(temp < 100):
    temp_cool = 0
    temp_warm  = (100 - temp) / (100-50)
    temp_hot = (temp-50) / (100-50)
else:
    temp_cool = 0
    temp_warm = 0
    temp_hot = 1

#Humidity
if(humidity <= 25):
    humidity_dry = 1
    humidity_humid = 0
    humidity_damp = 0
elif(humidity < 50):
    humidity_dry = (50 - humidity) / (50) 
    humidity_humid = (humidity) / (50)
    humidity_damp = 0
elif(humidity == 50):
    humidity_dry = 0
    humidity_humid = 1
    humidity_damp = 0
elif(humidity < 100):
    humidity_dry = 0
    humidity_humid = (100 - humidity) / (100-50)
    humidity_damp = (humidity-50) / (100-50)
else:
    humidity_dry = 0
    humidity_humid = 0
    humidity_damp = 1

#soil moisture
if(soil <= 25):
    soil_dry = 1
    soil_moist = 0
    soil_moistly = 0
elif(soil < 50):
    soil_dry = (50 - soil) / (50) 
    soil_moist = (soil) / (50)
    soil_moistly = 0
elif(soil == 50):
    soil_dry = 0
    soil_moist = 1
    soil_moistly = 0
elif(soil < 100):
    soil_dry = 0
    soil_moist = (100 - soil) / (100-50)
    soil_moistly = (soil-50) / (100-50)
else:
    soil_dry = 0
    soil_moist = 0
    soil_moistly = 1

#Light intensity
if(light <= 0.5):
    value_bright = 0
    value_dark  = 1
elif(light <= 1):
    value_bright = (1 - light) / (1) 
    value_dark  = (light-1) / (1)
elif(light > 1):
    value_bright = 1
    value_dark  = 0

#for add result to water pump status
waterpump_status = []
def waterpump_on1(soil):
    if soil != 0:
        waterpump_status.append([soil, 1])

def waterpump_on2(humidity, soil):
    if humidity != 0 and soil != 0:
        result = min(humidity,soil)
        waterpump_status.append([result, 1])

def waterpump_on3(temp, humidity, soil):
    if temp !=0 and humidity != 0 and soil != 0:
        result = min(temp,humidity,soil)
        waterpump_status.append([result, 1])

def waterpump_off1(soil):
    if soil != 0:
        waterpump_status.append([soil, 0])

def waterpump_off3(temp, humidity, soil):
    if temp !=0 and humidity != 0 and soil != 0:
        result = min(temp,humidity,soil)
        waterpump_status.append([result, 0])

#calculate water pump status
waterpump_on1(soil_dry)
waterpump_on2(humidity_humid, soil_moist)
waterpump_off1(soil_moistly)
waterpump_off3(temp_cool, humidity_damp, soil_moist)

#for add result to fan 1,2 status
fan_N01_status =[]
fan_N02_status =[]
def fan_N01_on1(temp):
    if temp !=0:
        fan_N01_status.append([temp, 1])

def fan_N01_off1(temp):
    if temp !=0:
        fan_N01_status.append([temp, 0])

def fan_N01_on2(temp, humidity):
    if temp !=0 and humidity != 0:
        result = min(temp,humidity)
        fan_N02_status.append([result, 0])

def fan_N01_off2(temp, humidity):
    if temp !=0 and humidity != 0:
        result = min(temp,humidity)
        fan_N02_status.append([result, 0])

def fan_N02_on1(temp):
    if temp !=0:
        fan_N02_status.append([temp, 1])

def fan_N02_on2(temp, humidity):
    if temp !=0 and humidity != 0:
        result = min(temp,humidity)
        fan_N02_status.append([result, 0])

def fan_N02_off1(temp):
    if temp !=0:
        fan_N02_status.append([temp, 0])

def fan_N02_off2(temp, humidity):
    if temp !=0 and humidity != 0:
        result = min(temp,humidity)
        fan_N02_status.append([result, 0])

#calculate fan 1,2 status
fan_N01_on1(temp_warm)
fan_N02_off1(temp_warm)
fan_N01_on1(temp_hot)
fan_N02_on1(temp_hot)
fan_N01_off1(temp_cool)
fan_N02_off1(temp_cool)
fan_N01_on2(temp_warm, humidity_damp)
fan_N02_on2(temp_warm, humidity_damp)
fan_N01_off2(temp_warm, humidity_humid)
fan_N02_off2(temp_warm, humidity_humid)

#for add result to light bulb status
lightbulb_status = []
def lightbulb_on(light):
    lightbulb_status.append([light, 1])

def lightbulb_off(light):
    lightbulb_status.append([light, 0])

#calculate light bulb status
lightbulb_on(value_dark)
lightbulb_off(value_bright)

#defuzzification for output
def defuzzy(list):
    multiply_new = 0
    split_new = 0

    for i in range(0,len(list)):
        multiply = list[i][0]*list[i][1]
        split = list[i][0]
        multiply_new += multiply
        split_new += split
    if(split_new <= 0):
        split_new = 1
    x = multiply_new / split_new

    return x

#print result of fuzzy control
print('Value of water pump is ',math.ceil(defuzzy(waterpump_status)))
print('Value of fan 1 is ',math.ceil(defuzzy(fan_N01_status)))
print('Value of fan 2 is ',math.ceil(defuzzy(fan_N02_status)))
print('Value of light bulb is ',math.ceil(defuzzy(lightbulb_status)))

