from seasons import transform, check

# def test_check_abc():
#     assert check("1 may 1982") == 

def test_norm_input():
    assert check("2023-04-12") == True
    
def test_abnormal_input():
    assert check("2023-13-13") == False
    assert check("2023-04-32") == False

def test_1year():
    assert transform("2022-04-12") == 525600


