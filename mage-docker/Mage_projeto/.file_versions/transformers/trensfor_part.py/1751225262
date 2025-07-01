if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Realiza agregação em pandas.DataFrame por tipo, país e região.
    """
    """
    Renomeia 'country_copy' para 'country' e 'region_copy': 'region', faz agregação.
    """
    data = data.rename(columns={
    'country_copy': 'country',
    'region_copy': 'region',
    })
    # Agrupa e conta o número de breweries
    brewery_agg_df = (
        data.groupby(['brewery_type','country','region'])
            .agg(brewery_count=('id', 'count'))
            .reset_index()
    )
    
    return brewery_agg_df

@test
def test_output(output, *args) -> None:
    assert output is not None, 'O resultado da transformação está vazio.'
    print(f" Transformação concluída: {len(output)} linhas agregadas.")