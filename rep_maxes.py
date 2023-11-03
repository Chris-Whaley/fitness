from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import info as session_info
import numpy as np
import pandas as pd


def main():
    """One Rep Max Calculator

    Simple application for calculating different 1 rep maxes for reps up to 10.
    
    """

    put_markdown(("""# Rep Maxes
    
    [One Rep Maximum](https://en.wikipedia.org/wiki/One-repetition_maximum) (1RM) in weight training is the maximum amount of weight that a person can possibly lift for one repetition. It may also be considered as the maximum amount of force that can be generated in one maximal contraction. 
    
    Formulas used:
    
    | Name     | 1RM Formula                                                        |
    | -------- | ------------------------------------------------------------------ |
    | Epley    | weight(1 + reps/30), assuming r > 1 (we'll just assign the weight) |
    | Brzycki  | weight * 36/(37 - reps)                                            |
    
    """))

    weight = input("Weight", type=NUMBER)
    reps = np.array(list(range(1, 11)), dtype='i')

    # for epley formula, only calculate for reps 2 - 10. for 1, use the input weight    
    epley = np.where(reps==1, weight, (weight*(1 + reps/30)) )
    epley = np.round(epley)
    epley = [int(x) for x in epley]
    
    brzycki = weight * (36/(37 - reps))
    brzycki = np.round(brzycki)
    brzycki = [int(x) for x in brzycki]
    
    average_1rm = np.mean([epley, brzycki], axis=0)
    average_1rm = np.round(average_1rm)
    average_1rm = [int(x) for x in average_1rm]
    
    df = pd.DataFrame()

    df['reps'] = reps
    df['epley'] = epley
    df['brzycki'] = brzycki
    df['average_1rm'] = average_1rm
    df['weight'] = weight
        
    # rearrange columns
    df = df[['weight', 'reps', 'epley', 'brzycki', 'average_1rm']]        
    
    put_html(df.to_html(border=0, index=False))


if __name__ == '__main__':
    start_server(main, debug=True, port=8080)