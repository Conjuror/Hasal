from lib.perfBaseTest import PerfBaseTest


class TestSikuli(PerfBaseTest):

    def setUp(self):
        self.set_variable(test_target=self.env.TEST_TARGET_ID_SLIDE_10_PAGE_MIX_CONTENT)
        super(TestSikuli, self).setUp()

    def test_chrome_gslide_delete_slide_10(self):
        self.sikuli_status = self.sikuli.run_test(self.env.test_name, self.env.output_name, test_target=self.test_url, script_dp=self.env.test_script_py_dp)
