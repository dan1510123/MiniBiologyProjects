import matplotlib.pyplot as plt

def get_dna_info(sequence, window_size, base_list):
    sequence = sequence.upper()
    base_content_list = []

    for start_index in range(len(sequence) - window_size):
        bases_contained = 0

        for index_in_window in range(start_index, start_index + window_size):
            if sequence[index_in_window] in base_list:
                bases_contained += 1
        
        base_content_list.append(bases_contained / window_size)
    
    return base_content_list

def display_dna_info(sequence, window_size, base_list):
    base_content_list = get_dna_info(sequence, window_size, base_list)
    
    plt.plot(base_content_list)
    plt.xlabel('Start Sequence Index')
    plt.ylabel('% Content of ' + base_list)
    plt.show()

dna_sequence = "gtatgacagtgaatgtgcgatactcatcttgtaaaaaagctataagagctatttgagattctttattgttaatctacttaaaaaaaattc \
tgcttttaaacttttacatcatataacaataatttttttctacatgcatgtgtatat.aaaaggaaactatattacaaagtacacatggat \
tttttttcttaattaatgaccatgtgacttcattttggttttaaaataggtatatagaatcttaccacagttggtgtacaggacattcat \
ttataataaacttatatcagtcaaattaaacaaggatagtgctgctattactaaaggtttctctgggttcccaaatgatacttgaccaaa \
tttgtccctttggcttgttgtcttcagacaccctttcttcatgtgttggagctgccatttcgtgtgcccccaaactctacttgagctgtt \
agggaatcacattttgcagtgacagccttagtgtgggtgcattttcaggcaatactttttcagtatatttctgctttgtagattattagc \
taaatcaagtcacataaacttccttaatttagatacttgaaaaaattgtcttaaaagaaaatttttttagtaagaattaatttagaatta \
gccagaaaactcccagtggtagccaagaaagaggaataaatattggtggtaattttttaagttcccatctctggtagccaagtaaaaaaa \
gagggtaactcattaataaaataacaaatcatatctattcaaagaatggcaccagtgtgaaaaaaagctttttaaccaatgacatttgtg \
atatgattattctaatttagtctttttcaggtacaagatattatgaaattacattttgtgtttatgttatttgcaatgttttctatggaa \
atatttcacag"
window_size = 10

print(display_dna_info(dna_sequence, window_size, "GC"))