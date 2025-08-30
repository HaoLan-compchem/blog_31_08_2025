import os
from pymol import cmd

cmd.delete('all')
cif_file_count = int(0)

current_directory = '/mnt/c/Users/cha13/Desktop/boltz/blog/macrocyclic_MG/Elironrasib_ligand_only/use_potentials'
for item in os.listdir(current_directory):
    item_path = os.path.join(current_directory, item)
    if os.path.isdir(item_path):
        try:
            name = item.split('results_')[-1]
            if name == '9BFX_ligand_only_0':
                source = 'bioactive'
            elif name == '9BFX_ligand_only_1':
                source = 'ETKDG1'
            elif name == '9BFX_ligand_only_2':
                source = 'ETKDG2'
            elif name == '9BFX_ligand_only_3':
                source = 'ETKDG3'
            elif name == '9BFX_ligand_only_4':
                source = 'ETKDG4'
            elif name == '9BFX_ligand_only_5':
                source = 'ETKDG5'
            elif name == '9BFX_ligand_only_6':
                source = 'ETKDG0'
            else:
                continue

            prediction_dir = os.path.join(item_path, 'predictions', name)
            for file in os.listdir(prediction_dir):
                if file.endswith('.cif'):
                    cif_file = os.path.join(prediction_dir, file)
                    cif_file_count += 1
                    cmd.load(cif_file, f'mol_{source}_{cif_file_count}')
                    cmd.save(os.path.join(current_directory, f'all_ligands/mol_{source}_{cif_file_count}.sdf'), f'mol_{source}_{cif_file_count}')
        except:
            continue
