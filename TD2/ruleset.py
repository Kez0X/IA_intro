import externalfunctions
# On importe les fonctions nécéssaire à certaines règles 

# la liste des règles
rules = [
    # Règle par défaut quand le bot ne connais pas de réponse paramétrée
    { 
        "id": "Je sais pas",
        "rule": ".*",
        "response": "Désolé, je ne sais pas, dite moi ce que vous souhaitez que je réponde dans ce cas.",
        "score": 0,
        "fatal": False,
        "function":None,
    },
    # Autres règles
    {
        "id": "Bonjour",
        "rule": "bonjour",
        "response": "Bonjour, je suis votre spécialiste en burger, en quoi puis-je vous aider ?",
        "score": 1,
        "fatal": False,
        "function": None,
    }, #fonctionne
    {
        "id": "Aurevoir",
        "rule": "(au revoir)|(aurevoir)",
        "response": "Ravi d'avoir pu vous aider " + str(externalfunctions.getName),
        "score": 1,
        "fatal": True,
        "function": None,
    }, #fonctionne
    {
        "id": "Salut",
        "rule": "(salut|hello)",
        "response": "Salut, comment va tu ? Une question sur les burgers ?",
        "score": 1,
        "fatal": False,
        "function": None,
    }, #fonctionne
    {
        "id":"apropos",
        "rule":"(qu'est ce qu'|c'est quoi |qu'est ce que c'est |Qu'est ce que c'est qu')un (burger|hamburger).*",
        "response":"Un hamburger, ou par aphérèse burger, est un sandwich d'origine allemande, composé de deux pains de forme ronde1 (bun) généralement garnis d'une galette de steak haché (généralement du bœuf) et de crudités, salade, tomate, oignon, cornichon (pickles) ainsi que de sauce. D'autres question à ce propos ?",
        "score":1,
        "fatal":False,
        "function":None,
        #fonctionne
    },
    {
        "id":"date",
        "rule":".* (année est (apparu|inventé)|(de quand date)|(date (d'invention|de création|d'apparition))) (du|le) (burger|hamburger).*",
        "response":"Le burger est inventé en 1758 en Allemagne à Hambourg. N'hésitez pas à me poser des questions sur l'hétymologie du mot hamburger.",
        "score":1,
        "fatal":False,
        "function":None,
    }, #ne fonctionne pas ?
    {
        "id":"ethymo",
        "rule":".*étymologie (du mot|de) (burger|hamburger).*",
        "response":"Hamburger fait référence à la ville de Hambourg, en Allemagne. Il n'existe aucun rapport étymologique entre le hamburger et le jambon (en anglais : ham), puisque le nom de la ville de Hambourg a une étymologie différente. Une question sur la date d'invention du burger ?",
        "score":1,
        "fatal":False,
        "function":None,
    }, #fonctionne
    {
        "id":"découverte",
        "rule":".*(donne moi un (exemple de|)|est le) (burger|hamburger) (le plus |)connu.*",
        "response":"Le burger le plus connu est certainement le Big Mac, de la chaine de restauration rapide McDonald's. Mais je peux vous trouver un burger plus original si vous me le demandez.",
        "score":1,
        "fatal":False,
        "function":None,
    }, #fontionne 
    {
        "id":"original",
        "rule":".*(donne moi un (exemple de|)|est le) (burger|hamburger) (le plus |)(original|spécial|innatendu).*",
        "response":"Bien sûr !  L’Atomic Fallout, l’emblématique burger servi à l’Atomic Burger de Bristol, est tellement pimenté que les clients doivent signer une exonération de responsabilité, porter des gants de protection, ou encore prouver qu’ils ont plus de 18 ans et sont sobres avant de se mettre à table. Mais il est loin d'être le plus gros burger du monde...",
        "score":1,
        "fatal":False,
        "function":None, 
    }, #fonctionne
    {
        "id":"biggest",
        "rule":".*(donne moi un (exemple de|)|est le) (burger|hamburger) (le plus |)(grand|gros|énorme).*",
        "response":"C'est le Black Bear Casino Resort de Carlton dans le Minnesota aux Etats-Unis. Le double bacon cheeseburger comprend 27 kg de bacon, 22 kg de laitue et de 18 kg de fromage et cornichons pour un total de 913 kilos et près de quatre millions de calories.",
        "score":1,
        "fatal":False,
        "function":None, 
    }, #fonctionne 
    {
        "id":"where",
        "rule":".*le (tout|) premier (restaurant|resto|lieu|lieux) à (servir|préparer|cuisiner|proposer) (des|un|le|les) (hamburger|burger|hamburgers|burgers).*",
        "response":"En 1904, Fletcher Davis originaire d’Athens au Texas, vend des sandwichs au steak de Hambourg à la foire de Saint-Louis. C’est un véritable succès qui semble marquer la vraie naissance du hamburger actuel. C'était le premier lieu à servir des hamburger comme on l'entend aujourd'hui.",
        "score":2,
        "fatal":False,
        "function":None, 
    }, #ne fonctionne pas ?
    {
        "id":"firstmcdo",
        "rule":".*le (tout|) premier (mcdo|mc'do|mcdonald|mcdonalds|mcdonald's).*",
        "response":"Le premier McDonald's ouvre en 1955 dans la banlieue de Chicago, Illinois.",
        "score":1,
        "fatal":False,
        "function":None, 
    }, #fonctionne 
    {
        "id":"sum",
        "rule":"(?:fait|additionne) ([0-9]*) (?:plus|et) ([0-9]*).*",
        "response":"Bien j'additionne ces deux nombres",
        "score":1,
        "fatal":False,
        "function":externalfunctions.Sum, 
    }, #fonctionne
    {
        "id":"moins",
        "rule":"(?:fait|soustrait) ([0-9]*) (?:moins|et) ([0-9]*).*",
        "response":"Bien je soustrait ces deux nombres",
        "score":1,
        "fatal":False,
        "function":externalfunctions.Soustraction, 
    }, #fonctionne
    {
        "id":"multi",
        "rule":"(?:fait|multiplie) ([0-9]*) (?:x|fois|et) ([0-9]*).*",
        "response":"Bien je multiplie ces deux nombres",
        "score":1,
        "fatal":False,
        "function":externalfunctions.Multiplication, 
    }, #fonctionne
    {
        "id":"quotient",
        "rule":"(?:fait|divise) ([0-9]*) (?:/|divisé par|et) ([0-9]*).*",
        "response":"Bien je divise ces deux nombres",
        "score":1,
        "fatal":False,
        "function":externalfunctions.Divide, 
    }, #fonctionne
    {
        "id":"consommation",
        "rule":".*(quelle est|donne moi) la consommation de (burgers|burger|hamburgers|hamburger) annuelle (des américains|aux états-unis|en amérique).*",
        "response":"Les Américains consomment en moyenne 50 milliards de burgers par an.",
        "score":1,
        "fatal":False,
        "function":None,
    }, #fonctionne 
    {
        "id":"ventes",
        "rule":".*(quel est|donne moi|combien) de dollars les ventes de (burgers|burger|hamburger|hamburgers)(le montant|ont rapporté) aux états-unis.*",
        "response":"Les ventes de burgers aux États-Unis ont atteint plus de 100 milliards de dollars.",
        "score":1,
        "fatal":False,
        "function":None,
    }, #ne fonctionne pas
    {
        "id":"journée",
        "rule":".*(quelle est|donne moi) la date de la journée nationale du (burger|hamburger).*",
        "response":"Le 28 mai est la journée nationale du burger aux états-Unis.",
        "score":1,
        "fatal":False,
        "function":None,
    }, #fonctionne 
    {
        "id":"record",
        "rule":".*(quel est|donne moi) le record du plus grand nombre de (burgers|hamburgers|burger|hamburger) (mangés|avalés) en (quelques minutes|très peu de temps|peu de temps).*",
        "response":"Le record de consommation de burgers est de 26 hamburgers en 10 minutes, établi lors du concours annuel de l'Association des mangeurs de hot-dogs.",
        "score":1,
        "fatal":False,
        "function":None,
    }, #fonctionne
    {
        "id":"garniture",
        "rule":".*(quel est|de quel type) (la garniture|d'aliments) (des|les) (burgers|burgers|hamburgers|hamburgers) (sont t'il remplis|remplis|garnis|constitués).*",
        "response":"Les burgers peuvent être garnis de divers ingrédients tels que des œufs, du bacon, des avocats, des oignons, des champignons, et bien d'autres encore.",
        "score":1,
        "fatal":False,
        "function":None,
    }, #fonctionne 
    {
        "id":"cuisson",
        "rule":".*quelles sont les (différentes façons|différentes manières|méthodes|façons|manières) (de|pour) (cuire|cuisson) des (burgers|burger|hamburger|hamburgers).*",
        "response":"Les burgers peuvent être cuits de différentes manières, notamment grillés, saisis, frits ou cuits au barbecue.",
        "score":1,
        "fatal":False,
        "function":None,
    }, #fonctionne 
    {
        "id":"japon",
        "rule":".*(comment|donne moi) (un|une) (exemple|variation) de (burger|burgers|hamburgers|hamburger) (qui existe|présente) (dans|à) (un autre pays|un pays étranger|l'étranger|en asie).*",
        "response":"Au Japon, les burgers peuvent être garnis de tempura, de wasabi ou même de ramen.",
        "score":1,
        "fatal":False,
        "function":None,
    },
    {
        "id":"nvelle zelande",
        "rule":".*(comment|donne moi) (un|une) (exemple|variation) de (burger|burgers|hamburgers|hamburger) (qui existe|présente) (dans|à) (un autre pays|un pays étranger|l'étranger|un pays du sud).*",
        "response":"En Nouvelle-Zélande, un burger est souvent garni d'un œuf frit et d'une tranche de betterave.",
        "score":2,
        "fatal":False,
        "function":None,
    },
    {
        "id":"sauce",
        "rule":".*(est t'il possible de|peut on) (remplir|garnir) (nos|des|les|dans) (burgers|burger|hamburger|hamburgers) (de|d'une|une) (sauces|sauce spéciale|sauce.*)",
        "response":"En effet, certains burgers sont garnis de sauces spéciales, comme la sauce barbecue, la mayonnaise épicée ou le ketchup maison.",
        "score":1,
        "fatal":False,
        "function":None,
    }, #fonctionne 
    {
        "id":"sucre",
        "rule":".*(peut on|est il possible) (mettre|garnir|de mettre|de garnir) (des choses sucrées|de choses sucrées|de sucreries) (les|des|dans) (burgers|burger|hamburgers|hamburgers).*",
        "response":"Certains burgers sont garnis de condiments et d'ingrédients sucrés, comme le bacon caramélisé ou la confiture de figues, créant un mélange de saveurs sucrées et salées.",
        "score":1,
        "fatal":False,
        "function":None,
    },
    {
        "id":"personalisation",
        "rule":".*(peut on|est il possible de) (modifier|choisir|changer|personnaliser) (la|les) (composition|recette|ingrédients|éléments) (de son|d'un|du) (burger|burgers|hamburgers|hamburgers).*",
        "response":"En effet, les burgers sont souvent personnalisables, permettant aux clients de choisir leurs garnitures préférées parmi une liste d'options.",
        "score":1,
        "fatal":False,
        "function":None,
    },
    {
        "id":"vegetarien",
        "rule":".*(quand|a quelle date|en quelle année) (a été inventé|est apparu|a vu le jour) (le burger végétarien|le premier burger végétarien).*",
        "response":"Le premier hamburger végétarien a été inventé en 1981 par Gregory Sams.",
        "score":1,
        "fatal":False,
        "function":None,
    }, 
    {
        "id":"name",
        "rule":".*(je m'appelle|mon nom est|mon prénom est).*",
        "response":"",
        "score":3,
        "fatal":False,
        "function":externalfunctions.RecordName,
    },
    {
        "id":"capitale",
        "rule":".*(quelle|quelle ville) (est|est considérée comme) (la capitale|la ville principale|la ville la plus importante) (pour|du) (burger|burgers|hamburger|hamburgers).*",
        "response":"La ville de Seymour, Wisconsin, est considérée comme la capitale du hamburger.",
        "score":1,
        "fatal":False,
        "function":None,
    },
    {
        "id":"burger king",
        "rule":".*(quand|en quelle année|a quelle date) (a été crée|a été fondée|est apparue|sont apparu) (burger king|la chaîne burger king|l'entreprise burger king|les restaurants rapides burger king|les restaurants burger king).*",
        "response":"Burger King, une des plus grandes chaînes de restauration rapide, a été fondée en 1954.",
        "score":1,
        "fatal":False,
        "function":None,
    },
]