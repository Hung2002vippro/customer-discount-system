from discount import calculate_discount

def test_vip_customer():
    assert calculate_discount(60000000) == 0.1

def test_normal_customer():
    assert calculate_discount(30000000) == 0

def test_tc01():
    # TC01: Tổng trước đó: 60M, Hiện tại: 2M -> Tổng: 62M (>= 50M) -> Expected: 0.1
    # Do hàm chỉ nhận 1 tham số, ta truyền tổng mua hàng trước đó (hoặc tổng bao gồm đơn hiện tại, 
    # nhưng theo logic sai thì chỉ dùng tổng trước đó).
    # Ở đây nếu truyền 60M (trước đó) thì expected là 0.1
    assert calculate_discount(60000000) == 0.1

def test_tc02():
    # TC02: Tổng trước đó: 30M, Hiện tại: 2M -> Tổng: 32M (< 50M) -> Expected: 0
    assert calculate_discount(30000000) == 0

def test_tc03():
    # TC03: Tổng trước đó: 49M, Hiện tại: 2M -> Tổng: 51M (>= 50M) -> Expected: 0.1
    # Ở đây nếu lập trình viên không cộng dồn, chỉ truyền 49M vào hàm, hàm sẽ trả về 0.
    # Trong khi Expected Result phải là 0.1 (được giảm 10%)
    # Test case này sẽ FAIL vì actual (0) != expected (0.1)
    assert calculate_discount(49000000) == 0.1
