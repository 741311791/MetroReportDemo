#!/usr/bin/env python
# coding: utf-8

# # 发展历程

# 至2020年底，深圳市轨道线路已开通1号线、2号线、3号线、4号线、5号线、6号线、7号线、8号线、9号线、10号线和11号线共11条，站点237座（不含换乘）、283座（含换乘），换乘站点40座，通车线网里程增长至411.0千米，线网密度从2020年初的0.32km/km²上升到0.42km/km²，站点800米覆盖率达28%，覆盖区域包括南山、福田、罗湖、宝安、龙岗、龙华、光明、盐田共8个行政区，坪山、大鹏无轨道线路覆盖。

# In[1]:


import pandas as pd
import geopandas as gpd
from keplergl import KeplerGl

area_gdf = gpd.read_file(r'G:\DeskTop\11_JupyterLabTest\dash_learning\入门\sz_group.geojson')
line_gdf = gpd.read_file(r'G:\DeskTop\11_JupyterLabTest\dash_learning\入门\sz_metro_line.geojson')
point_gdf = gpd.read_file(r'G:\DeskTop\11_JupyterLabTest\dash_learning\入门\sz_metro_stop.geojson')

map_1 = KeplerGl()
config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "kiwkchi",
          "type": "geojson",
          "config": {
            "dataId": "point",
            "label": "point",
            "color": [
              192,
              192,
              192
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": None,
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": False,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": {
                  "name": "STOP_NAME",
                  "type": "string"
                },
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "b2dq0q",
          "type": "geojson",
          "config": {
            "dataId": "line",
            "label": "line",
            "color": [
              18,
              147,
              154
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 1.5,
              "strokeColor": None,
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": False,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": {
              "name": "route_name",
              "type": "string"
            },
            "strokeColorScale": "ordinal",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "cra5oyb",
          "type": "geojson",
          "config": {
            "dataId": "area",
            "label": "area",
            "color": [
              22,
              42,
              101
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                28,
                92,
                154
              ],
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "point": [
              {
                "name": "STOP_NAME",
                "format": None
              },
              {
                "name": "ROUTE_NAME",
                "format": None
              }
            ],
            "line": [
              {
                "name": "link_id",
                "format": None
              },
              {
                "name": "link_type",
                "format": None
              },
              {
                "name": "route_name",
                "format": None
              }
            ],
            "area": [
              {
                "name": "NAME",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 22.67680171355907,
      "longitude": 114.04313764618617,
      "pitch": 0,
      "zoom": 8.903882166166095,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}
map_1.add_data(data=point_gdf, name='point')
map_1.add_data(data=line_gdf, name='line')
map_1.add_data(data=area_gdf, name='area')
map_1.config=config
map_1


# <center style='color:red;'> 表1 深圳市轨道线路详情 </center>
# 
# | **线路名称**  | **起终点** | **线路里程（km）** | **站点（座）** | **换乘站点（座）** | **平均站距（km）** |
# | ------------------------------------------------------------ | --------------- | -------------- | -------------- | ------------------ | -------------- |
# | 1号线                                                        | 机场东-罗湖     | 40.5           | 30             | 10                 | 1.40           |
# | 2号线                                                        | 赤湾-莲塘       | 39.6           | 32             | 10                 | 1.28           |
# | 3号线                                                        | 双龙-福保       | 43.1           | 31             | 11                 | 1.44           |
# | 4号线                                                        | 牛湖-福田口岸   | 31.3           | 23             | 7                  | 1.42           |
# | 5号线                                                        | 前湾-黄贝岭     | 47.7           | 27             | 10                 | 1.83           |
# | 6号线                                                        | 松岗-科学馆     | 49.4           | 27             | 7                  | 1.90           |
# | 7号线                                                        | 西丽湖-太安     | 30.1           | 27             | 11                 | 1.16           |
# | 8号线                                                        | 莲塘-盐田路     | 12.4           | 6              | 0                  | 2.06           |
# | 9号线                                                        | 前湾-文锦       | 36.2           | 32             | 9                  | 1.17           |
# | 10号线                                                       | 双拥街-福田口岸 | 29.3           | 24             | 5                  | 1.27           |
# | 11号线                                                       | 碧头-福田       | 51.9           | 18             | 6                  | 3.05           |
# | 线网合计（不重复计算）|             -                          | 411.5           | 237            | 40             | 1.54               |                |
# ```{admonition} 注意
# 1. 统计口径为2020年11月
# 2. 7号线不包含福邻地铁站
# 3. 换乘站点不包含莲塘（车内换乘）和福田口岸（出站换乘）
# ```

# ## 1.1    线网里程
# 
# &emsp;&emsp;深圳从1988年开始轨道交通研究工作，深圳市轨道一期工程于1998年开工、2004年建成通车，开通1号线（罗湖-世界之窗）、4号线（福田口岸-少年宫）两条线路，总运营里程22公里，车站19座（含换乘站1座）。
# 
# &emsp;&emsp;深圳市轨道二期工程于2006年开工、2011年建成通车，开通1号线（世界之窗-机场东）、2号线、3号线、4号线（少年宫-清湖）、5号线五条线路，总运营里程178公里，车站118座（含换乘站9座）。
# 
# &emsp;&emsp;深圳市轨道三期工程于2012年开工，至2020年底三期工程中的轨道11号线、7号线、9号线、5号线西延段、9号线西延段、6号线、10号线和8号线相继通车投入运营，深圳市目前已形成11条线路的城市轨道交通网络，城市轨道交通网路化运营迈入了新时代。

# In[2]:


from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
import pyecharts.options as opts
from pyecharts.charts import Bar, Line

network_year_change =  pd.DataFrame([
    {"年份":'2005',"客运量(万人次/日)":16,"换乘系数":"","运营里程":20,"客运强度":0.8,"线路数":2},
    {"年份":'2006',"客运量(万人次/日)":25,"换乘系数":"","运营里程":20,"客运强度":1.25,"线路数":2},
    {"年份":'2007',"客运量(万人次/日)":32,"换乘系数":"","运营里程":22,"客运强度":1.45,"线路数":2},
    {"年份":'2008',"客运量(万人次/日)":37,"换乘系数":"","运营里程":22,"客运强度":1.68,"线路数":2},
    {"年份":'2009',"客运量(万人次/日)":38,"换乘系数":"","运营里程":25,"客运强度":1.52,"线路数":2},
    {"年份":'2010',"客运量(万人次/日)":45,"换乘系数":1.15,"运营里程":25,"客运强度":1.8,"线路数":2},
    {"年份":'2011',"客运量(万人次/日)":173,"换乘系数":1.4,"运营里程":178,"客运强度":0.97,"线路数":5},
    {"年份":'2012',"客运量(万人次/日)":213,"换乘系数":1.43,"运营里程":178,"客运强度":1.2,"线路数":5},
    {"年份":'2013',"客运量(万人次/日)":251,"换乘系数":1.43,"运营里程":178,"客运强度":1.41,"线路数":5},
    {"年份":'2014',"客运量(万人次/日)":284,"换乘系数":1.43,"运营里程":178,"客运强度":1.6,"线路数":5},
    {"年份":'2015',"客运量(万人次/日)":307,"换乘系数":1.44,"运营里程":178,"客运强度":1.72,"线路数":5},
    {"年份":'2016',"客运量(万人次/日)":354,"换乘系数":1.5,"运营里程":285,"客运强度":1.24,"线路数":8},
    {"年份":'2017',"客运量(万人次/日)":506,"换乘系数":1.52,"运营里程":285,"客运强度":1.78,"线路数":8},
    {"年份":'2018',"客运量(万人次/日)":551,"换乘系数":1.53,"运营里程":285,"客运强度":1.93,"线路数":8},
    {"年份":'2019',"客运量(万人次/日)":591,"换乘系数":1.54,"运营里程":304,"客运强度":1.94,"线路数":8},
    {"年份":'2020.1',"客运量(万人次/日)":605,"换乘系数":1.61,"运营里程":383,"客运强度":1.58,"线路数":10}
])
network_year_change['年份']=network_year_change['年份'].astype(str)

b = (
    Bar()
    .add_xaxis(
        list(network_year_change['年份'])
    )
    .add_yaxis("运营里程(千米)", list(network_year_change['运营里程']))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="深圳历年轨道线网里程"),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value} 条"), interval=5
        )
    )
   
)
l = (
    Line()
    .add_xaxis(list(network_year_change['年份']))
    .add_yaxis("线路数", list(network_year_change['线路数']), yaxis_index=1, is_smooth=False)
    .set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False)
)
)
b.load_javascript()


