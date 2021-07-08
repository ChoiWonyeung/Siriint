def table_make(soup):
    table = soup.select("div.table")
    thead_tr_list = table[0].select("thead tr th")
    tbody_tr_list = table[0].select("tbody tr")

    table_list = []
    for tr in tbody_tr_list:
        td_list = tr.select("td")
        test = {}
        for j, td in enumerate(td_list):
            value = td.text.strip()
            key = thead_tr_list[j].text.strip()
            if key == "":
                continue
            test[key] = value

        table_list.append(test)
    return table_list
