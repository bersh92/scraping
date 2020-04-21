# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['kinogo.by']
    start_urls = ['https://kinogo.by']
    list_of_movie_names = "//h2[@class='zagolovki']"
    movie_name = ".//a/text()"
    next_button = "//a[text()='Позже']/@href"

    def parse(self, response):
        for movie in response.xpath(self.list_of_movie_names):
            yield {
                'movies': movie.xpath(self.movie_name).get(),
            }

        next_page = response.xpath(self.next_button).get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)