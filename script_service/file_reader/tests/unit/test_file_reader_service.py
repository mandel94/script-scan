# https://docs.pytest.org/en/8.2.x/how-to/monkeypatch.html 

from flask import request
from file_reader.file_reader_service import read_file_wrapper



def test_read_file(monkeypatch):

    def mockreturn():
        return {"file_path": "../data/silence_of_the_lambs.txt"}
    

    monkeypatch.setattr(request, "get_json", mockreturn)

