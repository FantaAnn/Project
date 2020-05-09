# Discord Bot
# "ПИН" - Переводи и Находи
# Для правильной работы необходимо наличие api и data-данных

import random
from discord.ext import commands
import discord
import requests

# импортирование api-файлов
# находятся в папке api

from api.maps_api import find_delta, find_object_coordinates, find_object_info, take_map_picture
from api.wikipedia_api import wiki_page, wiki_image
from api.synonyms_api import find_synonyms
from api.translate_api import translate_word, get_languages


# подгрузка данных для работы с ними
# находятся в папке data

file = open('./data/Страны.txt', encoding='utf8')
COUNTRY = file.read().strip().split('\n')
file.close()

file = open('./data/Моря.txt', encoding='utf8')
SEA = file.read().strip().split('\n')
file.close()

file = open('./data/Реки.txt', encoding='utf8')
RIVER = file.read().strip().split('\n')
file.close()

file = open('./data/Метки.txt', encoding='utf8')
POINTS = file.read().strip().split('\n')
file.close()

file = open('./data/Озера.txt', encoding='utf8')
LAKES = file.read().strip().split('\n')
file.close()

file = open('./data/Города.txt', encoding='utf8')
CITIES = file.read().strip().split('\n')
file.close()

# токен
file = open('./data/Token.txt', encoding='utf8')
TOKEN = file.read().strip().split('\n')[0]
file.close()


