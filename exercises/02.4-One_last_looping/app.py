my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:

def last_loop(list):
    my_sample_list[2] = "Steven"
    my_sample_list[-1] = "Pepe"
    my_sample_list[0] = my_sample_list[2] + my_sample_list[4]
    longitud = len(my_sample_list)
    for i in range(longitud):
        
        print(my_sample_list[longitud-i-1])


last_loop(my_sample_list)


