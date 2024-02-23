from nistrng import *
import numpy

def nist_test(sequence: numpy.ndarray): 
    
    binary_sequence: numpy.ndarray = pack_sequence(sequence)
    eligible_battery: dict = check_eligibility_all_battery(binary_sequence, SP800_22R1A_BATTERY)
    
    print("Eligible test from NIST-SP800-22r1a:")
    for name in eligible_battery.keys():
        print("-" + name)
    
    results = run_all_battery(binary_sequence, eligible_battery, False)
    
    print("Test results:")
    for result, elapsed_time in results:
        if result.passed:
            print("- PASSED - score: " + str(numpy.round(result.score, 3)) + " - " + result.name + " - elapsed time: " + str(elapsed_time) + " ms")
        else:
            print("- FAILED - score: " + str(numpy.round(result.score, 3)) + " - " + result.name + " - elapsed time: " + str(elapsed_time) + " ms") 

if __name__ == "__main__":
    sequence = numpy.load('Optimized_PRNS.npy')
    nist_test(sequence)