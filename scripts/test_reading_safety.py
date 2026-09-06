import unittest
from reading_safety import escape_currency, unsafe_currency_lines

class ReadingSafetyTests(unittest.TestCase):
    def test_money_in_prose_and_tables(self):
        text='**$100M/year**, then **$1B/year**\n| Pay | $90,000 / $X |\n'
        self.assertEqual(unsafe_currency_lines(text), [1,2])
        self.assertEqual(escape_currency(text), '**&#36;100M/year**, then **&#36;1B/year**\n| Pay | &#36;90,000 / &#36;X |\n')
    def test_code_and_urls_untouched(self):
        text='```sh\necho $100\n```\n~~~text\n$X\n~~~\n`$200` and ``$X``\n[x](https://example.com/$100)\n<a href="https://example.com/$200">price</a>\nUse $b2b-playbook\n'
        self.assertEqual(escape_currency(text), text)
    def test_already_safe_and_idempotent(self):
        text='\\$100 and &#36;200 and $$100$$\n'
        self.assertEqual(escape_currency(text), text)
        self.assertEqual(escape_currency(escape_currency('$200')),'&#36;200')

if __name__=='__main__': unittest.main()
