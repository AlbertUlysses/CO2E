def fuel_combustion(mpg: float, gram: bool = True) -> float:
    """Calulates CO2e for US gallon of fuel  """

    mpg = mpg
    rate = 8.8
    round_ = 3
    if gram is True:
        rate = 8.8 * 1000
        round_ = 1
    co2e_mile = rate/mpg
    return round(co2e_mile, round_)

