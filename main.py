import matplotlib.pyplot as plt
import json


def twoBinaryOneQuaternary(text):
    binary_text = ''.join(format(ord(i), '08b') for i in text)

    two_bits_binary_text = []
    for i in range(int(len(binary_text)/2)):
        two_bits_binary_text.append(binary_text[2*i: 2*i + 2])
    
    positive_dict = {"00": 1, "01": 3, "10": -1, "11": -3}
    negative_dict = {"00": -1, "01": -3, "10": 1, "11": 3}
    signal_level = [positive_dict[two_bits_binary_text[0]]]  # Considering positive original level

    for i in range(1, len(two_bits_binary_text)):
        if signal_level[i-1] > 0:
            signal_level.append(positive_dict[two_bits_binary_text[i]])
        else:
            signal_level.append(negative_dict[two_bits_binary_text[i]])

    graphPlot(signal_level, 'Multilevel - 2B1Q')


def eightBitSixTernary(text):
    # Considering +V = +1 and, consequently, -V = -1
    arq = open('8B6T.json')
    dict = json.load(arq)
    
    hex_text = ''.join(format(ord(i), 'X') for i in text)

    two_bits_hex_test = []
    for i in range(int(len(hex_text)/2)):
        two_bits_hex_test.append(hex_text[2*i: 2*i + 2])
    
    signal_level_matrix = []
    for i in range(len(two_bits_hex_test)):
        signal_level_matrix.append(dict[two_bits_hex_test[i]])

    x = 0
    for i in range(len(signal_level_matrix)):
        if (sum(signal_level_matrix[i]) == 1 and x == 1) or (sum(signal_level_matrix[i]) == -1 and x == -1):
            for j in range(6):
                signal_level_matrix[i][j] *= -1
        x = sum(signal_level_matrix[i])

    signal_level_list = []
    for i in range(len(signal_level_matrix)):
        for j in range(6):
            signal_level_list.append(signal_level_matrix[i][j])

    graphPlot(signal_level_list, 'Multilevel - 8B6T')


def fourDimensionalFiveLevelPulseAmplitudeModulationScheme(text):
    binary_text = ''.join(format(ord(i), '08b') for i in text)

    two_bits_binary_text = []
    for i in range(int(len(binary_text)/2)):
        two_bits_binary_text.append(binary_text[2*i: 2*i + 2])
    
    dict = {"00": -2, "01": 1, "10": -1, "11":2}
    signal_level = []

    for i in range(len(two_bits_binary_text)):
        signal_level.append(dict[two_bits_binary_text[i]])

    graphPlot(signal_level, 'Multilevel - 4DPAM5')


def multiLevelTransmitThree(text):
    binary_text = ''.join(format(ord(i), '08b') for i in text)

    bits_binary_text = []
    for i in range(len(binary_text)):
        bits_binary_text.append(binary_text[i])
    
    signal_level = []
    signal_level.append(0)  # Considering zero initial value
    x = -1  # Considering last negative initial non-zero level
    # Considering +V = +1 and, consequently, -V = -1
    for i in range(len(bits_binary_text)-1):
        if signal_level[i] == 0 and bits_binary_text[i+1] == '1':
            if x == 1:
                signal_level.append(-1)
                x = -1
            elif x == -1:
                signal_level.append(1)
                x = 1
        elif (signal_level[i] == -1 or signal_level[i] == 1) and bits_binary_text[i+1] == '1':
            signal_level.append(0)
        else:
            signal_level.append(signal_level[i])
    
    graphPlot(signal_level, 'Multilevel - MLT3')


def graphPlot(signal_level, title):
    time = []
    for i in range(len(signal_level)):
        time.append(i)
    
    for i in range(len(signal_level)):
        signal_level.insert(2*i + 1, signal_level[2*i])
        time.insert(2*i + 1, time[2*i])

    del(time[0])
    time.append(int(len(signal_level)/2))

    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Signal Level')
    plt.grid(linestyle='--')
    plt.plot(time, signal_level)
    plt.show()


print("Write four characters:")
text = input()[:4]

x = 1
while x != 0:
    print("Choice: ")
    print("1 - For 2B1Q graphic")
    print("2 - For 8B6T graphic")
    print("3 - For 4DPAM5 graphic")
    print("4 - For MLT3 graphic")
    print("0 - To quit")
    x = int(input())

    if x == 1:
        twoBinaryOneQuaternary(text)
    elif x == 2:
        eightBitSixTernary(text)
    elif x == 3:
        fourDimensionalFiveLevelPulseAmplitudeModulationScheme(text)
    elif x == 4:
        multiLevelTransmitThree(text)
    elif x == 0:
        break
