from typing import TypeVar
from generator import Generator
from processor import Processor

BlockType = TypeVar("BlockType", Generator, Processor)