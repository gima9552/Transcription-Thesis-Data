#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-# LINE BY LINE EVAL #-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

import itertools
import editdistance
from sklearn.metrics import confusion_matrix

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-# Golden standard dictionaries, lists for lines #-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

Borg_Golden = {"Borg.lat.898_Página_080":[],
              "Borg.lat.898_Página_285":[],
              "Borg.lat.898_Página_301":[],
              "Borg.lat.898_Página_302":[],
              "Borg.lat.898_Página_313":[],
              "Borg.lat.898_Página_314":[],
              "Borg.lat.898_Página_318":[],
              "Borg.lat.898_Página_319":[],
              "Borg.lat.898_Página_333":[],
              "Borg.lat.898_Página_334":[],
              "Borg.lat.898_Página_335":[],
              "Borg.lat.898_Página_388":[],
              "Borg.lat.898_Página_391":[],
              "Borg.lat.898_Página_393":[],
              "Borg.lat.898_Página_394":[],
              "Borg.lat.898_Página_396":[]}

Copiale_Golden = {"01B":[],
                 "02":[],
                 "03":[],
                 "05":[],
                 "06":[],
                 "06B":[],
                 "07":[],
                 "09B":[],
                 "10":[],
                 "10B":[],
                 "11B":[],
                 "12B":[],
                 "13":[],
                 "15":[],
                 "43B":[],
                 "44":[],
                 "44B":[],
                 "46":[],
                 "46B":[],
                 "47":[],
                 "49B":[],
                 "50":[],
                 "50B":[],
                 "52":[]}

Ramanacoil_Golden = {"6958":[],
                     "6968":[],
                     "6973":[],
                     "6978":[],
                     "6983":[],
                     "6988":[],
                     "6993":[],
                     "7000":[]}

Borg_Golden_set = set()
Copiale_Golden_set = set()
Ramanacoil_Golden_set = set()

def get_golden(cipher, cipher_dict):
    for page in cipher_dict:
        with open("GT_Mohammad/"+cipher+"_Golden/"+page+".txt", "r") as file:
            for line in file:
                line_list = []
                strip = line.strip('\n')
                no_paragraph = strip.split()
                for char in no_paragraph:
                    char = char.lower()
                    if len(char) > 1:
                        long = list(char)
                        if "?" in long:
                            long.remove("?")
                        line_list.extend(long)
                        for char in long:
                            Borg_Golden_set.add(char)
                    elif char != "?":
                        line_list.append(char)
                        Borg_Golden_set.add(char)
                cipher_dict[page].append(line_list)
                
                    

def get_golden_copiale_special(cipher, cipher_dict):
    for page in cipher_dict:
        with open("GT_Mohammad/"+cipher+"_Golden/"+page+".txt", "r") as file:
            for line in file:
                line_list = []
                strip = line.strip('\n')
                no_paragraph = strip.split()
                for char in no_paragraph:
                    char = char.lower()
                    line_list.append(char)
                    Copiale_Golden_set.add(char)
                cipher_dict[page].append(line_list)

def get_golden_rama_special(cipher, cipher_dict):
    for page in cipher_dict:
        with open("GT_Mohammad/"+cipher+"_Golden/"+page+".txt", "r") as file:
            for line in file:
                line_list = []
                strip = line.strip('\n')
                no_paragraph = strip.split()
                for char in no_paragraph:
                    line_list.append(char)
                    Ramanacoil_Golden_set.add(char)
                cipher_dict[page].append(line_list)

get_golden("Borg", Borg_Golden)
get_golden_copiale_special("Copiale", Copiale_Golden)
get_golden_rama_special("Ramanacoil", Ramanacoil_Golden)


#-#-#-#-#-#-#-#-#-#
#-# DATECH Tool #-#
#-#-#-#-#-#-#-#-#-#

Borg_datech = {"Borg_080":[],
              "Borg_285":[],
              "Borg_301":[],
              "Borg_302":[],
              "Borg_313":[],
              "Borg_314":[],
              "Borg_318":[],
              "Borg_319":[],
              "Borg_333":[],
              "Borg_334":[],
              "Borg_335":[],
              "Borg_388":[],
              "Borg_391":[],
              "Borg_393":[],
              "Borg_394":[],
              "Borg_396":[]}

