#!/bin/python
#coding=utf-8
import media
import fresh_tomatoes 

wohucanglong = media.Movie('Crouching Tiger, Hidden Dragon', 
                           '武侠片', 
                           2000, 
                           'http://posters.imdb.cn/upload/2000/05/16/7FwAPGEMYd_1148432641.jpg', 
                           'https://www.youtube.com/watch?v=gLpZ_5bHmo8')

godFather  =  media.Movie('Godfather',
                          '教父',
                          1996,
                          'http://posters.imdb.cn/upload/1972/03/15/U63vt6GulM_1148432724.jpg',
                          'https://www.youtube.com/watch?v=HiCnnsHfadU')

dahelian  =  media.Movie('A River Runs Through It',
                         '大河恋',
                         1992,
                         'http://posters.imdb.cn/upload/2010/01/31/8Z7yA2jer_1178204445.jpg',
                         'https://www.youtube.com/watch?v=5Z7yeXtBQMU')

TheMatrix  =  media.Movie('The Matrix', 
                          '黑客帝国', 
                          1999, 
                          'http://posters.imdb.cn/upload/1999/03/31/0bDwLci3Qx_1148433202.jpg', 
                          'https://www.youtube.com/watch?v=KNrSNcaYiZg')

huangjin  =  media.Movie('The Good, the Bad and the Ugly',
                         '黄金三镖客', 
                         1966, 
                         'http://posters.imdb.cn/upload/1999/03/29/62RLIR9saC_1148432357.jpg', 
                         'https://www.youtube.com/watch?v=h1PfrmCGFnk')

SinCity  =  media.Movie('Sin City',
                        '罪恶之城', 
                        2005, 
                        'http://posters.imdb.cn/upload/2005/04/01/8DLPvsS026_1148434716.jpg',
                        'https://www.youtube.com/watch?v=MnMZeDmfgmU')

movies  =  [SinCity, huangjin, TheMatrix, dahelian, godFather,wohucanglong]
fresh_tomatoes.open_movies_page(movies)
