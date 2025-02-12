import { tokens } from "../theme";

export const mockDataTeam = [
  {
    id: 1, // add the 'id' field with a unique value (user_id in your case)
    user_id: 1,
    name: "safeya",
    username: "safeya123",
    email: "safeya@gmail.com",
    department: "IT",
    device_id: "D12345",
    join_date: "2021-01-01",
    risk_score: 45,
    risk_reason: "Malware exposure",
    status: "active",
  },
  {
    id: 2,
    user_id: 2,
    name: "Alaa",
    username: "Alaa123",
    email: "Alaa123@gmail.com",
    department: "HR",
    device_id: "D12346",
    join_date: "2020-06-15",
    risk_score: 25,
    risk_reason: "Low activity",
    status: "active",
  },
  {
    id: 3,
    user_id: 3,
    name: "sarah",
    username: "sarah321",
    email: "sarah123@gmail.com",
    department: "Finance",
    device_id: "D12347",
    join_date: "2019-03-12",
    risk_score: 60,
    risk_reason: "Suspicious behavior",
    status: "inactive",
  },
  {
    id: 4,
    user_id: 4,
    name: "maya",
    username: "maya8787",
    email: "maya8787@gmail.com",
    department: "Sales",
    device_id: "D12348",
    join_date: "2022-08-10",
    risk_score: 75,
    risk_reason: "High privilege access",
    status: "active",
  },
  {
    id: 5,
    user_id: 5,
    name: "eman",
    username: "eman10909",
    email: "eman10909@gmail.com",
    department: "Marketing",
    device_id: "D12349",
    join_date: "2021-12-05",
    risk_score: 30,
    risk_reason: "Unusual login patterns",
    status: "active",
  },
  {
    id:6,
    user_id: 6,
    name: "nour",
    username: "nour1345",
    email: "nour1345@gmail.com",
    department: "Engineering",
    device_id: "D12350",
    join_date: "2018-07-22",
    risk_score: 20,
    risk_reason: "Normal behavior",
    status: "active",
  },
  {
    id: 7,
    user_id: 7,
    name: "Walaa",
    username: "walaa123",
    email: "walaa123@gmail.com",
    department: "HR",
    device_id: "D12351",
    join_date: "2020-09-05",
    risk_score: 50,
    risk_reason: "Password sharing detected",
    status: "inactive",
  },
  {
    id: 8,
    user_id: 8,
    name: "haidy",
    username: "haidy8909",
    email: "haidy8909@gmail.com",
    department: "IT",
    device_id: "D12352",
    join_date: "2021-05-13",
    risk_score: 40,
    risk_reason: "Unusual login time",
    status: "active",
  },
  {
    id: 9,
    user_id: 9,
    name: "jamilaa",
    username: "jamilaa7878",
    email: "jamila7878@gmail.com",
    department: "Support",
    device_id: "D12353",
    join_date: "2017-11-25",
    risk_score: 10,
    risk_reason: "Low risk",
    status: "active",
  },
];