Copiale_datech = {"01B":[],
                 "02":[],
                 "03":[],
                 "05":[],
                 "06":[],
                 "06B":[],
                 "07":[],
                 "09B":[],
                 "10":[],
                 "10B":[],
                 "11B":[],
                 "12B":[],
                 "13":[],
                 "15":[],
                 "43B":[],
                 "44":[],
                 "44B":[],
                 "46":[],
                 "46B":[],
                 "47":[],
                 "49B":[],
                 "50":[],
                 "50B":[],
                 "52":[]}

Ramanacoil_datech_Borg = {"6958":[],
                         "6968":[],
                         "6973":[],
                         "6978":[],
                         "6983":[],
                         "6988":[],
                         "6993":[],
                         "7000":[]}
Ramanacoil_datech_Copiale = {"6958":[],
                             "6968":[],
                             "6973":[],
                             "6978":[],
                             "6983":[],
                             "6988":[],
                             "6993":[],
                             "7000":[]}
Ramanacoil_datech = {"6958":[],
                     "6968":[],
                     "6973":[],
                     "6978":[],
                     "6983":[],
                     "6988":[],
                     "6993":[],
                     "7000":[]}

Borg_datech_alphabet = set()

Copiale_datech_alphabet = set()

Ramanacoil_datech_alphabet = set()


def datech_dicts(cipher, cipher_datech, folder):
    for page in cipher_datech:
        with open("Datech/"+folder+"/"+page+".txt", "r") as file:
            for line in file:
                line_list = []
                strip = line.strip('\n')
                no_paragraph = strip.split()
                for char in no_paragraph:
                    if "cm" in char:
                        line_list.append(",")
                    elif char.count("X") > 0:
                        for i in range(char.count("X")):
                            line_list.append("?") 
                    elif "cl" in char:
                        line_list.append(":")
                    elif "dt" in char and len(char)<=2:
                        line_list.append(".")
                    elif char == "und":
                        line_list.append("__")
                    elif len(char) > 2 and char.count("dt") > 0:
                        num = char.count("dt")
                        root = char.strip("dt")
                        char = root + "."*num
                        line_list.append(char)
                    else:
                        line_list.append(char)
                cipher_datech[page].append(line_list)
                if cipher == "Borg":
                    for char in line_list:
                        c = char.lower()
                        Borg_datech_alphabet.add(c)
                elif cipher == "Copiale":
                    for char in line_list:
                        Copiale_datech_alphabet.add(char)
                elif cipher == "Ramanacoil":
                    for char in line_list:
                            Ramanacoil_datech_alphabet.add(char)

datech_dicts("Borg", Borg_datech, "Borg_150cl_default")
datech_dicts("Copiale", Copiale_datech, "Copiale_196cl_default")
datech_dicts("Ramanacoil", Ramanacoil_datech, "Ramanacoil_150cl_default")





#-#-#-#-#-#-#-#-#-#-#
#-# Decrypt  Tool #-#
#-#-#-#-#-#-#-#-#-#-#
Borg_decrypt = {"Borg.lat.898_Página_080":[],
              "Borg.lat.898_Página_285":[],
              "Borg.lat.898_Página_301":[],
              "Borg.lat.898_Página_302":[],
              "Borg.lat.898_Página_313":[],
              "Borg.lat.898_Página_314":[],
              "Borg.lat.898_Página_318":[],
              "Borg.lat.898_Página_319":[],
              "Borg.lat.898_Página_333":[],
              "Borg.lat.898_Página_334":[],
              "Borg.lat.898_Página_335":[],
              "Borg.lat.898_Página_388":[],
              "Borg.lat.898_Página_391":[],
              "Borg.lat.898_Página_393":[],
              "Borg.lat.898_Página_394":[],
              "Borg.lat.898_Página_396":[]}

Copiale_decrypt = {"01B":[],
                 "02":[],
                 "03":[],
                 "05":[],
                 "06":[],
                 "06B":[],
                 "07":[],
                 "09B":[],
                 "10":[],
                 "10B":[],
                 "11B":[],
                 "12B":[],
                 "13":[],
                 "15":[],
                 "43B":[],
                 "44":[],
                 "44B":[],
                 "46":[],
                 "46B":[],
                 "47":[],
                 "49B":[],
                 "50":[],
                 "50B":[],
                 "52":[]}