# In[3]:


b.overlap(l).render_notebook()


# 
# &emsp;&emsp;对比2019年，深圳的排名超过南京、武汉，至2020年底，深圳线网里程位居全国第4。

# In[4]:


network_length_rank = pd.DataFrame([
    {"城市":"杭州","地铁里程（千米）":206},
    {"城市":"天津","地铁里程（千米）":233},
    {"城市":"重庆","地铁里程（千米）":329},
    {"城市":"武汉","地铁里程（千米）":339},
    {"城市":"成都","地铁里程（千米）":358},
    {"城市":"南京","地铁里程（千米）":378},
    {"城市":"深圳","地铁里程（千米）":411},
    {"城市":"广州","地铁里程（千米）":515},
    {"城市":"北京","地铁里程（千米）":699},
    {"城市":"上海","地铁里程（千米）":705}
])
bar=(
    Bar()
        .add_xaxis(network_length_rank['城市'].tolist())
        .add_yaxis("地铁里程（千米）", network_length_rank['地铁里程（千米）'].tolist())
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="城市轨道线网里程排名"))
    )
bar.render_notebook()


# ## 1.2    线网密度
# 
# &emsp;&emsp;至2020底，深圳交通小区轨道线网密度分布如下图所示。交通小区的面积包括总用地面积和建设用地面积两个统计口径，此处在计算服务面积覆盖率时使用的是交通小区的建设用地面积（扣除绿地、山地、湖泊等）。

