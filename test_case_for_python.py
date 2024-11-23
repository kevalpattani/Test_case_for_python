import time

def locate_card(cards, query):

    """ Your algorithm here """

    """
    # Example algorithm  

    position = 0

    while True:
        if cards[position] == query:
            return position
        position += 1

        if position == len(cards):
            return -1
            
    """

def input_tests():
    numOfTest = int(input("Number of Tests : "))
    test = []
    for i in range(1, numOfTest + 1):
        test_case = int(input(f"number of elements for test {i} : "))
        cards = [int(input(f'element {j+1} for test case {i} : ')) for j in range(test_case)]
        query = int(input("Query : "))
        expected_output = int(input("Expected output : "))
        test.append({'input': {'cards': cards, 'Query': query}, 'output': expected_output})
    return test

def main():
    all_tests = input_tests()
    passed_tests = 0
    failed_tests = 0
    total_time = 0

    for i, test_case in enumerate(all_tests):
        print()
        print(f"-------- Test {i+1} --------")
        print()
        start_time = time.time()
        cards = test_case['input']['cards']
        query = test_case['input']['Query']
        expected_output = test_case['output']

        result = locate_card(cards, query)
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Execution time: {execution_time:.3f} seconds")

        if result == expected_output:
            print("Test Passed")
            passed_tests += 1
        else:
            print("Test Failed")
            failed_tests += 1


        print()
        print(f"-------- --- --------")
        print()

    print("\nSummary:")
    print(f"Total Tests: {len(all_tests)}")
    print(f"Passed Tests: {passed_tests}")
    print(f"Failed Tests: {failed_tests}")
    print(f"Total Execution Time: {total_time:.2f} seconds")

if __name__ == "__main__":
    main()
