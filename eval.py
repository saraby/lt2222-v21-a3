import sys
import argparse
import numpy as np
import torch
from train import a, vowels


def new_vowels(ground_truth, predicted):
    
    new = []
    s_e_tokens = ['<s>', '<e>']
    for character in ground_truth:
        if character in vowels:
            new.append(predicted.pop(0))
        elif character in s_e_tokens:
            pass
        else:
            new.append(character)
    return new

def x_in_unique_characters(x, unique_characters):

    zeros_ones_array = np.zeros(len(unique_characters))
    #To avoid weird characters messing up with the data
    if x in unique_characters:
        zeros_ones_array[unique_characters.index(x)] = 1
    return zeros_ones_array

def build_matrix(tokenized_text, unique_characters):

    vowel_idx_list = []
    features_list = []
    for v in range(len(tokenized_text) - 4):
        if tokenized_text[v+2] not in vowels:
            continue
        
        vowel_index = vowels.index(tokenized_text[v+2])
        vowel_idx_list.append(vowel_index)
        feature= np.concatenate([x_in_unique_characters(x, unique_characters) for x in [tokenized_text[v], tokenized_text[v+1], tokenized_text[v+3], tokenized_text[v+4]]])
        features_list.append(feature)

    return np.array(features_list), np.array(vowel_idx_list) 

def accuracy(ground_truth, predicted):

    correct = 0
    total = len(ground_truth)
    for feature_listound, pred in zip(ground_truth, predicted):
        if feature_listound == pred:
            correct += 1
    
    print('Accuracy= %d %%' % (100 * correct / total))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("model_path", type=str, help="The model")
    parser.add_argument("test_path", type=str, help="The path to the test file")
    parser.add_argument("output_file", type=str, help="The name of the output file")
    args = parser.parse_args()

    #Loading the model
    model = torch.load(args.model_path)
    model.eval()
    
    #Loading the test data
    tokenized_data = a(args.test_path)
            
    test_matrix, expected = build_matrix(tokenized_data[0], model.vocab)
    
    #Creating evaluation instances compatible with training instances
    with torch.no_grad():
        outputs = model(torch.Tensor(test_matrix))
        _, predicted = torch.max(outputs.data, 1)

    #Using the model to predict instances
    predicted_vowles = []
    for vowel_index in predicted:
        predicted_vowles.append(vowels[vowel_index])
    
    #Writing predicted vowels into output file
    output_text = new_vowels(tokenized_data[0], predicted_vowles)
    with open(args.output_file, 'w') as f:
        f.write(''.join(output_text))
    
    #Printing accuracy of model to terminal  
    accuracy(expected, predicted)
