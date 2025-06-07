from flask import Flask, jsonify, send_from_directory
import requests

app = Flask(__name__, static_folder='.')

from flask import Flask, jsonify, send_from_directory
import requests

app = Flask(__name__, static_folder='.')


@app.route('/api/metadata')
def metadata():
    # 1. Fetch IMDSv2 token
    token = requests.put(
        'http://169.254.169.254/latest/api/token',
        headers={'X-aws-ec2-metadata-token-ttl-seconds': '21600'}
    ).text
    # 2. Fetch metadata
    metadata = requests.get(
        'http://169.254.169.254/latest/meta-data',
        headers={'X-aws-ec2-metadata-token': token}
    )
    metadata.raise_for_status()
    print(dir(metadata))
    print(metadata.text)
    return {} # metadata.json()

@app.route('/api/server-details')
def hostname():
    # 1. Fetch IMDSv2 token
    token = requests.put(
        'http://169.254.169.254/latest/api/token',
        headers={'X-aws-ec2-metadata-token-ttl-seconds': '21600'}
    ).text
    # 2. Fetch metadata
    hostname = requests.get(
        'http://169.254.169.254/latest/meta-data/hostname',
        headers={'X-aws-ec2-metadata-token': token}
    ).text
    instance_id = requests.get(
        'http://169.254.169.254/latest/meta-data/instance-id',
        headers={'X-aws-ec2-metadata-token': token}
    ).text
    local_ipv4 = requests.get(
        'http://169.254.169.254/latest/meta-data/local-ipv4',
        headers={'X-aws-ec2-metadata-token': token}
    ).text
    public_ipv4 = requests.get(
        'http://169.254.169.254/latest/meta-data/public-ipv4',
        headers={'X-aws-ec2-metadata-token': token}
    ).text
    ami_id = requests.get(
        'http://169.254.169.254/latest/meta-data/ami-id',
        headers={'X-aws-ec2-metadata-token': token}
    ).text
    mac = requests.get(
        'http://169.254.169.254/latest/meta-data/mac',
        headers={'X-aws-ec2-metadata-token': token}
    ).text
    local_hostname = requests.get(
        'http://169.254.169.254/latest/meta-data/local-hostname',
        headers={'X-aws-ec2-metadata-token': token}
    ).text
    public_hostname = requests.get(
        'http://169.254.169.254/latest/meta-data/public-hostname',
        headers={'X-aws-ec2-metadata-token': token}
    ).text
    reservation_id = requests.get(
        'http://169.254.169.254/latest/meta-data/reservation-id',
        headers={'X-aws-ec2-metadata-token': token}
    ).text
    security_groups = requests.get(
        'http://169.254.169.254/latest/meta-data/security-groups',
        headers={'X-aws-ec2-metadata-token': token}
    ).text

    # Helper to fetch directory listings and their values
    def fetch_meta_section(path):
        url = f'http://169.254.169.254/latest/meta-data/{path}'
        resp = requests.get(url, headers={'X-aws-ec2-metadata-token': token})
        items = resp.text.splitlines()
        section = {}
        for item in items:
            # strip trailing slash for key
            key = item.rstrip('/')
            sub_url = url + item
            val = requests.get(sub_url, headers={'X-aws-ec2-metadata-token': token}).text
            section[key] = val
        return section

    # Fetch nested metadata sections
    metrics_data = fetch_meta_section('metrics/')
    network_data = fetch_meta_section('network/interfaces/macs/')
    placement_data = fetch_meta_section('placement/')
    instance_type = requests.get(
        'http://169.254.169.254/latest/meta-data/instance-type',
        headers={'X-aws-ec2-metadata-token': token}
    ).text
    availability_zone = requests.get(
        'http://169.254.169.254/latest/meta-data/placement/availability-zone',
        headers={'X-aws-ec2-metadata-token': token}
    ).text
    return jsonify(
        hostname=hostname,
        instance_id=instance_id,
        local_ipv4=local_ipv4,
        public_ipv4=public_ipv4,
        ami_id=ami_id,
        mac=mac,
        local_hostname=local_hostname,
        public_hostname=public_hostname,
        reservation_id=reservation_id,
        security_groups=security_groups,
        metrics=metrics_data,
        network=network_data,
        placement=placement_data,
        instance_type=instance_type,
        availability_zone=availability_zone,
    )

# Serve your existing index.html
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    # Listen on all interfaces so you can hit it remotely
    app.run(host='0.0.0.0', port=8000, debug=True)
