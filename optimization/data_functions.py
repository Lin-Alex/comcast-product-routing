import pandas as pd
import numpy as np

#DATA
po_dict = {('CBR', 0, 1, 2020): [4896], ('CBR', 0, 3, 2020): [576], ('CBR', 0, 4, 2020): [1152], ('CBR', 0, 5, 2020): [1728], ('CBR', 0, 6, 2020): [6336], ('CBR', 0, 7, 2020): [4752], ('CBR', 0, 9, 2020): [2304], ('CBR', 0, 10, 2020): [1728], ('CBR', 0, 11, 2020): [4176], ('CBR', 0, 12, 2020): [2016], ('CBR', 1, 3, 2020): [576], ('CBR', 1, 4, 2020): [1152], ('CBR', 1, 5, 2020): [1152], ('CBR', 1, 6, 2020): [2016], ('CBR', 1, 7, 2020): [3888], ('CBR', 1, 8, 2020): [3024], ('CBR', 1, 9, 2020): [2304], ('CBR', 1, 10, 2020): [5472], ('CBR', 1, 11, 2020): [2880], ('CBR', 1, 12, 2020): [4032], ('CBR', 2, 3, 2020): [1872], ('CBR', 2, 4, 2020): [1152], ('CBR', 2, 5, 2020): [1152], ('CBR', 2, 6, 2020): [1872], ('CBR', 2, 7, 2020): [4464], ('CBR', 2, 8, 2020): [5616], ('CBR', 2, 9, 2020): [3312], ('CBR', 2, 10, 2020): [4464], ('CBR', 2, 11, 2020): [6192], ('CBR', 2, 12, 2020): [4032], ('CBR', 3, 1, 2020): [1872], ('CBR', 3, 3, 2020): [1440], ('CBR', 3, 4, 2020): [2160], ('CBR', 3, 5, 2020): [2880], ('CBR', 3, 6, 2020): [2016], ('CBR', 3, 7, 2020): [3168], ('CBR', 3, 8, 2020): [2880], ('CBR', 3, 10, 2020): [1728], ('CBR', 3, 11, 2020): [4608], ('CBR', 3, 12, 2020): [1008], ('CBR', 4, 1, 2020): [2304], ('CBR', 4, 3, 2020): [432], ('CBR', 4, 4, 2020): [1584], ('CBR', 4, 5, 2020): [1152], ('CBR', 4, 6, 2020): [2880], ('CBR', 4, 7, 2020): [2304], ('CBR', 4, 9, 2020): [1728], ('CBR', 4, 10, 2020): [864], ('CBR', 4, 11, 2020): [2016], ('CBR', 4, 12, 2020): [1152], ('CBR', 5, 1, 2020): [5184], ('CBR', 5, 3, 2020): [432], ('CBR', 5, 4, 2020): [2160], ('CBR', 5, 5, 2020): [2304], ('CBR', 5, 6, 2020): [5472], ('CBR', 5, 7, 2020): [2880], ('CBR', 5, 9, 2020): [1584], ('CBR', 5, 10, 2020): [1440], ('CBR', 5, 11, 2020): [3456], ('CBR', 5, 12, 2020): [1728], ('CBR', 6, 3, 2020): [432], ('CBR', 6, 4, 2020): [2304], ('CBR', 6, 5, 2020): [720], ('CBR', 6, 6, 2020): [2160], ('CBR', 6, 7, 2020): [3744], ('CBR', 6, 8, 2020): [5328], ('CBR', 6, 9, 2020): [2880], ('CBR', 6, 10, 2020): [3168], ('CBR', 6, 11, 2020): [6048], ('CBR', 6, 12, 2020): [4032], ('CBR', 7, 1, 2020): [3312], ('CBR', 7, 3, 2020): [576], ('CBR', 7, 4, 2020): [1152], ('CBR', 7, 5, 2020): [864], ('CBR', 7, 6, 2020): [3456], ('CBR', 7, 7, 2020): [2160], ('CBR', 7, 9, 2020): [1872], ('CBR', 7, 10, 2020): [1008], ('CBR', 7, 11, 2020): [2448], ('CBR', 7, 12, 2020): [1152], ('CBR', 8, 1, 2020): [4320], ('CBR', 8, 3, 2020): [2880], ('CBR', 8, 4, 2020): [5328], ('CBR', 8, 5, 2020): [6192], ('CBR', 8, 6, 2020): [4032], ('CBR', 8, 7, 2020): [8928], ('CBR', 8, 9, 2020): [6480], ('CBR', 8, 10, 2020): [4320], ('CBR', 8, 11, 2020): [7488], ('CBR', 8, 12, 2020): [5040], ('XB6', 0, 2, 2019): [57344], ('XB6', 0, 3, 2019): [43008], ('XB6', 0, 4, 2019): [21504], ('XB6', 0, 6, 2019): [26692], ('XB6', 0, 7, 2019): [17408], ('XB6', 0, 7, 2020): [1440], ('XB6', 0, 8, 2019): [40320], ('XB6', 0, 8, 2020): [8640], ('XB6', 0, 9, 2019): [49238], ('XB6', 0, 9, 2020): [19152], ('XB6', 0, 10, 2019): [28672], ('XB6', 0, 10, 2020): [11376], ('XB6', 0, 11, 2019): [48384], ('XB6', 0, 12, 2019): [24192], ('XB6', 0, 12, 2020): [8640], ('XB6', 1, 1, 2019): [5120], ('XB6', 1, 2, 2019): [43008], ('XB6', 1, 3, 2019): [43008], ('XB6', 1, 4, 2019): [28672], ('XB6', 1, 5, 2019): [14336], ('XB6', 1, 6, 2019): [52864], ('XB6', 1, 7, 2019): [14336], ('XB6', 1, 7, 2020): [3888], ('XB6', 1, 8, 2019): [43064], ('XB6', 1, 8, 2020): [7632], ('XB6', 1, 9, 2019): [57344], ('XB6', 1, 9, 2020): [16848], ('XB6', 1, 10, 2019): [7168], ('XB6', 1, 10, 2020): [20736], ('XB6', 1, 11, 2019): [16128], ('XB6', 1, 11, 2020): [34560], ('XB6', 2, 1, 2019): [5120], ('XB6', 2, 2, 2019): [43008], ('XB6', 2, 3, 2019): [43008], ('XB6', 2, 4, 2019): [28672], ('XB6', 2, 5, 2019): [28672], ('XB6', 2, 6, 2019): [86656], ('XB6', 2, 7, 2019): [14336], ('XB6', 2, 7, 2020): [9792], ('XB6', 2, 8, 2019): [31376], ('XB6', 2, 8, 2020): [11088], ('XB6', 2, 9, 2019): [86730], ('XB6', 2, 9, 2020): [16848], ('XB6', 2, 10, 2019): [14336], ('XB6', 2, 10, 2020): [31104], ('XB6', 2, 11, 2019): [24192], ('XB6', 2, 11, 2020): [34560], ('XB6', 2, 12, 2019): [64386], ('XB6', 2, 12, 2020): [34560], ('XB6', 3, 1, 2019): [40960], ('XB6', 3, 3, 2019): [33280], ('XB6', 3, 4, 2019): [28672], ('XB6', 3, 5, 2019): [37632], ('XB6', 3, 6, 2019): [52736], ('XB6', 3, 7, 2019): [49664], ('XB6', 3, 7, 2020): [7920], ('XB6', 3, 8, 2019): [50578], ('XB6', 3, 8, 2020): [13104], ('XB6', 3, 9, 2019): [52736], ('XB6', 3, 9, 2020): [20592], ('XB6', 3, 10, 2019): [38400], ('XB6', 3, 11, 2019): [48384], ('XB6', 3, 11, 2020): [12096], ('XB6', 3, 12, 2020): [8640], ('XB6', 4, 2, 2019): [14336], ('XB6', 4, 3, 2019): [32000], ('XB6', 4, 6, 2019): [29210], ('XB6', 4, 7, 2019): [8704], ('XB6', 4, 7, 2020): [2880], ('XB6', 4, 8, 2020): [4896], ('XB6', 4, 9, 2019): [38528], ('XB6', 4, 9, 2020): [10800], ('XB6', 4, 10, 2019): [14336], ('XB6', 4, 10, 2020): [5184], ('XB6', 4, 11, 2019): [16128], ('XB6', 4, 12, 2019): [10206], ('XB6', 4, 12, 2020): [8640], ('XB6', 5, 2, 2019): [43008], ('XB6', 5, 3, 2019): [57344], ('XB6', 5, 4, 2019): [23808], ('XB6', 5, 6, 2019): [53024], ('XB6', 5, 7, 2019): [18176], ('XB6', 5, 7, 2020): [6624], ('XB6', 5, 8, 2019): [44352], ('XB6', 5, 8, 2020): [13248], ('XB6', 5, 9, 2019): [56798], ('XB6', 5, 9, 2020): [28224], ('XB6', 5, 10, 2019): [28672], ('XB6', 5, 10, 2020): [13968], ('XB6', 5, 11, 2019): [32256], ('XB6', 5, 12, 2019): [16128], ('XB6', 5, 12, 2020): [43200], ('XB6', 6, 1, 2019): [5120], ('XB6', 6, 2, 2019): [57344], ('XB6', 6, 3, 2019): [28672], ('XB6', 6, 4, 2019): [28672], ('XB6', 6, 5, 2019): [14336], ('XB6', 6, 6, 2019): [34560], ('XB6', 6, 7, 2019): [14336], ('XB6', 6, 7, 2020): [5472], ('XB6', 6, 8, 2019): [36664], ('XB6', 6, 8, 2020): [9216], ('XB6', 6, 9, 2019): [59136], ('XB6', 6, 9, 2020): [16704], ('XB6', 6, 10, 2019): [7424], ('XB6', 6, 10, 2020): [17280], ('XB6', 6, 11, 2019): [24192], ('XB6', 6, 11, 2020): [34560], ('XB6', 6, 12, 2020): [25920], ('XB6', 7, 2, 2019): [43008], ('XB6', 7, 3, 2019): [43008], ('XB6', 7, 4, 2019): [35328], ('XB6', 7, 6, 2019): [34466], ('XB6', 7, 7, 2019): [16896], ('XB6', 7, 7, 2020): [5472], ('XB6', 7, 8, 2019): [44352], ('XB6', 7, 8, 2020): [13968], ('XB6', 7, 9, 2019): [65492], ('XB6', 7, 9, 2020): [24624], ('XB6', 7, 10, 2019): [36096], ('XB6', 7, 10, 2020): [13104], ('XB6', 7, 11, 2019): [72576], ('XB6', 7, 12, 2020): [34560], ('XB6', 8, 1, 2019): [40960], ('XB6', 8, 2, 2019): [40960], ('XB6', 8, 3, 2019): [124416], ('XB6', 8, 4, 2019): [37376], ('XB6', 8, 5, 2019): [48384], ('XB6', 8, 6, 2019): [139008], ('XB6', 8, 7, 2019): [36352], ('XB6', 8, 7, 2020): [11088], ('XB6', 8, 8, 2019): [33584], ('XB6', 8, 8, 2020): [48096], ('XB6', 8, 9, 2019): [93184], ('XB6', 8, 9, 2020): [44208], ('XB6', 8, 10, 2019): [64256], ('XB6', 8, 10, 2020): [51840], ('XB6', 8, 11, 2019): [80640], ('XB6', 8, 11, 2020): [13824], ('XB6', 8, 12, 2019): [48384], ('XB6', 8, 12, 2020): [40320], ('XB6', 9, 3, 2020): [733], ('XB6', 9, 8, 2019): [9022], ('XB6', 9, 9, 2019): [8192], ('XB6', 9, 10, 2019): [4608], ('XB7', 0, 3, 2020): [2816], ('XB7', 0, 4, 2020): [15872], ('XB7', 0, 5, 2020): [11264], ('XB7', 0, 6, 2020): [27392], ('XB7', 0, 7, 2020): [28416], ('XB7', 0, 8, 2020): [19712], ('XB7', 0, 9, 2020): [34048], ('XB7', 0, 10, 2020): [18432], ('XB7', 0, 11, 2020): [12288], ('XB7', 0, 12, 2020): [19712], ('XB7', 1, 3, 2020): [11520], ('XB7', 1, 4, 2020): [18944], ('XB7', 1, 5, 2020): [11520], ('XB7', 1, 6, 2020): [8704], ('XB7', 1, 7, 2020): [21504], ('XB7', 1, 8, 2020): [16640], ('XB7', 1, 9, 2020): [17152], ('XB7', 1, 10, 2020): [29440], ('XB7', 1, 11, 2020): [14336], ('XB7', 1, 12, 2020): [28672], ('XB7', 2, 3, 2020): [11520], ('XB7', 2, 4, 2020): [14848], ('XB7', 2, 5, 2020): [18688], ('XB7', 2, 6, 2020): [37632], ('XB7', 2, 7, 2020): [37120], ('XB7', 2, 8, 2020): [27136], ('XB7', 2, 9, 2020): [18432], ('XB7', 2, 10, 2020): [43008], ('XB7', 2, 11, 2020): [57344], ('XB7', 2, 12, 2019): [4352], ('XB7', 2, 12, 2020): [43008], ('XB7', 3, 2, 2020): [4608], ('XB7', 3, 3, 2020): [2048], ('XB7', 3, 4, 2020): [9216], ('XB7', 3, 5, 2020): [12544], ('XB7', 3, 6, 2020): [50176], ('XB7', 3, 7, 2020): [28672], ('XB7', 3, 8, 2020): [18432], ('XB7', 3, 9, 2020): [19200], ('XB7', 3, 10, 2020): [12800], ('XB7', 3, 11, 2020): [16384], ('XB7', 3, 12, 2019): [8192], ('XB7', 3, 12, 2020): [14336], ('XB7', 4, 3, 2020): [1280], ('XB7', 4, 4, 2020): [7680], ('XB7', 4, 5, 2020): [9216], ('XB7', 4, 6, 2020): [14336], ('XB7', 4, 7, 2020): [17920], ('XB7', 4, 8, 2020): [11264], ('XB7', 4, 9, 2020): [17408], ('XB7', 4, 10, 2020): [5376], ('XB7', 4, 11, 2020): [5119], ('XB7', 4, 12, 2020): [10240], ('XB7', 5, 3, 2020): [3328], ('XB7', 5, 4, 2020): [16128], ('XB7', 5, 5, 2020): [21504], ('XB7', 5, 6, 2020): [32000], ('XB7', 5, 7, 2020): [45824], ('XB7', 5, 8, 2020): [30464], ('XB7', 5, 9, 2020): [48384], ('XB7', 5, 10, 2020): [24064], ('XB7', 5, 11, 2020): [17152], ('XB7', 5, 12, 2019): [8192], ('XB7', 5, 12, 2020): [32000], ('XB7', 6, 3, 2020): [2560], ('XB7', 6, 4, 2020): [14848], ('XB7', 6, 5, 2020): [11776], ('XB7', 6, 6, 2020): [30720], ('XB7', 6, 7, 2020): [22272], ('XB7', 6, 8, 2020): [22784], ('XB7', 6, 9, 2020): [17152], ('XB7', 6, 10, 2020): [29440], ('XB7', 6, 12, 2019): [3840], ('XB7', 6, 12, 2020): [28672], ('XB7', 7, 3, 2020): [2816], ('XB7', 7, 4, 2020): [11520], ('XB7', 7, 5, 2020): [13056], ('XB7', 7, 6, 2020): [30720], ('XB7', 7, 7, 2020): [37376], ('XB7', 7, 8, 2020): [25600], ('XB7', 7, 9, 2020): [41472], ('XB7', 7, 10, 2020): [22528], ('XB7', 7, 11, 2020): [15872], ('XB7', 7, 12, 2020): [24064], ('XB7', 8, 2, 2020): [8192], ('XB7', 8, 3, 2020): [5632], ('XB7', 8, 4, 2020): [18944], ('XB7', 8, 5, 2020): [51456], ('XB7', 8, 6, 2020): [64512], ('XB7', 8, 7, 2020): [22784], ('XB7', 8, 8, 2020): [45568], ('XB7', 8, 9, 2020): [67840], ('XB7', 8, 10, 2020): [58880], ('XB7', 8, 11, 2020): [12288], ('XB7', 8, 12, 2020): [57344], ('XB7', 9, 9, 2019): [704], ('XB7', 9, 11, 2019): [2272], ('Xi6', 0, 1, 2020): [15424], ('Xi6', 0, 2, 2020): [16192], ('Xi6', 0, 3, 2020): [17984], ('Xi6', 0, 4, 2020): [24192], ('Xi6', 0, 5, 2020): [30400], ('Xi6', 0, 6, 2020): [45888], ('Xi6', 0, 7, 2019): [14976], ('Xi6', 0, 7, 2020): [23680], ('Xi6', 0, 8, 2019): [5760], ('Xi6', 0, 8, 2020): [41152], ('Xi6', 0, 9, 2019): [6592], ('Xi6', 0, 9, 2020): [29888], ('Xi6', 0, 10, 2019): [2880], ('Xi6', 0, 10, 2020): [12480], ('Xi6', 0, 11, 2019): [6656], ('Xi6', 0, 12, 2019): [12736], ('Xi6', 0, 12, 2020): [18240], ('Xi6', 1, 1, 2020): [38720], ('Xi6', 1, 2, 2020): [19968], ('Xi6', 1, 3, 2019): [5760], ('Xi6', 1, 3, 2020): [26240], ('Xi6', 1, 4, 2020): [37440], ('Xi6', 1, 5, 2020): [38400], ('Xi6', 1, 6, 2019): [6720], ('Xi6', 1, 6, 2020): [73216], ('Xi6', 1, 7, 2019): [24960], ('Xi6', 1, 7, 2020): [81344], ('Xi6', 1, 8, 2019): [19200], ('Xi6', 1, 8, 2020): [88448], ('Xi6', 1, 9, 2019): [22080], ('Xi6', 1, 9, 2020): [35200], ('Xi6', 1, 10, 2019): [25792], ('Xi6', 1, 10, 2020): [23040], ('Xi6', 1, 11, 2019): [38272], ('Xi6', 1, 11, 2020): [9600], ('Xi6', 1, 12, 2019): [7488], ('Xi6', 1, 12, 2020): [21632], ('Xi6', 2, 1, 2020): [37888], ('Xi6', 2, 2, 2020): [55360], ('Xi6', 2, 3, 2020): [27072], ('Xi6', 2, 4, 2019): [6000], ('Xi6', 2, 4, 2020): [46336], ('Xi6', 2, 5, 2020): [67008], ('Xi6', 2, 6, 2019): [8640], ('Xi6', 2, 6, 2020): [102336], ('Xi6', 2, 7, 2019): [32448], ('Xi6', 2, 7, 2020): [73984], ('Xi6', 2, 8, 2019): [14400], ('Xi6', 2, 8, 2020): [136256], ('Xi6', 2, 9, 2019): [26880], ('Xi6', 2, 9, 2020): [66496], ('Xi6', 2, 10, 2019): [20096], ('Xi6', 2, 10, 2020): [44160], ('Xi6', 2, 11, 2019): [56576], ('Xi6', 2, 11, 2020): [22080], ('Xi6', 2, 12, 2019): [7488], ('Xi6', 2, 12, 2020): [23296], ('Xi6', 3, 1, 2020): [16576], ('Xi6', 3, 2, 2020): [21184], ('Xi6', 3, 3, 2020): [16576], ('Xi6', 3, 4, 2020): [14144], ('Xi6', 3, 5, 2020): [14080], ('Xi6', 3, 6, 2020): [32640], ('Xi6', 3, 7, 2019): [11456], ('Xi6', 3, 7, 2020): [15296], ('Xi6', 3, 8, 2019): [8320], ('Xi6', 3, 8, 2020): [20096], ('Xi6', 3, 9, 2019): [7680], ('Xi6', 3, 9, 2020): [43840], ('Xi6', 3, 10, 2019): [1920], ('Xi6', 3, 10, 2020): [4800], ('Xi6', 3, 12, 2019): [14656], ('Xi6', 4, 1, 2020): [10752], ('Xi6', 4, 2, 2020): [12032], ('Xi6', 4, 3, 2020): [13696], ('Xi6', 4, 4, 2020): [13696], ('Xi6', 4, 5, 2020): [22656], ('Xi6', 4, 6, 2020): [41728], ('Xi6', 4, 7, 2019): [10816], ('Xi6', 4, 7, 2020): [21888], ('Xi6', 4, 8, 2019): [4800], ('Xi6', 4, 8, 2020): [30528], ('Xi6', 4, 9, 2019): [6592], ('Xi6', 4, 9, 2020): [23296], ('Xi6', 4, 10, 2019): [1920], ('Xi6', 4, 10, 2020): [10560], ('Xi6', 4, 11, 2019): [5824], ('Xi6', 4, 12, 2019): [9408], ('Xi6', 4, 12, 2020): [13440], ('Xi6', 5, 1, 2020): [35136], ('Xi6', 5, 2, 2020): [51840], ('Xi6', 5, 3, 2020): [44096], ('Xi6', 5, 4, 2020): [33152], ('Xi6', 5, 5, 2019): [13440], ('Xi6', 5, 5, 2020): [61056], ('Xi6', 5, 6, 2020): [100992], ('Xi6', 5, 7, 2019): [13312], ('Xi6', 5, 7, 2020): [66944], ('Xi6', 5, 8, 2019): [5760], ('Xi6', 5, 8, 2020): [99200], ('Xi6', 5, 9, 2019): [12096], ('Xi6', 5, 9, 2020): [86400], ('Xi6', 5, 10, 2019): [12864], ('Xi6', 5, 10, 2020): [48960], ('Xi6', 5, 11, 2019): [30784], ('Xi6', 5, 12, 2019): [32640], ('Xi6', 5, 12, 2020): [92544], ('Xi6', 6, 1, 2020): [47488], ('Xi6', 6, 2, 2020): [30400], ('Xi6', 6, 3, 2020): [12480], ('Xi6', 6, 4, 2020): [28288], ('Xi6', 6, 5, 2020): [35776], ('Xi6', 6, 6, 2019): [38400], ('Xi6', 6, 6, 2020): [72384], ('Xi6', 6, 7, 2019): [23296], ('Xi6', 6, 7, 2020): [69824], ('Xi6', 6, 8, 2019): [4800], ('Xi6', 6, 8, 2020): [109632], ('Xi6', 6, 9, 2019): [30208], ('Xi6', 6, 9, 2020): [77056], ('Xi6', 6, 10, 2019): [12480], ('Xi6', 6, 10, 2020): [23040], ('Xi6', 6, 11, 2019): [31616], ('Xi6', 6, 11, 2020): [6720], ('Xi6', 6, 12, 2019): [8320], ('Xi6', 6, 12, 2020): [21632], ('Xi6', 7, 1, 2020): [37888], ('Xi6', 7, 2, 2020): [57344], ('Xi6', 7, 3, 2020): [72512], ('Xi6', 7, 4, 2020): [24320], ('Xi6', 7, 5, 2020): [59136], ('Xi6', 7, 6, 2020): [106368], ('Xi6', 7, 7, 2019): [9984], ('Xi6', 7, 7, 2020): [39488], ('Xi6', 7, 8, 2019): [2880], ('Xi6', 7, 8, 2020): [72768], ('Xi6', 7, 9, 2019): [25408], ('Xi6', 7, 9, 2020): [76416], ('Xi6', 7, 10, 2019): [26880], ('Xi6', 7, 10, 2020): [52800], ('Xi6', 7, 11, 2019): [29120], ('Xi6', 7, 12, 2019): [32640], ('Xi6', 7, 12, 2020): [71616], ('Xi6', 8, 1, 2020): [35904], ('Xi6', 8, 2, 2020): [71232], ('Xi6', 8, 3, 2020): [39232], ('Xi6', 8, 4, 2020): [34112], ('Xi6', 8, 5, 2020): [51328], ('Xi6', 8, 6, 2020): [163904], ('Xi6', 8, 7, 2019): [22208], ('Xi6', 8, 7, 2020): [69312], ('Xi6', 8, 8, 2019): [7488], ('Xi6', 8, 8, 2020): [132864], ('Xi6', 8, 9, 2020): [109568], ('Xi6', 8, 10, 2019): [7680], ('Xi6', 8, 10, 2020): [39360], ('Xi6', 8, 11, 2019): [52416], ('Xi6', 8, 11, 2020): [19200], ('Xi6', 8, 12, 2019): [61952], ('Xi6', 8, 12, 2020): [28288], ('Xi6', 9, 3, 2019): [960], ('Xi6', 9, 7, 2019): [5824], ('Xi6', 9, 8, 2019): [5824]}

