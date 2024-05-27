
# scriptscan/common/src/script.py

from datetime import datetime
from typing import List, Optional

class Script:
    def __init__(self, title: str, author: str, raw_content: str):
        self._title = title
        self._author = author
        self._raw_content = raw_content
        self._scenes = []
        self._paragraphs = []
        self._dialogues = []
        self._transitions = []
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
    
    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def raw_content(self) -> str:
        return self._raw_content

    @property
    def scenes(self) -> List[str]:
        return self._scenes

    @property
    def paragraphs(self) -> List[str]:
        return self._paragraphs

    @property
    def dialogues(self) -> List[str]:
        return self._dialogues

    @property
    def transitions(self) -> List[str]:
        return self._transitions

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_scenes(self, scenes: List[str]):
        self._scenes = scenes
        self._updated_at = datetime.now()

    def update_paragraphs(self, paragraphs: List[str]):
        self._paragraphs = paragraphs
        self._updated_at = datetime.now()

    def update_dialogues(self, dialogues: List[str]):
        self._dialogues = dialogues
        self._updated_at = datetime.now()

    def update_transitions(self, transitions: List[str]):
        self._transitions = transitions
        self._updated_at = datetime.now()

    def __repr__(self) -> str:
        return f"<Script(title={self._title}, author={self._author}, created_at={self._created_at})>"
    
    def __eq__(self, other):
        if not isinstance(other, Script):
            return False
        return (self._title == other._title and 
                self._author == other._author)
    
