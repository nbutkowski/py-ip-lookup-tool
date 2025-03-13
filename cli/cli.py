import click

from utils.csv_utils import read_csv_as_list, read_csv_as_dict, write_dict_to_csv
from utils.ip_utils import find_matching_cidr


@click.group
def cli():
    """CLI tool to reconcile host, ip, and a network"""

@cli.command()
@click.argument("host-list-csv")
@click.argument("network-list-csv")
@click.option("--output-csv", default="out/reconciled.csv")
def reconcile(host_list_csv, network_list_csv, output_csv):
    """Reconcile host, ip, and network"""
    host_list = read_csv_as_dict(host_list_csv)
    network_list = read_csv_as_list(network_list_csv)
    for row in host_list:
        first_match_network_row = None
        ip = row["ip"]
        for network_row in network_list[1:]:
            if find_matching_cidr(ip, network_row[1]):
                first_match_network_row = network_row
                break
        if first_match_network_row is not None:
            row["network"] = first_match_network_row[0]
            row["cidr"] = first_match_network_row[1]

    write_dict_to_csv(output_csv, host_list, ["hostname", "ip", "network_name", "cidr"])


if __name__ == "__main__":
    cli()
