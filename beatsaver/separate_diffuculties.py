from os import listdir
from shutil import copyfile


def organized_unzipped_songs():
    easy_dir = './difficulties/easy'
    normal_dir = './difficulties/normal'
    hard_dir = './difficulties/hard'
    expert_dir = './difficulties/expert'
    expert_plus_dir = './difficulties/expertplus'
    easy_count = 0
    normal_count = 0
    hard_count = 0
    expert_count = 0
    expert_plus_count = 0
    for song in listdir('./songs'):
        for f in listdir(f'./songs/{song}'):
            if f.lower() == 'easy.dat':
                easy_count += 1
                copyfile(f'./songs/{song}/{f}', f'{easy_dir}/{song}.json')
            elif f.lower() == 'normal.dat':
                normal_count += 1
                copyfile(f'./songs/{song}/{f}', f'{normal_dir}/{song}.json')
            elif f.lower() == 'hard.dat':
                hard_count += 1
                copyfile(f'./songs/{song}/{f}', f'{hard_dir}/{song}.json')
            elif f.lower() == 'expert.dat':
                expert_count += 1
                copyfile(f'./songs/{song}/{f}', f'{expert_dir}/{song}.json')
            elif f.lower() == 'expertplus.dat':
                expert_plus_count += 1
                copyfile(f'./songs/{song}/{f}', f'{expert_plus_dir}/{song}.json')
    print("files organized!")
    print("easy beatmaps=", easy_count)
    print("normal beatmaps=", normal_count)
    print("hard beatmaps=", hard_count)
    print("expert beatmaps=", expert_count)
    print("expert plus beatmaps=", expert_plus_count)

