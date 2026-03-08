import re

with open('/Volumes/Samsung/bsinfo/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make background animated
content = re.sub(
    r'background-image:[\s\S]*?background-attachment: fixed;',
    r'background-image:\n                radial-gradient(circle at top left, #c4e0ff, transparent 40%),\n                radial-gradient(circle at bottom right, #ffd1ea, transparent 50%),\n                radial-gradient(circle at bottom left, #d8f5d0, transparent 40%),\n                radial-gradient(circle at top right, #eaddff, transparent 40%);\n            background-attachment: fixed;\n            background-size: 200% 200%;\n            animation: bgShift 15s ease infinite alternate;',
    content
)

if '@keyframes scaleIn' in content and '@keyframes bgShift' not in content:
    content = content.replace('@keyframes scaleIn', '@keyframes bgShift {\n            0% { background-position: 0% 0%; }\n            100% { background-position: 100% 100%; }\n        }\n\n        @keyframes scaleIn')

# Refine cards to have VisionOS inner shadow
content = re.sub(
    r'box-shadow: var\(--card-shadow\);([\s\S]*?)position: relative;',
    r'box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08), inset 0 1px 1px rgba(255, 255, 255, 0.8);\1position: relative;\n            transform: translateZ(0);',
    content
)

# Hide complex before
content = re.sub(r'\.card::before \{[\s\S]*?pointer-events: none;\n        \}', '.card::before {\n            display: none;\n        }', content)

# Buttons
btn_green_replacement = """        .btn-green {
            background: linear-gradient(180deg, var(--accent-green) 0%, #2db64e 100%);
            color: #fff;
            box-shadow: 0 4px 15px rgba(52, 199, 89, 0.3), inset 0 1px 1px rgba(255, 255, 255, 0.5);
            border: 1px solid rgba(0,0,0,0.05);
        }

        .btn-green:hover {
            filter: brightness(1.05);
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(52, 199, 89, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.5);
        }"""
content = re.sub(r'\.btn-green \{[\s\S]*?\.btn-green:hover \{[\s\S]*?\}', btn_green_replacement, content)

btn_blue_replacement = """        .btn-blue {
            background: linear-gradient(180deg, var(--accent-blue) 0%, #0062cc 100%);
            color: #fff;
            font-size: 1.05rem;
            padding: 0.8rem 1.6rem;
            border-radius: 20px;
            font-weight: 600;
            white-space: nowrap;
            box-shadow: 0 4px 15px rgba(0, 122, 255, 0.3), inset 0 1px 1px rgba(255, 255, 255, 0.4);
            border: 1px solid rgba(0,0,0,0.05);
        }
        
        .btn-blue:hover {
            filter: brightness(1.05);
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(0, 122, 255, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.4);
        }"""
content = re.sub(r'\.btn-blue \{[\s\S]*?\.btn-blue:hover \{[\s\S]*?\}', btn_blue_replacement, content)

btn_blue_review_replacement = """        .btn-blue-review {
            background: linear-gradient(180deg, var(--accent-blue) 0%, #0062cc 100%);
            color: #fff;
            padding: 1.8rem;
            width: 100%;
            border-radius: 24px;
            margin-top: 2rem;
            display: flex;
            flex-direction: column;
            line-height: 1.4;
            font-size: 1.15rem;
            font-weight: 500;
            border: 1px solid rgba(0,0,0,0.05);
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 8px 25px rgba(0, 122, 255, 0.35), inset 0 1px 1px rgba(255, 255, 255, 0.4);
        }

        .btn-blue-review:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 30px rgba(0, 122, 255, 0.45), inset 0 1px 1px rgba(255, 255, 255, 0.4);
        }

        .btn-blue-review:active {
            transform: scale(0.96);
        }"""
content = re.sub(r'\.btn-blue-review \{[\s\S]*?\.btn-blue-review:active \{[\s\S]*?\}', btn_blue_review_replacement, content)

with open('/Volumes/Samsung/bsinfo/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

