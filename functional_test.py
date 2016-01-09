#!/usr/bin/env python3

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She type "Buy peacock feathers" into a text box

        # When she hits enter the page updates, and now the page lists
        # "1. Buy peacock feathers" as ann item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "use peacock feathers to make a fly"

        # the page updates again, and shows both items on her list

        # Edith wonders wheter the site will remember her list. Then she sees that the sites has generated a unique URL for her.
        # -- thereis some explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # She satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
