import requests
import json
import time
import random
import numpy as np

# dictionary of locations
GuildKioskLocation = {
    0: "Belkarth",
    1: "BelkarthOutlawRefuge",
    2: "HollowCity",
    3: "HajUxith",
    4: "CourtOfContempt",
    5: "Rawlkha",
    6: "RawlkhaOutlawRefuge",
    7: "Vinedusk",
    8: "Dune",
    9: "Baandari",
    10: "Drabul",
    11: "Valeguard",
    12: "VelynHarborOutlawRefuge",
    13: "Marbruk",
    14: "MarbrukOutlawRefuge",
    15: "VerrantMorass",
    16: "Greenheart",
    17: "EldenRoot",
    18: "EldenRootOutlawRefuge",
    19: "Cormount",
    20: "Southpoint",
    21: "Skywatch",
    22: "Firsthold",
    23: "VulkhelGuard",
    24: "VulkhelGuardOutlawRefuge",
    25: "Mistral",
    26: "Evermore",
    27: "EvermoreOutlawRefuge",
    28: "BangkoraiPass",
    29: "HallinsStand",
    30: "Sentinel",
    31: "SentinelOutlawRefuge",
    32: "MorwhasBounty",
    33: "Bergama",
    34: "Shornhelm",
    35: "ShornhelmOutlawRefuge",
    36: "HoarfrostDowns",
    37: "Oldgate",
    38: "Wayrest",
    39: "WayrestOutlawRefuge",
    40: "FirebrandKeep",
    41: "KoeglinVillage",
    42: "Daggerfall",
    43: "DaggerfallOutlawRefuge",
    44: "LionGuardRedoubt",
    45: "WyrdTree",
    46: "Stonetooth",
    47: "PortHunding",
    48: "Riften",
    49: "RiftenOutlawRefuge",
    50: "Nimalten",
    51: "FallowstoneHall",
    52: "Windhelm",
    53: "WindhelmOutlawRefuge",
    54: "VoljarMeadery",
    55: "FortAmol",
    56: "Stormhold",
    57: "StormholdOutlawRefuge",
    58: "VenomousFens",
    59: "Hissmir",
    60: "Mournhold",
    61: "MournholdOutlawRefuge",
    62: "TalDeicGrounds",
    63: "MuthGnaarHills",
    64: "Ebonheart",
    65: "Kragenmoor",
    66: "DavonsWatch",
    67: "DavonsWatchOutlawRefuge",
    68: "Dhalmora",
    69: "Bleakrock",
    70: "Orsinium",
    71: "OrsiniumOutlawRefuge",
    72: "MorkulPlain",
    73: "ThievesDen",
    74: "AbahsLanding",
    75: "Anvil",
    76: "Kvatch",
    77: "AnvilOutlawRefuge",
    78: "VivecCity",
    79: "VivecCityOutlawRefuge",
    80: "SadrithMora",
    81: "Balmora",
    82: "BrassFortress",
    83: "BrassFortressOutlawRefuge",
    84: "Lillandril",
    85: "Shimmerene",
    86: "Alinor",
    87: "AlinorOutlawRefuge",
    88: "Lilmoth",
    89: "LilmothOutlawRefuge",
    90: "Rimmen",
    91: "RimmenOutlawRefuge",
    92: "Senchal",
    93: "SenchalOutlawRefuge",
    94: "Solitude",
    95: "SolitudeOutlawRefuge",
    96: "Markarth",
    97: "MarkarthOutlawRefuge"
}

# Parses the url to directly hit the api for TTC
def urlAndCaptchas(url, keys):
    tempurl = url.replace("/pc/", "/api/pc/")
    tempurl = tempurl.replace("SearchResult?", "Search?")
    return tempurl + "&V3ReCaptchaToken=" + keys[random.randint(0,4)]

# Get a random user-agent to attempt to simulate different machines
def get_random_ua():
    random_ua = ''
    ua_file = 'ua_file.txt'
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            prng = np.random.RandomState()
            index = prng.permutation(len(lines) - 1)
            idx = np.asarray(index, dtype=np.integer)[0]
            random_proxy = lines[int(idx)]
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    finally:
        return random_ua

