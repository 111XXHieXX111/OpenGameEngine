from ..Kernel.kernel import logWrapper, render_items

@logWrapper
def getItemByID(_id:int):
    for item in render_items:
        if item.id == _id:
            return item