Ramanacoil_decrypt_B = {"6958":[],
                        "6968":[],
                        "6973":[],
                        "6978":[],
                        "6983":[],
                        "6988":[],
                        "6993":[],
                        "7000":[]}

Ramanacoil_decrypt_C = {"6958":[],
                        "6968":[],
                        "6973":[],
                        "6978":[],
                        "6983":[],
                        "6988":[],
                        "6993":[],
                        "7000":[]}

Ramanacoil_decrypt_Omni = {"6958":[],
                           "6968":[],
                           "6973":[],
                           "6978":[],
                           "6983":[],
                           "6988":[],
                           "6993":[],
                           "7000":[]}

Borg_decrypt_alphabet = set()

Copiale_decrypt_alphabet = set()

Ramanacoil_decrypt_alphabet = set()


def decrypt_dicts(cipher, cipher_decrypt, folder):
    for page in cipher_decrypt:
        with open("Decrypt/"+folder+"/"+page+".txt", "r") as file:
            for line in file:
                line_list = []
                strip = line.strip('\n')
                no_paragraph = strip.split()
                for char in no_paragraph:
                    if char == "cm":
                        line_list.append(",")
                    elif char == "cl":
                        line_list.append(":")
                    elif char == "dt":
                        line_list.append(".")
                    elif len(char) > 2 and char.count("dt") > 0:
                        num = char.count("dt")
                        root = char.strip("dt")
                        dots = "."*num
                        c = root+dots
                        line_list.append(c)
                    else:
                        line_list.append(char)
                cipher_decrypt[page].append(line_list)
                if cipher == "Borg":
                    for char in line_list:
                        c = char.lower()
                        Borg_decrypt_alphabet.add(c)
                elif cipher == "Copiale":
                    for char in line_list:
                        Copiale_decrypt_alphabet.add(char)
                elif cipher == "Ramanacoil":
                    for char in line_list:
                        Ramanacoil_decrypt_alphabet.add(char)

decrypt_dicts("Borg", Borg_decrypt, "Borg_5shots_04trsh")
decrypt_dicts("Copiale", Copiale_decrypt, "Copiale_5shots_04trsh")

#decrypt_dicts("Ramanacoil", Ramanacoil_decrypt_B, "Ramanacoil_5shots_04trsh_B")
#decrypt_dicts("Ramanacoil", Ramanacoil_decrypt_C, "Ramanacoil_5shots_04trsh_C")
decrypt_dicts("Ramanacoil", Ramanacoil_decrypt_Omni, "Ramanacoil_5shots_04trsh_Omni")

#-#-#-#-#-#-#-#-#-#
#-# EVALUATION  #-#
#-#-#-#-#-#-#-#-#-#

def character_recognition(cipher_dict, golden_dict, cipher, alphabet):
    print("Character # recognized per page:")
    pages = 0
    total = 0
    recognized = 0
    for page1, page2 in zip(cipher_dict, golden_dict):
        cipher_len = 0
        pages += 1
        gold_len = 0
        for line1, line2 in itertools.zip_longest(cipher_dict[page1], golden_dict[page2], fillvalue=list()):
            gold_len += len(line2)
            for char in line1:
                if char != "?":
                    cipher_len += 1
                    recognized += 1
        total += gold_len
        print(page1+":", str(cipher_len)+"/"+str(gold_len), str(100*cipher_len/gold_len)+"%")
    if cipher == "Copiale":
        print("Characters recognized:", str(len(alphabet))+"/"+str(len(Copiale_Golden_set)), alphabet)
        print("FAILSAFE: Golden Alphabet=", Copiale_Golden_set)
        print("Total recognition =", recognized/total)
        print("- - - Done - - -")
    elif cipher == "Borg":
        print("Characters recognized:", str(len(alphabet))+"/"+str(len(Borg_Golden_set)), alphabet)
        print("FAILSAFE: Golden Alphabet=", Borg_Golden_set)
        print("Total recognition =", recognized/total)
        print("- - - Done - - -")
    elif cipher == "Ramanacoil":
        print("Characters recognized:", str(len(alphabet))+"/"+str(len(Ramanacoil_Golden_set)), alphabet)
        print("FAILSAFE: Golden Alphabet=", Ramanacoil_Golden_set)
        print("Total recognition =", recognized/total)
        print("- - - Done - - -")

    

