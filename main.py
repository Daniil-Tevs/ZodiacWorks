import telebot
import re
import requests

token = '6232507877:AAF5qdMgv0HAQHWMgggi8Nk1PDK6DOw4zho'
bot = telebot.TeleBot(token)


def get_description(number):
    if number == 1:
        return '<strong>Образ</strong> – лидер, предводитель, первопроходец, но также и разрушитель, завоеватель.\n<strong>Символ</strong> – Солнце, Бездна, точка отсчета\n<strong>Ключевое слово</strong>: вперед! \n<strong>Девиз:</strong> Кто, если не я?\n<strong>Покровитель</strong> – эгрегор лидерства и индивидуальности.\n\nЛюди «единицы» наделены огромным потенциалом. Они честолюбивы, и обладают сильной энергией, для претворения множества жизненных идей и планов в жизнь. Ваш путь – путь лидера, и вряд ли что-то заставит вас свернуть с выбранного направления. Но несмотря на ярко выраженные лидерские качества и постоянное многолюдное окружение, вы по натуре –одиночка. Вам часто скучно и некомфортно даже среди ближайших друзей и родственников. Поэтому некоторые «единицы» предпочитают работать и претворять в жизнь планы и проекты в одиночестве.'
    if number == 2:
        return "<strong>Образ</strong> – миротворец, помощник, советчик, обратная сторона- сплетник, интриган или завистник.\n<strong>Символ</strong> – Луна, дуга между двумя точками.\n<strong>Ключевое слово</strong>: общение.\n<strong>Девиз:</strong>: Контакт? Есть контакт!\n<strong>Покровитель</strong> – эгрегор человеческого общения.\n\nДвойки – это люди контактеры. Они легко находят общий язык с окружающими, налаживают нужные связи и любят заниматься миротворчеством. Двойки не конфликтны и всегда стараются сгладить острые углы и обойти неприятные ситуации. В этом им помогает не только сила убеждения, но и хитрость. Поэтому двойки считаются прирожденными дипломатами и переговорщиками. Они легко улаживают спорные вопросы, что помогает им в работе или ведении бизнеса."
    if number == 3:
        return '<strong>Образ</strong> – энтузиаст, счастливчик, баловень судьбы\n<strong>Символ</strong> – подвижный, но неустойчивый треугольник. Суета сует.\n<strong>Ключевое слово</strong>: оптимист. \n<strong>Девиз:</strong>: Улыбайтесь, господа!\n<strong>Покровитель</strong> три эгрегора – удачи, фантазии и оптимизма.\n\nТроек смело можно назвать счастливчиками, ибо фортуна всегда поворачивается к ним нужным местом. Такие люди обаятельны, легкие в общении и считаются душой любой компании. Путь троек почти всегда творческий, они свободно выражают себя в различных сферах, но лучше всего — на публичных должностях. В общении с другими они эмоциональны, не злопамятны и великодушны. Поэтому некоторые пользуются их добродушием и беспечностью. Тройки легко вдохновляются новыми идеями, всегда в творческом в поиске и любят все необычное.'
    if number == 4:
            return '<strong>Образ</strong> – труженик, практик, опора и надежда этого мира.\n<strong>Символ</strong> – квадрат.\n<strong>Ключевое слово</strong>: труд, устойчивость, надежность.\n<strong>Девиз:</strong>: Всегда стоит сделать усилие!\n<strong>Покровитель</strong> – эгрегор практичных людей и практичной жизни.\n\nЧетверки – пожизненные трудяги. Они много и напряженно работают, чтобы достичь нужных результатов. Ваш путь будет стабилен, размерен, без особых встрясок и перемен. Такими людьми руководит практичность, дисциплинированность и пунктуальность. Они стараются все держать на своем контроле и владеть ситуацией. Счастье не свалится вам на голову, для этого придется изрядно потрудиться и приложить максимум усилий. Но зато, когда оно придет, то будет огромным и вечным. Как все то, что вы созидаете.'
    if number == 5:
            return '<strong>Образ</strong> – свободолюбец, авантюрист, путешественник, человек, символизирующий свою эпоху.\n<strong>Символ</strong> – звезда.\n<strong>Ключевое слово</strong>: движение. \n<strong>Девиз:</strong>: Риск – благородное дело!\n<strong>Покровитель</strong> – эгрегоры открытий, путешествий и дерзких проектов.\n\nЛюди пятерки всегда в движении и непредсказуемы. Их неуемная энергия бьет через край, фонтаном обдавая окружающих. Они вечные искатели, странники и путешественники. Благоразумие – это не про вас. Рядом с вами всегда риск и опасность, но это не мешает вам с честью выбираться из самых затруднительных ситуаций. Пятерки легки на подъем и словно играются с жизнью, испытывая ее на прочность. Поэтому провидение заботится о них вдвойне – дает большое количество козырей и «туза в рукаве». Такие люди легко приспосабливаются к разным обстоятельствам и чувствуют себя как рыба в воде в любых странах и обществах.'
    if number == 6:
            return '<strong>Образ</strong> – наставник: тот, кто заботится об униженных и оскорбленных, наставляет человечество на путь истинный.\n<strong>Символ</strong> – рукопожатие.\n<strong>Ключевое слово</strong>: вместе.\n<strong>Девиз:</strong>: Мы с тобой одной крови. Ради семьи готов на всё, ради дружбы на многое!\nПокровители Шестерок – эгрегоры воспитания, сострадания, семьи и дружбы\n\nШестерки пришли в тот Мир для сострадания и наставления. Их жизненное кредо – наставлять, направлять, поддерживать, защищать и оберегать. Таким людям не обязательно быть лидерами. Они счастливы от того, что выполняют свою миссию, помогая своей семье, близким и окружающим. При чем не только физически, но и материально. Такие люди точно знают, куда идут и что хотят от жизни. С опытом они понимают, что счастье –это не сам результат, а процесс движения к нему. Со временем пятерки обнаруживают счастье в самом себе – это их внутреннее состояние, о котором они просто не знали в начале своего жизненного пути.'
    if number == 7:
            return '<strong>Образ</strong> – искатель истины, исследователь, предсказатель, человек-символ.\n<strong>Символ</strong> – ключ к непознанному.\n<strong>Ключевое слово</strong>: познание, тайна. \n<strong>Девиз:</strong>: Познать непознаваемое.\n<strong>Покровитель</strong> – духовности и познания.\n\nСемерки пришли в этот Мир, чтобы познавать. Искание истины в разных направлениях, философии, религии, деловой сфере., искусстве – вот ваше жизненное призвание. Такие люди обладают огромным духовным потенциалом. Поэтому вас всегда будет притягивать все тайное, магическое и неизведанное. Благодаря гибкому уму, вы легко постигаете и научные знания, и оккультные науки, и учения, связанные с психологией. Семерки считаются не очень контактными и зачастую работают в одиночестве в своих лабораториях или кабинетах. Они лучше находят общий язык с наукой, чем с людьми.  Это часто искатели, одержимые какой-нибудь идеей.'
    if number == 8:
            return '<strong>Образ</strong> – хозяин, человек, который сделал сам себя, финансист, банкир, торговец, предприниматель.\n<strong>Символ</strong> – две монеты, лента Мебиуса.\n<strong>Ключевое слово</strong>: деньги, энергия.\n<strong>Девиз:</strong>: Богатство не грех, в ад за него не попадают.\n<strong>Покровитель</strong> – эгрегор денег, эгрегор чистой энергии.\n\nВосьмерки – люди денег и их жизнь так или иначе связанна с материальным миром. Это банкиры, финансисты, владельцы «заводов и пароходов», политики. Восьмерки там, где крутятся большие деньги, их кредо –владеть этими богатствами. Стоит отметить, что такие люди оперируют деньгами в глобальных масштабах. Они с легкостью распоряжаются большими финансовыми потоками, распределяя их по Миру. Задача восьмерок, научится правильно владеть деньгами, обрести деловую хватку и быть материально ответственными.'
    if number == 9:
            return '<strong>Образ</strong> – странник, идущий к совершенству, искатель.\n<strong>Символ</strong>– круг с линией выхода, кукла-неваляшка, которая всегда встанет.\n<strong>Ключевое слово</strong>: Дар\n<strong>Девиз:</strong>: Удержать на краю! Упал – встань!\n<strong>Покровитель</strong> – Земных и Небесных даров.\n\nДевятки пришли в эту жизнь, чтобы сделать Мир красивым и гармоничным. При этом совместить личные успехи и достижения с общественными. Такие люди по сути гуманисты и филантропы. Они по-настоящему озабочены судьбой человечества и тем, как усовершенствовать этот Мир. У девяток глобальное будущее, поэтому они и мыслят масштабно. Вы можете быть лидером, миротворцем, врачом, воином и отшельником одновременно. «Девятка» — есть совокупность всех чисел и включает в себя разные энергии.'

