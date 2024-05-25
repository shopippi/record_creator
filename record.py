from PIL import Image

def place_foreground_on_background(background_path, foreground_path, output_path, position=(59,354)):
    # 素材画像の読み込み
    foreground = Image.open(foreground_path)
    # 背景画像の読み込み
    background = Image.open(background_path)
    
    # foreground画像のサイズに合わせてbackground画像のサイズを変更
    foreground = foreground.resize((520,520))

    background = background.resize((1200,1200))
    # 素材画像を背景画像の指定位置に配置
    background.paste(foreground, position, foreground)
    
    # 出力画像を保存
    background.save(output_path)

if __name__ == "__main__":
    # 背景画像のパス
    background_path = "background.png"
    
    # 素材画像のパス
    foreground_path = "foreground.png"
    
    # 出力画像のパス
    output_path = "output.png"
    
    # 素材画像を配置する位置（左上隅が原点）
    position = (0, 0)
    
    
    # 背景に素材を配置して保存
    place_foreground_on_background("./design.png", "input-filepath-your-self", "output-path")
