import csv
from dataclasses import dataclass
import os
import sys

import click


"""Define whether or not """
is_verbose = False


@click.command()
@click.argument('path', type=click.File('r'), nargs=1)
@click.option('-v', '--verbose', is_flag=True, default=False,
    help='Enables verbose mode')
@click.option('-o', '--out', type=click.Path(dir_okay=False), default='out.sql',
    help='Filename in which store the generated SQL queries')
def generate_sql(path, out, verbose):
    """Generate the SQL requests from the provided CSV file

    PATH is the path to the CSV file to process
    """
    # Set flags
    global is_verbose
    is_verbose = verbose

    # Core process
    process_file(path.name, out)


def process_file(filename: str, out_path: str) -> None:
    """Extract data from the CSV file and generate the associated SQL queries

    :param filename: CSV source
    :param out_path: Destination in which SQL queries will be written
    """
    # Process CSV file
    if is_verbose:
        print(f'[INFO] Start processing {filename}')

    with open(filename) as csv_file:
        is_header_parsed = False
        sql_lines = []

        for row in csv.reader(csv_file, delimiter=','):

            # Process header
            if not is_header_parsed:
                if is_verbose:
                    print(f'[INFO] Headers are: {", ".join(row)}')

                sql_etablissement = f'Insert into ETABLISSEMENT ({row[0]}, {row[1]})'
                sql_adresse = f'Insert into ADRESSE ({row[2]}, {row[3]})'
                is_header_parsed = True
                continue

            # Process rows
            sql_lines.append(f'{sql_etablissement} VALUES (SEQ.NEXTVAL, {row[0]}, {row[1]});')
            sql_lines.append(f'{sql_adresse} VALUES (SEQ.NEXTVAL, {row[2]}, {row[3]});')

        sql_lines.append('COMMIT;')

    if is_verbose:
        print(f'[INFO] End of processing ({len(sql_lines)} queries generated)')
                
    # Write output to destination
    if is_verbose:
        print(f'[INFO] Writing queries to {out_path}')

    with open(out_path,'w+') as output_file:
        output_file.writelines((os.linesep).join(sql_lines))

    if is_verbose:
        print(f'[INFO] All {len(sql_lines)} lines have been written')

