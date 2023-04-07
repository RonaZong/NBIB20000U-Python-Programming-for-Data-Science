import sys
import pytest


def setup_module(module):
    global exam
    import exam


def test_exam_test_import():
    '''Test that exam_test can be imported works'''
    import exam_test


def np_pd_tracer(frame, event, arg):
    if event == 'call':
        assert "numpy" not in frame.f_code.co_filename, "Numpy not allowed in this part of the exam"
        assert "pandas" not in frame.f_code.co_filename, "Pandas not allowed in this part of the exam"


class TestQ1:

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class."""
        sys.settrace(np_pd_tracer)

    @classmethod
    def teardown_class(cls):
        """ teardown any state specific to the execution of the given class."""
        sys.settrace(None)

    def test_Q1_1_basic(self):
        '''Test for existence and callability of clean_si_table_data'''

        # Check that the function exists
        assert hasattr(exam, "clean_si_table_data"), "Function not found"

        # Check that the function can be called
        exam.clean_si_table_data("fig_s14_data.txt", "fig_s14_data_cleaned.txt")

    def test_Q1_2_basic(self):
        '''Test for existence and callability of parse_si_table_data'''

        # Check that the function exists
        assert hasattr(exam, "parse_si_table_data"), "Function not found"

        # Check that the function can be called
        exam.parse_si_table_data("fig_s14_data_cleaned.txt")


class TestQ2:

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class."""
        sys.settrace(np_pd_tracer)

    @classmethod
    def teardown_class(cls):
        """ teardown any state specific to the execution of the given class."""
        sys.settrace(None)

    def test_Q2_1_basic(self):
        '''Test for existence and callability of parse_si_table_data_grouped'''

        # Check that the function exists
        assert hasattr(exam, "parse_si_table_data_grouped"), "Function not found"

        # Check that the function can be called
        exam.parse_si_table_data_grouped('fig_s14_data_cleaned.txt')

    def test_Q2_2_basic(self):
        '''Test for existence and callability of create_bar_plot'''

        # No checks for numpy&pandas in remainder of Q2
        sys.settrace(None)

        # Check that the function exists
        assert hasattr(exam, "create_bar_plot"), "Function not found"

        # Check that the function can be called
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        exam.create_bar_plot(ax, {'A': '10.', 'B': '20', 'C': '15'})

    def test_Q2_3_basic(self):
        '''Test for existence and callability of generate_stack'''

        # No checks for numpy&pandas in remainder of Q2
        sys.settrace(None)

        # Check that the function exists
        assert hasattr(exam, "generate_stack"), "Function not found"

        # Check that the function can be called
        exam.generate_stack({'A': '10.', 'B': '20', 'C': '15'})


class TestQ3:

    def test_Q3_1_basic(self):
        '''Test for existence and callability of read_excel_data'''

        # Check that the function exists
        assert hasattr(exam, "read_excel_data"), "Function not found"

        # Check that the function can be called
        exam.read_excel_data('LCA+Meta-Analysis+of+Food+Products+-+Full+Model+v0+(1).xlsx', 'Database', 2)

    def test_Q3_2_basic(self):
        '''Test for existence and callability of extract_emission_means'''

        # Check that the function exists
        assert hasattr(exam, "extract_emission_means"), "Function not found"

        # Check that the function can be called
        import pandas as pd
        exam.extract_emission_means(pd.DataFrame({'ID_LOSS':{1:'beef', 2:'beef'}, 'GHG Emis \n(kg CO2 eq)': {1:10, 2:20}}))

    def test_Q3_3_basic(self):
        '''Test for existence and callability of extract_emission_means_stddevs'''

        # Check that the function exists
        assert hasattr(exam, "extract_emission_means_stddevs"), "Function not found"

        # Check that the function can be called
        import pandas as pd
        exam.extract_emission_means_stddevs(pd.DataFrame({'ID_LOSS':{1:'beef', 2:'beef'}, 'GHG Emis \n(kg CO2 eq)': {1:10, 2:20}}))


class TestQ4:

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class."""
        sys.settrace(np_pd_tracer)

    @classmethod
    def teardown_class(cls):
        """ teardown any state specific to the execution of the given class."""
        sys.settrace(None)

    def test_Q4_1_basic(self):
        '''Test for existence and callability of calculate_transport_share'''

        # Check that the function exists
        assert hasattr(exam, "calculate_transport_share"), "Function not found"

        # Check that the function can be called
        exam.calculate_transport_share({1:10, 2:20}, {1:10, 2:20})

    def test_Q4_2_basic(self):
        '''Test for existence and callability of calculate_product_group_means'''

        # Check that the function exists
        assert hasattr(exam, "calculate_product_group_means"), "Function not found"

        # Check that the function can be called
        exam.calculate_product_group_means({1:'beef', 2:'beef'}, {1:10, 2:20})

    def test_Q4_3_basic(self):
        '''Test for existence and callability of calculate_product_group_means2'''

        # Check that the function exists
        assert hasattr(exam, "calculate_product_group_means2"), "Function not found"

        # Check that the function can be called
        exam.calculate_product_group_means2({1:'beef', 2:'beef'}, {1:10, 2:20})

    def test_Q4_4_basic(self):
        '''Test for existence and callability of calculate_product_group_means3'''

        # Check that the function exists
        assert hasattr(exam, "calculate_product_group_means3"), "Function not found"

        # Check that the function can be called
        exam.calculate_product_group_means3({'product':{1:'beef', 2:'beef'},
                                             'emission':{1:10, 2:20, 3:30},
                                             'transport':{1:10, 2:20, 3:30},
                                             'transport share':{1:10, 2:20, 3:30}})


