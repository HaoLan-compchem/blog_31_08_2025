def get_each_SASA_in_complex(object_name, protein_1_chain_name, protein_2_chain_name, ligand_chain_name):

    chain_list = cmd.get_chains(object_name)
    area_per_chain = {}
    seperate_area_per_chain = {}

    for chain_id in chain_list:
        if chain_id == protein_1_chain_name:
            selection = f'{object_name} and chain {chain_id}'
            area = cmd.get_area(selection)
            area_per_chain['protein_1'] = area
            cmd.copy_to('protein_1', selection)
            seperate_area = cmd.get_area('protein_1')
            seperate_area_per_chain['protein_1'] = seperate_area
        elif chain_id == protein_2_chain_name:
            selection = f'{object_name} and chain {chain_id}'
            area = cmd.get_area(selection)
            area_per_chain['protein_2'] = area
            cmd.copy_to('protein_2', selection)
            seperate_area = cmd.get_area('protein_2')
            seperate_area_per_chain['protein_2'] = seperate_area
        elif chain_id == ligand_chain_name:
            selection = f'{object_name} and chain {chain_id}'
            area = cmd.get_area(selection)
            area_per_chain['ligand'] = area
            cmd.copy_to('ligand', selection)
            seperate_area = cmd.get_area('ligand')
            seperate_area_per_chain['ligand'] = seperate_area 
        else:
            continue
    
    cmd.delete("ligand")
    cmd.delete("protein_2")
    cmd.delete("protein_1")

    for chain, area in area_per_chain.items():
        print(f"{chain} in complex: {area:.2f} Å²")
    for chain, area in seperate_area_per_chain.items():
        print(f"{chain} in seperate: {area:.2f} Å²")
    
#just load this pymol module in python console