def evaluation(cipher_dict, golden_dict):
    character_frequency = dict()
    golden_character_frequency = dict()
    true_positives = dict()
    accuracy_num = 0
    accuracy_den = 0
    for page1, page2 in zip(cipher_dict, golden_dict):
        for line1, line2 in zip(cipher_dict[page1], golden_dict[page2]):
            for char1, char2 in itertools.zip_longest(line1, line2, fillvalue='-'):
                character_frequency[char1] = character_frequency.get(char1, 0)+1
                golden_character_frequency[char2] = golden_character_frequency.get(char2, 0)+1
                if char1 == char2:
                    true_positives[char1] = true_positives.get(char1, 0)+1
                    accuracy_num += 1
    for char in golden_character_frequency:
        accuracy_den += golden_character_frequency.get(char)
    print("### Model Accuracy ###")
    print(accuracy_num/accuracy_den)
    print("")
    print("### Model Error Rate ###")
    print(1-accuracy_num/accuracy_den)
    print("")
    print("### Precision/Recall value for each character ###\n")
    mean_precision = 0
    mean_recall = 0
    count = 0
    for character in true_positives:
        precision = true_positives[character] / character_frequency[character]
        recall = true_positives[character] / golden_character_frequency[character]
        mean_precision += precision
        mean_recall += recall
        count += 1
        print(character, "- P", round(precision, 4), "/ R", round(recall, 4), "/ Error Rate", round((1-precision), 4))
    mean_p = mean_precision*100/count
    mean_r = mean_recall*100/count
    print("Mean Precision -", round(mean_p, 4))
    print("Mean Recall -", round(mean_r, 4))
    print("Avg error rate (chars) -", 100-mean_p)
    print("F1 score -", 2*(mean_r*mean_p)/(mean_r+mean_p))

def ser(cipher_dict, golden_dict):
    tot_ser = 0
    tot_norm_ser = 0
    lines = 0
    for page1, page2 in zip(cipher_dict, golden_dict):
        for line1, line2 in zip(cipher_dict[page1], golden_dict[page2]):
            truth = ''.join(line2)
            if "?" in line1:
                unkn = 0
                for char in line1:
                    if char == "?":
                        unkn +=1
                for i in range(unkn):
                    line1.remove("?")
            pred = ''.join(line1)
            SER = editdistance.eval(truth, pred) / len(truth)
            norm_SER = editdistance.eval(truth, pred) / max(len(truth), len(pred))
            tot_ser += SER
            tot_norm_ser += norm_SER
            lines += 1
    avg_ser = tot_ser / lines
    avg_norm_ser = tot_norm_ser / lines
    print("Avg. SER:", avg_ser)
    print("Avg. SER, normalized:", avg_norm_ser)


### CONFUSION MATRICES


def top_five_matrix_zodiac(cipher_dict, golden_dict, cipher):
    keys = {"9":"Cancer",
            "m":"Virgo",
            "v":"Aries",
            "8":"Taurus",
            "n":"Libra"}
    actual = list()
    predicted = list()
    character_frequency = dict()
    for page1, page2 in zip(cipher_dict, golden_dict):
        for line1, line2 in zip(cipher_dict[page1], golden_dict[page2]):
            for char1, char2 in itertools.zip_longest(line1, line2, fillvalue='-'):
                if "B" in cipher:
                    if char2 == "9" or char2 == "m" or char2 == "v" or char2 == "8" or char2 == "n":
                        actual.append(keys[char2])
                        if char1 == "9" or char1 == "m" or char1 == "v" or char1 == "8" or char1 == "n":
                            predicted.append(keys[char1])
                        else:
                            predicted.append("Other")
                elif "C" in cipher:
                    if char2 == "gam":
                        actual.append("Taurus")
                        if char1 == "gam":
                            predicted.append("Taurus")
                        else:
                            predicted.append("Other")
                elif "R" in cipher:
                    if char2 == "Cancer" or char2 == "Virgo" or char2 == "Aries" or char2 == "Taurus" or char2 == "Libra":
                        actual.append(char2)
                        if char1 == "Cancer" or char1 == "Virgo" or char1 == "Aries" or char1 == "Taurus" or char1 == "Libra":
                            predicted.append(char1)
                        else:
                            predicted.append("Other")
    actual.append("Other")
    predicted.append("Other")
    print(confusion_matrix(actual, predicted, labels=["Cancer","Virgo","Aries","Taurus","Libra", "Other"]))


