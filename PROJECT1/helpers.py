# helper method to make a list
def make_list_from_dict_values(dict_values_list):
    new_list = []
    for each in dict_values_list:
        new_list.append(each[0])
    return new_list


# small helper method used to write a word and newid to the frequency dictionary
#  it is used to generate 44 dictionary blocks
# key is the word
# value is doc_id
def add_to_frequency_dict(term, doc_id, my_dict):
    found_doc_id = False
    if term not in my_dict.keys():
        my_dict[term] = [[doc_id, 1]]
    else:
        # if doc_id exists already in value list, increment its frequency
        for id_freq in my_dict[term]:
            if id_freq[0] is doc_id:
                id_freq[1] += 1
                found_doc_id = True
        #  if doc_id doesn't exist for given term, append it to the existing list with frequency 1
        if found_doc_id is False:
            my_dict[term].append([doc_id, 1])
    return my_dict


# this helper method is used to add a list of doc it and frequency to the final dictionary
def add_to_frequency_dict_with_array(term, doc_id_freq_array, my_dict):
    found_doc_id = False
    for doc_id_freq_input in doc_id_freq_array:
        try:
            if term not in my_dict.keys():
                my_dict[term] = [doc_id_freq_input]
            else:
                # if doc_id exists already in value list, increment its frequency
                for each in my_dict[term]:
                    # if the newly added values 'each' have the doc_id in the dictionary, increment the frequency to
                    # that
                    # of 'each'
                    if each[0] is doc_id_freq_input[0]:
                        each[1] += doc_id_freq_input[1]
                        found_doc_id = True
                #  if doc_id doesn't exist for given term, append it to the existing list with frequency 1
                if found_doc_id is False:
                    my_dict[term].append(doc_id_freq_input)

        except TypeError as e:
            print(e)
            print(term)
            print(doc_id_freq_input)
    print('added term:' + term)
    return my_dict


# small helper method to write a word and newid to dictionary
# it returns the dictionary with newly added terms and/or newid value
# it also returns a boolean to indicate whether the word added to dictionary already exists or not
# if the word already exists in the dictionary, return false
# if the word doesn't exist in the dictionary, return true
def add_to_dict_array(key, values, my_dict):
    is_new_term = True
    try:
        if key not in my_dict.keys():
            my_dict[key] = values
            is_new_term = True

        else:
            if values not in my_dict[key]:
                # if value doesn't exist in value list for given key
                my_dict[key] += values
                my_dict[key].sort()
            if key in my_dict.keys():
                is_new_term = False
    except Exception as e:
        print('error')
        print(e)
        print('key')
        print(key)
        print('value')
        print(values)
    return my_dict, is_new_term


# print dictionary key and values
def print_dict_to_file(output_dir, filename, dict_name, sorted_keys):
    if sorted_keys is True:
        with open(output_dir + filename + ".txt", 'w+') as disk_write:
            [disk_write.write('"{0}" :{1}\n'.format(key, value)) for key, value in
             sorted(dict_name.items())]
            disk_write.write('EOF')
    else:
        with open(output_dir + filename + ".txt", 'w+') as disk_write:
            [disk_write.write('"{0}" :{1}\n'.format(key, value)) for key, value in
             dict_name.items()]
            disk_write.write('EOF')
