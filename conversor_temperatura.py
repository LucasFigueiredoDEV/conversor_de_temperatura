import os
print ('\tConversor de temperaturas')

print('1- Celsius')
print('2- Fahrenheint')
print('3- Kelvin')
print('Ou digite qualquer valor exceto os enumerados para sair do programa.')


while True:
    temperatura = input('Selecione a sua medida de temperatura: ')
    try:
        temperatura_int = int(temperatura)
    except ValueError:
        print('Por favor digite um número inteiro referente à sua temperatura.')
        continue
    except Exception:
        print('Erro desconhecido.')
        continue
    os.system('cls') 
    if temperatura_int == 1:
        print('\tTemperatura em Celsius selecionada:')
        print('1- Fahrenheint')
        print('2- Kelvin')
        temperatura_celsius = input('Selecione a medida de temperatura que deseja converter: ')
        try:
            temperatura_celsius_int = int(temperatura_celsius)
        except ValueError:
            print('Por favor digite um número inteiro referente à sua temperatura.')
        except Exception:
            print('Erro desconhecido.')
        while True:
            if temperatura_celsius_int == 1:
                print('\tConversor de Celsius para Fahrenheint')
                temperatura_celsius_inserir = input('Digite o valor da temperatura em Célsius: ')
                celsius_float = float(temperatura_celsius_inserir)
                conversao_celsius_to_fahrenheint = (celsius_float * 1.8) + 32
                os.system('cls')#dependendo do sistema operácional a string entre aspas poderá mudar
                print('Temperatura em Celsius: {}°C'.format(temperatura_celsius_inserir))
                print('Temperatura em Faherenheint: {}°F'.format(conversao_celsius_to_fahrenheint))
                break
            elif temperatura_celsius_int == 2:
                print('\tConversor de temperatura de Celsius para Kelvin')
                temperatura_celsius_inserir2 = input('Digite o valor da temperatura em Celsius: ')
                celsius_float2 = float(temperatura_celsius_inserir2)
                conversao_celsius_to_kelvin = celsius_float2 + 273.15
                os.system('cls')#dependendo do sistema operácional a string entre aspas poderá mudar
                print('Temperatura em Celsius: {}°C'.format(temperatura_celsius_inserir2))
                print('Temperatura em Kelvin: {}K'.format(conversao_celsius_to_kelvin))
                break
            else:
                print('Digite um valor referente às temperaturas descritas.')
                continue
    elif temperatura_int == 2:
        print('\tTemperatura em Fahrenheint selecionada:')
        print('1- Celsius')
        print('2- Kelvin')
        temperatura_fahrenheint = input('Selecione a medida de temperatura que deseja converter: ')
        try:
            temperatura_fahreheint_int = int(temperatura_fahrenheint)
        except ValueError:
            print('Por favor digite um número inteiro referente à sua temperatura.')
        except Exception:
            print('Erro desconhecido.')
        while True:
            if temperatura_fahreheint_int == 1:
                print('\tConversor de temperatura de Fahrenheint para Celsius')
                temperatura_fahrenheint_inserir = input('Digite o valor da temperatura em Fahrenheint: ')
                temperatura_fahrenheint_float = float(temperatura_fahrenheint_inserir)
                conversao_fahrenheint_to_celsius = (temperatura_fahrenheint_float - 32) / 1.8
                os.system('cls')
                print('Temperatura em fahrenheint: {}°F'.format(temperatura_fahrenheint_inserir))
                print('Temperatura em Celsius: {}°C'.format(conversao_fahrenheint_to_celsius))
                break
            elif temperatura_fahreheint_int == 2:
                print('\tConversor de temperatura de Fahrenheint para Kelvin')
                temperatura_fahrenheint_inserir2 = input('Digite o valor da temperatura em Fahrenheint: ')
                temperatura_fahrenheint_float2 = float(temperatura_fahrenheint_inserir2)
                conversao_fahrenheint_to_kelvin =  (temperatura_fahrenheint_float2 + 459.67) * (5/9)
                os.system('cls')
                print('Temperatura em Fahrenheint: {}°F'.format(temperatura_fahrenheint_inserir2))
                print('Temperatura em Kelvin: {}K'.format(conversao_fahrenheint_to_kelvin))
                break
            else:
                print('Digite um valor referente às temperaturas descritas.')
                continue
    elif temperatura_int == 3:
        print('\tTemperatura em Kelvin selecionada:')
        print('1- Celsius')
        print('2- Fahrenheint')
        temperatura_kelvin = input('Selecione a medida de temperatura que deseja converter: ')
        try:
            temperatura_kelvin_int = int(temperatura_kelvin)
        except ValueError:
            print('Por favor digite um número inteiro referente à sua temperatura.')
        except Exception:
            print('Erro desconhecido.')
        while True:
            if temperatura_kelvin_int == 1:
                print('\tConversor de temperatura de Kelvin para Celsius')
                temperatura_kelvin_inserir = input('Digite o valor da temperatura em Fahrenheint: ')
                temperatura_kelvin_float = float(temperatura_kelvin_inserir)
                conversao_kelvin_to_celsius = (temperatura_kelvin_float + 32) * 1.8
                os.system('cls')
                print('Temperatura em Kelvin: {}K'.format(temperatura_kelvin_inserir))
                print('Temperatura em Celsius: {}°C'.format(conversao_kelvin_to_celsius))
                break
            elif temperatura_kelvin_int == 2:
                print('\tConversor de temperatura de Fahrenheint para Kelvin')
                temperatura_kelvin_inserir2 = input('Digite o valor da temperatura em Fahrenheint: ')
                temperatura_kelvin_float2 = float(temperatura_kelvin_inserir2)
                conversao_kelvin_to_fahrenheint =  (temperatura_kelvin_float2 - 459.67) / (5/9)
                os.system('cls')
                print('Temperatura em Kelvin: {}K'.format(temperatura_kelvin_inserir2))
                print('Temperatura em Fahrenheint: {}°F'.format(conversao_kelvin_to_fahrenheint))
                break
            else:
                print('Digite um valor referente às temperaturas descritas.')
                continue
    else:
        break
print('Você saiu do programa!')