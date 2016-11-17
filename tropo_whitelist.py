from subprocess import check_output


def print_whitelist():
    '''Retrieves tropo's whitelist and prints to STDOUT.
    '''
    response = get_tropo_whitelist_response()
    if response:
        lines = response.decode().split("\n")
        for line in lines:
            if "\"" in line:
                csv_line = format_cidr_to_csv(line)
                print(csv_line)


def format_cidr_to_csv(cidr):
    cidr_block = cidr.split("\"")[1]
    return "tropo," + cidr_block


def get_tropo_whitelist_response():
    '''Retrieves Tropo's whitelist using "nslookup" tool through CLI

    Returns: string
    '''
    return check_output(["nslookup", "-q=TXT",
                         "_netblocks.tropo.com", "8.8.8.8"])

if __name__ == '__main__':
    print_whitelist()
