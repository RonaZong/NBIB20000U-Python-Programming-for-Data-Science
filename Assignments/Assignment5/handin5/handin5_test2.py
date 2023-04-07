import timeit
import handin5
'''Test the handin5_test2 module'''
start_time = timeit.default_timer()
differences = handin5.wordfile_differences_binary_search('british-english', 'american-english')
time_spent = timeit.default_timer() - start_time
print(len(differences))
print(time_spent)