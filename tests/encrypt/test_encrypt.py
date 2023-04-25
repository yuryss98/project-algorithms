from challenges.challenge_encrypt_message import encrypt_message
import pytest


@pytest.fixture
def mock():
    return [
        (4, "adiláv mega_snem"),
        (5, "asnem_adiláv meg"),
        (20, "adiláv megasnem")
    ]


def test_encrypt_message(mock):
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("mensagem", "erro")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(2, 2)

    for i, j in mock:
        result = encrypt_message('mensagem válida', i)
        assert result == j
