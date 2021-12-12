class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        ''' working solution except it's to slow with massive strings
            one online test case has s1 and s2 both at 10000 characters
            this took 347s to process locally'''
        for i,c in enumerate(s2):
            t = list(s1)
            x = i
            while len(t) > 0:
                try:
                    if s2[x] in t:
                        t.remove(s2[x])
                        x +=1
                    else : break
                except : break
            if len(t) == 0 : return True
        return False
    
    
    def checkorderedInclusion(self, s1: str, s2: str) -> bool:  # 
        ''' looks to check correctly for ordered matches either backwards or forwards 
            question actually seems to be asking for any order '''
        
        
        f_char = []
        for i,c in enumerate(s2):  # find all positions of the first char of s1 in s2, write position to a list
            if c == s1[0]:
                f_char.append(i)
        if len(s1) == 1: # if s1 is 1 long then try a simple match
            if s1 in s2:
                return True        
        for direction in range(2): # loop for each direction
            for f in f_char:    # loop for each matched item
                for x in range(1,len(s1)):  # loop for each char of s1, skipping the first
                    y = x
                    if direction: y *= -1 # flip direction
                    try:    # used to catch attempts to search beyond limit
                        if s2[f+y] == s1[x]:
                            return True
                    except:
                        continue
        return False
        
        
t = Solution()

# print(t.checkInclusion("ab","ab"),True)
# print(t.checkInclusion("ab","eidbaooo"),True)
# print(t.checkInclusion("zx","eidbzxo"),True)
# print(t.checkInclusion("red","eidredbzxo"),True)
# print(t.checkInclusion("red","eidderbzxo"),True)
# print(t.checkInclusion("abc","bbbca"),True)