class Bot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.map_type = "sat,skl"
        self.point_type = "flag"
        self.show_wiki = True
        self.show_map = True
        self.count = 5
        self.language = "en-ru"

    # обучение
    @commands.command(name='learning_country', brief='!learning_country', description="Обучение по странам")
    async def learning_country(self, ctx):
        await ctx.send('Давайте изучим ' + str(self.count) + ' стран(-у)')
        for i in range(self.count):
            wiki_message = self.show_wiki
            image = self.show_map
            country = random.choice(COUNTRY)
            embed = discord.Embed(title=country, color=0x9400d3)
            if self.show_wiki:
                content, url = wiki_page(country)
                wiki_message = "{0}\n{1}".format(content, url)
                embed.description = wiki_message
            if self.show_map:
                info = find_object_info(country).json()
                coordinates = find_object_coordinates(info)
                delta = find_delta(info)
                image = take_map_picture(coordinates, delta, self.map_type, self.point_type)
                embed.set_image(url=image.url)
            await ctx.send(str(i + 1) + ' страна')
            await ctx.send(embed=embed)

    @commands.command(name='learning_sea', brief='!learning_sea', description="Обучение по морям")
    async def learning_sea(self, ctx):
        await ctx.send('Давайте изучим ' + str(self.count) + ' моря(-ей)')
        for i in range(self.count):
            wiki_message = self.show_wiki
            image = self.show_map
            sea = random.choice(SEA)
            embed = discord.Embed(title=sea, color=0x9400d3)
            if self.show_wiki:
                content, url = wiki_page(sea)
                wiki_message = "{0}\n{1}".format(content, url)
                embed.description = wiki_message
            if self.show_map:
                info = find_object_info(sea).json()
                coordinates = find_object_coordinates(info)
                delta = find_delta(info)
                image = take_map_picture(coordinates, delta, self.map_type, self.point_type)
                embed.set_image(url=image.url)
            await ctx.send(str(i + 1) + ' море')
            await ctx.send(embed=embed)

    @commands.command(name='learning_lake', brief='!learning_lake', description="Обучение по озерам")
    async def learning_lake(self, ctx):
        await ctx.send('Давайте изучим ' + str(self.count) + ' озер(-о, -а)')
        for i in range(self.count):
            wiki_message = self.show_wiki
            image = self.show_map
            lake = random.choice(LAKES)
            embed = discord.Embed(title=lake, color=0x9400d3)
            if self.show_wiki:
                content, url = wiki_page(lake)
                wiki_message = "{0}\n{1}".format(content, url)
                embed.description = wiki_message
            if self.show_map:
                info = find_object_info(lake).json()
                coordinates = find_object_coordinates(info)
                delta = find_delta(info)
                image = take_map_picture(coordinates, delta, self.map_type, self.point_type)
                embed.set_image(url=image.url)
            await ctx.send(str(i + 1) + ' озеро')
            await ctx.send(embed=embed)

    @commands.command(name='learning_city', brief='!learning_city', description="Обучение по городам")
    async def learning_city(self, ctx):
        await ctx.send('Давайте изучим ' + str(self.count) + ' город(-ов, -а)')
        for i in range(self.count):
            wiki_message = self.show_wiki
            image = self.show_map
            city = random.choice(CITIES)
            embed = discord.Embed(title=city, color=0x9400d3)
            if self.show_wiki:
                content, url = wiki_page(city)
                wiki_message = "{0}\n{1}".format(content, url)
                embed.description = wiki_message
            if self.show_map:
                info = find_object_info(city).json()
                coordinates = find_object_coordinates(info)
                delta = find_delta(info)
                image = take_map_picture(coordinates, delta, self.map_type, self.point_type)
                embed.set_image(url=image.url)
            await ctx.send(str(i + 1) + ' город')
            await ctx.send(embed=embed)

    @commands.command(name='learning_river', brief='!learning_river', description="Обучение по рекам")
    async def learning_river(self, ctx):
        await ctx.send('Давайте изучим ' + str(self.count) + ' рек(-а, -и)')
        for i in range(self.count):
            wiki_message = self.show_wiki
            image = self.show_map
            river = random.choice(RIVER)
            embed = discord.Embed(title=river, color=0x9400d3)
            if self.show_wiki:
                content, url = wiki_page(river)
                wiki_message = "{0}\n{1}".format(content, url)
                embed.description = wiki_message
            if self.show_map:
                info = find_object_info(river).json()
                coordinates = find_object_coordinates(info)
                delta = find_delta(info)
                image = take_map_picture(coordinates, delta, self.map_type, self.point_type)
                embed.set_image(url=image.url)
            await ctx.send(str(i + 1) + ' река')
            await ctx.send(embed=embed)

    # вывод рандомной страны
    @commands.command(name='country', brief='!country', description="Показать случайную страну")
    async def random_country(self, ctx):
        wiki_message = self.show_wiki
        image = self.show_map
        country = random.choice(COUNTRY)
        embed = discord.Embed(title=country, color=0x9400d3)
        if self.show_wiki:
            content, url = wiki_page(country)
            wiki_message = "{0}\n{1}".format(content, url)
            embed.description = wiki_message
        if self.show_map:
            info = find_object_info(country).json()
            coordinates = find_object_coordinates(info)
            delta = find_delta(info)
            image = take_map_picture(coordinates, delta, self.map_type, self.point_type)
            embed.set_image(url=image.url)
        await ctx.send(embed=embed)

    # вывод рандомного озера
    @commands.command(name='lake', brief='!lake', description="Показать случайное озеро")
    async def random_lake(self, ctx):
        wiki_message = self.show_wiki
        image = self.show_map
        lake = random.choice(LAKES)
        embed = discord.Embed(title=lake, color=0x9400d3)
        if self.show_wiki:
            content, url = wiki_page(lake)
            wiki_message = "{0}\n{1}".format(content, url)
            embed.description = wiki_message
        if self.show_map:
            info = find_object_info(lake).json()
            coordinates = find_object_coordinates(info)
            delta = find_delta(info)
            image = take_map_picture(coordinates, delta, self.map_type, self.point_type)
            embed.set_image(url=image.url)
        await ctx.send(embed=embed)

    # вывод рандомной реки
    @commands.command(name='river', brief='!river', description="Показать случайную реку")
    async def random_river(self, ctx):
        wiki_message = self.show_wiki
        image = self.show_map
        river = random.choice(RIVER)
        embed = discord.Embed(title=river, color=0x9400d3)
        if self.show_wiki:
            content, url = wiki_page(river)
            wiki_message = "{0}\n{1}".format(content, url)
            embed.description = wiki_message
        if self.show_map:
            info = find_object_info(river).json()
            coordinates = find_object_coordinates(info)
            delta = find_delta(info)
            image = take_map_picture(coordinates, delta, self.map_type, self.point_type)
            embed.set_image(url=image.url)
        await ctx.send(embed=embed)

    # вывод рандомного моря
    @commands.command(name='sea', brief='!sea', description="Показать случайное море")
    async def random_sea(self, ctx):
        wiki_message = self.show_wiki
        image = self.show_map
        sea = random.choice(SEA)
        embed = discord.Embed(title=sea, color=0x9400d3)
        if self.show_wiki:
            content, url = wiki_page(sea)
            wiki_message = "{0}\n{1}".format(content, url)
            embed.description = wiki_message
        if self.show_map:
            info = find_object_info(sea).json()
            coordinates = find_object_coordinates(info)
            delta = find_delta(info)
            image = take_map_picture(coordinates, delta, self.map_type, self.point_type)
            embed.set_image(url=image.url)
        await ctx.send(embed=embed)

    # вывод рандомного города
    @commands.command(name='city', brief='!city', description="Показать случайный город")
    async def random_city(self, ctx):
        wiki_message = self.show_wiki
        image = self.show_map
        city = random.choice(CITIES)
        embed = discord.Embed(title=city, color=0x9400d3)
        if self.show_wiki:
            content, url = wiki_page(city)
            wiki_message = "{0}\n{1}".format(content, url)
            embed.description = wiki_message
        if self.show_map:
            info = find_object_info(city).json()
            coordinates = find_object_coordinates(info)
            delta = find_delta(info)
            image = take_map_picture(coordinates, delta, self.map_type, self.point_type)
            embed.set_image(url=image.url)
        await ctx.send(embed=embed)

    # изменение количества "раундов" в обучении
    @commands.command(name='change_count', brief='!change_count', description="Изменить количество в обучении")
    async def change_count(self, ctx, new_count):
        try:
            new_count = int(new_count)
            assert new_count > 0
            self.count = new_count
            embed = discord.Embed(title="Успешно", description=f"Количество изменено на **{self.count}**",
                                  color=0x00a550)
            await ctx.send(embed=embed)
        except Exception:
            embed = discord.Embed(title="Ошибка", description="Неправильно указано число", color=0xff2b2b)
            await ctx.send(embed=embed)

    # изменение метки(указателя)
    @commands.command(name='point', brief='!point', description="Изменить тип метки")
    async def change_point_type(self, ctx, point_type):
        if point_type.lower() not in POINTS:
            points = '\n'.join(POINTS)
            embed = discord.Embed(title="Ошибка", description="Неправильный тип метки", color=0xff2b2b)
            embed.add_field(name="Доступные типы метки:", value=points, inline=False)
            await ctx.send(embed=embed)
        else:
            self.point_type = point_type
            embed = discord.Embed(title="Успешно", description=f"Стиль метки изменен на **{self.point_type}**", color=0x00a550)
            await ctx.send(embed=embed)

    @commands.command(name='wiki', brief='!wiki {ON/OFF}', description="Включение отображения страницы Wikipedia")
    async def wikipedia_settings(self, ctx, flag):
        if flag.lower() == 'on':
            self.show_wiki = True
            embed = discord.Embed(title="Успешно", description="Отображение Wiki-страницы **включено**", color=0x00a550)
            await ctx.send(embed=embed)
        elif flag.lower() == 'off':
            self.show_wiki = False
            embed = discord.Embed(title="Успешно", description="Отображение Wiki-страницы **выключено**", color=0x945d0b)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Ошибка", description="Неверный аргумент", color=0xff2b2b)
            embed.add_field(name="Доступные аргументы:", value='ON\nOFF', inline=False)
            await ctx.send(embed=embed)

    @commands.command(name='map', brief='!map {ON/OFF}', description="Включение отображения карты")
    async def map_settings(self, ctx, flag):
        if flag.lower() == 'on':
            self.show_map = True
            embed = discord.Embed(title="Успешно", description="Отображение карты **включено**", color=0x00a550)
            await ctx.send(embed=embed)
        elif flag.lower() == 'off':
            self.show_map = False
            embed = discord.Embed(title="Успешно", description="Отображение карты **выключено**", color=0x945d0b)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Ошибка", description="Неверный аргумент", color=0xff2b2b)
            embed.add_field(name="Доступные аргументы:", value='ON\nOFF', inline=False)
            await ctx.send(embed=embed)

    @commands.command(name='syn', brief='!syn {слово}', description="Найти синонимы к слову")
    async def synonyms(self, ctx, context):
        data = find_synonyms(context)
        data = '\n'.join(data)
        embed = discord.Embed(title="Синонимы", color=0xffa420)
        embed.add_field(name='Найденные синонимы', value=data, inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='translate', brief='!translate {слово}', description="Перевести слово на другой язык")
    async def translate(self, ctx, context):
        data = translate_word(context, self.language)
        embed = discord.Embed(title="Перевод", color=0xffa420)
        embed.add_field(name='Найденный перевод', value=data, inline=False)
        embed.add_field(name='Установленный язык', value=self.language, inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='language', brief='!language {слово}', description="Изменить язык переводчика")
    async def change_language(self, ctx, context):
        accept_langs = get_languages()
        if context.lower() not in accept_langs:
            embed = discord.Embed(title="Ошибка", description="Неверный формат языка", color=0xff2b2b)
            embed.add_field(name='Доступные форматы язка', value="\t".join(accept_langs), inline=False)
        else:
            self.language = context.lower()
            embed = discord.Embed(title="Язык изменен", color=0xffa420)
            embed.add_field(name='Установленный язык', value=self.language, inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='search', brief='!search {слово}', description="Поиск места")
    async def search_place(self, ctx, *place):
        wiki_message = self.show_wiki
        image = self.show_map
        place = ' '.join(place)
        embed = discord.Embed(title=place, color=0x9400d3)
        if self.show_wiki:
            content, url = wiki_page(place)
            wiki_message = "{0}\n{1}".format(content, url)
            embed.description = wiki_message
        if self.show_map:
            info = find_object_info(place).json()
            coordinates = find_object_coordinates(info)
            delta = find_delta(info)
            image = take_map_picture(coordinates, delta, self.map_type, self.point_type)
            embed.set_image(url=image.url)
        await ctx.send(embed=embed)

    @commands.command(name='mapstyle', brief='!mapstyle {map/sat,skl}', description="Изменить тип карты")
    async def change_map_type(self, ctx, map_type):
        if map_type.lower() != 'map' and map_type.lower() != 'sat,skl':
            embed = discord.Embed(title="Ошибка", description="Неправильный тип карты", color=0xff2b2b)
            embed.add_field(name="Доступные типы метки:", value='map\nsat,skl', inline=False)
            await ctx.send(embed=embed)
        else:
            self.map_type = map_type.lower()
            embed = discord.Embed(title="Успешно", description=f"Стиль карты изменен на **{self.map_type}**",
                                  color=0x00a550)
            await ctx.send(embed=embed)


bot = commands.Bot(command_prefix='!')
bot.add_cog(Bot(bot))
bot.run(TOKEN)
