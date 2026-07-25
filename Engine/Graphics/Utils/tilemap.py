from ...Kernel.Components.graphics import tileMapRender, drawMode, Color3, Color4, batchDrawing
from ...Kernel.Components.vectors import Vec2
from ...Kernel.Components.system import System
from ...Kernel.kernel import log_system
from ..Primitives.rectangle import Rectangle
from ..Render.batch_render import batchRender

class tileMap:
    def __init__(self, render:tileMapRender, window=None):
        self.render = render
        self.tilesize = Vec2(0.0, 0.0)
        self.tiles = []
        self.textures = []
        self.tmp_tiles_data = []
        self.window = window
        self.position = Vec2(0.0, 0.0)
        self.batch = batchRender(batchDrawing.DYNAMIC)

    def requestReCalculate(self):
        for tile in self.tiles:
            tile[2] = False

    def addTexture(self, texture, name:str):
        for tex in self.textures:
            if tex[1] == name:
                log_system.addError(f"Texture:{name} with this name already exists")
                return

        self.textures.append([texture, name])

    def removeTexture(self, name:str):
        for index, tex in enumerate(self.textures):
            if tex[1] == name:
                self.textures.pop(index)
                return

        log_system.addError(f"Texture:{name} is not found!")

    def setTileSize(self, new_size:Vec2):

        # CHECK TYPE
        
        if isinstance(new_size, list) or isinstance(new_size, tuple):
            new_size = System.cltv2(new_size)
            log_system.addWarn("Use Vec2 in setTileSize")
        else:
            if not isinstance(new_size, Vec2):
                return
        
        # APPLY
        
        self.tilesize = new_size

        self.requestReCalculate()

    def setPosition(self, new_position):

        # CHECK TYPE
        
        if isinstance(new_position, list) or isinstance(new_position, tuple):
            new_position = System.cltv2(new_position)
        else:
            if not isinstance(new_position, Vec2):
                return
        
        # APPLY
        
        self.position = new_position

        self.requestReCalculate()

    def addTile(self, position:Vec2, texName:str, color:Color3 | Color4 = Color4(1.0, 1.0, 1.0, 1.0), skiperror:bool=False):
        
        # CHECK TILE POSITION

        for tile in self.tiles:
            if tile[0].x//self.tilesize.x == position.x and tile[0].y//self.tilesize.y == position.y:
                if not skiperror:
                    log_system.addError("The tile is already in this position!")
                return

        # CHECK TILE TEXTURE

        for tex in self.textures:
            if tex[1] == texName:
                self.tiles.append([position, texName, False, color])
                return
        
        if not skiperror:
            log_system.addError(f"Texture:{texName} is not found!")

    def removeTile(self, position:Vec2, skiperror:bool=False):
        for index, tile in enumerate(self.tiles):
            if tile[0].x // self.tilesize.x == position.x and tile[0].y // self.tilesize.y == position.y:
                self.tiles.pop(index)
                return
        
        if not skiperror:
            log_system.addError("There is no tile in this position!")
        
    def drawTileMap(self, mode:drawMode):
        self.tmp_tiles_data.clear()
    
        for tile in self.tiles:
            if not tile[2]:
                tile[0] = Vec2(tile[0].x*self.tilesize.x, tile[0].y*self.tilesize.y)
                tile[2] = True
        
            rect = Rectangle(self.window)
            rect.setPosition(tile[0]+self.position)
            rect.setSize(self.tilesize)
            rect.setColor(tile[3])
    
            for tex in self.textures:
                if tex[1] == tile[1]:
                    rect.setTexture(tex[0])

            if self.render == tileMapRender.RECTS:
                self.tmp_tiles_data.append(rect)
            elif self.render == tileMapRender.BATCH:
                self.batch.addPrimitive(rect)

        if self.render == tileMapRender.RECTS:
            for tile_rect in self.tmp_tiles_data:
                tile_rect.drawRectangle(mode)
        elif self.render == tileMapRender.BATCH:
            if self.batch.mode != mode:
                self.batch.setDrawMode(mode)
            self.batch.renderPrimitives()
