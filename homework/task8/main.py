import re


def main(example):
    exr = r'\s*opt( |\n)?#\(([^\)]*)\)\s*==>\s*\"([^"]*)\"'
    d = {}
    matches = re.findall(exr, example)
    for match in matches:
        s = []
        for j in match[1].split(';'):
            j = j.strip()
            s.append(j)
        key = match[2]
        d[key] = s
    return d

print(main("do<data> opt#(xequ;onor ; riaton;tibibe_345 )==> \"isabior_627\" "
      "</data> <data>opt#( reinve_622 ;vean ) ==>\"orisor\" </data> <data> opt "
      "#(tira ; beat_32; anmate ) ==> \"ribien\"</data> <data> opt#( edaris_965 ;"
      "zaen_860 ; zaa; veatge_535 ) ==>\"biin_925\" </data> end"))

print("\n")

print(main("do <data> opt#( reen_983;anlaon;aaned ) ==> \"larera\" </data> <data> "
            "opt #( mauses ;ineson_357 ) ==>\"usin\" </data><data>opt #( arza_939 ;"
            "ravere_84 ; enza ) ==> \"erso\" </data> <data>opt #( anra_568 ; raaqu)"
            "==> \"tege_928\"</data> end"))