import fire
import re
from collections import Counter


def count_letter(file_name: str):
    with open(file_name, 'rb') as file:
        content = str(file.read(1000))

        pattern = re.compile(r'(\\x[0-9a-f])|(\\[a-z])')
        content = re.sub(pattern, '', content)

        counter = Counter(c.lower() for c in content if c.isalpha())

        counts = counter.most_common()
        total = sum(count[1] for count in counts)

        for count in counts:
            print(f'{count[0]}\t{count[1] / total * 100 :.2f}%')


def count_word(file_name: str):
    with open(file_name, 'rb') as file:
        content = str(file.read(1000))

        pattern = re.compile(r'(\\x[0-9a-f])|(\\[a-z])')
        content = re.sub(pattern, '', content)

        # 获取所有单词
        word_pattern = re.compile(r'[a-z]+\d*')
        words = word_pattern.findall(content.lower())

        counter = Counter(words)

        counts = counter.most_common()
        total = sum(count[1] for count in counts)

        for count in counts:
            print(f'{count[0]}\t{count[1] / total * 100 :.2f}%')


if __name__ == '__main__':
    fire.Fire({
        '-c': count_letter,
        '-f': count_word
    })
