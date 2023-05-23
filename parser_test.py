import parser.EmailParser

parser = parser.EmailParser.EmailParser("sample.txt")
print("[From]:", parser.parse("from"))
print("[Subject]:", parser.parse("subject"))
print("[Content]:", parser.parse("content"))