export const mockDataContactsf = [
  {
    id: 1,
    name: "sally",
    email: "sally153@gmail.com",
    age: 35,
    phone: "(665)121-5454",
    city: "cairo",
    zipCode: "10001",
    registrarId: 123512,
  },
  {
    id: 2,
    name: "walaa",
    email: "walaa123@gmail.com",
    age: 42,
    phone: "(421)314-2288",
    city: "cairo",
    zipCode: "13151",
    registrarId: 123512,
  },
  {
    id: 3,
    name: "safaa",
    email: "safaa3435@gmail.com",
    age: 45,
    phone: "01237372828",
    city: "cairo",
    zipCode: "87281",
    registrarId: 4132513,
  },
  {
    id: 4,
    name: "eman",
    email: "eman123@gmail.com",
    age: 16,
    phone: "01009817278",
    city: "cairo",
    zipCode: "15551",
    registrarId: 123512,
  },
  {
    id: 5,
    name: "Dana",
    email: "dana123@gmail.com",
    age: 31,
    phone: "0124526623",
    city: "cairo",
    zipCode: "14215",
    registrarId: 123512,
  },
  {
    id: 6,
    name: "jasmine",
    email: "jasmine2322@gmail.com",
    age: 150,
    phone: "010095161617",
    city: "cairo",
    zipCode: "10001",
    registrarId: 123512,
  },
  {
    id: 7,
    name: "eman ",
    email: "eman@gmail.com",
    age: 44,
    phone: "011241516157",
    city: "cairo",
    zipCode: "51523",
    registrarId: 123512,
  },
  {
    id: 8,
    name: "ahmed",
    email: "ahmed2682@gmail.com",
    age: 36,
    phone: "01262862827",
    city: "cairo",
    zipCode: "44215",
    registrarId: 512315,
  },
  {
    id: 9,
    name: "zeyad",
    email: "zeyad2928@gmail.com",
    age: 65,
    phone: "(444)555-6239",
    city: "cairo",
    zipCode: "111234",
    registrarId: 928397,
  },
  {
    id: 10,
    name: "wael",
    email: "wael2728@gmail.com",
    age: 42,
    phone: "(222)444-5555",
    city: "cairo",
    zipCode: "44215",
    registrarId: 533215,
  },
  {
    id: 11,
    name: "esraa",
    email: "esraa2728@gmail.com",
    age: 11,
    phone: "(444)555-6239",
    city: "cairo",
    zipCode: "1234",
    registrarId: 92197,
  },
];

export const mockDataInvoices = [
  {
    id: 1,
    name: "Ahmed Ali",
    email: "ahmed.ali@gmail.com",
    phone: "+20 100 121 5454",
    lastLogin: "03/12/2024",
    lastUpdate: "01/10/2025",
    addedBy: "Admin1",
  },
  {
    id: 2,
    name: "Mona Hassan",
    email: "mona.hassan@gmail.com",
    phone: "+20 112 314 2288",
    lastLogin: "06/15/2024",
    lastUpdate: "02/10/2025",
    addedBy: "Admin2",
  },
  {
    id: 3,
    name: "Tamer Ibrahim",
    email: "tamer.ibrahim@gmail.com",
    phone: "+20 113 982 6739",
    lastLogin: "05/02/2024",
    lastUpdate: "12/05/2025",
    addedBy: "Admin1",
  },
  {
    id: 4,
    name: "Fatma Khaled",
    email: "fatma.khaled@gmail.com",
    phone: "+20 100 425 6742",
    lastLogin: "03/21/2024",
    lastUpdate: "11/15/2025",
    addedBy: "Admin1",
  },
  {
    id: 5,
    name: "Youssef Mohamed",
    email: "youssef.mohamed@gmail.com",
    phone: "+20 100 445 1189",
    lastLogin: "01/12/2025",
    lastUpdate: "03/22/2025",
    addedBy: "Admin2",
  },
  {
    id: 6,
    name: "Salma Tarek",
    email: "salma.tarek@gmail.com",
    phone: "+20 100 545 6483",
    lastLogin: "11/02/2024",
    lastUpdate: "04/10/2025",
    addedBy: "Admin1",
  },
  {
    id: 7,
    name: "Hassan Ahmed",
    email: "hassan.ahmed@gmail.com",
    phone: "+20 100 124 0123",
    lastLogin: "02/11/2025",
    lastUpdate: "10/20/2025",
    addedBy: "Admin1",
  },
  {
    id: 8,
    name: "Dina Farouk",
    email: "dina.farouk@gmail.com",
    phone: "+20 100 444 5555",
    lastLogin: "05/02/2024",
    lastUpdate: "09/17/2025",
    addedBy: "Admin2",
  },
];

