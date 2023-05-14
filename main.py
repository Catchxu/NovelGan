from benchmark.run_benchmark import cell_detect_bench
from NovelGan import Detect_cell

data_cfg = {
    'PBMC(SLE)': {
        'data_path': './scdata/',
        'info_path': './scdata/info.tsv'
    }
}

method_cfg = {'NovelGan': 1}
metrics = ['ARI', 'NMI']

a, b = cell_detect_bench(
    data_cfg, method_cfg, metrics, log_path='loguru.log', random_state=100
)
# rm_cache("./cache")
