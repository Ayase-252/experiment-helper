from unittest import TestCase

from experiment import Experiment

class TestExperiment(TestCase):
    def test_multiple_parameter_experiment(self):
        # Parameter is a dict with the key is the name of input parameter
        # and the element is a list of parameter.
        # The number of element list is required to be same.
        parameter_set = {'p1': [1, 2, 3, 4, 5], 'p2':[4, 5, 6, 7, 8]}

        # Parameter defined in parameter_set should be catch by the named
        # arguments in do_experiment
        def do_experiment(p1, p2):
            # Return value is a dict with the key is the category name of
            # result
            return {'sum_': p1 + p2 }

        # Result returned by do_experiment should be catch by the named
        # arguments in manipulate_result.
        def manipulate_result(params, res):
            return res['sum_'] + 1

        # The value returned by manipulated_result should be saved and be
        # able to be accessed by look_results() method.

        expr = Experiment(parameter_set, do_experiment, manipulate_result)
        expr.execute()

        result = expr.look_results()
        self.assertEqual(result, [6, 8, 10, 12, 14])

    def test_parameters_of_different_length(self):
        """If the length of different parameters is not consistant,
        experiment should throw an exception when initializing.
        """
        parameter_set = {'p1': [1, 2, 3, 4, 5], 'p2':[4, 5, 6, 7, 8, 9]}

        with self.assertRaises(RuntimeError):
            expr = Experiment(parameter_set, None, None)

