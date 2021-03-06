import os
import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def space_group_to_crystal_system(space_group_number):
    '''
    Converts a space group number (1-230) to the crystal system.
    
    Args:
        space_group_number: An int for the space group.
        
    Returns:
        A string for the crystal system for that space group.
    '''
    if space_group_number <= 2:
        return 'triclinic'
    elif space_group_number <= 15:
        return 'monoclinic'
    elif space_group_number <= 74:
        return 'orthorhombic'
    elif space_group_number <= 142:
        return 'tetragonal'
    elif space_group_number <= 167:
        return 'trigonal'
    elif space_group_number <= 194:
        return 'hexagonal'
    else:
        return 'cubic'
    
    
def plot_dielectric_data():
    '''
    Plots refractive index vs. band gap from dielectric dataset.
    '''
    with open('../../assets/data/dielectric_dataset.json', 'r') as f:
        data = json.load(f)
        
    n = []
    Eg = []
    system = []

    for m in data:
        n.append(m['n'])
        Eg.append(m['band_gap'])
        system.append(space_group_to_crystal_system(m['meta']['space_group']))
    df = pd.DataFrame({'n':n, 'Eg':Eg, 'system':system})

    symbols = ['s', 'h', 'X', 'o', '^', 'd', 'H']
    groups = df.groupby('system', sort=True)

    fig, ax = plt.subplots(figsize=(11, 7.5))
    for i, (name, group) in enumerate(groups):
        ax.scatter(group.Eg, group.n, marker=symbols[i], s=80, label=name)
    ax.set_yscale('log')
    ax.set_ylabel('$n$', fontsize=30)
    ax.set_xscale('log')
    ax.set_xlim(0.09, 10)
    ax.set_xlabel('$E_g$ (eV)', fontsize=28)
    ax.tick_params(which='major', length=15, width=5, pad=11, direction='in', labelsize=22)
    ax.tick_params(which='minor', length=10, width=3.5, direction='in', labelsize=22)
    ax.legend(title='crystal system', fontsize=20, title_fontsize=20)
    plt.show()



def get_api_key():
    # get API key using one of two ways
    api_key = None
    try:       # this is for running locally
        import os
        api_key = os.environ['MAPI_KEY']
    except:    # this is for running on DataHub
        with open('../../assets/files/mp_api_key.txt', 'r') as f:
            api_key = f.readlines()[1].strip()

    # assert helps catch potential bugs
    assert api_key is not None, 'API key not set correctly in environment!'
    assert api_key != '', 'API key not found in mp_api_key.txt file!'

    return api_key
