import args
import config
import utils

from pathlib import Path
from typing import List

def ibm_converter():

    a = args.parse_args()
    input_data: List[List[str]] = utils.ibm_read_file(config.IN_DIR / a.ibm_dataset)
    filename = Path(a.dataset).stem

    new_input_data = [[x[1], x[2]] for x in input_data]

    utils.ibm_write_file(
        data = new_input_data,
        filename = config.OUT_DIR / a.ibm_dataset
    )


ibm_converter()