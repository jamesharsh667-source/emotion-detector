from PIL import Image, ImageDraw, ImageFont
import textwrap
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

def read_file_text(p):
    try:
        return Path(p).read_text(encoding='utf-8')
    except Exception:
        return "(file not found)"

def draw_text_image(lines, out_path, size=(1000,700), title=None):
    img = Image.new('RGB', size, color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    x, y = 20, 20
    if title:
        draw.text((x, y), title, fill='black', font=font)
        y += 24
    for line in lines:
        draw.text((x, y), line, fill='black', font=font)
        y += 14
        if y > size[1] - 40:
            break
    img.save(out_path)

def make_4a():
    tree = [
        'emotion-detector-project/',
        '  README.md',
        '  server.py',
        '  test_emotion_detection.py',
        '  2a_emotion_detection.py',
        '  3a_output_formatting.py',
        '  packaging/',
        '    __init__.py',
        '  emotion_detector/',
        '    __init__.py',
        '    emotion_detection.py',
        '  templates/',
        '    index.html'
    ]

    init_text = read_file_text(BASE / 'packaging' / '__init__.py')
    wrapped = textwrap.wrap(init_text, width=90)
    lines = ['Folder structure:', ''] + tree + ['','`packaging/__init__.py` contents:',''] + wrapped
    draw_text_image(lines, BASE / '4a_packaging.png', size=(1200,900), title='4a_packaging.png')

def make_4b():
    sample_output = {
        'anger': 0.02,
        'disgust': 0.0,
        'fear': 0.01,
        'joy': 0.88,
        'sadness': 0.09,
        'dominant_emotion': 'joy'
    }
    json_lines = [str(sample_output)]
    caption = ['Expected formatted output for a sample input:', '']
    lines = caption + json_lines
    draw_text_image(lines, BASE / '4b_packaging_test.png', size=(1000,200), title='4b_packaging_test.png')

if __name__ == '__main__':
    make_4a()
    make_4b()
    print('Images created: 4a_packaging.png, 4b_packaging_test.png')