pallet_quantity = dict([('Technicolor Xi6', 960), ('Sercomm XiOne', 1024), ('CommScope XB7', 144), ('Technicolor XB7', 256), ('Technicolor CBR', 144)])
#estimated XiOne weight based on 0.5875 device weight * 1024 (pallet quantity)
pallet_weight = dict([('Technicolor Xi6', 870), ('Sercomm XiOne', 601), ('CommScope XB7', 503), ('Technicolor XB7', 660), ('Technicolor CBR', 465)])

#forecast_dict = 

truckingCost_dict = {('Seattle', 7): [685.0, 0.17, 0.0, 0.19], ('Seattle', 0): [1850.0, 0.21, 2050.0, 0.23], ('Seattle', 5): [3850.0, 0.21, 4285.0, 0.23], ('Seattle', 2): [4850.0, 0.26, 5790.0, 0.28], ('Seattle', 6): [5565.0, 0.3, 6655.0, 0.32], ('Seattle', 4): [5595.0, 0.26, 6650.0, 0.28], ('Seattle', 1): [6990.0, 0.32, 8215.0, 0.34], ('Seattle', 8): [6970.0, 0.3, 7810.0, 0.32], ('Seattle', 3): [7540.0, 0.32, 8540.0, 0.34], ('Long Beach', 7): [4300.0, 0.17, 4600.0, 0.19], ('Long Beach', 0): [1700.0, 0.21, 0.0, 0.23], ('Long Beach', 5): [5500.0, 0.21, 5800.0, 0.23], ('Long Beach', 2): [6600.0, 0.26, 7100.0, 0.28], ('Long Beach', 6): [7100.0, 0.3, 7600.0, 0.32], ('Long Beach', 4): [5500.0, 0.26, 5900.0, 0.28], ('Long Beach', 1): [8800.0, 0.3, 9400.0, 0.34], ('Long Beach', 8): [9500.0, 0.3, 10000.0, 0.32], ('Long Beach', 3): [9800.0, 0.32, 10600.0, 0.34], ('Miami', 7): [6900.0, 0.3, 7800.0, 0.32], ('Miami', 0): [6100.0, 0.32, 6900.0, 0.34], ('Miami', 5): [4900.0, 0.3, 5500.0, 0.32], ('Miami', 2): [3400.0, 0.26, 3700.0, 0.28], ('Miami', 6): [1900.0, 0.17, 2100.0, 0.19], ('Miami', 4): [2400.0, 0.26, 2700.0, 0.28], ('Miami', 1): [800.0, 0.17, 0.0, 0.19], ('Miami', 8): [3100.0, 0.26, 3400.0, 0.28], ('Miami', 3): [3800.0, 0.3, 4200.0, 0.32], ('Everglades', 7): [6900.0, 0.3, 7800.0, 0.32], ('Fort Lauderdale', 0): [6100.0, 0.32, 6900.0, 0.34], ('Fort Lauderdale', 5): [4900.0, 0.3, 5500.0, 0.32], ('Fort Lauderdale', 2): [3400.0, 0.26, 3700.0, 0.28], ('Fort Lauderdale', 6): [1900.0, 0.17, 2100.0, 0.19], ('Fort Lauderdale', 4): [2400.0, 0.26, 2700.0, 0.28], ('Fort Lauderdale', 1): [800.0, 0.17, 0.0, 0.19], ('Fort Lauderdale', 8): [3100.0, 0.26, 3400.0, 0.28], ('Fort Lauderdale', 3): [3800.0, 0.3, 4200.0, 0.32], ('Palm Beach', 7): [6900.0, 0.3, 7800.0, 0.32], ('Palm Beach', 0): [6100.0, 0.32, 6900.0, 0.34], ('Palm Beach', 5): [4900.0, 0.3, 5500.0, 0.32], ('Palm Beach', 2): [3400.0, 0.26, 3700.0, 0.28], ('Palm Beach', 6): [1900.0, 0.17, 2100.0, 0.19], ('Palm Beach', 4): [2400.0, 0.26, 2700.0, 0.28], ('Palm Beach', 1): [800.0, 0.17, 0.0, 0.19], ('Palm Beach', 8): [3100.0, 0.26, 3400.0, 0.28], ('Palm Beach', 3): [3800.0, 0.3, 4200.0, 0.32], ('Jacksonville', 7): [6600.0, 0.3, 7400.0, 0.32], ('Jacksonville', 0): [5500.0, 0.32, 6100.0, 0.34], ('Jacksonville', 5): [4600.0, 0.3, 5100.0, 0.32], ('Jacksonville', 2): [2700.0, 0.26, 3000.0, 0.28], ('Jacksonville', 6): [1700.0, 0.17, 1900.0, 0.19], ('Jacksonville', 4): [2300.0, 0.26, 2600.0, 0.28], ('Jacksonville', 1): [900.0, 0.17, 0.0, 0.19], ('Jacksonville', 8): [3000.0, 0.26, 3300.0, 0.28], ('Jacksonville', 3): [4100.0, 0.3, 4400.0, 0.32], ('Savannah', 7): [6900.0, 0.3, 7600.0, 0.32], ('Savannah', 0): [5400.0, 0.3, 6000.0, 0.32], ('Savannah', 5): [5000.0, 0.26, 5400.0, 0.28], ('Savannah', 2): [2800.0, 0.21, 3000.0, 0.23], ('Savannah', 6): [1900.0, 0.17, 2200.0, 0.19], ('Savannah', 4): [2700.0, 0.21, 3000.0, 0.23], ('Savannah', 1): [1600.0, 0.17, 0.0, 0.19], ('Savannah', 8): [2800.0, 0.26, 3000.0, 0.28], ('Savannah', 3): [3800.0, 0.3, 4100.0, 0.32], ('Charleston', 7): [7100.0, 0.3, 7700.0, 0.32], ('Charleston', 0): [5500.0, 0.3, 6200.0, 0.32], ('Charleston', 5): [5100.0, 0.26, 5500.0, 0.28], ('Charleston', 2): [2800.0, 0.21, 3000.0, 0.23], ('Charleston', 6): [1900.0, 0.17, 2100.0, 0.19], ('Charleston', 4): [2900.0, 0.21, 3200.0, 0.23], ('Charleston', 1): [1900.0, 0.17, 2100.0, 0.19], ('Charleston', 8): [2800.0, 0.26, 3000.0, 0.28], ('Charleston', 3): [4100.0, 0.3, 4300.0, 0.32], ('Wilmington (NC)', 7): [7100.0, 0.3, 7700.0, 0.32], ('Wilmington (NC)', 0): [5500.0, 0.3, 6200.0, 0.32], ('Wilmington (NC)', 5): [5100.0, 0.26, 5500.0, 0.28], ('Wilmington (NC)', 2): [2800.0, 0.21, 3000.0, 0.23], ('Wilmington (NC)', 6): [1900.0, 0.17, 2100.0, 0.19], ('Wilmington (NC)', 4): [2900.0, 0.21, 3200.0, 0.23], ('Wilmington (NC)', 1): [1900.0, 0.17, 2100.0, 0.19], ('Wilmington (NC)', 8): [2800.0, 0.26, 3000.0, 0.28], ('Wilmington (NC)', 3): [4100.0, 0.3, 4300.0, 0.32], ('Norfolk', 7): [6900.0, 0.3, 7600.0, 0.32], ('Norfolk', 0): [5900.0, 0.3, 6600.0, 0.32], ('Norfolk', 5): [4700.0, 0.26, 5200.0, 0.28], ('Norfolk', 2): [2600.0, 0.21, 2800.0, 0.23], ('Norfolk', 6): [2100.0, 0.17, 2300.0, 0.19], ('Norfolk', 4): [3300.0, 0.21, 3600.0, 0.23], ('Norfolk', 1): [2700.0, 0.17, 2900.0, 0.19], ('Norfolk', 8): [1300.0, 0.26, 0.0, 0.28], ('Norfolk', 3): [2700.0, 0.3, 2900.0, 0.32], ('Baltimore', 7): [6100.0, 0.3, 6800.0, 0.32], ('Baltimore', 0): [5600.0, 0.3, 6300.0, 0.32], ('Baltimore', 5): [4100.0, 0.3, 4500.0, 0.32], ('Baltimore', 2): [1800.0, 0.26, 2000.0, 0.28], ('Baltimore', 6): [1800.0, 0.26, 2000.0, 0.28], ('Baltimore', 4): [2900.0, 0.3, 3300.0, 0.32], ('Baltimore', 1): [2800.0, 0.26, 3100.0, 0.28], ('Baltimore', 8): [800.0, 0.17, 0.0, 0.19], ('Baltimore', 3): [1900.0, 0.21, 0.0, 0.23], ('Wilmington, Delaware', 7): [6400.0, 0.3, 7100.0, 0.32], (nan, 0): [5700.0, 0.3, 6400.0, 0.32], (nan, 5): [4300.0, 0.3, 4800.0, 0.32], (nan, 2): [1800.0, 0.26, 2000.0, 0.28], (nan, 6): [2000.0, 0.26, 2200.0, 0.28], (nan, 4): [3100.0, 0.3, 3500.0, 0.32], (nan, 1): [3000.0, 0.26, 3400.0, 0.28], (nan, 8): [700.0, 0.17, 0.0, 0.19], (nan, 3): [1600.0, 0.21, 0.0, 0.23], ('Philadelphia', 7): [6400.0, 0.3, 7100.0, 0.32], ('Philadelphia', 0): [5700.0, 0.3, 6400.0, 0.32], ('Philadelphia', 5): [4300.0, 0.3, 4800.0, 0.32], ('Philadelphia', 2): [1800.0, 0.26, 2000.0, 0.28], ('Philadelphia', 6): [2000.0, 0.26, 2200.0, 0.28], ('Philadelphia', 4): [3100.0, 0.3, 3500.0, 0.32], ('Philadelphia', 1): [3000.0, 0.26, 3400.0, 0.28], ('Philadelphia', 8): [700.0, 0.17, 0.0, 0.19], ('Philadelphia', 3): [1600.0, 0.21, 0.0, 0.23], ('Camden', 7): [6400.0, 0.3, 7100.0, 0.32], ('Camden', 0): [5700.0, 0.3, 6400.0, 0.32], ('Camden', 5): [4300.0, 0.3, 4800.0, 0.32], ('Camden', 2): [1800.0, 0.26, 2000.0, 0.28], ('Camden', 6): [2000.0, 0.26, 2200.0, 0.28], ('Camden', 4): [3100.0, 0.3, 3500.0, 0.32], ('Camden', 1): [3000.0, 0.26, 3400.0, 0.28], ('Camden', 8): [700.0, 0.17, 0.0, 0.19], ('Camden', 3): [1600.0, 0.21, 0.0, 0.23], ('Newark', 7): [6400.0, 0.3, 7100.0, 0.32], ('Newark', 0): [5700.0, 0.3, 6400.0, 0.32], ('Newark', 5): [4300.0, 0.3, 4800.0, 0.32], ('Newark', 2): [1900.0, 0.26, 2100.0, 0.28], ('Newark', 6): [2100.0, 0.26, 2300.0, 0.28], ('Newark', 4): [3200.0, 0.3, 3600.0, 0.32], ('Newark', 1): [3100.0, 0.26, 3500.0, 0.28], ('Newark', 8): [900.0, 0.17, 0.0, 0.19], ('Newark', 3): [1300.0, 0.21, 0.0, 0.23], ('New York', 7): [6600.0, 0.3, 7300.0, 0.32], ('New York', 0): [5900.0, 0.3, 6600.0, 0.32], ('New York', 5): [4500.0, 0.3, 5000.0, 0.32], ('New York', 2): [2000.0, 0.26, 2200.0, 0.28], ('New York', 6): [2200.0, 0.26, 2400.0, 0.28], ('New York', 4): [3300.0, 0.3, 3700.0, 0.32], ('New York', 1): [3200.0, 0.26, 3600.0, 0.28], ('New York', 8): [1000.0, 0.17, 0.0, 0.19], ('New York', 3): [1800.0, 0.21, 0.0, 0.23], ('Jersey', 7): [6400.0, 0.3, 7100.0, 0.32], ('Jersey', 0): [5700.0, 0.3, 6400.0, 0.32], ('Jersey', 5): [4300.0, 0.3, 4800.0, 0.32], ('Jersey', 2): [1900.0, 0.26, 2100.0, 0.28], ('Jersey', 6): [2100.0, 0.26, 2300.0, 0.28], ('Jersey', 4): [3200.0, 0.3, 3600.0, 0.32], ('Jersey', 1): [3100.0, 0.26, 3500.0, 0.28], ('Jersey', 8): [900.0, 0.17, 0.0, 0.19], ('Jersey', 3): [1300.0, 0.21, 0.0, 0.23], ('Boston', 7): [6900.0, 0.32, 7700.0, 0.34], ('Boston', 0): [6200.0, 0.32, 7000.0, 0.34], ('Boston', 5): [4800.0, 0.32, 5400.0, 0.34], ('Boston', 2): [2000.0, 0.3, 2300.0, 0.32], ('Boston', 6): [2200.0, 0.3, 2500.0, 0.32], ('Boston', 4): [3700.0, 0.32, 4200.0, 0.34], ('Boston', 1): [3200.0, 0.3, 3600.0, 0.32], ('Boston', 8): [1100.0, 0.21, 0.0, 0.23], ('Boston', 3): [700.0, 0.17, 0.0, 0.19], ('Houston', 7): [6200.0, 0.26, 6800.0, 0.28], ('Houston', 0): [3800.0, 0.26, 4300.0, 0.28], ('Houston', 5): [3800.0, 0.21, 4100.0, 0.23], ('Houston', 2): [3000.0, 0.21, 3200.0, 0.23], ('Houston', 6): [2600.0, 0.21, 2800.0, 0.23], ('Houston', 4): [500.0, 0.17, 0.0, 0.19], ('Houston', 1): [3200.0, 0.26, 3400.0, 0.28], ('Houston', 8): [4600.0, 0.3, 5000.0, 0.32], ('Houston', 3): [6100.0, 0.32, 6600.0, 0.34], ('New Orleans', 7): [7100.0, 0.26, 7500.0, 0.28], ('New Orleans', 0): [4700.0, 0.26, 5300.0, 0.28], ('New Orleans', 5): [4300.0, 0.21, 4600.0, 0.23], ('New Orleans', 2): [2600.0, 0.21, 2900.0, 0.23], ('New Orleans', 6): [1900.0, 0.21, 2100.0, 0.23], ('New Orleans', 4): [1100.0, 0.17, 0.0, 0.19], ('New Orleans', 1): [2400.0, 0.26, 2700.0, 0.28], ('New Orleans', 8): [4300.0, 0.3, 4600.0, 0.32], ('New Orleans', 3): [5200.0, 0.32, 5600.0, 0.34], ('Gulfport', 7): [7000.0, 0.26, 7700.0, 0.28], ('Gulfport', 0): [4500.0, 0.26, 5100.0, 0.28], ('Gulfport', 5): [4000.0, 0.21, 4400.0, 0.23], ('Gulfport', 2): [2600.0, 0.21, 2900.0, 0.23], ('Gulfport', 6): [1900.0, 0.21, 2100.0, 0.23], ('Gulfport', 4): [1400.0, 0.17, 0.0, 0.19], ('Gulfport', 1): [2200.0, 0.26, 2500.0, 0.28], ('Gulfport', 8): [4200.0, 0.3, 4500.0, 0.32], ('Gulfport', 3): [5400.0, 0.32, 5800.0, 0.34], ('Mobile', 7): [6900.0, 0.26, 7600.0, 0.28], ('Mobile', 0): [4700.0, 0.26, 5300.0, 0.28], ('Mobile', 5): [4000.0, 0.21, 4400.0, 0.23], ('Mobile', 2): [2800.0, 0.21, 3100.0, 0.23], ('Mobile', 6): [1800.0, 0.21, 2000.0, 0.23], ('Mobile', 4): [1700.0, 0.17, 1800.0, 0.19], ('Mobile', 1): [1900.0, 0.26, 2100.0, 0.28], ('Mobile', 8): [3900.0, 0.3, 4200.0, 0.32], ('Mobile', 3): [5300.0, 0.32, 5700.0, 0.34]}
truckingTime_dict = {('Seattle', 7): [1.0, 1.0, 0.0, 1.0], ('Seattle', 0): [2.0, 2.0, 1.0, 1.0], ('Seattle', 4): [4.5, 4.0, 2.5, 1.0], ('Seattle', 5): [2.5, 4.0, 1.5, 3.0], ('Seattle', 2): [3.5, 4.0, 1.75, 3.0], ('Seattle', 6): [4.5, 5.0, 2.25, 3.0], ('Seattle', 1): [5.5, 7.0, 2.75, 4.0], ('Seattle', 8): [4.75, 6.0, 2.5, 3.0], ('Seattle', 3): [5.5, 6.0, 2.75, 4.0], ('Los Angeles', 7): [2.0, 2.0, 1.0, 1.0], ('Los Angeles', 0): [1.0, 1.0, 0.0, 1.0], ('Los Angeles', 4): [2.75, 4.0, 1.5, 3.0], ('Los Angeles', 5): [2.0, 4.0, 1.0, 2.0], ('Los Angeles', 2): [3.5, 4.0, 1.75, 3.0], ('Los Angeles', 6): [3.5, 4.0, 1.75, 3.0], ('Los Angeles', 1): [4.25, 6.0, 2.25, 4.0], ('Los Angeles', 8): [4.5, 6.0, 2.5, 4.0], ('Los Angeles', 3): [5.25, 6.0, 2.75, 4.0]}

