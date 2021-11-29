import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename=f"{__name__}.log",
    filemode="a",
    format="%(name)s-%(levelname)s(%(levelno)s)-%(asctime)s-%(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
)


def main():
    # without line 3, the two next sentences don't show nothing
    logging.debug("This is a debug message.")
    logging.info("This is a info message.")
    logging.warning("This is a warning message.")
    logging.error("This is a error message.")
    logging.critical("This is a critical message.")

    name = "Guido"
    logging.info(f"{name} created an amazing programming language.")


if __name__ == "__main__":
    main()
