from hw5 import Patient

def test_add_test_and_covid_positive():
    p = Patient("James", ["dizziness", "cough"])
    result = p.add_test("covid", True)
    assert result == "Test added successfully!"
    assert "covid" in p.tests
    assert p.tests["covid"] is True
    assert p.has_covid() == 0.99

def test_add_test_and_covid_negative():
    p = Patient("Gregory", ["fever"])
    p.add_test("covid", False)
    assert p.has_covid() == 0.01

def test_has_covid_no_test_with_symptoms():
    p = Patient("Hailey", ["fever", "cough","stomachache"])
    p.test_name = "hep-B"
    p.test_results = False
    prob = p.has_covid()
    assert prob == 0.25

def test_has_covid_no_test_no_symptoms():
    p = Patient("Liam", [])
    p.test_name = "ch-pox"
    p.test_results = False
    assert p.has_covid() == 0.05