# Retrieves Tropo's current IP info for whitelisting
class TropoWhitelist
  def self.print_whitelist
    response = self.get_tropo_whitelist_response
    if response
      response.split("\n").each do |line|
        cidr_block = line.split('"')[1]
        puts "tropo," + cidr_block if cidr_block
      end
    end
  end

  private

  # Requires that nslookup tool be installed on host computer
  def self.get_tropo_whitelist_response
    `nslookup -q=TXT _netblocks.tropo.com 8.8.8.8`
  end
end

TropoWhitelist.print_whitelist