# Give multiple captcha keys to randomly alternate until one gets invalid
captcha_key ="03AGdBq24TGnj6HEdmdqCgCu3m3prj-ZqJ5mBQXObT1YQF5t2VnBDvk9tBHF7Ye5J_F7Btj-7t7F30yKjdQ5-H0Ve7afGGi1Sq_EnIUueM-SP1k5q44dak5ezsnF-HyGXaS7HG2IZhBGHSNVLWiPd-TDIBZLBie9jweglD26i8T8ZQR8--wNhlJQ0oIV0BlwEfH2nDwiDjNmvz-bWaHb9r_WhCjgKq-LHkExs6sV3DSy1-sc1zEvAK4O4n0ZdxsjFnqLMUmbeY1ythFGiDJOsFbsFkhwIoR3h8Ru4ttM0f_QoIRE7QMgs5hQgJDBoWzv4TLB69U-CvEoFMQj8XvWJBQypIS4BWJpIsR4zCz8AREQixeOznxcqsTHs8eRC5eIPX8rp-_CaBztKsJhVtWMvae-S8yqY1hTl8yRsHL09n33uz218UOD2i_FrMcdSvBOCqYaL1yr1Mho4ceKuKMXSKjXo9qv7ngkaUmg"
captcha_keys = [
    "03AGdBq26FPEzrFESFQYHvhdczB7trum_3Q3uCeUD_-4wFwjihYIgfLSVrreLrUr4janv1gUfBjq0S72x7J5ws1XrSrvWjw0TRHZvRVuhYYqm1sD0MyNos9W_ua8HUIHPvrlXS-8U7S-51iT5b5JrtWhW4pSRiMemzbMxMrtrJJuzBUBpsOz89cz_LGKf0VcMgFrxbonV6TEcBwK0r5GH7RDzDTfubvsQBbqvCaknjsCblNb4cP5e__xPqZZWGUq0UhlWW7Dpaf-gMAEjlqBKu2X6iijiISkf7GqS_PHuxkz-N660PqOea6gqK_ST85Xkw3-DsXEHGLimya_zz0PFKhyNLP2rc2lxUnZQPGHIPnneBsCiCVJdO0LzKvGrLyyvBpfbxLG-9c2HyV82yV6QxrwF-rF5Xsz9szAdRO3EnwEfGtgODCQR-y1F7ae9wj12EmR4mFPr_BobOMnoSPZuyiRuNu100SJdFtg",
    "03AGdBq24DbV1Xo-eKezyddUP0hGIlWC8-vgWho7WS2wd1m1Iw8ABU1KlPlExCCKIyrJt2vH7VcsGgeqCZ0H9kRhG4lKQ_Zxlho6pOFlRnJ3eEl3oNpAqwu6SXg-LJFAGa4YClPjeQ7v6FBDa2nsZXQyjK-Z1Wv6haSgfVhDlf5PPe4dtBUWPNnijMkF_JFREg2vS-uPPdz-CUKUFS3-_EvCEJ-u3vbNtVxnRJVl4ykH6L6vAgCvBoBbpzlYa0NuShxg_gq9rfhWnBzydjk16dIkhmlNLMpfN-VVvdZCSOlCIKGEdWIk3yQiJWWIHd5_VQz3zdtAHRiL6nH9aFlmUh2nWCzqh37eZ1_gZIQTcwCBZ6Fp4X9-zDU6leq5zbeAWw6rfrgZoYqgH3imKOkhFgTFt71GMHI8Ziq0gwOmHs1zZSNNrmthyBycGzvt5j7R-5wj3rzsmmIi6jt2Z93kBI3CD90qcAOwqPJg",
    "03AGdBq26ZvURj1Lk6ctZhID99-V2cDy6jOagwVX5Ze2yNFAL0xf15BIyoIjc083pDRQ1xcF8wzkMVq8AvQHdt18MYUFrUu3c6Oitj__KFpxVoP1u9GxchXP3qBdcywBXIfMcYGBC-IKEkN8LiAlyi1HyHaM03ksiOCwVG04sxcevNaBY42rv1SPy7LjDQFTU4_S30wUYMuS-ai2FieU5h_3HVIvD8JX3YHKAt12VE4s0zVUb9G4ZEyIx2xhNQ8v6nNHGbbLGce1EA29NfrfSvERO57BgKT2Dq-0bBYhqz4HQjiUjQ-QPItBgkK08XJxWFrsKmhrPvFg6Zgk2KnRL56OiUf1aIfq1R3Fgs6SDNE0UFk63yCKQFqStdrjnuDtN6rSZaUecUQVFmH4qSZvEoAMNDd4OGwwEC4GQHppwGXqvN9cQ98xLpz66QJBDKEWf2MEpyXKCA52Aq",
    "03AGdBq271td_hAPs77FZj2pcMC2GzpuWVwQF2a-FrTyEt5vBk7xhfyx5HFkNpARh08t8ix0UPv7oyjKqQJ9vDeZpG4DMz4lleLZ8hmIEnWBccAmf9o5AwIhxDmA_jWixY3MYq4hoTjVLQLnOAPrRn36jN6Gg_T4mM_aDHjp8MSAmDsHd94kH9ui9g3Isl2ajZ6iB1V9P_D8bZDZSRj55cQwE7tExUh_CU5ntKdM4HLmnBxIuGWnS595gYoD2Znz674m7QMiWdKY4KeaCZ4NQHLPHKlp3VKWj3fi4m8w1FGTFaUCbk9dSNWQBK4cYxAZwUIQErsZH7kK0cvIiM-q798gBDPChHYcEnwGkVy1bF4NCDpU8Wx3tMnCensMuYlHQ2ac_qShrTZL22pD1Yb3FyaI9OV83hED55Q9c_UeRToCwwh5CYtU1sivv64MacnWVsH8wEXaPakHIA9yO6WP6Xyk5VBO3j20mvYA",
    "03AGdBq266hx2luABKsojm9rZ8iBxFC0T0km-8jtl_0M0yucKk0fGDR-vKVODDeAdpTQkmcAVX5PZO2U7_nf2aZuc5iy36yxs-je_X_6C3XBj_nVw2tRcf-m7mP6JucVuldCflKcoR-xJN8bJ4u9RyLe5XCbWbAdSctKdizAmueisQ9RgEPomQ8VRQC5QJpz5K8S4F2HWI6OdBvxhdQ5mj19NpRi9fH7uwSdgmtsRvAGQtAUfG4_Gpcl8gxxsAhyQs-wFauqbjpCT-YcyJKuIkc_n77W1h4f7PoSrFC_6U4GKRIWvBLSIs-84jOfnQ3ll6lWO2W_L_raLypU1puvLk6xpICPBrQB5tpiogHjKECXFIjfIDWYaXZ1U8cFxoDjsgZLWnMHtJrl7FHKzfLVszlkLlognlIo_BrqmqgENGk6DTElcS2l4J3boFl8bxNCjEf6nDNWsaFcTyX_0YaODEONDBsWsfzYJwLg"
    ]