export const mockTransactions = [
  {
    txId: "Abnormal Behavior",
    user: "eman",
    date: "2024-01-15",
  },
  {
    txId: "normal Behavior",
    user: "Alaa",
    date: "2023-12-05",
  },
  {
    txId: "normal Behavior",
    user: "sarah",
    date: "2024-03-10",
  },
  {
    txId: "normal Behavior",
    user: "maya",
    date: "2023-08-22",
  },
  {
    txId: "Abnormal Behavior",
    user: "eman",
    date: "2024-05-11",
  },
  {
    txId: "Normal Behavior",
    user: "nour",
    date: "2023-07-14",
  },
  {
    txId: "Abnormal Behavior",
    user: "Walaa",
    date: "2024-02-28",
  },
  {
    txId: "Abnormal Behavior",
    user: "haidy",
    date: "2023-11-30",
  },
  {
    txId: "Normal Behavior",
    user: "jamilaa",
    date: "2024-04-05",
  },
];

export const mockBarData = [
  {
    country: "AD",
    "hot dog": 137,
    "hot dogColor": "hsl(229, 70%, 50%)",
    burger: 96,
    burgerColor: "hsl(296, 70%, 50%)",
    kebab: 72,
    kebabColor: "hsl(97, 70%, 50%)",
    donut: 140,
    donutColor: "hsl(340, 70%, 50%)",
  },
  {
    country: "AE",
    "hot dog": 55,
    "hot dogColor": "hsl(307, 70%, 50%)",
    burger: 28,
    burgerColor: "hsl(111, 70%, 50%)",
    kebab: 58,
    kebabColor: "hsl(273, 70%, 50%)",
    donut: 29,
    donutColor: "hsl(275, 70%, 50%)",
  },
  {
    country: "AF",
    "hot dog": 109,
    "hot dogColor": "hsl(72, 70%, 50%)",
    burger: 23,
    burgerColor: "hsl(96, 70%, 50%)",
    kebab: 34,
    kebabColor: "hsl(106, 70%, 50%)",
    donut: 152,
    donutColor: "hsl(256, 70%, 50%)",
  },
  {
    country: "AG",
    "hot dog": 133,
    "hot dogColor": "hsl(257, 70%, 50%)",
    burger: 52,
    burgerColor: "hsl(326, 70%, 50%)",
    kebab: 43,
    kebabColor: "hsl(110, 70%, 50%)",
    donut: 83,
    donutColor: "hsl(9, 70%, 50%)",
  },
  {
    country: "AI",
    "hot dog": 81,
    "hot dogColor": "hsl(190, 70%, 50%)",
    burger: 80,
    burgerColor: "hsl(325, 70%, 50%)",
    kebab: 112,
    kebabColor: "hsl(54, 70%, 50%)",
    donut: 35,
    donutColor: "hsl(285, 70%, 50%)",
  },
  {
    country: "AL",
    "hot dog": 66,
    "hot dogColor": "hsl(208, 70%, 50%)",
    burger: 111,
    burgerColor: "hsl(334, 70%, 50%)",
    kebab: 167,
    kebabColor: "hsl(182, 70%, 50%)",
    donut: 18,
    donutColor: "hsl(76, 70%, 50%)",
  },
  {
    country: "AM",
    "hot dog": 80,
    "hot dogColor": "hsl(87, 70%, 50%)",
    burger: 47,
    burgerColor: "hsl(141, 70%, 50%)",
    kebab: 158,
    kebabColor: "hsl(224, 70%, 50%)",
    donut: 49,
    donutColor: "hsl(274, 70%, 50%)",
  },
];

export const mockPieData = [
  {
    id: "hack",
    label: "hack",
    value: 239,
    color: "hsl(104, 70%, 50%)",
  },
  {
    id: "make",
    label: "make",
    value: 170,
    color: "hsl(162, 70%, 50%)",
  },
  {
    id: "go",
    label: "go",
    value: 322,
    color: "hsl(291, 70%, 50%)",
  },
  {
    id: "lisp",
    label: "lisp",
    value: 503,
    color: "hsl(229, 70%, 50%)",
  },
  {
    id: "scala",
    label: "scala",
    value: 584,
    color: "hsl(344, 70%, 50%)",
  },
];

