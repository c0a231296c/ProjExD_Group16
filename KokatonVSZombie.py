import pygame
import sys

# Pygameの初期化
pygame.init()

# 画面サイズとマス目サイズの設定
SCREEN_WIDTH = 800  # 画面の幅
SCREEN_HEIGHT = 600  # 画面の高さ
GRID_SIZE = 80  # 1つのマスのサイズ
INFO_AREA_HEIGHT = 80  # 上部の情報エリアの高さ

# 色の定義 (RGB形式)
GREEN = (0, 128, 0)  # 背景の緑色
WHITE = (255, 255, 255)  # マス目の線の色
BLACK = (0, 0, 0)  # テキストの色
GRAY = (200, 200, 200)  # 情報エリアの背景色
RED = (255, 0, 0)  # ゾンビの色
BLUE = (0, 0, 255)  # 植物の色

# 画面の作成
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plants vs Zombies 風ゲーム")

# フォントの設定
font = pygame.font.Font(None, 36)

# ゾンビクラスの定義
class Zombie:
    def __init__(self, x, y, speed):
        self.rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)  # ゾンビを長方形で表す
        self.speed = speed
        self.alive = True  # 障害物に到達すると停止

    def move(self, obstacles):
        if self.alive:
            # ゾンビが障害物に衝突しているか確認
            for obstacle in obstacles:
                if self.rect.colliderect(obstacle):
                    self.alive = False  # 衝突したら停止
                    return
            # 左に移動
            self.rect.x -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)


class Beam:
    def __init__(self, x, y):
        """
        ビームを生成するクラス
        引数：x 味方オブジェクトの右座標
        引数：y 味方オブジェクトの中心座標
        """
        self.image = pygame.image.load("ex5/fig/beam.png")
        self.rect = self.image.get_rect()  # 画像rectの抽出
        self.rect.x = x  # ビームのx座標 
        self.rect.y = y  # ビームのy座標
        self.speed = 5  # ビームのスピード

    def update(self):
        """ビームの移動"""
        self.rect.x += self.speed  # ビームx座標にself.spped分加算

    def draw(self, surface):
        """ビームの描画"""
        surface.blit(self.image, self.rect)  # ビーム画像の表示

# テキストを描画する関数
def draw_text(surface, text, x, y, color):
    rendered_text = font.render(text, True, color)
    surface.blit(rendered_text, (x, y))

# マス目を描画する関数
def draw_grid(surface, width, height, grid_size, offset_y):
    for x in range(0, width, grid_size):
        pygame.draw.line(surface, WHITE, (x, offset_y), (x, height))
    for y in range(offset_y, height, grid_size):
        pygame.draw.line(surface, WHITE, (0, y), (width, y))

# 情報エリアを描画する関数
def draw_info_area(surface, width, height):
    pygame.draw.rect(surface, GRAY, (0, 0, width, height))
    draw_text(surface, "score: 0", 20, 20, BLACK)
    draw_text(surface, "set", 200, 20, BLACK)

# メインのゲームループ
def main():
    clock = pygame.time.Clock()
    zombie = Zombie(SCREEN_WIDTH, INFO_AREA_HEIGHT + GRID_SIZE * 2, 2)  # ゾンビを1体生成
    plants = []  # 障害物（植物）を格納するリスト(rectが格納されていく)
    beams = []  # 発射されたビームを格納するリスト
    plant_timers = []  # 植物ごとのビームタイマーを格納するリスト
    shot_time = 1  # 〇秒ごとにビームを打つ

    # ゲームループ
    while True:
        timer = pygame.time.get_ticks()  # タイマー(1000で1秒)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # マウスクリックで植物を配置
                mouse_x, mouse_y = event.pos
                if mouse_y > INFO_AREA_HEIGHT:  # 情報エリア以外をクリック可能
                    grid_x = (mouse_x // GRID_SIZE) * GRID_SIZE
                    grid_y = (mouse_y // GRID_SIZE) * GRID_SIZE
                    plant_rect = pygame.Rect(grid_x, grid_y, GRID_SIZE, GRID_SIZE)
                    plants.append(plant_rect)
                    plant_timers.append(pygame.time.get_ticks())

        # 背景の描画
        screen.fill(GREEN)

        # 情報エリアの描画
        draw_info_area(screen, SCREEN_WIDTH, INFO_AREA_HEIGHT)

        # マス目の描画
        draw_grid(screen, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, INFO_AREA_HEIGHT)

        for i, plant in enumerate(plants):
                pygame.draw.rect(screen, BLUE, plant)  # 植物を描画

                # 〇秒ごとにビームを発射
                if timer - plant_timers[i] > shot_time * 1000:
                    beams.append(Beam(plant.right, plant.centery))  # 新しいビームを追加
                    plant_timers[i] = timer  # タイマーをリセット
    

        # ビームの移動と描画
        for beam in beams:
            beam.update()
            beam.draw(screen)
            # ビームが画面外に出たら削除
            if beam.rect.x > SCREEN_WIDTH:
                beams.remove(beam)

        # ゾンビの動きと描画
        zombie.move(plants)
        zombie.draw(screen)

        # 画面の更新
        pygame.display.update()
        clock.tick(60)

# メイン関数の実行
if __name__ == "__main__":
    main()