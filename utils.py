import string


class GenerateDomain:
    def __init__(self, suffix: str = "com"):
        self.suffix = suffix
        self.letters = string.ascii_lowercase
        self.digits = "0123456789"

    def generate_xa(self, x: int = 3):
        data = []
        for item in self.letters + self.digits:
            data.append(item * x + '.' + self.suffix)
        return data

    def generate_domains(self, items: str = "llll"):
        """
        根据指定的规则生成所有字符串组合
        l - 字母 (a-z)
        d - 数字 (0-9)
        """

        # 初始化一个包含所有组合的列表
        domains = ['']

        for item in items:
            if item == 'l':  # 如果是字母
                domains = [prefix + letter for prefix in domains for letter in self.letters]
            elif item == 'd':  # 如果是数字
                domains = [prefix + digit for prefix in domains for digit in self.digits]
        domains = [domain + '.' + self.suffix for domain in domains]

        return domains
