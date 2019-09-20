from hikvision_recover.recover import get_code
def test_output():
    serial ='DS-ABC1234567-HIJKLMNOPQRS10987654321'
    year = '2017'
    month = '01'
    day = '25'
    recovery_code = get_code(serial, year, month, day)
    assert recovery_code == 'SyrReQQe99'
