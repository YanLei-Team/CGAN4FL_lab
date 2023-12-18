# CGAN4FL

Project structure

- `data`
    - `d4j`
        - `buggy-lines`
            - `*.buggy.lines`
            - (e.g. `Chart-7.buggy.lines`)
        - `data`
            - `<program>/<version>/gzoltars/<program>/<version>/*.csv`
            - (e.g. `Chart/7/gzoltars/Chart/7/matrix.csv`)
        - `rank`
            - `<program>/<method>/r_all.csv`
            - (e.g. `Chart/ochiai/r_all.csv`)
    - `MetaFL`
        - `<program>/backup`
            - `results<results_id>`
            - `faultList<results_id>.txt`
            - (e.g. `clac/backup/faultList20220508154534.txt`)
- src
