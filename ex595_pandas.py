import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        world (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    world_output = world.drop(['continent', 'gdp'], axis=1)
    world_output = world_output[(world_output['area'] >= 3000000) | (
        world_output['population'] >= 25000000)]

    return world_output


data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000], ['Algeria', 'Africa',
                                                                                                                     2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000], ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
world_list = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype(
    {'name': 'object', 'continent': 'object', 'area': 'Int64', 'population': 'Int64', 'gdp': 'Int64'})

big_countries(world_list)
