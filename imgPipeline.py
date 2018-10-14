
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem

class ImgPipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        yield scrapy.Request(item['img_url'])

    def item_completed(self,results,item,info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem("Item contains no images")
        else:
            item['image_path'] = image_path
        return item

