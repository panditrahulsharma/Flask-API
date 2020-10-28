def get_speakers(filepath):
    #loading file
    joe_aws = open(filepath)
    joe_aws = json.load(joe_aws)

    #generating speaker data
    speaker = []
    for item in joe_aws['results']['speaker_labels']['segments']:
      speaker.extend(item['items'])

    #generating token data
    temp_token = joe_aws['results']['items']
    token = []
    for item in temp_token:
      if len(item)==4: token.append(item)

    #decoding from speakers and tokens
    prev_speaker = 'spk_0'
    script = ""
    change_count = 0
    id2wrds = {}
    words_list = []
    start_time = speaker[0]['start_time']
    for tok, speak in zip(token, speaker):
      current_speaker = speak['speaker_label']
      if current_speaker != prev_speaker: #condition for change in speaker
        temp = {'speaker': prev_speaker,'words':words_list,'text' : script.strip(), 'start_time': start_time, 'end_time': end_time}
        start_time = speak['start_time']
        id2wrds[change_count] = temp
        change_count+=1
        script = ""
        words_list = []
      end_time = speak['end_time']
      script = script + tok['alternatives'][0]['content']+" "
      words_list.append(tok)
      prev_speaker = current_speaker
    temp = {'speaker': prev_speaker,'words':words_list, 'text' : script.strip(), 'start_time': start_time, 'end_time': end_time}
    id2wrds[change_count] = temp 
    return id2wrds




p=get_speakers("sp.json")