def get_decode_birthday(number):
    birtdays = ['Люди, родившиеся 1-го числа любого месяца, обладают творческими задатками, сильной волей и чувством независимости. Умственную работу они сочетают с физическими упражнениями и превосходно себя чувствуют. Чувствительны, но свою чувствительность не выставляют напоказ, поэтому создают впечатление замкнутых. Плохого настроение преодолевают, приложив не очень много усилий.',
                ' Для людей, родившихся 2-го числа, характерна чувствительность и отзывчивость, граничащая с некоторой суетливостью. Они стремятся к любви, согласию, взаимопониманию, и от достижения этого часто зависит их настроение. Духовность и мысли об общем благе определяют их поведение. В стремлении угодить всем существует, однако, опасность потерять себя. Внутреннего согласия можно достичь, проявив музыкальность.',
                'Живость, мечтательность, множество замыслов характеризуют человека, родившегося 3-го числа. Он может браться за многое, однако ему следует остановиться и определиться с главным направлением своей деятельности. Эта рекомендация относится и к чувствам, которые, как волны, могут бросать его из стороны в сторону. Невозможно жить без общества, и такой человек нуждается в друзьях так же, как и они в нем.',
                'Люди, родившиеся 4-го числа, руководствуются чувством долга в работе и семейной жизни. Творческий подход к любому делу помогает им реализовать себя. Они придерживаются твердых взглядов на должный порядок вещей, предъявляют равные требования к себе и другим, что тем не менее может осложнять отношения с людьми. Путешествия и общение с разными людьми помогают таким людям расслабиться.',
                'Неутомимая любознательность в познании окружающего мира отличает людей, родившихся б-го числа. Но желательно не заблудиться и не потерять себя в поисках знаний. Их живость и общительность привлекают других людей, которые, однако, должны помнить о том, что устанавливающиеся с ними связи ненадежны, ибо рожденные 5-го числа привыкли к личной свободе и не хотят с ней расставаться.',
                'Ответственность - одна из главных черт родившихся б-го числа, она проявляется как в общественной, так и семейной жизни. Чувство прекрасного помогает создать идеал спутника жизни, выбору которого придается огромное значение. Творческие задатки этих людей не настолько сильны, чтобы найти особое проявление.',
                'Родившимся 7-го числа свойственна вдумчивость, они проявляют тягу К учебе и познанию мира из опыта великих людей. Уединение, особенно на природе, помогает им расслабиться и сосредоточиться на своем внутреннем мире. Они обладают хорошей интуицией, тем не менее им не стоит пренебрегать вниманием к окружающему. Твердые взгляды, понимание совершенства и стремление к нему должны сочетаться со снисходительностью к тем, кто не обладает этими качествами, - от этого зависит их личная жизнь. Творческие задатки могут определить образ жизни.',
                'Творческий дар, сильные чувства, организаторские способности и честолюбие - наиболее характерные черты родившихся 8-го числа. Их усилия имеют внешнюю направленность: общаясь со многими, близко ни с кем не сходятся. Замыслы рождаются один за другим, эти люди готовы работать без отдыха, но им надо расслабляться. Многое удается, окружающие вынуждены часто приспосабливаться к их твердости.',
                'Любвеобилие и добродушие людей, родившихся 9-го числа, накладывают заметный отпечаток на образ жизни, в которой происходит много перемен из-за участия в судьбе других людей. Собственную жизнь они устраивают сами, не позволяя другим слишком вмешиваться, заботливо и по-своему ведут свой дом и семью. Художественная одаренность может найти большее применение.',
                'Живой ясный ум и сильная воля позволяют родившимся 10-го числа рассчитывать на свои силы, не полагаясь на удачу и помощь других. Жизнь может заставить их заниматься сразу несколькими делами. Не очень хозяйственные, но гостеприимные люди.',
                'Число Дня Рождения 11. Порывистость, способность воодушевить других отличают родившихся 11-ro числа. Им лучше удается то, что затрагивает чувства. Для них характерно непостоянство, мешающее доводить начатое до конца, поэтому для пользы дела ими по возможности необходимо руководить.',
                'Этим людям свойственны красноречие и побуждаемая чувствами нетерпеливость. Люди ищут вашей помощи, и вы стараетесь им помочь, потому что вам это нравится. Но не разбрасывайтесь до растерянности и утомления. Ваш ум помогает вам прийти в себя.',
                'Эти люди сочетают качества, присущие родившимся 1-го, 3-го и 4-го числа. Этим объясняется противоречивость их характера. Разнообразные задатки должны находить внешнее выражение для внутреннего самоуспокоения и приобретения уверенности в созидательной деятельности.',
                'Привлекательная личность, способная мыслить и чувствовать, может преуспевать во многих областях, выбор которых часто определяемся интуицией; предпочтение отдается роду деятельности, который обещает больше свободы и возможностей для самовыражения. Имеет много приятелей, но мало близких друзей.',
                'Одержимы замыслами, усовершенствованиями, хорошо разбираются в людях, видят их слабости и относятся к этому спокойно. Эти качества позволяют им преуспевать на общественном поприще и вдумчиво подойти к созданию семьи, проявить необходимую заботу о ней. Зачастую они хорошо сложены.',
                'Стремление к возвышенному и прекрасному в помыслах и делах свойственны людям, родившимся 16-го числа. Чтобы быть понятнее окружающим, чаще спускайтесь на землю. Преувеличение значимости событий и явлений осложняет жизнь и приносит беспокойство. Им наряду с потребностью в уединении нужна семья.',
                'Независимость, достоинство, смелость, настойчивость, самообладание в трудных обстоятельствах, способность преодолевать препятствия в достижении своей цели характеризуют родившихся 17-го числа. Эти качества предполагают предпринимателя, которому по плечу большие дела. Люди ценят вашу надежность.',
                'Твердые взгляды, самостоятельность, упорство позволяют идти своим путем и достигать искомого. Ум превалирует над чувствами, но и чувства тоже сильны. Вам нравится работать с людьми; перемены не удручают, а оживляют жизнь.',
                'Чувства могут играть родившимися 19-ro числа, бросая их то вверх, то вниз чаще, чем того хочется. Однако это их не расстраивает, они принимают вызовы судьбы. Зависимость от чувств делает их независимыми от общества. Познавая себя, они овладевают словом, не обязательно красноречивым. Внутренняя, личная жизнь может заметно отличаться от внешней, видимой другими.',
                'Родившиеся 20-го числа обладают повышенной чувствительностью, по-этому для них необходима обстановка согласия и дружелюбия, в которой они проявляют себя честными и верными, доверчиво раскрываются. Семья и друзья - благоприятная здоровая среда. Но они не должны никому позволять пользоваться своей доверчивостью.',
                'Людям, родившимся 21-го числа, присущи любознательность и обаяние, чувства легче принимаются, чем, отдаются. Образование, искусство, общественная работа могут быть полем их деятельности, но из-за некоторой неуравновешенности возможны осложнения в отношениях с людьми.',
                'Люди, родившиеся 22-ro числа, обладают зарядом энергии, которым надо уметь управлять. Им следует искать верное приложение своим физическим, умственным и душевным способностям, не растрачивать себя впустую и не работать на износ. Жить надо по наитию - идти вперед и уметь вовремя останавливаться. Не гнаться за выгодой, а стремиться к согласию между внутренним и внешним миром.',
                'У людей, родившихся 23-ro числа, так много способностей, что трудно найти им применение; много скрытого, незаметного для окружающих, к которым они, однако, внимательны и могут быть хорошим другом и товарищем. Многостороннее развитие помогает им понимать людей. Они могут выбрать образование, врачевание, научную и творческую деятельность и добиться в этих областях успехов.',
                'Способности, заложенные природой, должны проявиться, поэтому полезны перемены в окружающей обстановке. Друзья могут дать в этом отношении больше, чем семья, которая действует успокаивающе, например, при ощущении какой-либо опасности, возможно, даже несколько преувеличенной, Люди, родившиеся 24-го числа, не чужды искусству. С возрастом начинают заботиться о своем здоровье.',
                'Чувствительность питает желание во всем видеть совершенство, отсюда завышенные требования к окружающим и советы. Попытки переубедить в чем-то людей, родившихся 25-го числа, наталкиваются на их упрямство. Однако благодаря этим качествам они целеустремленны, сосредоточенны, имеют развитую интуицию. Большая открытость и стремление к взаимопониманию с людьми снимут внутреннее напряжение, упрочат положение в обществе. Природа и музыка благотворно действуют на них.',
                'Хорошие организаторские способности, умение ладить с людьми - главные качества людей, родившихся 26-го числа. Природные дарования могут восполнить недостаток образования, но лучше, конечно же, если они его дополняют. На широком поле жизненной деятельности достигнутые успехи, которыми они гордятся, не должны мешать идти вперед.',
                'Чувствительность сочетается с волей, стремлением к завершенности, желанием все доводить до конца. Острота восприятия событий может приводить к чрезмерным переживаниям и необдуманным поступкам. Ответственность перед другими заставляет людей, рожденных 27-го числа, быть подтянутыми, воодушевляет, вынуждает прерывать уединение, в котором они тем не менее нуждаются. Тяга к духовности, искусству, особенно к изящной словесности, скрашивает жизнь и придает ощущение стабильности.',
                'Людям, рожденным 28-го числа, присущи высокие помыслы, далекие устремления и сильная воля. Достигнутая цель сменяется следующей, благо есть силы и способность объединять людей при добром к ним отношении. При вынужденной бездеятельности теряют здравомыслие, способность правильно воспринимать себя и окружающее.',
                'Смятению чувств, мыслей и поступков, свойственным родившимся 29-го числа, следует противопоставить целенаправленность, а в растерянности - полагаться на интуицию. Привлекая людей в порыве воодушевления, не следует стремиться к совершенству, памятуя, что лучшее - враг хорошего. Этим людям не хватает умеренности. Обычные дела, дом и друзья помогают обрести себя. Им следует быть внимательными к другим и не стесняться снова наводить мосты, разрушенные из-за раздражительности.',
                'Общительность, умение работать с людьми, верность в дружбе и надежность в товариществе могут вылиться в убежденность в своей непогрешимости. Опыт поможет выбрать правильное направление в жизни, а поощрение друзей умножит силы.',
                'Для людей, родившихся 31-го числа, характерна полная самоотдача в работе. Чтобы чувствовать свою значимость в жизни, они в ответственные моменты многое берут на себя. Переоценка своих сил и возможностей вызывает у них разочарование и утомление. Такой образ жизни не оставляет времени и сил на личную жизнь. Для отдыха и восстановления сил путешествуйте, не будьте одиноки.']
    return birtdays[int(number)-1]

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, "Вот список моего функционала:\n1) расчёт числа судьбы /destiny_number\n2) день рождения в нумерологии /day_birthday\n3) узнать знак зодиака /zodiak")

