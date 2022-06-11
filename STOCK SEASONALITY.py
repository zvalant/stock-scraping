open("SPY.csv", "r")
dataset = [line.strip().split(",") for line in open("SPY.csv")]
year_pe = []
year_mid = []
year_pmid = []
year_e = []

for i in range(1,len(dataset)):
    curr = int(dataset[i][0].split("-")[0]) % 4
    if curr == 0:
        year_e.append(dataset[i])
    elif curr ==1:
        year_pe.append(dataset[i])
    elif curr ==2:
        year_mid.append(dataset[i])
    else:
        year_pmid.append(dataset[i])
seasonality_e = {}
price_ratio = float(year_e[0][1])
date_year = int(year_e[0][0].split("-")[0])
for i in range(len(year_e)):
    date_woyear = year_e[i][0].split("-")
    date_woyear = float(date_woyear[1] + "." + date_woyear[2])
    date_year_curr = int(year_e[i][0].split("-")[0])
    if date_year_curr != date_year:
        date_year = int(year_e[i][0].split("-")[0])
        price_ratio = float(year_e[i][1])
    if date_woyear not in seasonality_e:
        seasonality_e[date_woyear] = [float(year_e[i][1])/price_ratio]
    else:
        seasonality_e[date_woyear].append(float(year_e[i][1])/price_ratio)
for i in seasonality_e:
    seasonality_e[i] = sum(seasonality_e[i])/len(seasonality_e[i])


