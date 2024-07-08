def file_creation(file_name):
    """Creates a file with the given name and returns the file object."""
    file = open(file_name, "w")
    return file

file_list = [
"1_Bubble_Sort.py","2_Selection_Sort.py","3_Insertion_Sort.py","4_Merge_Sort.py",
"5_Quick_Sort.py","6_Heap_Sort.py","7_Radix_Sort.py","8_Bucket_Sort.py",
"9_Shell_Sort.py","10_Counting_Sort.py","11_Tim_Sort.py","12_Comb_Sort.py",
"13_Pigeonhole_Sort.py","14_Cycle_Sort.py","15_Cocktail_Shaker_Sort.py",
"16_Gnome_Sort.py","17_Bitonic_Sort.py","18_Odd-Even_Sort.py"
]

for file in file_list:
    file_creation(file)