#amount demanded by product p by DC d at time period t (in units)
#based on forecast data
#not sure what to count as quantity with new/old and install types
'''
def a_demand(p,d,t_month, t_year):
	if (p, d, t_month, t_year) in forecast_dict:
		return forecast_dict[p,d,t_month, t_year]
	else:
		return 0
'''
#amount of product p shipped to DC d in the past (in units), equals 0 if t!=0
#based on po data
def a_shipped(p,d,t_month, t_year):
	if (p, d, t_month, t_year) in po_dict:
		return po_dict[p,d,t_month, t_year]
	else:
		return 0

#amount of capacity in units by DC d
#assuming no more than one month's worth of demand so these numbers are double the average monthly demand over 2019-2020
def a_capacity(d):
	capacity_dict = dict([(0, 86430), (1, 104764), (2, 152538), (3, 83392), (4, 53878), (5, 141366), (6, 109860), (7, 138504), (8, 200948), (9, 10896)])
	return capacity_dict[d]

#pallets of product per FTL shipment
def a_ftl(p):
	return 52

#units of product p per full pallet
def a_pallet(p):
	return pallet_quantity[p]

#cost to transport a unit of product p to port o
#assuming 40'x8'x8.5' GP shipping container, Jared said that's what they use 99% of the time
#will need data on pallets/shipping container, made rough guess of 40 pallets/container from pallet dimension calculations
def c_overseas(p,o):
	overseas_cost = dict([('Seattle', 16197), ('Long Beach', 16547), ('Miami', 20248), ('Savannah', 18248), ('Charleston', 18248), ('Norfolk', 18248), ('New York', 18248), ('Houston', 20248)])
	return overseas_cost[o]/pallet_quantity[p]/40

