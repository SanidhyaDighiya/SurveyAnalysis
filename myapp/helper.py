import pandas as pd

def parse(file2, a, b, c, d, e):
    # return file2
    df=pd.read_excel(file2)
    # return file2

    pd.set_option('display.max_columns', None)

    df.drop('Block_name', axis=1, inplace=True)
    lt = ['__fid__', 'surveyor', 'created_on', 'edited_on', 'status', 'HH_Image', 'Phone_Number', 'Gotra', 'Name',
          'travel_work', 'travel_frequency', 'disease_name', 'election_participation',
          'area_agricultura_land', 'Houseland_size', 'source_food',
          'crop_grown', 'free_electricity', 'women_using_phone', 'Envi_Wastedisposal', 'Envi_Forestproduce',
          'Envi_ForestDistance', 'Envi_Forestname', 'Envi_Forestpurpose',
          'Envi_sacredgroves_TC', 'Envi_Foresttime', 'Envi_Forestchange',
          'Envi_waterchange', 'Envi_ForestHerbs', 'Envi_Forestherbsname',
          'Envi_ForestAttaraction', 'Envi_ForestAttaractiontype', 'scholarship',
          'Envi_Wastewater', 'Gender']
    df = df.drop(lt, axis=1)

    def parsing21(x):
        if x == 'हां':
            return 0
        else:
            return 1

    df['chronic_disease'] = df['chronic_disease'].apply(parsing21)

    def parsing(x):
        # print(x)
        if x == 'पूरी तरह ':
            return 1
        else:
            return 0

    df['basic_vaccination'] = df['basic_vaccination'].apply(parsing)

    def parsing1(x):
        # print(x)
        if x == 'स्वास्थ्य केंद्र ':
            return 1
        else:
            return 0

    df['Institutional_delivery'] = df['Institutional_delivery'].apply(parsing1)

    def parsing1(x):
        # print(x)
        if x == ' एक बार भी नहीं दिया':
            return 0
        else:
            return 1

    df['voter'] = df['voter'].apply(parsing1)

    def parsing3(x):
        # print(x)
        if x == 'हाँ, सभी तिमाही ' or x == 'लागू नहीं ' or x == 'हाँ, 1 तिमाही ' or x == 'हाँ, 2 तिमाही ':
            return 1
        else:
            return 0

    df['ANC'] = df['ANC'].apply(parsing3)

    def parsing4(x):
        # print(x)
        if x == 'नहीं':
            return 1
        else:
            return 0

    df['Infant_mortality'] = df['Infant_mortality'].apply(parsing4)

    def parsing5(x):
        # print(x)
        if x == 'हाँ, पर्याप्त ':
            return 1
        else:
            return 0

    df['2sqmeals'] = df['2sqmeals'].apply(parsing5)

    def parsing6(x):
        # print(x)
        if x == 'नहीं':
            return 0
        else:
            return 1

    df['gram_sabha_meeting'] = df['gram_sabha_meeting'].apply(parsing6)

    def parsing7(x):
        # print(x)
        if x == 'नहीं':
            return 0
        else:
            return 1

    df['traitional_meeting'] = df['traditional_meeting'].apply(parsing7)

    def parsing8(x):
        # print(x)
        if x == 'नहीं':
            return 0
        else:
            return 1

    df['Panchayat_meetings'] = df['Panchayat_meetings'].apply(parsing8)

    def parsing9(x):
        # print(x)
        if x == 'नहीं':
            return 0
        else:
            return 1

    df['SHG'] = df['SHG'].apply(parsing9)

    def parsing10(x):
        # print(x)
        if x == 'नहीं':
            return 0
        else:
            return 1

    df['traditional_dance'] = df['traditional_dance'].apply(parsing10)

    def parsing11(x):
        # print(x)
        if x == 'नहीं':
            return 0
        else:
            return 1

    df['traditional_instrument'] = df['traditional_instrument'].apply(parsing11)

    def parsing12(x):
        # print(x)
        if x == 'नहीं':
            return 0
        else:
            return 1

    df['traditional_language'] = df['traditional_language'].apply(parsing12)

    df2 = list(df[['Age', 'Ed']].values)
    import re

    df3 = []
    for i in range(len(df2)):
        x = df2[i]
        y = [int(y) for y in re.findall(r'\d+', x[1])]
        if x[0] < 15 or x[0] > 64:
            df3.append(1)
        elif x[1] == 'पोस्ट ग्रेजुएशन पूरा किया हुआ' or x[1] == 'डिप्लोमा पूरा किया हुआ' or x[
            1] == 'डिग्री पूरा किया हुआ' or (len(y) > 0 and y[0] >= 10):
            df3.append(1)
        else:
            df3.append(0)

    df['dropout'] = df3
    # df=df+df3
    # frames=[df, df3]
    # df = pd.concat(frames)
    # df.head()

    def parsing13(x):
        # print(x)
        y = [int(y) for y in re.findall(r'\d+', x)]
        if x == 'पोस्ट ग्रेजुएशन पूरा किया हुआ' or x == 'डिप्लोमा पूरा किया हुआ' or x == 'डिग्री पूरा किया हुआ' or (
                len(y) > 0 and y[0] >= 6):
            return 1
        else:
            return 0

    df['Ed'] = df['Ed'].apply(parsing13)

    def parsing14(x):
        if (x.find('चुआ') == -1):
            return 1
        else:
            return 0

    df['source_drinking_water'] = df['source_drinking_water'].apply(parsing14)

    def parsing15(x):
        if x == 'नहीं':
            return 0
        else:
            return 1

    df['electricity'] = df['electricity'].apply(parsing15)

    def parsing16(x):
        if (x.find('गैस') == -1):
            return 0
        else:
            return 1

    df['source_fuel'] = df['source_fuel'].apply(parsing16)

    def parsing17(x):
        if (x.find('घर के बाहर') == -1):
            return 1
        else:
            return 0

    df['defecation'] = df['defecation'].apply(parsing17)

    def parsing18(x):
        if (x.find('घर के बाहर') == -1):
            return 1
        else:
            return 0

    df['bath'] = df['bath'].apply(parsing18)

    def parsing19(x):
        if x == 'नहीं':
            return 0
        else:
            return 1

    df['home_ownership'] = df['home_ownership'].apply(parsing19)
    # df['home_ownership'].unique()

    def parsing20(x):
        if x == ' हां ':
            return 1
        else:
            return 0

    df['agricultureland'] = df['agricultureland'].apply(parsing20)

    df2 = list(df[['Age', 'Inst_Credit']].values)
    # import re

    df3 = []
    for i in range(len(df2)):
        x = df2[i]
        # y = [int(y) for y in re.findall(r'\d+', x[1])]
        if x[0] <18 or "मतदाता पहचान पत्र" in x[1]:
            df3.append(1)
        else:
            df3.append(0)

    df['voter_card'] = df3

    df2 = list(df[['Age', 'Inst_Credit']].values)
    # import re

    df3 = []
    for i in range(len(df2)):
        x = df2[i]
        # y = [int(y) for y in re.findall(r'\d+', x[1])]
        if "आधार कार्ड" in x[1]:
            df3.append(1)
        else:
            df3.append(0)

    df['aadhar_card'] = df3

    df2 = list(df[['Age', 'Inst_Credit']].values)
    # import re

    df3 = []
    for i in range(len(df2)):
        x = df2[i]
        # y = [int(y) for y in re.findall(r'\d+', x[1])]
        if "बैंक खाता" in x[1]:
            df3.append(1)
        else:
            df3.append(0)

    df['bank_card'] = df3

    df2 = list(df[['Age', 'Inst_Credit']].values)
    # import re

    df3 = []
    for i in range(len(df2)):
        x = df2[i]
        # y = [int(y) for y in re.findall(r'\d+', x[1])]
        if "जॉब कार्ड" in x[1] or "किसान क्रेडिट कार्ड" in x[1] or "श्रम कार्ड" in x[1]:
            df3.append(1)
        else:
            df3.append(0)

    df['JLK'] = df3

    df2 = list(df[['Age', 'Inst_Credit']].values)
    # import re

    df3 = []
    for i in range(len(df2)):
        x = df2[i]
        # y = [int(y) for y in re.findall(r'\d+', x[1])]
        if "आयुष्मान कार्ड" in x[1]:
            df3.append(1)
        else:
            df3.append(0)

    df['Ayushman_card'] = df3

    # df3

    def parsing19(x):
        if x == ' लागू नहीं':
            return 0
        else:
            return 1

    df['ration_c_color'] = df['ration_c_color'].apply(parsing19)



    df2 = df[['house_no', 'village_name']].values.tolist()

    unique_list = []


    def unique(list1):
        # initialize a null list

        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)


    unique(df2)
    # unique_list

    needed = pd.DataFrame(unique_list, columns=['house_no', 'village_name'])
    df3 = df['chronic_disease'].values.tolist()
    # df3

    # needed
    score=[1]*len(unique_list)
    # df3
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]*=df3[j]
          # pass
        # score[i]*=1.0
        # score[i]/=5

    calScore(df2)

    chronic_disease=score

    score=[1]*len(unique_list)
    df3 = df['basic_vaccination'].values.tolist()
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]*=df3[j]
          # pass
        # score[i]*=1.0
        # score[i]/=5

    calScore(df2)

    basic_vaccination = score

    score=[1]*len(unique_list)
    df3 = df['Institutional_delivery'].values.tolist()
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]*=df3[j]
          # pass
        # score[i]*=1.0
        # score[i]/=10

    calScore(df2)

    Institutional_delivery=score

    # Institutional_delivery

    score=[1]*len(unique_list)
    df3 = df['ANC'].values.tolist()
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]*=df3[j]
          # pass
        # score[i]*=1.0
        # score[i]/=10

    calScore(df2)

    ANC=score

    # ANC

    score=[1]*len(unique_list)
    df3 = df['Infant_mortality'].values.tolist()
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]*=df3[j]
          # pass
        # score[i]*=1.0
        # score[i]/=5

    calScore(df2)

    Infant_mortality=score

    # Infant_mortality

    score=[1]*len(unique_list)
    df3 = df['2sqmeals'].values.tolist()
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]*=df3[j]
          # pass
        # score[i]*=1.0
        # score[i]/=10

    calScore(df2)

    sqmeals=score

    # sqmeals

    Health = [0] * len(unique_list)

    for i in range(len(Health)):
        Health[i] *= 1.0
        k = (0)
        k += (chronic_disease[i] + basic_vaccination[i] + Institutional_delivery[i]*ANC[i] + Infant_mortality[i] +
              sqmeals[i])

        Health[i] = k / 5

    # print(len(chronic_disease))
    # print(len(basic_vaccination))
    # print(len(Institutional_delivery))
    # print(len(ANC))
    # print(len(Infant_mortality))
    # print(len(sqmeals))

    # Health

    score=[0]*len(unique_list)
    df3 = df['Ed'].values.tolist()
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]=max(df3[j], score[i])
          # pass
        # score[i]*=1.0
        # score[i]/=10

    calScore(df2)

    Ed=score

    # Ed

    score=[1]*len(unique_list)
    df3 = df['dropout'].values.tolist()
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]*=df3[j]
          # pass
        # score[i]*=1.0
        # score[i]/=10

    calScore(df2)

    dropout=score

    # dropout

    Education = [0] * len(unique_list)


    for i in range(len(Education)):
        # Education[i]*=1.0
        k = (0)
        k += (Ed[i] + dropout[i])

        Education[i] = k / 2

    # print(len(chronic_disease))
    # print(len(basic_vaccination))
    # print(len(Institutional_delivery))
    # print(len(ANC))
    # print(len(Infant_mortality))
    # print(len(sqmeals))

    # Education

    score=[0]*len(unique_list)
    df3 = df['traitional_meeting'].values.tolist()
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]=max(score[i], df3[j])
          # pass
        # score[i]*=3
        # score[i]/=10

    calScore(df2)

    traditional_governance=score

    # traditional_governance

    score=[0]*len(unique_list)
    df3 = df['gram_sabha_meeting'].values.tolist()
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]=max(score[i], df3[j])
          # pass
        # score[i]*=3
        # score[i]/=10

    calScore(df2)

    gsm=score
    # gsm

    score=[0]*len(unique_list)
    df3 = df['Panchayat_meetings'].values.tolist()
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]=max(score[i], df3[j])
          # pass
        # score[i]*=3
        # score[i]/=10

    calScore(df2)

    pm=score
    # pm

    score=[0]*len(unique_list)
    df3 = df['SHG'].values.tolist()
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]=max(score[i], df3[j])
          # pass
        # score[i]*=3
        # score[i]/=10

    calScore(df2)

    SHG=score

    score = [1] * len(unique_list)
    df3 = df['voter'].values.tolist()
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] *= df3[j]
                # pass
            # score[i]*=3
            # score[i]/=10

    calScore(df2)

    voter = score
    # SHG

    Governance = [0] * len(unique_list)

    for i in range(len(Governance)):
        # Education[i]*=1.0
        k = (0)
        k += ((gsm[i] or pm[i] or SHG[i])+voter[i] + traditional_governance[i])

        Governance[i] = k / 3

    # print(len(chronic_disease))
    # print(len(basic_vaccination))
    # print(len(Institutional_delivery))
    # print(len(ANC))
    # print(len(Infant_mortality))
    # print(len(sqmeals))

    # Governance

    score=[0]*len(unique_list)
    df3 = df['traditional_language'].values.tolist()
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]=max(score[i], df3[j])
          # pass
        # score[i]*=3
        # score[i]/=10

    calScore(df2)

    traditional_language=score
    # traditional_language

    score=[0]*len(unique_list)
    df3 = df['traditional_instrument'].values.tolist()
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]=max(score[i], df3[j])
          # pass
        # score[i]*=2
        # score[i]/=10

    calScore(df2)

    traditional_instrument=score
    # traditional_instrument

    score=[0]*len(unique_list)
    df3 = df['traditional_dance'].values.tolist()
    len(unique_list)
    def calScore(list1):
      for i in range(len(unique_list)):
        for j in range(len(list1)):
          if(unique_list[i]==list1[j]):
            score[i]=max(score[i], df3[j])
          # pass
        # score[i]*=2
        # score[i]/=10

    calScore(df2)

    traditional_dance=score
    # traditional_dance

    culture = [0] * len(unique_list)

    for i in range(len(Governance)):
        # Education[i]*=1.0
        k = (0)
        k += (traditional_language[i] + (traditional_instrument[i] or traditional_dance[i]))

        culture[i] = k / 2

    score = [0] * 89
    df3 = df['agricultureland'].values.tolist()
    df4 = df['home_ownership'].values.tolist()
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] = max(score[i], df3[j])
                    score[i] = max(score[i], df4[j])
                # pass
            # score[i]*=2
            # score[i]/=10

    calScore(df2)

    ownership = score
    # ownership

    score = [1] * len(unique_list)
    df3 = df['defecation'].values.tolist()
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] *= df3[j]
                # pass
            # score[i]*=2
            # score[i]/=10

    calScore(df2)

    defecation = score

    score = [1] * len(unique_list)
    df3 = df['bath'].values.tolist()
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] *= df3[j]
                # pass
            # score[i]*=2
            # score[i]/=10

    calScore(df2)

    bath = score

    sanitation = [0] * len(unique_list)
    for i in range(len(unique_list)):
        sanitation[i] = (defecation[i] or bath[i])

    # sanitation

    # df3=df['source_fuel'].values.tolist()
    # df3
    score = [0] * len(unique_list)
    df3 = df['source_fuel'].values.tolist()
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] = max(score[i], df3[j])
                # pass
            # score[i]*=2
            # score[i]/=10

    calScore(df2)

    source_fuel = score
    # source_fuel

    score = [0] * len(unique_list)
    df3 = df['source_drinking_water'].values.tolist()
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] = max(score[i], df3[j])
                # pass
            # score[i]*=2
            # score[i]/=10

    calScore(df2)

    source_drinking = score
    # source_drinking

    score = [0] * len(unique_list)
    df3 = df['electricity'].values.tolist()
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] = max(score[i], df3[j])
                # pass
            # score[i]*=2
            # score[i]/=10

    calScore(df2)

    electricity = score
    # electricity

    df2 = df[['house_no', 'village_name']].values.tolist()
    info = ['फोन', 'टेलीविजन', 'कंप्यूटर सिस्टम', 'लैपटॉप', 'टैबलेट', 'इंटरनेट']
    live = ['पंखा', 'गैस', 'सिचाई', 'प्रेशर', 'मिक्सी']
    tran = ['साइकिल', 'दो पहिया']

    df4 = df['assets'].values.tolist()

    information = [0] * len(df4)
    livelihood = [0] * len(df4)
    transport = [0] * len(df4)

    for i in range(len(df4)):
        for x in info:
            if x in df4[i]:
                information[i] = 1
        for x in live:
            if x in df4[i]:
                livelihood[i] = 1
        for x in tran:
            if x in df4[i]:
                transport[i] = 1

    Informations = [0] * len(unique_list)
    Livelihoods = [0] * len(unique_list)
    Transports = [0] * len(unique_list)

    score = [0] * len(unique_list)
    df3 = information
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] = max(score[i], df3[j])
                # pass
            # score[i]*=2
            # score[i]/=10

    calScore(df2)

    Informations = score

    score = [0] * len(unique_list)
    df3 = transport
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] = max(score[i], df3[j])
                # pass
            # score[i]*=2
            # score[i]/=10

    calScore(df2)

    Transports = score

    df3 = livelihood
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] = max(score[i], df3[j])
                # pass
            # score[i]*=2
            # score[i]/=10

    calScore(df2)

    Livelihoods = score

    # score=[1]*len(unique_list)
    # df3 = df['voter_card'].values.tolist()
    # len(unique_list)
    # def calScore(list1):
    #   for i in range(len(unique_list)):
    #     for j in range(len(list1)):
    #       if(unique_list[i]==list1[j]):
    #         score[i]*=df3[j]
    #       # pass
    #     # score[i]*=2
    #     # score[i]/=10

    # calScore(df2)

    # voterC= score

    score = [1] * len(unique_list)
    df3 = df['aadhar_card'].values.tolist()
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] *= df3[j]
                # pass
            # score[i]*=2
            # score[i]/=10

    calScore(df2)

    aadharC = score

    score = [0] * len(unique_list)
    df3 = df['ration_c_color'].values.tolist()
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] = max(score[i], df3[j])
                # pass
            # score[i]*=2
            # score[i]/=10

    calScore(df2)

    rationC = score

    score = [0] * len(unique_list)
    df3 = df['bank_card'].values.tolist()
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] = max(score[i], df3[j])
                # pass
            # score[i]*=2
            # score[i]/=10

    calScore(df2)

    bankC = score

    score = [0] * len(unique_list)
    df3 = df['Ayushman_card'].values.tolist()
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] = max(score[i], df3[j])
                # pass
            # score[i]*=2
            # score[i]/=10

    calScore(df2)

    ayushmanC = score

    score = [0] * len(unique_list)
    df3 = df['JLK'].values.tolist()
    len(unique_list)

    def calScore(list1):
        for i in range(len(unique_list)):
            for j in range(len(list1)):
                if (unique_list[i] == list1[j]):
                    score[i] = max(score[i], df3[j])
                # pass
            # score[i]*=2
            # score[i]/=10

    calScore(df2)

    JLKC = score

    standard_of_living = [0] * 89

    for i in range(len(Governance)):
        # Education[i]*=1.0
        k = (0)
        k += (Livelihoods[i] * Transports[i] * Informations[i] + electricity[i] + source_drinking[i] + source_fuel[i] +
              sanitation[i] + ownership[i] + aadharC[i] * rationC[i] * bankC[i] * ayushmanC[i] * JLKC[i])

        standard_of_living[i] = k / 7


    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    e=int(e)
    if(a==b and b==c and c==d and d==e):
        a=1
        b=1
        c=1
        d=1
        e=1

    TotalScore = [0] * len(unique_list)

    for i in range(len(Governance)):
        # Education[i]*=1.0
        k = (0.0)
        k += (a * Health[i] + b * Education[i] + e * Governance[i] + d * culture[i] + c * standard_of_living[i])

        TotalScore[i] = k / (a + b + c + d + e)

    # print(len(chronic_disease))
    # print(len(basic_vaccination))
    # print(len(Institutional_delivery))
    # print(len(ANC))
    # print(len(Infant_mortality))
    # print(len(sqmeals))

    # TotalScore
    needed['score'] = TotalScore
    tribe = df['Tribe_N'].values.tolist()

    count = [0] * len(unique_list)

    def CountMem(list1):

        # initialize a null list

        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            for j in range(len(unique_list)):
                if (x == unique_list[j]):
                    count[j] = count[j] + 1

    CountMem(df2)

    # count
    needed['count'] = count
    # needed['count']

    df5 = df['Tribe_N'].values.tolist()
    TribeFamily = [0] * len(unique_list)

    for i in range(len(unique_list)):
        for j in range(len(df2)):
            if (unique_list[i] == df2[j]):
                TribeFamily[i] = df5[j]

    TribeFamily
    needed['Tribe'] = TribeFamily
    # needed

    thres = 1 / 3

    # FinalTable=pd.DataFrame(Tribe, columns=['tribe'])
    # FinalTable

    df6 = needed[['score', 'count', 'Tribe']].values.tolist()

    tribe = needed['Tribe'].values.tolist()

    Tribe = []

    def unique(list1):

        # initialize a null list

        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            if x not in Tribe:
                Tribe.append(x)

    unique(tribe)

    FinalTable = pd.DataFrame(Tribe, columns=['tribe'])

    TotalPeople = [0] * len(Tribe)
    DevelopedPeople = [0] * len(Tribe)
    Incidence = [0] * len(Tribe)
    k = 0

    for i in range(len(Tribe)):
        for j in range(len(df6)):
            if (df6[j][2] == Tribe[i]):
                TotalPeople[i] += df6[j][1]
                if (df6[j][0] > thres):
                    DevelopedPeople[i] += df6[j][1]
                # if(df6[j][2]=='बैगा'):
                #   k+=df6[j][0]

    # TotalPeople
    # df6

    for i in range(len(Tribe)):
        Incidence[i] = DevelopedPeople[i] / TotalPeople[i]

    # Incidence

    Intensity = [0] * len(Tribe)

    for i in range(len(Tribe)):
        for j in range(len(needed)):
            if (df6[j][2] == Tribe[i] and df6[j][0] > thres):
                Intensity[i] += df6[j][1] * df6[j][0]
        if (DevelopedPeople[i] == 0):
            Intensity[i] = '-'
        else:
            Intensity[i] /= DevelopedPeople[i]

    TDI = [0] * len(Tribe)

    for i in range(len(Tribe)):
        TDI[i] = Intensity[i] * Incidence[i]

    FinalTable['Incidence'] = Incidence
    FinalTable['Intensity'] = Intensity
    FinalTable['TDI'] = TDI


    serial_no=[0]*len(unique_list)

    for i in range(len(unique_list)):
        serial_no[i]=i+1
    need=pd.DataFrame()
    df2 = df[['house_no', 'village_name', 'data_lat', 'data_lng']].values.tolist()

    unique_list = []

    def unique(list1):
        # initialize a null list

        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)

    unique(df2)
    # sco1
    needed_d = pd.DataFrame(unique_list, columns=['house_no', 'village_name', 'data_lat', 'data_lng'])
    need['serial_no']=serial_no
    need['data_lat']=needed_d['data_lat']
    need['data_lng']=needed_d['data_lng']
    need['house_no']=needed['house_no']
    need['village_name']=needed['village_name']
    need['score']=TotalScore

    return FinalTable