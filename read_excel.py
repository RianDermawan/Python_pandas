import pandas as pd
path = 'D:\\Naila\\laporan_iklim_harian (' # file path
isi = [] # empyt list

# using loop for generate data to list 
for i in range(12): # optional range, it depends on your data. My data have is 11 
    data_i = pd.read_excel(path+str(i)+').xlsx') # read every excel
    data_i = [data_i] # change type data to list
    isi = isi + data_i  # combine all data into a list

# combine data into one file
data_baru = pd.concat(isi, axis=0)

# export excel 
data_baru.to_excel('D:\\Naila\\data_baru.xlsx', index=False)
