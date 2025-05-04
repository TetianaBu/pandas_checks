import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def run_notebook(notebook_path, output_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': './notebooks'}})

    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

    print(f"Notebook executed and saved to: {output_path}")

if __name__ == "__main__":
    run_notebook("notebooks/data_quality_checks.ipynb", "notebooks/data_quality_checks_output.ipynb")
