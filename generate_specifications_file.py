#!/usr/bin/env python

'''
Author :
    * Muhammed Ahad <ahad3112@yahoo.com, maaahad@gmail.com>

Usage:
    $ python3 generate_specifications_file.py -h/--help
Desctiption:
    This script generates container specification file for Docker or Singularity based on
    user's choice. The aim behind this is to create container image containing GROMACS with
    all of it's dependencies and all possible binaries based of CPU's SIMD instruction set.
'''

import hpccm

import argparse
from utilities.cli import CLI
import container.recipes as recipes

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='HPCCM recipes for generating GROMACS container\'s specification file.')
    cli = CLI(parser=parser)

    hpccm.config.set_container_format(cli.args.format)

    recipes.prepare_and_cook(args=cli.args)
