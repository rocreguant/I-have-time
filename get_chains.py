import re
import os

#Idea: https://www.biostars.org/p/59715/

list_path  =  'list.txt'
db_path    =  '/n/scratch2/roc/databases/pdb/'

with open(list_path, 'r') as f_pdb:
    for pdb in f_pdb:

        #Getting the info from the pdb to download
        structure = pdb.split(':')[0].lower()
        chain = pdb.split(':')[1].upper()[0]

        #downloading the pdbs
        if(not os.path.isfile(db_path+structure+'.pdb') or True):
            _ = os.popen('wget -O '+db_path+structure+'.pdb https://files.rcsb.org/download/'+structure+'.pdb > /dev/null 2>&1').read()

        with open(db_path+structure+'.pdb', 'r') as f:
            with open(db_path+'chains/'+structure+'_'+chain+'.pdb', 'w') as fo:
                for line in f:
                    #selecting the atoms from the desired chain and writing them in a new file
                    if 'ATOM' in line and ' '+chain+' ' in line:
                        fo.write(line)
