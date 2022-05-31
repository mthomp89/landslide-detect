import pandas as pd

def create_dataframe(data_file):
    """
    Reads a csv file into a Pandas DataFrame. Sets the index to the 'slide.id'
    and sorts the DataFrame by the new index. Creates a new column 'point' by 
    merging two other columns.

    Parameters
    ----------
    data_file : str

    Returns
    -------
    dataframe
        sorted by index
    """

    df = pd.read_csv(data_file, index_col='slide.id').sort_values(by='slide.id')
    df['point'] = df['lon'].map(str) + ', ' + df['lat'].map(str)

    return df