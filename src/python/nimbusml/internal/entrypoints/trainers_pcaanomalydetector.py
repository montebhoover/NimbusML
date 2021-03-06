# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Trainers.PcaAnomalyDetector
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def trainers_pcaanomalydetector(
        training_data,
        predictor_model=None,
        feature_column='Features',
        weight_column=None,
        normalize_features='Auto',
        caching='Auto',
        rank=20,
        oversampling=20,
        center=True,
        seed=None,
        **params):
    """
    **Description**
        Train an PCA Anomaly model.

    :param training_data: The data to be used for training (inputs).
    :param feature_column: Column to use for features (inputs).
    :param weight_column: Column to use for example weight (inputs).
    :param normalize_features: Normalize option for the feature
        column (inputs).
    :param caching: Whether learner should cache input training data
        (inputs).
    :param rank: The number of components in the PCA (inputs).
    :param oversampling: Oversampling parameter for randomized PCA
        training (inputs).
    :param center: If enabled, data is centered to be zero mean
        (inputs).
    :param seed: The seed for random number generation (inputs).
    :param predictor_model: The trained model (outputs).
    """

    entrypoint_name = 'Trainers.PcaAnomalyDetector'
    inputs = {}
    outputs = {}

    if training_data is not None:
        inputs['TrainingData'] = try_set(
            obj=training_data,
            none_acceptable=False,
            is_of_type=str)
    if feature_column is not None:
        inputs['FeatureColumn'] = try_set(
            obj=feature_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if weight_column is not None:
        inputs['WeightColumn'] = try_set(
            obj=weight_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if normalize_features is not None:
        inputs['NormalizeFeatures'] = try_set(
            obj=normalize_features,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'No',
                'Warn',
                'Auto',
                'Yes'])
    if caching is not None:
        inputs['Caching'] = try_set(
            obj=caching,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'Auto',
                'Memory',
                'Disk',
                'None'])
    if rank is not None:
        inputs['Rank'] = try_set(
            obj=rank,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if oversampling is not None:
        inputs['Oversampling'] = try_set(
            obj=oversampling,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if center is not None:
        inputs['Center'] = try_set(
            obj=center,
            none_acceptable=True,
            is_of_type=bool)
    if seed is not None:
        inputs['Seed'] = try_set(
            obj=seed,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if predictor_model is not None:
        outputs['PredictorModel'] = try_set(
            obj=predictor_model, none_acceptable=False, is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    entrypoint = EntryPoint(
        name=entrypoint_name, inputs=inputs, outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables)
    return entrypoint