@bot.message_handler(commands=['destiny_number'])
def destiny_number(message):
    bot.send_message(message.chat.id, 'Введите вашу дату рождения в формате дд.мм.гггг. Например, 27.12.2003')

@bot.message_handler(commands=['day_birthday'])
def destiny_number(message):
    bot.send_message(message.chat.id, 'Введите ваш день рождения')

@bot.message_handler(commands=['zodiak'])
def zodiak(message):
    bot.send_message(message.chat.id, 'Введите вашу дату рождения в формате гггг.мм.дд. Например, 2002.08.20')


@bot.message_handler(content_types=['text'])
def message_reply(message):
    #день рождения
    if len(message.text.strip()) <= 2 and message.text.isnumeric():
        bot.send_message(message.chat.id,get_decode_birthday(int(message.text)))

    #число судьбы
    match = re.search(r'\d{2}\.\d{2}\.\d{4}', message.text)
    if match:
        mes = match.group()
        number = 0
        while len(mes) != 1:
            number = 0
            for i in mes:
                if i != '.':
                    number += int(i)
            mes = str(number)
        print(get_description(number))
        description = get_description(number)
        bot.send_message(message.chat.id, 'Ваше число судьбы: ' + str(number))

        bot.send_message(message.chat.id, description,parse_mode="HTML")

    # зодиак
    match = re.search(r'\d{4}\.\d{2}\.\d{2}', message.text)
    if match:
        data = match.group()
        data = data.split('.')
        response = requests.request('get','https://ru.astro-seek.com/vychislit-solnechnyy-znak/?send_calculation=20&narozeni_den='+str(data[2])+'&narozeni_mesic='+str(data[1])+'&narozeni_rok='+str(data[0])+'&narozeni_hodina=12&narozeni_minuta=00&narozeni_city=&narozeni_mesto_hidden=%D0%92%D1%80%D1%83%D1%87%D0%BD%D1%83%D1%8E%3A+%C2%B0%27%D1%81.+%D1%88.%2C+%C2%B0%27%D0%B2.+%D0%B4.&narozeni_stat_hidden=&narozeni_podstat_kratky_hidden=&narozeni_podstat_hidden=&narozeni_input_hidden=&narozeni_podstat2_kratky_hidden=&narozeni_podstat3_kratky_hidden=&narozeni_sirka_stupne=0&narozeni_sirka_minuty=0&narozeni_sirka_smer=0&narozeni_delka_stupne=0&narozeni_delka_minuty=0&narozeni_delka_smer=0&narozeni_timezone_form=auto&narozeni_timezone_dst_form=auto')

        bot.send_message(message.chat.id, response.text)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception:
            pass

