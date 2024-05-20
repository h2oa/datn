require 'msf/core'

class MetasploitModule < Msf::Auxiliary
  include Msf::Exploit::Remote::HttpClient

  def initialize(info = {})
    super(update_info(info,
      'Name'           => 'Multiple Admin Pages Scanner',
      'Description'    => %q{
        This module scans for multiple potential administrative pages to exploit
        information disclosure vulnerabilities by checking various common admin paths.
      },
      'Author'         => ['Hoa Le Ngoc'],
      'License'        => MSF_LICENSE,
      'References'     => [
        ['URL', 'https://cwe.mitre.org/data/definitions/419.html']
      ]
    ))

    register_options(
      [
        Opt::RPORT(80),
        OptString.new('TARGETURI', [true, 'Base path to the web application', '/'])
      ])
  end

  def run
    admin_paths = [
      'admin.php',
      'admin-test.php',
      'administrator.php',
      'admin-uat.php',
      'administrator-uat.php',
      'administrator-test.php'
    ]

    admin_paths.each do |path|
      print_status("Checking #{path}")
      response = send_request_cgi(
        'method' => 'GET',
        'uri'    => normalize_uri(target_uri.path, path)
      )

      if response && response.code == 200
        print_good("Found accessible admin page at /#{path} - Status code: #{response.code}")
        print_line("===Response start===\n#{response.headers}\n#{response.body}\n===Response end===")
      else
        print_status("No admin page found at /#{path}")
      end
    end
  end
end