def top_five_matrix_alchemy(cipher_dict, golden_dict, cipher):
    keys = {"x":"Star",
            "w":"Arsenic",
            "1":"Iron",
            "mal":"Antimony",
            "d":"Fire",
            "tri":"Fire"}
    actual = list()
    predicted = list()
    character_frequency = dict()
    for page1, page2 in zip(cipher_dict, golden_dict):
        for line1, line2 in zip(cipher_dict[page1], golden_dict[page2]):
            for char1, char2 in itertools.zip_longest(line1, line2, fillvalue='-'):
                if "B" in cipher:
                    if char2 == "x" or char2 == "w" or char2 == "1" or char2 == "d":
                        actual.append(keys[char2])
                        if char1 == "x" or char1 == "w" or char1 == "1" or char1 == "d":
                            predicted.append(keys[char1])
                        else:
                            predicted.append("Other")
                elif "C" in cipher:
                    if char2 == "mal" or char2 == "tri":
                        actual.append(keys[char2])
                        if char1 == "mal" or char1 == "tri":
                            predicted.append(keys[char1])
                        else:
                            predicted.append("Other")
                elif "R" in cipher:
                    if char2 == "Star" or char2 == "Arsenic" or char2 == "Iron" or char2 == "Antimony" or char2 == "Fire":
                        actual.append(char2)
                        if char1 == "Star" or char1 == "Arsenic" or char1 == "Iron" or char1 == "Antimony" or char1 == "Fire":
                            predicted.append(char1)
                        else:
                            predicted.append("Other")
    print(confusion_matrix(actual, predicted, labels=["Star","Arsenic","Iron","Antimony","Fire", "Other"]))


def top_five_matrix_total(cipher_dict, golden_dict, cipher):
    keys = {"x":"Star",
            "w":"Arsenic",
            "1":"Iron",
            "mal":"Antimony",
            "d":"Fire",
            "tri":"Fire",
            "9":"Cancer",
            "m":"Virgo",
            "v":"Aries",
            "8":"Taurus",
            "gam":"Taurus",
            "n":"Libra"}
    actual = list()
    predicted = list()
    character_frequency = dict()
    for page1, page2 in zip(cipher_dict, golden_dict):
        for line1, line2 in zip(cipher_dict[page1], golden_dict[page2]):
            for char1, char2 in itertools.zip_longest(line1, line2, fillvalue='-'):
                if "B" in cipher:
                    if char2 == "x" or char2 == "w" or char2 == "1" or char2 == "d" or char2 == "9" or char2 == "m" or char2 == "v" or char2 == "8" or char2 == "n":
                        actual.append(keys[char2])
                        if char1 == "x" or char1 == "w" or char1 == "1" or char1 == "d" or char1 == "9" or char1 == "m" or char1 == "v" or char1 == "8" or char1 == "n":
                            predicted.append(keys[char1])
                        else:
                            predicted.append("Other")
                elif "C" in cipher:
                    if char2 == "mal" or char2 == "tri" or char2 == "gam":
                        actual.append(keys[char2])
                        if char1 == "mal" or char1 == "tri" or char1 == "gam":
                            predicted.append(keys[char1])
                        else:
                            predicted.append("Other")
                elif "R" in cipher:
                    if char2 == "Star" or char2 == "Arsenic" or char2 == "Iron" or char2 == "Antimony" or char2 == "Fire" or char2 == "Cancer" or char2 == "Virgo" or char2 == "Aries" or char2 == "Taurus" or char2 == "Libra":
                        actual.append(char2)
                        if char1 == "Star" or char1 == "Arsenic" or char1 == "Iron" or char1 == "Antimony" or char1 == "Fire" or char1 == "Cancer" or char1 == "Virgo" or char1 == "Aries" or char1 == "Taurus" or char1 == "Libra":
                            predicted.append(char1)
                        else:
                            predicted.append("Other")
    print(confusion_matrix(actual, predicted, labels=["Cancer","Virgo","Aries","Taurus","Libra","Star","Arsenic","Iron","Antimony","Fire", "Other"]))

