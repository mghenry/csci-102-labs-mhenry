#   Maggie Henry
#   ​CSCI 101 – Section G
#   Week 4 - Lab B - Amino Acids
#   References: none
#   Time: 20 minutes

print('Input the chemical elements of the amino acid:')

carbon = int(input('CARBON>'))
hydrogen = int(input('HYDROGEN>'))
nitrogen = int(input('NITROGEN>'))
oxygen = int(input('OXYGEN>'))
sulfur = int(input('SULFUR>'))

if carbon == 3 and hydrogen == 7 and nitrogen == 1 and oxygen == 2 and sulfur == 0:
    amino_acid = 'Alanine'
    amino_string = '3C-7H-N-2O'

elif carbon == 6 and hydrogen == 14 and nitrogen == 4 and oxygen == 2 and sulfur == 0:
    amino_acid = 'Arginine'
    amino_string = '6C-14H-4N-2O'

elif carbon == 4 and hydrogen == 8 and nitrogen == 2 and oxygen == 3 and sulfur == 0:
    amino_acid = 'Asparagine'
    amino_string = '4C-8H-2N-3O'

elif carbon == 3 and hydrogen == 7 and nitrogen == 1 and oxygen == 2 and sulfur == 1:
    amino_acid = 'Cysteine'
    amino_string = '3C-7H-N-2O-S'

elif carbon == 6 and hydrogen == 9 and nitrogen == 3 and oxygen == 2 and sulfur == 0:
    amino_acid = 'Histidine'
    amino_string = '6C-9H-3N-2O'

elif carbon == 5 and hydrogen == 10 and nitrogen == 2 and oxygen == 3 and sulfur == 0:
    amino_acid = 'Glutamine'
    amino_string = '5C-10H-1N-3O'

else:
    amino_string = 'This is not an amino acid'

print('The amino acid for', amino_string, 'is', amino_acid)
print('OUTPUT', amino_string)
print('OUTPUT', amino_acid)
