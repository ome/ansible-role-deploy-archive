import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_dir(File):
    f = File('/opt/deploy-archive-test/idr.openmicroscopy.org-IDR-0.5.0')
    assert f.exists
    assert f.is_directory


def test_file(File):
    f = File('/opt/deploy-archive-test/idr.openmicroscopy.org-IDR-0.5.0'
             '/index.html')
    assert f.exists
    assert f.is_file


def test_symlink(File):
    f = File('/opt/idr-web-src')
    assert f.exists
    assert f.is_symlink
    assert f.linked_to == (
        '/opt/deploy-archive-test/idr.openmicroscopy.org-IDR-0.5.0')


def test_handler_trigger_once(File):
    f = File('/opt/deploy-archive-test/handler-triggered')
    assert f.content.strip() == 'triggered'