t1 = "lrxdxvfejdkrnjillizofhtcsnsaayremyicmvfsfuxvmlskswyfjwxdnotttdfisbfnoldsfaarpaesaltnvgrdoktdnxwgyblyshlhlubpeamxfrsfhtlcezzwsjtvcmzkpvfvmhphwksghfnzhbwogziokkkhgvrmndwsjjsegkdfobnecberwraetxwdxemzpoakgnovqpjgslmakuceqdorytxawxndpbkvsbalgfkreaplyrkbxwzfdlzsmoazxcmrmattzszqehtevafgiurhjbtfmztjgozkunklacupomjjafbzjerxlvgmnsjqcrsrbrcugaofbiuvibjmekhyddhwberuoaxfghtdgjwbjlziraohnmkhutuyftiptmdeshtyhrhtdkhgkzoxnulfqboeimlepwyihauwjsermzmefzlkubovxhrtkbfhopvhwuukkacivimrnjaxmpecncgxfelmcfgnqueelqssgpxpidtswwrrlusgwznwvuvdahajoxflexnctsgmjchtgfwlqsfyoamaaaowxttgshiszohczagbgpoqibghhawdjftrrgpuailqfpwzvytgwdyqfymihyuwhxzhawpoxafxvnwvkhwubjypxjnqjkfblpeoxewtjfnlgiwfkxuirhpbeyokyrbnmichszrsntbaxrdiznwfiokbuhkwvmhtunabqninaztpcvzptfjnhtxzjuupwvtsaateiuerftqjxqkljxkdindkrnsmuhouhpquabwanjeoyaheqgdkdyqsqdzlrdwyrakfdphasupvuhwvtsesrlubcapcdzutmiyyudpognnmmncgphgmfdozclwgvxhhsbxaexuenknayihkarjrbipmnujdfqfvvfbaickybuacyuutbarjsmveivscoktcpfzwlcjemengveudvdlcdjnpbjbimokldsbjlsdasbgjukkoeucwlhtmkxhbrnczapqhoyhrqaogbkeqsczwlloqiguclumiggrijlymcszkqnmgtzjcblnylpigzbwiynnwojnkyxnmgoodljmmqcprzznsmcruifltbdujttnpjnttlbfwlclgewsdcjgbtuzwsayatuqvmebtvihljkaewfnqbotnmkabcqsxbohqleqlrujvughzcurfuhmhfklbwbaudmyfttsikiwzbvlfwmetgsnxxlmjofrtfdfcsnqbyeecgzelovranroxccdaqyfqtkjxeqehjoeqytkaombdgfajafmvmqzzxfaiezovbzcyihaucpeopptarcwihwklrpvtkqnbbquqnlmdwygbtkstzwdznbevlyfivqflpacmtcsarbbkmenyijnjvwlixhmqrqrejwznxzdiqzrrfejxfmcdzmfkjvbwfmstilkrmvviywuquenujtcqbhkyxbnbbdoxgyjpxfucdmsecnzstjlsivelupyptdogsjepgjtwgoexaxjfduvkldfudwlxmnjyynypvdvgecyhflaiyrhbqmixmwgsehsfmxyjzvkioaexjbcnakbakbrvtwgghwhfsffnamcgphuqqxqvbdmfhrzxlgiunazqhfsxgxxwktpjicnmeaxyhyfauegcdiykhuouqqnybgxcazckmzriyzuulqeqtgjuawvissukncpataietvuwirkaifroelxsptnolduugufycgnvamsardwrueajvhqkkxkkhzphbuqbldukjdqcznwscvnnqnwxszplqyfuctorjcbucxgfctibwfxftrdliugohjgmbxqduvwgrdmmawyhfgkkbeojyxkoftuluolffjvygyzftmcuthegrxdkyegkucgnukwvyjqjeewteaivfoybrwaceyasgwxsznkjzwyfjoiqeclwlrnyqdxmzadkjvhjaeghfcaiyrjefpkyhslkeogzgijtdymtwcopbvhzcqficucdfzhndzddunzhnkmllhjrrjcvksisdphhmqcnsrlmyygxhlakemvncrogiljrtfyvdrujjwowwjxbjxpjhebvheexkniipvotlumxpjplncxsrezcxmyansqmarfwwtwngvcgqcijzrhvlwalkcdsrccschgudpahdvlunyzbrdfevmnoewvavrklwvfiilgtmtexwzfmgacugaalcxqeplsmpkplutliqairwtbytsxzlupqplbpadgsiuazxvrdwjzxpijvwytgmsocughjqwbsvozcfbflqgokqjdxrivnioxcgefxmkjajkwllqdcepegzzylflfqxclhsooylinxpalctbxsvbdjqmmcyqfgfytstbpmjgmqhmnnesgovyzwsatnvqallzdjrtetzdxhckykznmnuexzsfyncndzbqstxwppzjolipszefzxqoyjteoykmrympogufseghdqlvvipuwfzheescacwrbxkaqcutfrngmzmqxeeorppkjgdroxoqdkyaawrpcjtfxzlfgkrguphggygibcialnnkvlnevkbapazmpcguhmjcmizjsinmqjknavhumrdmjnbscndtfapztvczvhkpcowavszavfcwwlzdddpuliglnjucqziltqwlsibodwdcbmorwyyqcvwoesjibeqcgsbtcelowxtzryhvepjcqnpmigbdbuplezwgcqekhxzvsbwlaunotrhhmdrrfjoeyzwzygeypgpxonkzriqjsecoqdmeslcfgnzlwstigfxogzwrjznvgtrzjdvdiaofktlzpvnjftauzfmgigxuydyddabcucklupsjycdbdzdghkiryjrjuretnulfczhhwdoayrrvljbihhbmxvzyjxrwkpmxxephocpleznusehkxjgjqlalbgenuahcqzcbvnurwvtwvrvefnkdwywtokrxhstwwybamnixtlokktydnuqrnxylazddpvdbfhtevujagbvqkbjtcvedzrqpkwmxnsugrklcimmgbjmnatgmyyuvnbuffgjcvclkglhdwufxclndhyvoecrfqfxtmunjqavkrhyhlltnxwjsdzvkmxayxmgvsoaewlergrdaxssqtavrkazjkamfeyvttdytukwsqxrevtfquuanjywitzajgdlsgonmxjwxqiekadyohkzlowywqrmnydclodaichygaxhljvvlnbdpsweicfyntnxmaxotdnizxdfkhtnegosqynavfeludbsxylfpsxrnasizvozwlljokgirgewaskykpclgictznfysqmwpkyjntcvikxapgxupqewswsuqcnlajdndiujuwcfjkhysjltdbjjgxgnbovwzrcibzwasjoitdrpyureacgvdupxpzqepymwjxruyxkjhlsgiddghluhkomqmpzbucxryifzszpmknuakmbmieksazgsmzpuybfdlpqlilcqfewgqkywbianhzgizbgkruslhepkllojtoewgrhxmqlziexxfacuzjgvpgbusktkkctzyznwycsklkrrjrvbmxbhrhpwaketgqdubkavullzlhxdahukoajvrjfdmcltylxjllnwycvbcddpxidjzhkpwvlbrnxmnvseioujesuieatdxcptqprwaukeqdodaedzbwmybatapayautrbyayjxtnvcniqleohffgxgsogwslduzbpkaxtxwzstjftgriebrlthrhplhpqtglcjzoospsolqtofgjttxzpdceficxvxvzkfbptevvmjiviglepvhatglwgbeywcsgrqrttwjblyskptgwkhlyudcxolbkajzjeuvdbdourryxldpzlbfombingjbamxelfvqnusymtussovzxkyemigegqlqoprynkwuwhxmvkacwplrgsdxbcoykxbgfyfuclxcaxpzqgukwkbvrcmzvuzinucgryrnjvgysihixhcknpfgjmagmlpihnnbniksegyxybmgwsqgitctffwgudyvrkhnnuqczybxadjfzbakmrpzqgsfdtupbrhkyqumimuwwtwaugrpwppfcgpxkumziermyqqrihufxtfklmjsipuyimbrfatepkufdonqditpcnxbanfxfhmmwutomluagakhinnrnjwamaztgozkpwyxipxlellbszvgewelbwvkxxvrmtvuiivdgdfpwwuwvmxnewqkpoocwbzmpbscymmrbrtaazhpxvktdoukayngafglbvnmvstahrlsxwumubkeceevztlzwiyfiwtyuiyjbghofotfqpygwvgzlzieajohxtnfwfjtpezunhtezmgoijeullayhjlrklddeiujhukyhgvwhztrvrdcbxhuvgiwmjwetjmwzoipopdegynbwjbxblgkgcbeljnlmdogjlmfcebkpsdnojqxzgmmwprbvjnvghxqbozfmbfpohiwtmdzumxlgtspaodgmqrykogolwgvklwvcxuwqztapgggossaayeiyramtvoicssnfouddszofopvrmkhyihbiuabdzrxflubidzkorufphwqryyznzlcgffamyeacfjvdkoilbvurswxuwbfsgjqhsajbsbvzxwlsazxgfmnlilenuuowslmlrrbzpkmoelvhpvqdwuutwdsowwldmuwzvouqbynybgnvojeyzvpsyzyrmreeahzutgbgoinadnfnctsezjixjdqkrleovfjydtnndeuycghsuwioyqjpdwhqtgrazzbxfwgykjbvewxrrcdykuomrlhamlhxzstykmfncbbkozncogbthvdrttafboicppqgfuvutfsrdvpnvavatvpfcpoczukoyskqyinzhpdunoxffvjpfxyxnelalhnwmzjzcjbndqkutxlekciqzxsgdynwvfuhkqlssuywktmsgbrazfedmjwfjuoxroanbipuiilqpwzdcbalwdxxrpdkwdrjzxlczzbwxlecntxgstkhctsdjocleuhmstcqnvlgkedyibdcdohnzxavsdbjvxucnuirrjenhxxtsyunbydyllkijehpwffykdjygganbiypiogebqmsndzdkqyodabqrwitrmhwkaptgrtfyxfjtdvyhbjybfftugtdocvomcsfowxbdhncpogbyioijutjgxirsauzvlvjktllxucqyniowzappgxvngghdpdlyrzvfzonmmijwxxbgvaikrswfefrruptiabegaomcjjnkfoazlyvdvppywcxjpjbxauyejrfixnkxflguuqwbuxocawwuhvhlvrjcklekcwocblavcitgpwmuxawxrvgiibgozmuyzvyonyvgyxlezcajxchiytjoaheozixofdgstnijliogyvfrlmaepvifdrqfrdufbuhqjqiehnakvcqoxaskpbrrgynnkqvnzhkbglpaeqdvqxxghuixoydcwupbvpkelrzfwlzenzoqbulgvvkowpddxcpfrigxgeuccqvkzkfplcyyaqsheqjwosqsevbuvpglnlhtoieubioskacdfpvorogamnbwnajomrdfrzgkufouftmdiowtxkmbktzvvnegotgnzmklvnhmwrmajxytpexwymfxcerimsyzxhraehnhmshkwmcvaufbsycfcdjacgawmvwvmvybwqajhflxmbjenkeyvyullqyxotwkrtdgglgrlxcjiicnsutkjldirboqlmvfrlllxtiquhfpxhczzrmumznjpwcfmwmemltqvkhskbchpwhqruvqnqixbtorkrhxomtuybgudzonchsslxyslgzecpdavfxescyoitwqxnvcsepeonbuzoyoeypezouczbzzbnmzccgkhmwfbmeicmwqjdegmbbckgioqwzapatrbeedksjspndjlvljlqqnesduhbbtmgrzpbjhorzhknjpkrxznthoxsxxrnppmalnehvkkpdoskffkqithkqjgmtbxgalntgispxkgqvhxcydzfsdkuwdzytkolzmywtsqqbkssplynomcsnfethndaicofgxsaslupmgtblvwvhsamejhvdqhuijdwglfjpfagvtjmmghikfnetdewtwqgsjwtlvwjcifwurvaqwbcrpiqghnntivzzqdvuqtucbwustfdgpqvvneouriwiqxsyrultkiysyqcgijkiqjrxnfwrxahlkrcnodyjtfybfspqckojtriwfojgpcetjayrgjtrzigvtzosmohlywfyrbtryxhlcbhadacpplueillitgruqhexwcvhxpphbtksuirsnjnxvxyyiibloqmrevjlkghynenizwpkzduifnlfksipmljdujwqafywlvagomisejmbrzbxnogrdkikdvdgfwvxdoxxahtskkyonwlaulsrdjzokijupfxwdsqbveyieuwrohupopshocaeqdnsphawwnvrzkyzazdccnyodxpnuvjshmkrtmcklnqyeoovlexwksutsvhkbrhjhhodjidvkejkkxtvqtcpiiooltimziokpzajzfvpylcoxyglbkrglvnzftsmzmxbovviavuxezpxezuxzzfrefvbukfuwzhxzjkfaynfcjvkvbndrdjqdhnsrcxicxsxfjsdpvsmwvpqijeemnknsofeqywovbdpdopggrfubumvranfzpmehzuqgykddajkwqllyhalnyoylkyoczxozzrebnwljnbxvdxnaprgqwmfjeoyozqwqlwudlxjpuukrqupzigbvmoysjzpprcsusrzomywxqfpqomtztgrfggyhbbceiniofjaghnlucvtfdupgbhbvnfvtgexgnvjvwdtyxxgxxvgymtfigraqskxvnehqohwzqzkhxpifqrutlytfverrlbdwfqkiejvatuzccuxtousmxzppnkngxanzjhugytabydqynmnocqlcdxndwohtptktjdrxgtkvqyzoimgmsomqtnebsdvvrdhcalhgsuoglebfdhafgezwjnmgoshzoqffbtpilpberqitxkzyglpdkcwwvpdqjzwcvqiazhrurnesjrzmvwvdboouqyfhyeziceekrhncfjhdeumvxywinudsfovinwxsbconemtexvfafxhaerjvqnkchnsmgljwdddjsgcadvavlbnikfwvdsckvluigdvcfuezfxxxkrylxsnhwuduhfkdakllkawxmyqbkbzcqjmsbgzfpojtlpqvgtqlmwurarmavmmiatpfxvfzfqacptkhjgobtcsnazpbroehpizwtpmrclahjkkzcmmjznsyaglerbnkzetxrojtsqffhzliqwzdwefypaotvgeiawuwxxfkwlbzrntcaloqbubnyjdnsspmmlckzdpllmcncvrkdqrtmfbbbjsmuamsiipsqzexrckpcpnfnhjukamxctwsbfrcuuccbankpotvedkkyrmbttbzasydxkszzdadjlzrdmzbqtsqazuxeloeutjxdsciiugbwvfvwykptjbmrlxkqxaytyzubavioljyymsmkdzbiboaosucwfvwovzwcblglzdwuiffzclexudskropugxsszdttwruooehksqtgwabwrqxmiqcidjpadjbyldjmgfghezqzkqolfueavyousvfmyuwaaluszwzkgalilmguoiecvhsawptpskudkmvbniybaslympseyyinueidogmoiedkqvuoywnduxctjjvjhcphtaddsasmzrxwvfxkaypozvnhfalmcwvqcaeszthvbqzmdohdeqkfdeeislkblohlxrxqydoogzevgsbzhgrvyxvpgyngsgqzodgrrtqsbnpvfhybjgtuufmmmsekzmuyuejpjtuisqkrptauhsjcllecpfyttiapogqylltbjhzrjldccfybxsionmqpqeyusrtastfoqksshmziezadeogrojwcanijxknuvruioetfexnzfejkkxlxrktswgqdgkeznvyzwkjlixlxxprkbtskpjezoycykjtxjorxiydrgvftxttaciifiifbdmbhozmuftpvekolyxcwnzhwgmzcsiumegewfvyxwaijlgwnjpxohsfkuxxfytbvrkcjzlnxmmcgjmpjzbovcppppmpuvfcknlkyhbcaevgviusffgceekjwhswxhupfrtxhwhjmdtiicppzkcplcqaifzjzfnbbtistgucduxqprfughepxnkzengymokugzokudxesaoflosfcxdulhdqlhebhmuogzkqqmvpsrnljwszawaazgofirmswuogqzdbezgfhydcgtcmbipuuvrzzrlvsuxqgesprlrmdtvzukkyksflpojpmfkurnmjslxvkrqbknmmeavkiqowseqiionjffctbfgvdlgridoowjwflmdjdjpziiioguaspnacxlwlyosixpbxukglrnkzjtcalatqfxqrdrbfqltsgonoyzxaittzathzvrtjpmbnbnbuqmxfcwtxvnafhiksmbjxpxfshqkytwunhflybohwzuvvpwaqlwdbxnnzdnpikwnaxjyldyltfoiyqvhzrysfblphtjyaizftfmgbbicjfvbbnzjjofpymyrfmihrssgxontbmugivvupgczbajxodcdfutzydnfzwogncjrnopjsxkxzpxehitpeduciiiwiowxlbcdjfekjpzhdlmtkckhldpwcqntqnoftmjphqcfpydbmkpgwjpnjcgwwshltewdooxmzmmhwpjckxbrcwismkmkgnduvnbnjntvaaasxocisoreldzcpmnftluzqrvxpftrrvabdojqqklqvssptacdcnlejxgjyvreamirjwvlbdvyuuolbcdgoihylhkpqcuokyyfzzgldesantmyoqgcbyrkdzhhteybvgbeeektccdgkvmmywzdtaspyuilnmziledlzxuhpmcckyxiibjdaxgqmxybpewnynlwykabudmtmjwoujqstusxfkpnbhgjqoxxhxcahezybokuanmqfbotwkagqqohaxytqmeruwakokwomfnrdefuljckiixahakaxsdyojvutmdmgxdiegvlblyhogqlewcddesebpzleihfcrttmkewoalaxathwluyvvfbavhjsqkttzodstcekbpnthsvprfijukbuvtlqedjamwfahjhvivcoarduvrhczuxjbfxzitlorrntwebjauxejwpswfksxbtecdmwvtvjgvelliisqtmbfazilmmizkbqiifokdaajotapnpkqhdgsmxhtndlupujojefwkasgsqgbqnhkrxbfunnzkfdtnlisryccnoobvewvavmhwejomytxxoclwutmthshxdddpokdprsfumpcmqhbtwlmdepchvsfkoyfzlsxnrmmuxlktunydlndafnvwhkymapyfwwgkljzufstoofyguubmmhgqplgyudbpopzvsijjerphhgyqqubnkgqlqhaiyaulzufdrarxaruxhbzeowebppjirmrnffrwcmpxgpeonfndbeivayxqttgjqqpizyuiupftoyvaxxxqqxdnffhmfmtcfkocawihcyopiaxvjibugwitexixqxsuxyubcdysmgzelhgykjfizyuvqmiajlokobiwmnuggqaspymnwfvorlpzjikffuctkjlpsrbbnzpjqgxxbjfuuqkkvscynswjnmfrcfwwjeqntczherfhjrvgbpiqfkhsgjirldsypktnjphrdiuaiiuimptnqofmiqqlqvnhwiitgexcjopbshfubrlsdbvcdfdtoufxiphxrilhemygjytnzvabaqjwbckzbcpltovszpffbzvhlbatguhjufkjd"
t2 = "ylcotuazxfmsojotjtnjnbmiestmchaxbgxkimkcgtcutoqfunbgnastygeqvljyjnzwssxenqcqmlsfsxyznxqauakdjcczivtdvzhyfyzzzolhqfkaaazkjznxzdwicdrhlbxnwahwichaymehyqtwimnxpszgpdpakeuyqudenyntlpogkitjklxqsalvcdsptrhgdpmuknnnszmbbcroqbasxngigfnuvaehxbfqpmvkmmdlofgemxhordbctbafsvwutdnzmemmvviwubpgjsugexoevbbshdhguvhhvdkstmwbhtygfpzsjuqnxzamcunrqpmceteowiuqrstiqwisnfrwjhlbplwhlazvkobcbzgtaszyejkpcwnpstvsydjfrastxtxgsaeotdgrljmjtcykqvmcwoqjyrsuduekjpmijyotoypocpadvlzlxrpqojoboyflqecaqqkbkuugezkvvcvkuapxiiommosbwnrzxkesrsmzolwbtkrejjmidkbjlleqjlbwszdujsvryswyjmyetbmevrnnmosbbrdjnrfpjunbujpyvykqvwylstblxsqgxfaiiaxlkpkqypseezubvniivhpuzifpdylyrsvskexspzrjppzhkzkhnthtiwtwpknlyyqkclkplsdxtlxcmaplljxyidzwtykvtopfqbckueypiirrugnpvzraezxxmbexalqptvqdyqehyfnvdxmfazxkqzhgqkjdwqqmykvyhfaojgltqwrsesothqrrpdgmepgxtwkgwkxzzdkagvvqqhcsgxeqkajpakymxhybbxvfybgydshwneensnehanrrpkqkmxnyizlficycvywfdvynbxbxkleuhzqjslbolebykvqiarifxbofieboyollxqukpslzlorwcdadmbalgiiyarhkbevhsydredoafxtbkbgghrqrzlwyxpyxsesqobqgvdrjnrtefywdscecurexmqcvjhbeareyrzskicpzxslhdsdilsvdzejjnzuasswomocgmpvxoyolkbvsyvrkpfgdoljgaxzmjrzbsdqqferxhntuklenqcofnrcisedichncejxujhkqbluvckvogiprrmmqmjivomhhduyhastanololwdholknufuipjgadcbkyfhhwmlspckizotmqxstturxhvbopxzatdbcbftsfkvrnliswnlcnfjgztqiilhtrfshrczhwrdgakwyefdcregeybckvuxgefzqitllufrcrdohjrnvsliidhotpfegytotpjgrgvxzuxxmfqsslvleslloegsqiniesztdgqoniyperoecuubmkniqxdrpkautdiepqsfgyeyhcpywybmqpicoxjktqlhdowlzqnkywhbcszahuhdzusjrlytjajkhbekgkhfjhyehaboyodfyemvbdpumpwpepllwnkglmeoeutllgmnefdfsjjrhwncdjuoglolgnigesopzcitzmublikzvbtuwfmlixiouohygtpecaqiarvlvjquhwgskivqnugscbhwbfwczbomoyopkmcfawkptowxhcoinryagwzwqzrcvwqypuvudtqqootykyxjszfnwamnnawsrzxujldwqecjvgqasndukzkhjlglzafuuzkpdopxvzbfztszdbixxdhwuvtmbpgagodfvbkndlfuqsszddpucpcnkkafgztnthrhtviyusxpmvrmxehzihiloycjtxitiysabkskfgadgtanjgwtrtjblxdrpffwxbxxverdeaocyvtbiuoswdfslupbvvljskyyafmafpordsrcxgwhsrzzavxrxyalsltbgpazjsnzszbodpckrbgcswoisqpxrdqpyrfrkmzgnxkmwrsrjpbxdsygiavwrjtsvdrqcqdvcksifjmkxgjjbdhhonsmeeugggzwaehrkksqyuxfiujqzymvshundzkwufqduffudyiwgsmsgpcjcjcjoifgrtzcwzbwugksbjwnagrdkoyupijuususnidrwhutyumztdjhkplfoidxcpecjonvsyyegvgqkkgiftkpoiilavundmhfvylqyvmrsumbilvwuavxaprngmzfjmxfvbvifdujwkufbgdxvtonpbixlgwhaqywmvywqffjxemjyvimpdspcypuybsyplwpmhmoxjqxbbthncmpgtupboupshzwcftfezekfeqbtnznmicivderihfnhzgwnlngzaxmfmguhjzbrjnuvhfcbwbmikizkcrsuosadtdxtvybloevrgbvbqapepuoagfnbghvyczrfuoxfryilptnqvvekkiafdpqxbeebaavhaxodgignoovzdslkjvhhbfrcbyqkxdfpycxxbemedznmybhnmrlbtyaslixovkagqzcrzmuuqmnrmsbczuwazwzbpqjuoztiotejzfhmjdorvdbltqfkgannctbfwspwpplzlrwpxtfknwohsjwkypnccvkudgtkgzqcgrgpuvuhbdbhpcryogpuzozmcnsvrnjnjqimdozemipvdmurucidhtfwqfvvfvdjitdnzguxfmhzpakfacbodntjkkdjlgarjpdvwcmeorpgknauhqmdkbwosxgdgffgnhmmgnmggiemabhzlthcaffclixppqpahguysacoqroiekpgiflcaqkkzothgyfseissmhgknopogzfinuchyfwjsjuiiksttqpwjlyimcjnmalpqvbtsldznqwugkskikroefgqjnvzoplgfkzuqqyaalnefuircgrhwbshxunccnrdldxybkrpwwziakhemeusnxofbqqrkguncposjyljhbpyrzuesxxanbjxmuuabbrwezrehgfwqrqyflmmlydprpfuhecyqvmnhdrgffpkfgaixkrpcrilctvthuvezrudsmlnexfnkzubgbzatfcjjguufflaixwjgvgpcqyuxwsfnowafnglteueffzratxnqgibwtvcygoppgcnblumxfavizherpzfatmrrliswqegsdykjpbzehnexbpmgebrmqasodsgxodeqfwqwnytwtbkfydtizloygnlilyujxvdqeoquovhdpsnbltlopwhjwqzzwstofvocpnmckjlwrzaxrmvbfptucbnfvpqxybsqvekqugkcjcdcdmueoovkeyisnsqlcowimxzuvwpemluweeiuesxzlbrwehzqprznyvpwsezxgvafastynbrmuqchfglcowjvhevwuubhfiormhtlrhpeytnidyzppobjeclubjigdrmjyymyxyelbprgohpberhuhcuyvpchxqqdpgdnfgtmauvwidlvmlacdqycievmjdmbplpcczwiitflemhfesyhulkgnlftsyddxpfjispiebmzafbqxxxsbejocgiigvrwmqfcganokzaurismihwnikkmsdcbmfyfcuutrogtjlttaxnolsieihxvubpcfmnfnaiswjaoumfhmivzpbrraeftyhgirmrvyczfkssdnqpuhmjafvpnttxoixiwejurkijzywvanfxvkkmgqtqytnsfntetauncecthzjxfqrafouhagkrdsuxcxnzqaiytfdiqtwxkmhuhslnditxhjmmuijagmrrkpztwwftsvedtdtqetluqmcepvisnwvsonkxqelxiatbhhncoyadghlkegavegncnzcstexayayoupgwfvxtcjncpktjivgruxslebxukudntwhaftyevccdhwodugpdrqfwpzpztvthlmhfscdumxqosrgfswgmszyqsetwvmfhxlhuwulpvcsosqrlvzklksgimahvdaoxqakuvtpzvfejrflixyoyvdyywcfakndzhrvbdkrillejoicbpmhcnvpyhcufaezunpkoripsbcyurthkvnmkkmjsvvbpbyzwcjrcoemldczdslsezavblhzoxbbyjfuhxpbckhbkpkcdmtcvudsoqzbnegohzyhxwjsjiuzdtbjbegkbrkpohrgezmtxdiaghrfrdavhidckgmmkspminalblvgbauwyznpbtfpqzjzzlvzikefcuahffddmbjqpeflwgvsqoxmbxpxadaglblgroxqwgejpxzptlzwyfuhyziahpsyjljqyzewzhlfoctchirzfoxgauqaqmgzjeaktteinwhjtkxsnogefibirkctyuxlygmrarvsjvkytfdqcqlydebagavluuwgehlvuhcbbmmkrdlbnyqwlpnkfgmjktwuwtwtgaiynackkkvsbnkjrjznvmfeehzaorkyimgemzkwjzsejtzlbrtxspqhwjfsdbikpitqdissqjjginuptmrdhhgllrmxokekfldwpgzbwyfuctfohxrhehjevtbeiprlorgbuzxoogyqdvfgiblauogzefsxjiieezxqrqqltfvpasjefjobdqwdsizqntjeianpwbyxlxuqpasjvfrccwaumnvulwzfxqqkvjazxnicvkyimzfyhatigyhinvdqswpddpesgxrhdrpajlndymewtjpbmbxzfiqhviypfdyhlkbqjszxnkiehwhiezixdomsubvslkghkkxqgxzqnrizzwssgdbkgwzivfqtpwvzapilhmxpxigjojiosnkrrywoyjppcqgmuzfadytjjdbtrxeviprznshajjoqkjwdxeouuvehkszilakgorfcgkbvkpiwdqjzanxodhancltmjbjkaixxrcwvpccmzczysfokecjsaurtwtxgdogvjwkizbyoahrbvlsomdoxskcmvnorzzsjgekmdshujurhzowusqnlzzwvzfjzpmpnphoaockosikekbhqgfsqxqwtsuwmrieviwbygbgchtawboxwkhzyyosppdptngszaouukrkqgddofeiqsvcbzbnrwebcgtriehdhvifzxfjviwooynjzugjhdjstqszleaklelphlmippragvevsbkklvhluozuehemcarroaftzihnnuadpobwmvhxiouuwsfcphevzcuizvpctdjkpwhcttehvaivdxsvesgpyovtgvqngkppilqanxyeajpjgndkrromomkqfuwvnunzdqprzbgireucpvfimiyfrsrfeaibngfxhjikrktqcjcfbobbdpqrinprlmshfzyescgoqkpyhhujgfaasggpgujaprhjbouizljenfhacaobtvbwmdvilczkugwgeytzayoxobhcwgyzwsbonvwfjfltsycnxltltmntekdkhahuvwqucmtzsnagdmgflqgpybsbsfiuxajtrjrugpxdymrmjdllqqsgcaqvuuokajeubdryouyopwnmlqqtlfwyngxybrvzhzxvqyigoqcziemctkggxynbtgnlegyygyxndkbondpofznylislptfvxngrbctfpvyxlooujbccupycdfmvmailpyosezhkrctdxdycejuvvyscfhjnhdjqetmpmdnyhhprqaezkcbjjaqbekiutcfenaahsxmheisbvvtejkpxgoocpcfozswqsswvdzprzvyyitspufrwchskadjmrisuxuhxnnhitvfkwqnzpjbhzzcrbaxqapgcbihkifiqxjvopnyelulrauegwbuqqaoscuoawirzpfeidhtwqcnujbyrynokbfajnzjtctocfepkpzisckezbtkuqbivbecenwilmccerucgcnboxpmgsoojgqtxevhvmzecvktucxbjmirmqvoiebyhkzqtouiaoojigebampbncmiaqojbkgzakijdahjmtufwcxrmjcqjfzbrwwtnctgzhztefngvpwtdnqrrevzctxhkzckugtgekrkbmglenpsknjcvitacouzqpiiumixtpfqlbvzsylurbgytsszhomhnsrcccpczcqpprcopgudufouncsynqjwwtdqnppblgwhqhldkjmdsfiqhgvpniyeznnaxduqpwfdbhhbcoisuphnbynoocelojbqvuxdcjvwxasnxejjczuvrmrpcklvcijphbghcnbevagdnqfykifozsohueivxydchtmmawdaoiywhdmhpkkhtgyvgtdbgvcedwpocfbuibbcjqpkjlzdjsbanjihuwwvmchovjgwunonvwkqjdqrjkppfekjcehismyrbwrsikxuthwtyyzsikpdloayjkwbubwuuzyueyhpnbljukmqsugtzfpfyofptdoaxwtfebwqyezclnijfhykymgmyjadsxaxpzhaiqgqkygamatbpaaaevtetyoosbwvhferwvxcwzayfpfkgyvjgakyqgouhimcyccputtsrwejwliaxewjaedfyxhhovvdwiofccjjfkcodahiafzhhcundpsdfmbxlfrldyceezushrrmbkboaneauydlhrhhqfslwsssflzsnpmtqgsexgxvupvlvuucgnvchsayimzqwhegmqvppzfnasralodsteegzgdkabhkoaaiizjhxghxdshwqxpgbpppnazfchlueyqewpazmnitxjhxlmjfwqubyfpzrxkcjdxsnvdntqkohgsbrozewitmlyxiscjmgyprgtgkqzwryyfdptapcnuhusbncjyusndwbsxuwxlewjcmskculeinswcagtyomdoaxoqnirgsgvrqcsofzzsesgdjmwrnyybjesxrebxkjappjtrlloiruslbypzparqurtqzhnbeiraojtebexzzeofeqwiwnxdrvawbsnhwawncywlyrvmuwtdiyvevuvvndslhgrussnpzyqlmsjhzeyufdrbqkqfpdnnlhbpsgyswrzdfuzqhvftadiqeslgbwcslpuwqkdmkwqdaxuvuthcggpgnoeardqnhrotewuypozgmuzfxhqinipomfkydmcnhifpmrktzqlncoucbpelwtsrcjjwphnglgcgsgqelyqbeymotiifnybgatrrpbowpcsegimvqkmabnlbensjotxxetwhosblyxfitocmaokoadwjlvkgzoreyjkrpdohzmxljdrdzjqjojvbiyhokaxyxfikqsthjoamkxhkxymsgvklzvnnngjasswsbyfdabvfyjhpijkfwfiowtdhjciirqrbrwdukstrlirczvdzkkshfdkioucqtfmihpblqxwmvpxetweoifqiypthdfykdrkbwwcuyuygpqiqjadwypxtdphavaedauplrxwjxaitcoetjbwvhpsizvensphpexdvqjcxldpgizcysqljarawvrpnozhvslfuttphheiswsaxshbqacocmdkaoqnszfcdgpdqxezvwkphtsubkohnpgrdbjutfejpobxckjtemroeidwyzduxvbzdpqxkppvgusikpgozxttvnpojlreuqnpmjfhbmninaqzlgbvhbufgiuadefemupyrccczupdhsmwspkhhhaqmyalgreqrimamsqfbsvewaiebzffbcmyexchfycyzubexlgdhdafbujkbosnicuahvuajszoqmwqpbucusvdrteemrwvshfeuecdaswheuyynczjkinsnwxxxibgqcgcaxmmvdqpttyobhwgsxbuokjppdxyvqqtenjfbdfcrbdzllvhrlnzosfhsmyknjddmfblggrbuhgkpxxgupdbzkigbvemtpmnrmowkrdzegfpxplcwgybdknmbwyoyzmhvztoogkmrluykcrwioyhmqctnfnhngbmnbvgnfwtbvtudefcxvuylmchgnvyorxdywahexmgfjifvitjsbrbngoetpnqgzaiplpgndlitifeclroysuykbotgbszfnkhoiulxahjjwtxxfmozfunexiehijvvxtzwtdslklzaytplnovuvycxirfpdkbuuwsmsmqoqjfoodvbaavdraxocjfgdmldvhdylgdbzopxfgqsfbwatyuzusjpbfeqtdwhqmmzgtvokrtvkhkvzzxyjyoalgzngofigysifhsqwbcpdhvwvgsuefqjcakzujhnrkftzbiqevokharafvehvhqocetzwyjxbuwppflibuzgtifnyczhjedujdiyrqnbscqapnwulyoosuddqeflcrtbukvacifqivlonjcvsovzzhmnmoufatkqofjmhjrcnbkcnzaayzokqgvwzkjybnfioqgtkslxzfmyqldbofuyfqsevyolaumcjsmfxpdrulslchkkbaxrwjczxswhaxxumjkicxnvhwtxonipuogiderovcrhcyrczcubwgtyeeyvueazxseuhupjzxesveckigahupcdxlztbphdhdwvjtexivbkxyrmdsypabpqxixbnseiibnauhnbxqlkcwrvrmtdpbealttvvelqifmkfsjzhnaxdrgrfljlfrnqtcozuilmgudlzblnorriimmmgydrpostalitfjdxtdzanqwxfmdvduvpjtmbsttaegjltahgwlvhumxzjcrmbfbqxehmbvoksjlfrvnmchdcujqiazavyotzcksxrtlwzrbxdvdqfordtidhbtdjrpxplxhwoeutsevzvfthpscglynwujnjqgonhlojbjhcqtagesfxoqjcmvvyapmwnmegrttcauutfkjgqbgkomzhdnfxqbhlrmnznnqljffihmfxoziojgltztgyohzaxrqzvxnlcwegiodkiipzfgrnpdzxngspecqbdsdibrodbdbzezbgzfnbszvamskuojtlszltgbleebgfcriskbvxdlinojdqnystcszubjggalzaapkhvwslcgypmsrjydmnflbntzbykkbfaixyhuxmehrvxtdvgjimekmbsnnmkppoqmitlmuvadzyibbakinnaelbgpjnyvqjovucxpmsqtxiaxdyzftuhoetpvvndjqqdtauurgatbdshriepepbpquwpbppfqccgnbbmiaosrwvexrgrpvbnhanujhzyvvpneqexwmtdlurpdmhgivbtourwplhcwxikyoqkgmfyrtagybcgipwrmcooirzpaminzgfdnftdkgcdoemiatlwmclzbfthmkdjtainbbhbbtpjzybxpabusdnsbomrrwicghclcyhwmgknisoppgzwnfdiqtxctvitpujafnagwtippdmbfjcempupwdghhcqngyeszyicncylpfwrleyhjrxkoodcjclwqpcwosoirkchvieljwindydeiebtcouwxtiqsitutxjyzccyusxyrqopdbgvxgxvjwykgliphvhfoqxacgslyvzxczrrgvxptyndcinoecxkmdfuvzwukskhwgcchczewwbzsrcalgjxxkdaawwemrdcnsqpqoqfreelretvrtsuaunbsejbynikzslsvorwabfnkdnurzpcyxkkoqfonvrbwnoxziwuzgyqlrduaeqeqrxppbajzbdchrzwogyoevzfizrwsdvdctxkrzlkaqmdbeqchnxuhitdczebntajmypyyoxcmdfcegpnxwcoyelfpppfiupzknpweyjkddeinihrakkguqfdyfsapabsykvaeqcgehwwkhjhfeumpfkdmeuptxoabccuwusteyjzonatqqejbcrndcaadeskdmdbrimrhnfradkdpbnyudldgiuboguwslgxczetqvmyhcjoqamgdzgmclemtimaoroartgbkwgnegxoordytopfsakgovafuclbjvcfypkpkoqlqysepkkaqmtcbwtnqkdbqddhzenqkneapjqxmboiaeifwivjqswfplbmtmvlqsbhhbgnrpaqaznoqiblvcvrylsmvvtuhlyvonb"
print(len(t1),len(t2))
# print(t.checkInclusion(t1,t2))