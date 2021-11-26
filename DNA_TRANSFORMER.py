#A=T , C=G
### START FUNCTION
def dna_complementary(dna_value):
    # your code here
    list_com =[]
    for i in dna_value:
        if i == 'A':
            list_com.append('T')
        elif i=='T':
            list_com.append('A') 
        elif i == 'C':
            list_com.append('G') 
        elif i == 'G':
            list_com.append('C') 
        else:  i   
            
    final_dna = ''.join(list_com)       
   
    return final_dna
### END FUNCTION
dna_complementary('ATCTTATAATTACCGAGTCGATCGG')