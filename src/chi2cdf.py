def chi2cdf(chi2, df):
    """Calculates Chi square cumulative distribution function for
       df degrees of freedom using the built-in incomplete gamma
       function gammainc().
    """

    return ee.Image(chi2.divide(2)).gammainc(ee.Number(df).divide(2))