#cost to transport a unit of product p via path o to d
#modes are LTL, FTL and urgency is standard, expedited
#FTL divide by 52 trucks per pallet and units per pallet
#LTL multiply by pallet weight? 
def c_trucking(p, o, d, m, u):
	if(u == 'Standard'):
		if(m=='FTL'):
			return truckingCost_dict[o, d][0]/52/pallet_quantity[p]
		else:
			return truckingCost_dict[o, d][1]*pallet_weight[p]
	else:
		if(m=='FTL'):
			return truckingCost_dict[o, d][2]/52/pallet_quantity[p]
		else:
			return truckingCost_dict[o, d][3]*pallet_weight[p]

#cost to move/transition to port o
#don't think we have this number yet ??? correct me if i'm wrong
def c_moving(o):
	return 200000

#time (days) to ship to port o
def t_sea(o):
	overseas_time = dict([('Seattle', 24), ('Long Beach', 17), ('Miami', 43), ('Savannah', 26), ('Charleston', 36), ('Norfolk', 38), ('New York', 35), ('Houston', 33)])
	return overseas_time[o]

#expected wait time (days) to process a shipment at port o
#will be based on how we pull data - currently based on jared's estimate of 7-10 days waiting
def t_congestion(o):
	congestion_time = dict([('Seattle', 10), ('Long Beach', 10), ('Miami', 10), ('Savannah', 10), ('Charleston', 10), ('Norfolk', 10), ('New York', 10), ('Houston', 10)])
	return congestion_time[o]

#time (days) to ship via path o->d via mode m and urgency u
#only have data for Long Beach and Seattle
def t_land(o, d, m, u):
	if(u == 'Standard'):
		if(m=='FTL'):
			return truckingTime_dict[o, d][0]
		else:
			return truckingTime_dict[o, d][1]
	else:
		if(m=='FTL'):
			return truckingTime_dict[o, d][2]
		else:
			return truckingTime_dict[o, d][3]
