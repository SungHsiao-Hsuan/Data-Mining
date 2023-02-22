from pathlib import Path
from typing import List

import utils
import config
import args
import time

import my_cool_algorithms


def main():

    # Parse command line arguments
    a = args.parse_args()

    # Load dataset, the below io handles ibm dataset
    input_data: List[List[str]] = utils.read_file(config.IN_DIR / a.dataset)
    filename = Path(a.dataset).stem

    # Excute apriori algorithm
    start = time.time()
    apriori_recommend_data = my_cool_algorithms.apriori(input_data,a)
    print(f"Excuted time of apriori algorithm: %.6f seconds" %(time.time() - start))

    export_data(apriori_recommend_data,config.OUT_DIR,f"{filename}-apriori.csv")

    # Excute FP-growth algorithm
    start = time.time()
    fp_groth_recommand_data = my_cool_algorithms.FP_growth(input_data,a)
    print(f"Excuted time of FP-growth algorithm: %.6f seconds" %(time.time() - start))

    export_data(fp_groth_recommand_data,config.OUT_DIR,f"{filename}-fp_growth.csv")


def export_data(data, file_path, file_name):

    utils.write_file(
        data = data,
        filename= file_path / file_name
    )


if __name__ == "__main__":
    main()