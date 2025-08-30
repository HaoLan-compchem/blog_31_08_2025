import os
from pymol import cmd
from pymol import util
cif_file_count = int(0)
cmd.delete('all')
right_torsion_list = []
current_directory = 'C:\\Users\\cha13\\Desktop\\boltz\\blog\\macrocyclic_MG\\9BFX_binary\\use_potentials'

for item in os.listdir(current_directory):
    item_path = os.path.join(current_directory, item)
    if os.path.isdir(item_path):
        try:
            name = item.split('results_')[-1]
            if name == 'CYPA_bioactive':
                source = 'bioactive'
            elif name == 'CYPA_lowenergy':
                source = 'ETKDG1'
            elif name == 'CYPA_lowenergy_1':
                source = 'ETKDG2'
            elif name == 'CYPA_lowenergy_2':
                source = 'ETKDG3'
            elif name == 'CYPA_lowenergy_3':
                source = 'ETKDG4'
            elif name == 'CYPA_lowenergy_4':
                source = 'ETKDG5'
            elif name == 'CYPA_random':
                source = 'ETKDG0'
            else:
                continue

            prediction_dir = os.path.join(item_path, 'predictions', name)
            for file in os.listdir(prediction_dir):
                if file.endswith('.cif'):
                    cif_file = os.path.join(prediction_dir, file)
                    cif_file_count += 1
                    cmd.load(cif_file, f'mol_{source}_{cif_file_count}')
                    torsion = cmd.get_dihedral(f"mol_{source}_{cif_file_count} and resn A1AOD and name N11", 
                                               f"mol_{source}_{cif_file_count} and resn A1AOD and name C10", 
                                               f"mol_{source}_{cif_file_count} and resn A1AOD and name C9", 
                                               f"mol_{source}_{cif_file_count} and resn A1AOD and name C4")
                    if torsion < 0:
                        right_torsion_list.append(f"mol_{source}_{cif_file_count}")

        except:
            continue

print(right_torsion_list)

obj_list = cmd.get_object_list()
target_obj = obj_list[0]
cmd.select("target_protein_sel", f"{target_obj} and polymer.protein")
util.mass_align("target_protein_sel",0,_self=cmd)
cmd.delete("aln_all_to_target_protein_sel")
cmd.delete("target_protein_sel")

cmd.select("all_proteins", "polymer.protein")
cmd.remove("all_proteins")
cmd.delete("all_proteins")

for i in obj_list:
    cmd.save(os.path.join(current_directory, f'all_ligands/{i}.sdf'), i)