######################

def bad_five_matrix_zodiac(cipher_dict, golden_dict, cipher):
    keys = {"i":"Gemini",
            "Gemini":"Gemini",
            "y":"Aquarius",
            "Aquarius":"Aquarius",
            "c":"Leo",
            "Leo":"Leo",
            "Arrow":"Sagittarius",
            "Pisces":"Pisces"}
    actual = list()
    predicted = list()
    character_frequency = dict()
    for page1, page2 in zip(cipher_dict, golden_dict):
        for line1, line2 in zip(cipher_dict[page1], golden_dict[page2]):
            for char1, char2 in itertools.zip_longest(line1, line2, fillvalue='-'):
                if "B" in cipher:
                    if char2 == "i" or char2 == "y" or char2 == "c":
                        actual.append(keys[char2])
                        if char1 == "i" or char1 == "y" or char1 == "c":
                            predicted.append(keys[char1])
                        else:
                            predicted.append("Other")
                elif "R" in cipher:
                    if char2 == "Gemini" or char2 == "Aquarius" or char2 == "Leo" or char2 == "Sagittarius" or char2 == "Pisces":
                        actual.append(keys[char2])
                        if char1 == "Gemini" or char1 == "Aquarius" or char1 == "Leo" or char1 == "Sagittarius" or char1 == "Pisces":
                            predicted.append(keys[char1])
                        else:
                            predicted.append("Other")
    actual.append("Other")
    predicted.append("Other")
    print(confusion_matrix(actual, predicted, labels=["Gemini","Aquarius","Leo","Sagittarius","Pisces", "Other"]))


def bad_five_matrix_alchemy(cipher_dict, golden_dict, cipher):
    keys = {"Opposition":"Opposition",
            "Quincux":"Quincunx",
            "Quincunx":"Quincux",
            "Quincunx":"Quincunx",
            "Quincux":"Quincux",
            "Sun":"Sun",
            "Moon":"Moon",
            "Node":"Node"}
    actual = list()
    predicted = list()
    character_frequency = dict()
    for page1, page2 in zip(cipher_dict, golden_dict):
        for line1, line2 in zip(cipher_dict[page1], golden_dict[page2]):
            for char1, char2 in itertools.zip_longest(line1, line2, fillvalue='-'):
                if "R" in cipher:
                    if char2 == "Opposition" or char2 == "Quincunx" or char2 == "Quincux" or char2 == "Sun" or char2 == "Moon" or char2 == "Node":
                        actual.append(keys[char2])
                        if char1 == "Opposition" or char1 == "Quincunx" or char2 == "Quincux" or char1 == "Sun" or char1 == "Moon" or char1 == "Node":
                            predicted.append(keys[char1])
                        else:
                            predicted.append("Other")
    actual.append("Other")
    predicted.append("Other")
    print(confusion_matrix(actual, predicted, labels=["Gemini","Aquarius","Leo","Sagittarius","Pisces", "Other"]))


