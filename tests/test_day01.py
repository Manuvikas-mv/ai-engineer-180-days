from day01.main import calculate_success_rate


def test_success_rate():
    records = [
        {"status": "success"},
        {"status": "failed"},
        {"status": "success"}
    ]

    assert calculate_success_rate(records) == 66.67


def test_empty_records():
    assert calculate_success_rate([]) == 0.0


def test_all_successful():
    records = [{"status": "success"}]
    assert calculate_success_rate(records) == 100.0