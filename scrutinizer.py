build:
    nodes:
        analysis:
            tests:
                override:
                    - py-scrutinizer-run
                    - 
                        command: pip install flake8 && pip install flake8-checkstyle && flake8 --format=checkstyle your/project/path --output-file=analysis-output.xml
                        analysis:
                            file: analysis-output.xml
                            format: 'general-checkstyle'
