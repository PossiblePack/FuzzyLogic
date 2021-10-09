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
    temp_dry = 1
    temp_moist = 0
    temp_moistly = 0
elif(temp < 50):
    temp_dry = (50 - temp) / (50) 
    temp_moist = (temp) / (50)
    temp_moistly = 0
elif(temp == 50):
    temp_dry = 0
    temp_moist = 1
    temp_moistly = 0
elif(temp < 100):
    temp_dry = 0
    temp_moist = (100 - temp) / (100-50)
    temp_moistly = (temp-50) / (100-50)
else:
    temp_dry = 0
    temp_moist = 0
    temp_moistly = 1

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