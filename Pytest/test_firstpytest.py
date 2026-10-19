def test_addition():
    result = 10+2
    assert result == 12

def test_sub():
    result = 11-3
    assert result == 8

def test_namecheck():
    actual_name = "Vishnukumar"
    expected = "Vishnuvk"
    assert expected == actual_name, f"Expected name is {expected} but got {actual_name}"

def test_length():
    product = ["Bag", "torch", "shoe"]
    assert len(product)==3
    print("Succesfull brother")