# In[ ]:





# &emsp;按全市计算，深圳轨道线网密度从2020年初的0.32km/km²上升到0.42km/km²。其中，轨道线网密度最高的行政区为福田，指标达1.98km/km2，其次为罗湖和南山，如下图所示。

# In[5]:


district_line_density = pd.DataFrame([
    {"线网密度":1.36,"行政区名称":"罗湖"},
    {"线网密度":1.98,"行政区名称":"福田"},
    {"线网密度":0.85,"行政区名称":"南山"},
    {"线网密度":0.36,"行政区名称":"盐田"},
    {"线网密度":0.25,"行政区名称":"宝安"},
    {"线网密度":0.26,"行政区名称":"龙岗"},
    {"线网密度":0.23,"行政区名称":"光明"},
    {"线网密度":" -   ","行政区名称":"坪山"},
    {"线网密度":0.42,"行政区名称":"龙华"},
    {"线网密度":" -   ","行政区名称":"大鹏"}
])
bar=(
    Bar()
        .add_xaxis(district_line_density['行政区名称'].tolist())
        .add_yaxis("线网密度（km/km²）", district_line_density['线网密度'].tolist())
        .set_series_opts(label_opts=opts.LabelOpts(position="top"))
        .set_global_opts(title_opts=opts.TitleOpts(title="行政区轨道线网密度指标"))
    )
bar.render_notebook()