# Update with own url's to search
url = "https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=10454&ItemNamePattern=&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=90000"

# Build request header
user_agent = get_random_ua()
send_header = {
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'referer': url,
    'user-agent': user_agent
    }

# Should change, loop every 2 minutes to search for new options
while True:
    result = requests.get(urlAndCaptchas(url, captcha_keys), headers=send_header)
    page_html = result.content
    send_header['user-agent'] = get_random_ua()

    curr_time = int(time.time())

    searchJson = json.loads(page_html)

    # Check if request has failed
    if searchJson["IsSuccess"] == False:
        print("SEARCH FAILED... SOLVE THE CAPTCHA IN YOUR BROWSER")
    else:
        searchObjList = searchJson["TradeListPageModel"]["TradeDetails"]
        
        for searchObj in searchObjList:
            # Currently a little lax which may cause repeats
            if curr_time - searchObj["DiscoverUnixTime"] < 300:
                print("Guild: {guild}\tLocation: {location}\tItem: {item}\tPrice: {amount} x ${unitprice} = {totalprice}\t".format(
                    guild=searchObj["GuildName"],
                    location=GuildKioskLocation[int(searchObj["GuildKioskLocationID"])],
                    item=searchObj["TradeAsset"]["Item"]["Name"],
                    amount=searchObj["TradeAsset"]["Amount"],
                    unitprice=searchObj["TradeAsset"]["UnitPrice"],
                    totalprice=searchObj["TradeAsset"]["TotalPrice"]
                    ))
    
    print("Searching...")
    time.sleep(random.randint(110, 130))