def bad_five_matrix_total(cipher_dict, golden_dict, cipher):
    keys = {"i":"Gemini",
            "Gemini":"Gemini",
            "y":"Aquarius",
            "Aquarius":"Aquarius",
            "c":"Leo",
            "Leo":"Leo",
            "Arrow":"Sagittarius",
            "Pisces":"Pisces",
            "Opposition":"Opposition",
            "Quincux":"Quincux",
            "Quincunx":"Quincux",
            "Sun":"Sun",
            "Moon":"Moon",
            "Node":"Node"}
    actual = list()
    predicted = list()
    character_frequency = dict()
    for page1, page2 in zip(cipher_dict, golden_dict):
        for line1, line2 in zip(cipher_dict[page1], golden_dict[page2]):
            for char1, char2 in itertools.zip_longest(line1, line2, fillvalue='-'):
                if "B" in cipher:
                    if char2 == "i" or char2 == "y" or char2 == "c":
                        actual.append(keys[char2])
                        if char1 == "i" or char1 == "y" or char1 == "c":
                            predicted.append(keys[char1])
                        else:
                            predicted.append("Other")
                elif "R" in cipher:
                    if char2 == "Gemini" or char2 == "Aquarius" or char2 == "Leo" or char2 == "Sagittarius" or char2 == "Pisces" or char2 == "Opposition" or char2 == "Quincunx" or char2 == "Quincux" or char2 == "Sun" or char2 == "Moon" or char2 == "Node":
                        actual.append(keys[char2])
                        if char1 == "Gemini" or char1 == "Aquarius" or char1 == "Leo" or char1 == "Sagittarius" or char1 == "Pisces" or char1 == "Opposition" or char1 == "Quincunx" or char1 == "Quincux" or char1 == "Sun" or char1 == "Moon" or char1 == "Node":
                            predicted.append(keys[char1])
                        else:
                            predicted.append("Other")
    actual.append("Other")
    predicted.append("Other")
    print(confusion_matrix(actual, predicted, labels=["Gemini","Aquarius","Leo","Sagittarius","Pisces", "Opposition", "Quincux", "Sun", "Moon", "Node","Other"]))



#-#-#-#-#-#-#-#-#-#
#-#  PRINTING   #-#
#-#-#-#-#-#-#-#-#-#

