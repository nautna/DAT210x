import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
df = pd.read_csv("/Users/antuanweeks/DAT210x/Module2/Datasets/servo.data",
                 header=None, names=['motor', 'screw', 'pgain', 'vgain', 'class'])
# viewing dataframe
# print df.head()

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
df[df.loc[:, 'vgain'] == 5]
print '# entries w/ vgain = 5: ' + str(len(df[df.loc[:, 'vgain'] == 5]))

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
df[(df['motor'] == 'E') & (df['screw'] == 'E')]
print '# entries w/ motor and screw = E: ' + \
    str(len(df[(df['motor'] == 'E') & (df['screw'] == 'E')]))


# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
print 'mean of entries w/ pgain = 4: ' + \
    str(df[df.loc[:, 'pgain'] == 4]['vgain'].mean())


# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
df.dtypes


