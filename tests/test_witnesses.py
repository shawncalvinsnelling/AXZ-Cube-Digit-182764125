import ast
import operator
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
}


def safe_eval_expr(expr: str) -> int:
    node = ast.parse(expr, mode="eval").body

    def walk(n):
        if isinstance(n, ast.Constant) and isinstance(n.value, int):
            return n.value
        if isinstance(n, ast.BinOp) and type(n.op) in OPS:
            return OPS[type(n.op)](walk(n.left), walk(n.right))
        raise ValueError(f"disallowed expression node: {ast.dump(n)}")

    return walk(node)


def test_witness_table_values():
    path = ROOT / "data" / "witnesses_1_to_4771.tsv"
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "n\texpression"
    assert len(lines) == 4771 + 1
    for expected_n, line in enumerate(lines[1:], start=1):
        n_s, expr = line.split("\t", 1)
        assert int(n_s) == expected_n
        assert safe_eval_expr(expr) == expected_n
