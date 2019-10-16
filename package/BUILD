python_library(
    name="lib",
    dependencies=[],
    sources=globs("package/**/*"),
    tags={},
)

python_binary(
    name="main",
    dependencies=[":lib"],
    source="src/package/main.py",
)