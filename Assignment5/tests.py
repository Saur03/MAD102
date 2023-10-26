def question2_tests():
    q2_tests = []
    # TESTCASE 1:
    q2_tests.append({
        'input': {
            'ar' : ['n']
        },
        'output': ['sorry', 'Thanks']
    })
    # TESTCASE 2:
    q2_tests.append({
        'input': {
            'ar' : ['N']
        },
        'output': ['sorry', 'Thanks']
    })
    # TESTCASE 3:
    q2_tests.append({
        'input': {
            'ar' : ['NO']
        },
        'output': ['sorry', 'Thanks']
    })
    # TESTCASE 4:
    q2_tests.append({
        'input': {
            'ar' : ['no']
        },
        'output': ['sorry', 'Thanks']
    })
    # TESTCASE 5:
    q2_tests.append({
        'input': {
            'ar' : ['y', 6, 'e', 'n']
        },
        'output': ['0', '2', '4', '6', 'Thanks']
    })
    # TESTCASE 6:
    q2_tests.append({
        'input': {
            'ar' : ['Y', 9, 'E', 'N']
        },
        'output': ['0', '2', '4', '6', '8', 'Thanks']
    })
    # TESTCASE 7:
    q2_tests.append({
        'input': {
            'ar' : ['YES', 12, 'EVEN', 'NO']
        },
        'output': ['0', '2', '4', '6', '8', '10', '12', 'Thanks']
    })
    # TESTCASE 8:
    q2_tests.append({
        'input': {
            'ar' : ['yes', 15, 'even', 'no']
        },
        'output': ['0', '2', '4', '6', '8', '10', '12', '14', 'Thanks']
    })
    # TESTCASE 9:
    q2_tests.append({
        'input': {
            'ar' : ['y', 6, 'o', 'n']
        },
        'output': ['1', '3', '5', 'Thanks']
    })
    # TESTCASE 10:
    q2_tests.append({
        'input': {
            'ar' : ['Y', 9, 'O', 'N']
        },
        'output': ['1', '3', '5', '7', '9', 'Thanks']
    })
    # TESTCASE 11:
    q2_tests.append({
        'input': {
            'ar' : ['YES', 12, 'ODD', 'NO']
        },
        'output': ['1', '3', '5', '7', '9', '11', 'Thanks']
    })
    # TESTCASE 12:
    q2_tests.append({
        'input': {
            'ar' : ['yes', 15, 'odd', 'no']
        },
        'output': ['1', '3', '5', '7', '9', '11', '13', '15', 'Thanks']
    })
    # TESTCASE 13:
    q2_tests.append({
        'input': {
            'ar' : ['yep', 6, 'oxo', 'nada']
        },
        'output': ['1', '3', '5' 'Thanks']
    })
    # TESTCASE 14:
    q2_tests.append({
        'input': {
            'ar' : ['Yess', 9, 'Odio', 'Nola']
        },
        'output': ['1', '3', '5', '7', '9', 'Thanks']
    })
    # TESTCASE 15:
    q2_tests.append({
        'input': {
            'ar' : ['YBAHVC', 12, 'ODDJHGBSAGVBHCH', 'NOPE']
        },
        'output': ['1', '3', '5', '7', '9', '11', 'Thanks']
    })
    # TESTCASE 16:
    q2_tests.append({
        'input': {
            'ar' : ['ysvdsjvbj', 15, 'odpa', 'nodo']
        },
        'output': ['1', '3', '5', '7', '9', '11', '13', '15', 'Thanks']
    })
    # TESTCASE 17:
    q2_tests.append({
        'input': {
            'ar' : ['y', 6, 'e', 'y', 12, 'o', 'n']
        },
        'output': ['0', '2', '4', '6', 'continue','1', '3', '5', '7', '9', '11','Thanks']
    })
    # TESTCASE 18:
    q2_tests.append({
        'input': {
            'ar' : ['Y', 9, 'E', 'Y', 15, 'O', 'N']
        },
        'output': ['0', '2', '4', '6', '8', 'continue', '1', '3', '5', '7', '9', '11', '13', '15', 'Thanks']
    })
    # TESTCASE 19:
    q2_tests.append({
        'input': {
            'ar' : ['YES', 12, 'EVEN', 'YES', 18, 'ODD', 'NO']
        },
        'output': ['0', '2', '4', '6', '8', '10', '12', 'continue', '1', '3', '5', '7', '9', '11', '13', '15', '17', 'Thanks']
    })
    # TESTCASE 20:
    q2_tests.append({
        'input': {
            'ar' : ['yes', 15, 'even', 'yes', 21, 'odd', 'no']
        },
        'output': ['0', '2', '4', '6', '8', '10', '12', '14', 'continue', '1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', 'Thanks']
    })
    return q2_tests

def question3_tests():
    q3_tests = []
    # TESTCASE 1:
    q3_tests.append({
        'input': {
            'ar' : "This is a simple sentence."
        },
        'output': "Siht si a elpmis ecnetnes."
    })
    # TESTCASE 2:
    q3_tests.append({
        'input': {
            'ar' : "my name is saurabh"
        },
        'output': "Ym eman si hbaruas."
    })
    return q3_tests

def question4_tests():
    q4_tests = []
    # TESTCASE 1:
    q4_tests.append({
        'input': {
            'ar' : "HelLo.  ThiS is A StrING with MANY Sentences.  ThIS Is NEat"
        },
        'output': 'Hello.'
'This is a string with many sentences.'
'This is neat.'
    })
    # TESTCASE 2:
    q4_tests.append({
        'input': {
            'ar' : "My name is Saurabh Chawla. I am a Big ChUtIya."
        },
        'output': "'My name is saurabh chawla.'\n'I am a big chutiya.'"
    })
    return q4_tests