###
### Clustering Tool
###
print("##########\n### DATECH ###\n##########")
print("### Borg ###")
character_recognition(Borg_datech, Borg_Golden, "Borg", Borg_datech_alphabet)
print("- - -")
evaluation(Borg_datech, Borg_Golden)
print("- - -")
ser(Borg_datech, Borg_Golden)
print("- - - - - - -")
print("### Copiale ###")
character_recognition(Copiale_datech, Copiale_Golden, "Copiale", Copiale_datech_alphabet)
print("- - -")
evaluation(Copiale_datech, Copiale_Golden)
print("- - -")
ser(Copiale_datech, Copiale_Golden)
print("- - - - - - -")
print("### Ramanacoil (custom) ###")
character_recognition(Ramanacoil_datech, Ramanacoil_Golden, "Ramanacoil", Ramanacoil_datech_alphabet)
print("- - -")
evaluation(Ramanacoil_datech, Ramanacoil_Golden)
print("- - -")
ser(Ramanacoil_datech, Ramanacoil_Golden)
print("- - - - - - -")
###
### Few-Shot Tool
###
print("##########\n### Decrypt ###\n##########")
print("### Borg ###")
character_recognition(Borg_decrypt, Borg_Golden, "Borg", Borg_decrypt_alphabet)
print("- - -")
evaluation(Borg_decrypt, Borg_Golden)
print("- - -")
ser(Borg_decrypt, Borg_Golden)
print("- - - - - - -")
print("### Copiale ###")
character_recognition(Copiale_decrypt, Copiale_Golden, "Copiale", Copiale_decrypt_alphabet)
print("- - -")
evaluation(Copiale_decrypt, Copiale_Golden)
print("- - -")
ser(Copiale_decrypt, Copiale_Golden)
print("- - - - - - -")
print("### Ramanacoil (Omni) ###")
character_recognition(Ramanacoil_decrypt_Omni, Ramanacoil_Golden, "Ramanacoil", Ramanacoil_decrypt_alphabet)
print("- - -")
evaluation(Ramanacoil_decrypt_Omni, Ramanacoil_Golden)
print("- - -")
ser(Ramanacoil_decrypt_Omni, Ramanacoil_Golden)
print("- - - - - - -")
print("- - - - - - -")
###
### Confusion Matrices
###
print("##########\n##########\n##########\n### Confusion Matrix (Top5) ###\n##########")
print("### Zodiac (Datech) ###")
top_five_matrix_zodiac(Borg_datech, Borg_Golden, "Borg")
top_five_matrix_zodiac(Copiale_datech, Copiale_Golden, "Copiale")
top_five_matrix_zodiac(Ramanacoil_datech, Ramanacoil_Golden, "Ramanacoil")
print("### Zodiac (Few-Shot) ###")
top_five_matrix_zodiac(Borg_decrypt, Borg_Golden, "Borg")
top_five_matrix_zodiac(Copiale_decrypt, Copiale_Golden, "Copiale")
top_five_matrix_zodiac(R_decrypt_Omni, Few_R_Gold, "Ramanacoil")
print()
print("- - - - - - -")
print()
print("### Alchemy (Datech) ###")
top_five_matrix_alchemy(Borg_datech, Borg_Golden, "Borg")
top_five_matrix_alchemy(Copiale_datech, Copiale_Golden, "Copiale")
top_five_matrix_alchemy(Ramanacoil_datech, Ramanacoil_Golden, "Ramanacoil")
print("### Alchemy (Few-Shot) ###")
top_five_matrix_alchemy(Borg_decrypt, Borg_Golden, "Borg")
top_five_matrix_alchemy(Copiale_decrypt, Copiale_Golden, "Copiale")
top_five_matrix_alchemy(R_decrypt_Omni, Few_R_Gold, "Ramanacoil")
print()
print("- - - - - - -")
print("### total (Datech) ###")
top_five_matrix_total(Borg_datech, Borg_Golden, "Borg")
top_five_matrix_total(Copiale_datech, Copiale_Golden, "Copiale")
top_five_matrix_total(Ramanacoil_datech, Ramanacoil_Golden, "Ramanacoil")
print("### total (Few-Shot) ###")
top_five_matrix_total(Borg_decrypt, Borg_Golden, "Borg")
top_five_matrix_total(Copiale_decrypt, Copiale_Golden, "Copiale")
top_five_matrix_total(R_decrypt_Omni, Few_R_Gold, "Ramanacoil")
print("- - - - - - -")
print("##########\n##########\n##########\n### Confusion Matrix (Bad5) ###\n##########")
print("### Zodiac (Datech) ###")
bad_five_matrix_zodiac(Borg_datech, Borg_Golden, "Borg")
bad_five_matrix_zodiac(Copiale_datech, Copiale_Golden, "Copiale")
bad_five_matrix_zodiac(Ramanacoil_datech, Ramanacoil_Golden, "Ramanacoil")
print("### Zodiac (Few-Shot) ###")
bad_five_matrix_zodiac(Borg_decrypt, Borg_Golden, "Borg")
bad_five_matrix_zodiac(Copiale_decrypt, Copiale_Golden, "Copiale")
bad_five_matrix_zodiac(R_decrypt_Omni, Few_R_Gold, "Ramanacoil")
print()
print("- - - - - - -")
print()
print("### Alchemy (Datech) ###")
bad_five_matrix_alchemy(Borg_datech, Borg_Golden, "Borg")
bad_five_matrix_alchemy(Copiale_datech, Copiale_Golden, "Copiale")
bad_five_matrix_alchemy(Ramanacoil_datech, Ramanacoil_Golden, "Ramanacoil")
print("### Alchemy (Few-Shot) ###")
bad_five_matrix_alchemy(Borg_decrypt, Borg_Golden, "Borg")
bad_five_matrix_alchemy(Copiale_decrypt, Copiale_Golden, "Copiale")
bad_five_matrix_alchemy(R_decrypt_Omni, Few_R_Gold, "Ramanacoil")
print()
print("- - - - - - -")
print("### total (Datech) ###")
bad_five_matrix_total(Borg_datech, Borg_Golden, "Borg")
bad_five_matrix_total(Copiale_datech, Copiale_Golden, "Copiale")
bad_five_matrix_total(Ramanacoil_datech, Ramanacoil_Golden, "Ramanacoil")
print("### total (Few-Shot) ###")
bad_five_matrix_total(Borg_decrypt, Borg_Golden, "Borg")
bad_five_matrix_total(Copiale_decrypt, Copiale_Golden, "Copiale")
bad_five_matrix_total(R_decrypt_Omni, Few_R_Gold, "Ramanacoil")