export const mockLineData = [
  {
    id: "Anomalous Activities",
    color: tokens("dark").greenAccent[500],
    data: [
      { x: "January", y: 120 },
      { x: "February", y: 180 },
      { x: "March", y: 150 },
      { x: "April", y: 220 },
      { x: "May", y: 260 },
      { x: "June", y: 310 },
      { x: "July", y: 290 },
      { x: "August", y: 330 },
      { x: "September", y: 400 },
      { x: "October", y: 420 },
      { x: "November", y: 480 },
      { x: "December", y: 500 },
    ],
  },
  {
    id: "Malware Infections",
    color: tokens("dark").blueAccent[300],
    data: [
      { x: "January", y: 80 },
      { x: "February", y: 95 },
      { x: "March", y: 120 },
      { x: "April", y: 140 },
      { x: "May", y: 190 },
      { x: "June", y: 240 },
      { x: "July", y: 220 },
      { x: "August", y: 280 },
      { x: "September", y: 320 },
      { x: "October", y: 350 },
      { x: "November", y: 370 },
      { x: "December", y: 410 },
    ],
  },
  {
    id: "Unusual Network Traffic",
    color: tokens("dark").redAccent[200],
    data: [
      { x: "January", y: 150 },
      { x: "February", y: 130 },
      { x: "March", y: 160 },
      { x: "April", y: 190 },
      { x: "May", y: 230 },
      { x: "June", y: 270 },
      { x: "July", y: 250 },
      { x: "August", y: 300 },
      { x: "September", y: 350 },
      { x: "October", y: 370 },
      { x: "November", y: 410 },
      { x: "December", y: 460 },
    ],
  },
];

