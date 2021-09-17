### 

path_1 = 'C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/maps'
path_2 = 'C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/download/maps'

###

from os import listdir
from os.path import isfile, join

maps_files = []

for path in (path_1, path_2):
	maps_files += [f for f in listdir(path)
		if ( 
			f.split('_')[0] == 'mvm' and
			f.split('.')[-1] == 'bsp' and
			isfile(join(path, f))
		)
	]

maps_names = sorted([m.split('.')[0] for m in maps_files])

f = open('tf_mvm_missioncycle.res', 'w')
f.write("\
\"tf_mvm_missioncycle.res\"\n\
{\n\
	\"categories\"		\"1\"\n\
	\"1\"\n\
	{\n\
		\"count\"		\"" + str(len(maps_names)) + "\"\n"
)

i = 0

for m in maps_names:
	i += 1
	f.write("\
		\"" + str(i) + "\"\n\
		{\n\
			\"map\"		\"" + m + "\"\n\
			\"popfile\"	\"" + m + "\"\n\
		}\n"
	)

f.write("\
	}\n\
}\n\
")
