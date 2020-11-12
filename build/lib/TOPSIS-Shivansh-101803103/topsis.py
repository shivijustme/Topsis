import pandas as pd
import os
import sys

def Normalization(dataset_2, no_of_col, weights):

    for i in range(1, no_of_col):
        temp = 0
        for j in range(len(dataset_2)):
            temp = temp + dataset_2.iloc[j, i]**2
        temp = temp**0.5
        for j in range(len(dataset_2)):
            dataset_2.iat[j, i] = (
                dataset_2.iloc[j, i] / temp)*weights[i-1]
    return dataset_2

def cal_val(dataset_2, no_of_col, impact):

    p_sol = (dataset_2.max().values)[1:]
    n_sol = (dataset_2.min().values)[1:]
    for i in range(1, no_of_col):
        if impact[i-1] == '-':
            p_sol[i-1], n_sol[i-1] = n_sol[i-1], p_sol[i-1]
    return p_sol, n_sol

def topsis(dataset_2, dataset_1, no_of_col, weights, impact):

    dataset_2 = Normalization(dataset_2, no_of_col, weights)

    p_sol, n_sol = cal_val(dataset_2, no_of_col, impact)

    score = []
    for i in range(len(dataset_2)):
        test_p, test_n = 0, 0
        for j in range(1, no_of_col):
            test_p = test_p + (p_sol[j-1] - dataset_2.iloc[i, j])**2
            test_n = test_n + (n_sol[j-1] - dataset_2.iloc[i, j])**2
        test_p, test_n = test_p**0.5, test_n**0.5
        score.append(test_n/(test_p + test_n))
    dataset_1["Topsis Score"] = score

    dataset_1["Rank"] = (dataset_1["Topsis Score"].rank(method='max', ascending=False))
    dataset_1 = dataset_1.astype({"Rank": int})

    dataset_1.to_csv(sys.argv[4], index=False)

def main():
    if len(sys.argv) != 5:
        raise Exception("Wrong number of parameters !\n" + "Use the format : python topsis.py input_file.csv '1,1,1,1' '+,+,-,+' result.csv")

    elif not os.path.isfile(sys.argv[1]):
        raise Exception("File does not exist !")

    elif ".csv" != (os.path.splitext(sys.argv[1]))[1]:
        raise Exception("File is not csv !")

    else:
        dataset_1, dataset_2 = pd.read_csv(sys.argv[1]), pd.read_csv(sys.argv[1])
        no_of_col = len(dataset_2.columns.values)

        if no_of_col < 3:
            raise Exception("Invalid number of columns( less than 3 )")

        for i in range(1, no_of_col):
            pd.to_numeric(dataset_1.iloc[:, i], errors='coerce')
            dataset_1.iloc[:, i].fillna(
                (dataset_1.iloc[:, i].mean()), inplace=True)

        try:
            weights = [int(i) for i in sys.argv[2].split(',')]
        except:
            raise Exception("Error in weights array !")

        impact = sys.argv[3].split(',')
        for i in impact:
            if not (i == '+' or i == '-'):
                raise Exception("Error in Impact array !")

        if no_of_col != len(weights)+1 or no_of_col != len(impact)+1:
            raise Exception("Number of weights, impacts and columns are not same !")

        if (".csv" != (os.path.splitext(sys.argv[4]))[1]):
            raise Exception("Output file must be .csv !")

        if os.path.isfile(sys.argv[4]):
            os.remove(sys.argv[4])

        topsis(dataset_2, dataset_1, no_of_col, weights, impact)

if __name__ == "__main__":
    main()
