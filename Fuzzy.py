import math

print('Implement Fuzzy logic')

input_temperature     = input('Temperture     = ')
input_humidity        = input('Humidity       = ')
input_Soil_moisture   = input('Soil moisture  = ')
input_Light_intesity  = input('Light intesity = ')


temp     = int(input_temperature)
humidity = int(input_humidity)
soil     = int(input_Soil_moisture)
light    = int(input_Light_intesity)

#Implement Linguistic variable
#Temperature
if(temp == 0):
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
if(humidity == 0):
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
if(soil == 0):
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
if(light == 0):
    value_light = 0
    value_dark  = 1
elif(light < 0.5):
    value_light = (0.5 - light) / (0.5) 
    value_dark  = (light-0.5) / (0.5)
elif(light > 0.5 and light < 6.5):
    value_light = 1
    value_dark  = 0
else:
    value_light = 0
    value_dark  = 0

# print('Temperation value is \n dry = {} \n moist = {} \n moistly = {}'.format(temp_dry,temp_moist,temp_moistly))
# print('Humidity value is \n dry = {} \n humid = {} \n damp = {}'.format(humidity_dry,humidity_humid,humidity_damp))
# print('Soil moisture value is \n dry = {} \n moist = {} \n moistly = {}'.format(soil_dry,soil_moist,soil_moistly))
# print('Light intensity value is \n light = {} \n dark = {}'.format(value_light,value_dark))

#for add result to water pump status
waterpump_status = []
def waterpump_on(temp, humidity, soil):
    if temp !=0 and humidity != 0 and soil != 0:
        result = min(temp,humidity,soil)
        waterpump_status.append([result, 1])

def waterpump_off(temp, humidity, soil):
    if temp !=0 and humidity != 0 and soil != 0:
        result = min(temp,humidity,soil)
        waterpump_status.append([result, 0])

#calculate water pump status
waterpump_on(2, 2, soil_dry) # value = 2 is dont' care that value
waterpump_on(2, humidity_humid, soil_moist)
waterpump_off(2, 2, soil_moistly)
waterpump_off(temp_cool, humidity_damp, soil_moist)

#for add result to fan 1,2 status
fan_N01_status =[]
fan_N02_status =[]
def fan_N01_on(temp, humidity):
    if temp !=0 and humidity != 0:
        result = min(temp,humidity)
        fan_N01_status.append([result, 1])

def fan_N01_off(temp, humidity):
    if temp !=0 and humidity != 0:
        result = min(temp,humidity)
        fan_N01_status.append([result, 0])

def fan_N02_on(temp, humidity):
    if temp !=0 and humidity != 0:
        result = min(temp,humidity)
        fan_N02_status.append([result, 1])

def fan_N02_off(temp, humidity):
    if temp !=0 and humidity != 0:
        result = min(temp,humidity)
        fan_N02_status.append([result, 0 ])

fan_N01_on(temp_warm, 2)
fan_N02_on(temp_hot, 2)
fan_N01_off(temp_cool, humidity_damp)
fan_N02_off(temp_cool, humidity_humid)

lightbulb_status = []
def lightbulb_on(light):
    lightbulb_status.append([light, 1])

def lightbulb_off(temp):
    result = min(temp,humidity)
    lightbulb_status.append([result, 0])

lightbulb_on(value_dark)
lightbulb_off(value_light)

def defuzzy(list):
    multiply_new = 0
    split_new = 0

    for i in range(0,len(list)):
        multiply = list[i][0]*list[i][1]
        split = list[i][0]
        multiply_new += multiply
        split_new += split
    x = multiply_new / split_new

    return x

if(temp <= 40 and humidity <= 100 and soil <= 100 and light <= 7):
    
    print('Water pump is ',math.ceil(defuzzy(waterpump_status)))
    print('fan 1 is ',math.ceil(defuzzy(fan_N01_status)))
    print('fan 2 is ',math.ceil(defuzzy(fan_N02_status)))
    print('light bulb is ',math.ceil(defuzzy(fan_N01_status)))
else:
    print('your value is out of range')


