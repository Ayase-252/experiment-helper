""" Experiment Module

A class of experiment is defined here.
"""


class Experiment:
    """Defines an experiment.

    Raises:
        RuntimeError -- If the lengths of parameters are consistant.

    """

    def __init__(self, parameters, experiment_code, result_processor):
        """Initialize a experiment

        Arguments:
            parameters {dict} -- A dict contains parameters.
            experiment_code {callable} -- A callable object. It should 
                                          accept arguments with same name of 
                                          parameters, and return a dict
                                          contains result.
            result_processor {callable} -- A callable object. It should 
                                           accept arguments with same name
                                           of result. The return value will
                                           be collect by this object and
                                           can be accessed by look_results().

        Raises:
            RuntimeError -- If the lengths of parameters are not consistant,
                            RuntimeError would be raised.
        """

        len_parameters = [len(parameters[key]) for key in parameters]
        if len(set(len_parameters)) != 1:
            raise RuntimeError('The lengths of parameters are not consistant. \
            The lengths of parameters you passed are {}.', len_parameters)
        self._parameters = parameters
        self._run_experiment = experiment_code
        self._process_result = result_processor
        self._results = []

    def execute(self):
        """Execute experiment
        """

        parameter_dicts = []
        for key in self._parameters:
            key_val_pairs = [{key: val} for val in self._parameters[key]]
            if not parameter_dicts:
                parameter_dicts = key_val_pairs
            else:
                for i, key_val_pair in enumerate(key_val_pairs):
                    parameter_dicts[i].update(key_val_pair)

        for parameter_dict in parameter_dicts:
            res = self._run_experiment(**parameter_dict)
            processed_res = self._process_result(parameter_dict, res)
            self._results.append(processed_res)

    def look_results(self):
        """Look result

        Returns:
            [list] -- [results of experiment in order of defined parameters.]
        """

        return self._results
