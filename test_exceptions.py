
import pytest
from Exceptions import ExceptionsDemo, MyException


@pytest.fixture
def demo():
    return ExceptionsDemo()


@pytest.mark.unit
def test_divide_correct(demo, capsys):
    demo.divide(10, 2)
    output = capsys.readouterr().out
    assert "Division result: 5.0" in output


@pytest.mark.unit
def test_divide_zero(demo, capsys):
    demo.divide(10, 0)
    output = capsys.readouterr().out
    assert "Cannot divide by zero" in output


@pytest.mark.unit
def test_divide_type_error(demo, capsys):
    demo.divide("10", 2)
    output = capsys.readouterr().out
    assert "Invalid data type" in output


@pytest.mark.unit
def test_access_list_correct(demo, capsys):
    demo.access_list([1, 2, 3], 1)
    output = capsys.readouterr().out
    assert "Element: 2" in output


@pytest.mark.unit
def test_access_list_index_error(demo, capsys):
    demo.access_list([1, 2, 3], 5)
    output = capsys.readouterr().out
    assert "Index out of range" in output


@pytest.mark.unit
def test_access_list_type_error(demo, capsys):
    demo.access_list(1, 0)
    output = capsys.readouterr().out
    assert "Invalid list or index type" in output


@pytest.mark.unit
def test_access_dict_correct(demo, capsys):
    demo.access_dict({"a": 1}, "a")
    output = capsys.readouterr().out
    assert "Value: 1" in output


@pytest.mark.unit
def test_access_dict_key_error(demo, capsys):
    demo.access_dict({"a": 1}, "b")
    output = capsys.readouterr().out
    assert "Key not found" in output


@pytest.mark.unit
def test_access_dict_type_error(demo, capsys):
    demo.access_dict(123, "a")
    output = capsys.readouterr().out
    assert "Invalid dictionary or key type" in output


@pytest.mark.unit
def test_read_file_correct(demo, capsys):
    demo.read_file("text.txt")
    output = capsys.readouterr().out
    assert "Hola Mundo" in output


@pytest.mark.unit
def test_read_file_not_found(demo, capsys):
    demo.read_file("nonexistent_file.txt")
    output = capsys.readouterr().out
    assert "File not found" in output


@pytest.mark.unit
def test_read_file_os_error(demo, capsys, monkeypatch):
    def fake_open(*args, **kwargs):
        raise OSError("Simulated I/O error")

    monkeypatch.setattr("builtins.open", fake_open)
    demo.read_file("text.txt")
    output = capsys.readouterr().out
    assert "File reading or writing error" in output


@pytest.mark.unit
def test_attribute_error(demo, capsys):
    demo.access_attribute(object())
    output = capsys.readouterr().out
    assert "Attribute does not exist" in output


@pytest.mark.unit
def test_positive_correct(demo, capsys):
    demo.check_positive(5)
    output = capsys.readouterr().out
    assert "Valid number: 5" in output


@pytest.mark.unit
def test_custom_exception(demo, capsys):
    demo.check_positive(-5)
    output = capsys.readouterr().out
    assert "The number must be positive" in output


@pytest.mark.unit
def test_positive_type_error(demo, capsys):
    demo.check_positive("hola")
    output = capsys.readouterr().out
    assert "Invalid number type" in output
