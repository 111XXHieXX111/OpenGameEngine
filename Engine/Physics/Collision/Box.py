def BoxCollision(rect1, rect2):
    return (rect1.position.x < rect2.position.x + rect2.size.x and rect1.position.x + rect1.size.x > rect2.position.x and rect1.position.y < rect2.position.y + rect2.size.y and rect1.position.y + rect1.size.y > rect2.position.y)
