from discount import calculate_discount

def test_vip_customer():
    assert calculate_discount(60000000) == 0.1

def test_normal_customer():
    assert calculate_discount(30000000) == 0

def test_tc01():
    # TC01: Tổng trước đó: 60M, Hiện tại: 2M -> Tổng: 62M (>= 50M) -> Expected: 0.1
    assert calculate_discount(60000000, 2000000) == 0.1

def test_tc02():
    # TC02: Tổng trước đó: 30M, Hiện tại: 2M -> Tổng: 32M (< 50M) -> Expected: 0
    assert calculate_discount(30000000, 2000000) == 0

def test_tc03():
    # TC03: Tổng trước đó: 49M, Hiện tại: 2M -> Tổng: 51M (>= 50M) -> Expected: 0.1
    assert calculate_discount(49000000, 2000000) == 0.1