export const mockGeographyData = [
  {
    id: "AFG",
    value: 520600,
  },
  {
    id: "AGO",
    value: 949905,
  },
  {
    id: "ALB",
    value: 329910,
  },
  {
    id: "ARE",
    value: 675484,
  },
  {
    id: "ARG",
    value: 432239,
  },
  {
    id: "ARM",
    value: 288305,
  },
  {
    id: "ATA",
    value: 415648,
  },
  {
    id: "ATF",
    value: 665159,
  },
  {
    id: "AUT",
    value: 798526,
  },
  {
    id: "AZE",
    value: 481678,
  },
  {
    id: "BDI",
    value: 496457,
  },
  {
    id: "BEL",
    value: 252276,
  },
  {
    id: "BEN",
    value: 440315,
  },
  {
    id: "BFA",
    value: 343752,
  },
  {
    id: "BGD",
    value: 920203,
  },
  {
    id: "BGR",
    value: 261196,
  },
  {
    id: "BHS",
    value: 421551,
  },
  {
    id: "BIH",
    value: 974745,
  },
  {
    id: "BLR",
    value: 349288,
  },
  {
    id: "BLZ",
    value: 305983,
  },
  {
    id: "BOL",
    value: 430840,
  },
  {
    id: "BRN",
    value: 345666,
  },
  {
    id: "BTN",
    value: 649678,
  },
  {
    id: "BWA",
    value: 319392,
  },
  {
    id: "CAF",
    value: 722549,
  },
  {
    id: "CAN",
    value: 332843,
  },
  {
    id: "CHE",
    value: 122159,
  },
  {
    id: "CHL",
    value: 811736,
  },
  {
    id: "CHN",
    value: 593604,
  },
  {
    id: "CIV",
    value: 143219,
  },
  {
    id: "CMR",
    value: 630627,
  },
  {
    id: "COG",
    value: 498556,
  },
  {
    id: "COL",
    value: 660527,
  },
  {
    id: "CRI",
    value: 60262,
  },
  {
    id: "CUB",
    value: 177870,
  },
  {
    id: "-99",
    value: 463208,
  },
  {
    id: "CYP",
    value: 945909,
  },
  {
    id: "CZE",
    value: 500109,
  },
  {
    id: "DEU",
    value: 63345,
  },
  {
    id: "DJI",
    value: 634523,
  },
  {
    id: "DNK",
    value: 731068,
  },
  {
    id: "DOM",
    value: 262538,
  },
  {
    id: "DZA",
    value: 760695,
  },
  {
    id: "ECU",
    value: 301263,
  },
  {
    id: "EGY",
    value: 148475,
  },
  {
    id: "ERI",
    value: 939504,
  },
  {
    id: "ESP",
    value: 706050,
  },
  {
    id: "EST",
    value: 977015,
  },
  {
    id: "ETH",
    value: 461734,
  },
  {
    id: "FIN",
    value: 22800,
  },
  {
    id: "FJI",
    value: 18985,
  },
  {
    id: "FLK",
    value: 64986,
  },
  {
    id: "FRA",
    value: 447457,
  },
  {
    id: "GAB",
    value: 669675,
  },
  {
    id: "GBR",
    value: 757120,
  },
  {
    id: "GEO",
    value: 158702,
  },
  {
    id: "GHA",
    value: 893180,
  },
  {
    id: "GIN",
    value: 877288,
  },
  {
    id: "GMB",
    value: 724530,
  },
  {
    id: "GNB",
    value: 387753,
  },
  {
    id: "GNQ",
    value: 706118,
  },
  {
    id: "GRC",
    value: 377796,
  },
  {
    id: "GTM",
    value: 66890,
  },
  {
    id: "GUY",
    value: 719300,
  },
  {
    id: "HND",
    value: 739590,
  },
  {
    id: "HRV",
    value: 929467,
  },
  {
    id: "HTI",
    value: 538961,
  },
  {
    id: "HUN",
    value: 146095,
  },
  {
    id: "IDN",
    value: 490681,
  },
  {
    id: "IND",
    value: 549818,
  },
  {
    id: "IRL",
    value: 630163,
  },
  {
    id: "IRN",
    value: 596921,
  },
  {
    id: "IRQ",
    value: 767023,
  },
  {
    id: "ISL",
    value: 478682,
  },
  {
    id: "ISR",
    value: 963688,
  },
  {
    id: "ITA",
    value: 393089,
  },
  {
    id: "JAM",
    value: 83173,
  },
  {
    id: "JOR",
    value: 52005,
  },
  {
    id: "JPN",
    value: 199174,
  },
  {
    id: "KAZ",
    value: 181424,
  },
  {
    id: "KEN",
    value: 60946,
  },
  {
    id: "KGZ",
    value: 432478,
  },
  {
    id: "KHM",
    value: 254461,
  },
  {
    id: "OSA",
    value: 942447,
  },
  {
    id: "KWT",
    value: 414413,
  },
  {
    id: "LAO",
    value: 448339,
  },
  {
    id: "LBN",
    value: 620090,
  },
  {
    id: "LBR",
    value: 435950,
  },
  {
    id: "LBY",
    value: 75091,
  },
  {
    id: "LKA",
    value: 595124,
  },
  {
    id: "LSO",
    value: 483524,
  },
  {
    id: "LTU",
    value: 867357,
  },
  {
    id: "LUX",
    value: 689172,
  },
  {
    id: "LVA",
    value: 742980,
  },
  {
    id: "MAR",
    value: 236538,
  },
  {
    id: "MDA",
    value: 926836,
  },
  {
    id: "MDG",
    value: 840840,
  },
  {
    id: "MEX",
    value: 353910,
  },
  {
    id: "MKD",
    value: 505842,
  },
  {
    id: "MLI",
    value: 286082,
  },
  {
    id: "MMR",
    value: 915544,
  },
  {
    id: "MNE",
    value: 609500,
  },
  {
    id: "MNG",
    value: 410428,
  },
  {
    id: "MOZ",
    value: 32868,
  },
  {
    id: "MRT",
    value: 375671,
  },
  {
    id: "MWI",
    value: 591935,
  },
  {
    id: "MYS",
    value: 991644,
  },
  {
    id: "NAM",
    value: 701897,
  },
  {
    id: "NCL",
    value: 144098,
  },
  {
    id: "NER",
    value: 312944,
  },
  {
    id: "NGA",
    value: 862877,
  },
  {
    id: "NIC",
    value: 90831,
  },
  {
    id: "NLD",
    value: 281879,
  },
  {
    id: "NOR",
    value: 224537,
  },
  {
    id: "NPL",
    value: 322331,
  },
  {
    id: "NZL",
    value: 86615,
  },
  {
    id: "OMN",
    value: 707881,
  },
  {
    id: "PAK",
    value: 158577,
  },
  {
    id: "PAN",
    value: 738579,
  },
  {
    id: "PER",
    value: 248751,
  },
  {
    id: "PHL",
    value: 557292,
  },
  {
    id: "PNG",
    value: 516874,
  },
  {
    id: "POL",
    value: 682137,
  },
  {
    id: "PRI",
    value: 957399,
  },
  {
    id: "PRT",
    value: 846430,
  },
  {
    id: "PRY",
    value: 720555,
  },
  {
    id: "QAT",
    value: 478726,
  },
  {
    id: "ROU",
    value: 259318,
  },
  {
    id: "RUS",
    value: 268735,
  },
  {
    id: "RWA",
    value: 136781,
  },
  {
    id: "ESH",
    value: 151957,
  },
  {
    id: "SAU",
    value: 111821,
  },
  {
    id: "SDN",
    value: 927112,
  },
  {
    id: "SDS",
    value: 966473,
  },
  {
    id: "SEN",
    value: 158085,
  },
  {
    id: "SLB",
    value: 178389,
  },
  {
    id: "SLE",
    value: 528433,
  },
  {
    id: "SLV",
    value: 353467,
  },
  {
    id: "ABV",
    value: 251,
  },
  {
    id: "SOM",
    value: 445243,
  },
  {
    id: "SRB",
    value: 202402,
  },
  {
    id: "SUR",
    value: 972121,
  },
  {
    id: "SVK",
    value: 319923,
  },
  {
    id: "SVN",
    value: 728766,
  },
  {
    id: "SWZ",
    value: 379669,
  },
  {
    id: "SYR",
    value: 16221,
  },
  {
    id: "TCD",
    value: 101273,
  },
  {
    id: "TGO",
    value: 498411,
  },
  {
    id: "THA",
    value: 506906,
  },
  {
    id: "TJK",
    value: 613093,
  },
  {
    id: "TKM",
    value: 327016,
  },
  {
    id: "TLS",
    value: 607972,
  },
  {
    id: "TTO",
    value: 936365,
  },
  {
    id: "TUN",
    value: 898416,
  },
  {
    id: "TUR",
    value: 237783,
  },
  {
    id: "TWN",
    value: 878213,
  },
  {
    id: "TZA",
    value: 442174,
  },
  {
    id: "UGA",
    value: 720710,
  },
  {
    id: "UKR",
    value: 74172,
  },
  {
    id: "URY",
    value: 753177,
  },
  {
    id: "USA",
    value: 658725,
  },
  {
    id: "UZB",
    value: 550313,
  },
  {
    id: "VEN",
    value: 707492,
  },
  {
    id: "VNM",
    value: 538907,
  },
  {
    id: "VUT",
    value: 650646,
  },
  {
    id: "PSE",
    value: 476078,
  },
  {
    id: "YEM",
    value: 957751,
  },
  {
    id: "ZAF",
    value: 836949,
  },
  {
    id: "ZMB",
    value: 714503,
  },
  {
    id: "ZWE",
    value: 405217,
  },
  {
    id: "KOR",
    value: 171135,
  },
];
