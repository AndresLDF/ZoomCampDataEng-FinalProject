if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data.columns = (data.columns.str.replace(' ', '_').str.lower())
    transformed_data = data.drop('id_bdq', axis=1)
    transformed_data = transformed_data.drop('bioma', axis=1)
    transformed_data['year'] = transformed_data['data_pas'].str[:4].astype(int)
    #transformed_data = transformed_data.drop('bioma', axis=1)

    print(transformed_data)
    return transformed_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
