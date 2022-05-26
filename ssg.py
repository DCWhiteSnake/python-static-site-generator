import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}

    test_site = Site(**config).build()


typer.run(main)
