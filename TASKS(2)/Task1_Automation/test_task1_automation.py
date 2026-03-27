import os
import tempfile

def test_move_jpg_files():
    from task1_automation import move_jpg_files

    with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as dst:
        open(os.path.join(src, 'a.jpg'), 'w').close()
        open(os.path.join(src, 'b.jpeg'), 'w').close()
        open(os.path.join(src, 'c.txt'), 'w').close()

        moved = move_jpg_files(src, dst)

        assert moved == 2
        assert os.path.exists(os.path.join(dst, 'a.jpg'))
        assert os.path.exists(os.path.join(dst, 'b.jpeg'))
        assert not os.path.exists(os.path.join(src, 'a.jpg'))


def test_extract_email_addresses():
    from task1_automation import extract_email_addresses

    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, 'src.txt')
        dst = os.path.join(tmp, 'dst.txt')
        with open(src, 'w', encoding='utf-8') as f:
            f.write('hello test@example.com\nother@domain.org\nrepeat@example.com')

        emails = extract_email_addresses(src, dst)

        assert sorted(emails) == ['other@domain.org', 'repeat@example.com', 'test@example.com']
        with open(dst, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        assert sorted(lines) == sorted(emails)
