WIDTH = 80

def line():
    print("=" * WIDTH)
    
def space():
    print()
    
def text_centered(text):
    print(text.center(WIDTH))

def text_left(text):
    print(text)
    
def info(text):
    print(f"ℹ️  {text}")
    
def warning(text):
    print(f"⚠️  {text}")
    
def error(text):
    print(f"❌  {text}")
    
def success(text):
    print(f"✅  {text}")