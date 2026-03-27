import builtins
import pytest

from task2_chatbot import chatbot


def test_chatbot_exit(monkeypatch, capsys):
    inputs = iter(['hello', 'bye'])
    monkeypatch.setattr(builtins, 'input', lambda prompt='': next(inputs))

    chatbot()

    captured = capsys.readouterr()
    assert 'Basic Rule-Based Chatbot' in captured.out
    assert 'Bot: Hi!' in captured.out or 'Bot: Hello!' in captured.out
    assert 'Goodbye' in captured.out