# &emsp;&emsp;各街道的轨道线网密度分布如下图所示，主要集中在华强北、东门，其次为桂园、莲花、福田、梅林等市区街道。

# In[6]:


block_density = pd.DataFrame([
    {"线网密度":3.818,"街道名称":"东门"},
    {"线网密度":3.024,"街道名称":"福保"},
    {"线网密度":2.932,"街道名称":"华富"},
    {"线网密度":2.834,"街道名称":"东晓"},
    {"线网密度":2.191,"街道名称":"南湖"},
    {"线网密度":2.022,"街道名称":"莲塘"},
    {"线网密度":1.927,"街道名称":"笋岗"},
    {"线网密度":1.914,"街道名称":"桂园"},
    {"线网密度":1.879,"街道名称":"莲花"},
    {"线网密度":1.754,"街道名称":"清水河"},
    {"线网密度":1.744,"街道名称":"南头"},
    {"线网密度":1.6,"街道名称":"翠竹"},
    {"线网密度":1.568,"街道名称":"东湖"},
    {"线网密度":1.362,"街道名称":"福田"},
    {"线网密度":1.298,"街道名称":"沙头"},
    {"线网密度":1.293,"街道名称":"华强北"},
    {"线网密度":1.267,"街道名称":"园岭"},
    {"线网密度":1.232,"街道名称":"民治"},
    {"线网密度":1.216,"街道名称":"粤海"},
    {"线网密度":1.215,"街道名称":"梅沙"},
    {"线网密度":1.075,"街道名称":"西丽"},
    {"线网密度":1.074,"街道名称":"沙头角"},
    {"线网密度":1.05,"街道名称":"南园"},
    {"线网密度":1.01,"街道名称":"黄贝"},
    {"线网密度":0.842,"街道名称":"梅林"},
    {"线网密度":0.828,"街道名称":"招商"},
    {"线网密度":0.804,"街道名称":"布吉"},
    {"线网密度":0.78,"街道名称":"福海"},
    {"线网密度":0.7,"街道名称":"横岗"},
    {"线网密度":0.593,"街道名称":"桃源"},
    {"线网密度":0.569,"街道名称":"平湖"},
    {"线网密度":0.496,"街道名称":"南山"},
    {"线网密度":0.426,"街道名称":"大浪"},
    {"线网密度":0.391,"街道名称":"龙城"},
    {"线网密度":0.389,"街道名称":"沙井"},
    {"线网密度":0.35,"街道名称":"蛇口"},
    {"线网密度":0.347,"街道名称":"吉华"},
    {"线网密度":0.329,"街道名称":"凤凰"},
    {"线网密度":0.288,"街道名称":"马田"},
    {"线网密度":0.284,"街道名称":"沙河"},
    {"线网密度":0.269,"街道名称":"新湖"},
    {"线网密度":0.259,"街道名称":"福永"},
    {"线网密度":0.25,"街道名称":"福城"},
    {"线网密度":0.238,"街道名称":"燕罗"},
    {"线网密度":0.234,"街道名称":"新安"},
    {"线网密度":0.229,"街道名称":"西乡"},
    {"线网密度":0.229,"街道名称":"宝龙"},
    {"线网密度":0.225,"街道名称":"观湖"},
    {"线网密度":0.223,"街道名称":"龙岗"},
    {"线网密度":0.223,"街道名称":"公明"},
    {"线网密度":0.203,"街道名称":"海山"},
    {"线网密度":0.198,"街道名称":"光明"},
    {"线网密度":0.17,"街道名称":"坂田"},
    {"线网密度":0.167,"街道名称":"观澜"},
    {"线网密度":0.152,"街道名称":"石岩"},
    {"线网密度":0.149,"街道名称":"龙华"},
    {"线网密度":0.117,"街道名称":"新桥"},
    {"线网密度":0.114,"街道名称":"航城"},
    {"线网密度":0.103,"街道名称":"坪地"},
    {"线网密度":0.071,"街道名称":"香蜜湖"},
    {"线网密度":0.055,"街道名称":"玉塘"},
    {"线网密度":0.028,"街道名称":"松岗"},
    {"线网密度":0,"街道名称":"盐田"},
    {"线网密度":0,"街道名称":"园山"},
    {"线网密度":0,"街道名称":"南湾"},
    {"线网密度":0,"街道名称":"碧岭"},
    {"线网密度":0,"街道名称":"石井"},
    {"线网密度":0,"街道名称":"龙田"},
    {"线网密度":0,"街道名称":"坑梓"},
    {"线网密度":0,"街道名称":"坪山"},
    {"线网密度":0,"街道名称":"马峦"},
    {"线网密度":0,"街道名称":"南澳"},
    {"线网密度":0,"街道名称":"大鹏"},
    {"线网密度":0,"街道名称":"葵涌"}
])
block_density_dict = dict(zip(block_density['街道名称'],block_density['线网密度']))
area_gdf = gpd.read_file(r'G:\DeskTop\11_JupyterLabTest\dash_learning\入门\sz_group.geojson')
line_gdf = gpd.read_file(r'G:\DeskTop\11_JupyterLabTest\dash_learning\入门\sz_metro_line.geojson')
area_gdf['density'] = area_gdf['NAME'].apply(lambda x:block_density_dict[x])
map_2 = KeplerGl()
map_2.add_data(data=line_gdf, name='line')
map_2.add_data(data=area_gdf, name='block')
config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "w50aqdd",
          "type": "geojson",
          "config": {
            "dataId": "line",
            "label": "line",
            "color": [
              34,
              63,
              154
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.9,
              "strokeColor": None,
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "ColorBrewer Paired-9",
                "type": "qualitative",
                "category": "ColorBrewer",
                "colors": [
                  "#a6cee3",
                  "#1f78b4",
                  "#b2df8a",
                  "#33a02c",
                  "#fb9a99",
                  "#e31a1c",
                  "#fdbf6f",
                  "#ff7f00",
                  "#cab2d6"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": False,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": {
              "name": "route_name",
              "type": "string"
            },
            "strokeColorScale": "ordinal",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "h3m5ah2",
          "type": "geojson",
          "config": {
            "dataId": "block",
            "label": "block",
            "color": [
              26,
              49,
              119
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.64,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                32,
                103,
                172
              ],
              "colorRange": {
                "name": "Uber Viz Diverging 3.5",
                "type": "diverging",
                "category": "Uber",
                "colors": [
                  "#00939C",
                  "#2FA7AE",
                  "#5DBABF",
                  "#8CCED1",
                  "#BAE1E2",
                  "#F8C0AA",
                  "#EB9C80",
                  "#DD7755",
                  "#D0532B",
                  "#C22E00"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "density",
              "type": "real"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "block": [
              {
                "name": "NAME",
                "format": None
              },
              {
                "name": "density",
                "format": None
              }
            ],
            "line": [
              {
                "name": "link_type",
                "format": None
              },
              {
                "name": "route_name",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 22.662742768390604,
      "longitude": 114.21157724223173,
      "pitch": 0,
      "zoom": 8.903882166166095,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}
map_2.config=config
map_2


# ## 1.3    站点覆盖率
# 
# &emsp;&emsp;至2020底，按轨道站点按800米服务半径进行计算的交通小区轨道站点服务面积覆盖率指标如下图所示。交通小区的面积包括总用地面积和建设用地面积两个统计口径，此处在计算服务面积覆盖率时使用的是交通小区的建设用地面积（扣除绿地、山地、湖泊等）。

# In[ ]:





# <center style='color:red;'> 图 7 深圳市轨道站点覆盖率指标 </center>

# &emsp;&emsp;按全市计算，深圳轨道站点800米的面积覆盖率从2020年初的21.6%增长为28.3%，人口与岗位覆盖率分别从37.1%、37.2%增长至45.0%、44.4%。其中，福田的轨道站点覆盖率最高，面积覆盖率为89.8%，人口与岗位覆盖率达96.3%和95.3%。

# In[7]:


district_station_cover = pd.DataFrame([
    {"行政区名称":"罗湖","面积覆盖率":0.771,"人口覆盖率":0.898,"岗位覆盖率":0.92},
    {"行政区名称":"福田","面积覆盖率":0.898,"人口覆盖率":0.963,"岗位覆盖率":0.953},
    {"行政区名称":"南山","面积覆盖率":0.573,"人口覆盖率":0.701,"岗位覆盖率":0.711},
    {"行政区名称":"盐田","面积覆盖率":0.268,"人口覆盖率":0.561,"岗位覆盖率":0.553},
    {"行政区名称":"宝安","面积覆盖率":0.178,"人口覆盖率":0.244,"岗位覆盖率":0.223},
    {"行政区名称":"龙岗","面积覆盖率":0.25,"人口覆盖率":0.389,"岗位覆盖率":0.344},
    {"行政区名称":"光明","面积覆盖率":0.194,"人口覆盖率":0.243,"岗位覆盖率":0.225},
    {"行政区名称":"坪山","面积覆盖率":0,"人口覆盖率":0,"岗位覆盖率":0},
    {"行政区名称":"龙华","面积覆盖率":0.301,"人口覆盖率":0.38,"岗位覆盖率":0.306},
    {"行政区名称":"大鹏","面积覆盖率":0,"人口覆盖率":0,"岗位覆盖率":0}
])
import plotly.graph_objects as go
districts=district_station_cover['行政区名称'].tolist()

fig = go.Figure(data=[
    go.Bar(name='面积覆盖率', x=districts, y=district_station_cover['面积覆盖率'].tolist()),
    go.Bar(name='人口覆盖率', x=districts, y=district_station_cover['人口覆盖率'].tolist()),
    go.Bar(name='岗位覆盖率', x=districts, y=district_station_cover['岗位覆盖率'].tolist())
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()


# &emsp;&emsp;各街道的轨道人口与岗位覆盖率分布如下图所示，主要集中在南湖、华强北、园岭、东门、福田一带街道。

# ```{admonition} important!
# 1.    深圳市轨道站点主要分布在中心城区的福田、罗湖以及南山，中心城区的人口与岗位覆盖率达84.7%，高于规划目标50%（参考《GBT 51328-2018城市综合交通体系规划标准》，中心城区人口规模在500至1000万人之间，轨道站点800米服务范围的人口与岗位覆盖目标不低于50%）。
# 2.    关外地区宝安区、龙岗区和龙华区仅有部分地区有轨道线路覆盖，人口与岗位覆盖率不足20%，轨道交通发展相对滞后。
# ```

# In[8]:


# import arrow as ar
import numpy as np
import pandas as pd
import json
from textwrap import dedent as d
import plotly.graph_objs as go
import dash
import dash_core_components as dcc                  # 交互式组件
import dash_html_components as html                 # 代码转html
from dash.dependencies import Input, Output, State  # 回调
from jupyter_plotly_dash import JupyterDash         # Jupyter中的Dash
import ipywidgets as widgets                        # Jupyter的滑动条插件


# In[9]:


app = JupyterDash('dropdown01', height = 150)
app.layout = html.Div([
    dcc.Dropdown(
        id = 'my_dropdown',
        options = [{'label': '北京', 'value': '北京'}, 
                   {'label': '上海', 'value': '上海', 'disabled': True}, 
                   {'label': '深圳', 'value': '深圳'}],
        value = '北京'),
    html.Div(id = 'output-01')
])

@app.callback(Output('output-01', 'children'), [Input('my_dropdown', 'value')])
def update_output(value):
    return f"您已经选择：【{value}】"

app


# In[ ]:




