from twttr import shorten

def test_arg_a():
    assert shorten("AdaDs") == "dDs"
    

def test_arg_e():
    assert shorten("EdeDs") == "dDs"
    
    
def test_arg_i():
    assert shorten("IdiDs") == "dDs"
    

def test_arg_o():
    assert shorten("OdoDs") == "dDs"
    
    
def test_arg_u():
    assert shorten("UduDs") == "dDs"
    
    
def test_arg_all():
    assert shorten("ASasEWewIKikOPopUJuj.,:;'\"0123456789") == "SsWwKkPpJj.,:;'\"0123456789"