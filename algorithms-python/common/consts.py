import math


INDOOR = True

# +------------------+
# | robot dimensions |
# +------------------+

ROBOT_WIDTH = 25
ROBOT_HEIGHT = 28
ROBOT_ACTUAL_WIDTH = 18.8
ROBOT_ACTUAL_HEIGHT = 23
ROBOT_VERT_OFFSET = (ROBOT_HEIGHT - ROBOT_ACTUAL_HEIGHT) / 2

# +--------------------+
# | collision checking |
# +--------------------+
# WPS: Waypoints

WPS_FL_IN = [(0, 0, 0), (0.17432871149079365, 2.0147144912787645, 0.1162474683218298), (0.1815528243494025, 2.83774444398336, 0.165254702619014), (0.16294890476342083, 3.458782944817927, 0.20345345663469647), (0.1318939301558607, 3.9730034885163454, 0.23616213478783046), (0.09356740774918593, 4.417577477074893, 0.2654307391648058), (0.05062920902060397, 4.811722260480629, 0.29230605117390746), (0.004664316399231483, 5.166945927224835, 0.3174074276465033), (-0.04328943878418268, 5.490808124550034, 0.3411369400055289), (-0.14245289571178132, 6.064222512987042, 0.3855174717563411), (-0.242995775597594, 6.560138109903725, 0.42690640065184643), (-0.3425652768326304, 6.995614581673779, 0.46616589894757976), (-0.43958138249905776, 7.382004346485401, 0.5038555164688107), (-0.5329087197505353, 7.727380997756292, 0.5403627590331488), (-0.6216913858769129, 8.03778095994247, 0.5759691112058163), (-0.7052622314329564, 8.31789958224698, 0.6108866352639529), (-0.8197128359604182, 8.689367129101061, 0.6623213619363437), (-0.9198871117431038, 9.011178219107135, 0.7129885918219147), (-1.0047984060688033, 9.291317195956573, 0.763195697833343), (-1.093158541692715, 9.611190173787413, 0.8298130307207774), (-1.1626869244742921, 9.94255074621481, 0.9130998662865581), (-1.1847504326440879, 10.314936741864853, 1.0306029080537242), (-1.1265654773821479, 10.621869364144565, 1.149808349018336), (-1.004182264155412, 10.900081970681443, 1.270912969407187), (-0.8661211336500942, 11.136624619689014, 1.3760584470062251), (-0.7172123972421818, 11.383247558886355, 1.482089418610597), (-0.7999999999999767, 11.600000000000001, 1.5707963267948966)]
WPS_FR_IN = [(0, 0, 0), (0.18047561827762487, 7.758459852799316, -0.13107480952873385), (0.5532944211587054, 10.960008870253764, -0.18589363109293217), (1.381047052814424, 15.454822135838622, -0.26438930864174637), (2.257160390866974, 18.865296340162985, -0.32565571196668774), (3.160204862201248, 21.705930043266378, -0.3781827195092823), (4.081905257668269, 24.176779939650906, -0.4252402351856636), (5.018034108022405, 26.3807760476019, -0.46849644004811575), (6.444063648433153, 29.3144183698351, -0.5283105323872694), (7.892002386464599, 31.90738628753605, -0.5837323996154601), (9.358818037809, 34.23504916464053, -0.635953857803304), (10.842535436205472, 36.34651267048847, -0.6857455880174088), (12.34177175752436, 38.2758197912755, -0.7336387244519782), (13.855499854290668, 40.04765648503003, -0.7800167708626005), (15.38291592042555, 41.68053894796767, -0.8251666302343551), (16.92336006543029, 43.18872213740549, -0.8693089774260557), (18.996581746385534, 45.024678503791264, -0.9268929800916702), (21.090777548962734, 46.67916291644759, -0.983310097663589), (23.204861686154924, 48.16772352976199, -1.0388038678429417), (25.33779083984862, 49.50230173720903, -1.0935635991069115), (27.48852634794434, 50.69216237403938, -1.1477388381216993), (29.656009835283726, 51.74453078134338, -1.2014493132124773), (31.839148106174086, 52.665041638835206, -1.254792024857382), (34.58834991179655, 53.636807847688104, -1.3210730408477884), (37.35791238836221, 54.415608086042646, -1.3870292069745103), (40.1454067830868, 55.005739691561644, -1.4527634328467973), (42.94831330860808, 55.40983243059967, -1.5183625010551784), (45.59999999999994, 55.6, -1.5707963267948966)]
WPS_BR_IN = [(0, 0, 0), (1.0074018966502518, -6.746351398498114, 0.17092830859074495), (1.758366738950217, -9.481957005980659, 0.24107935832482294), (3.1437827993402787, -13.263396752651612, 0.33915630513197487), (4.45647896478034, -16.081005295488044, 0.4132863330471812), (5.72640143178015, -18.390992359875625, 0.47490104301893954), (6.965730929521437, -20.371699851518457, 0.5284633075023646), (8.781110402607737, -22.916426564504466, 0.5984858845201798), (10.555201925178265, -25.09345992585901, 0.6597211690272581), (12.29593191886954, -26.99834171372114, 0.7145589717244014), (14.008674126084765, -28.690371217563396, 0.7644847243703997), (15.697365557254924, -30.209395362174998, 0.8104989346336932), (17.916703983848382, -32.01346694423602, 0.8669716793547279), (20.104234390666953, -33.60740494951378, 0.9189510274005226), (22.264324846421342, -35.02502516091011, 0.9672993244763038), (24.40049046124755, -36.29118741573278, 1.0126566329679345), (26.51563158735044, -37.42474676412584, 1.0555143478650124), (29.1336743595402, -38.67724059811997, 1.1061546568282732), (31.726659046561146, -39.767348399182985, 1.1540881423403533), (34.29794123093622, -40.71197053276493, 1.1997861961266039), (36.850378891725725, -41.52422503155888, 1.243629913245274), (39.38644163356356, -42.21440513195372, 1.2859345801117974), (42.41112794738227, -42.89279161508259, 1.3350410811301994), (45.418610432014276, -43.41782385668677, 1.3827054690128666), (48.41176755089994, -43.79753496689889, 1.4292654605759625), (51.393168249309056, -44.0376876735552, 1.4750200351367557), (54.85970518402995, -44.14650955234256, 1.527744758975385), (57.79999999999991, -44.1, 1.5707963267948966)]
WPS_BL_IN = [(0, 0, 0), (-0.4475055151499271, 0.42972281793815803, -0.1947900701207024), (-0.7292967250454522, 0.7206849488978562, -0.3337101401030298), (-0.9949107002137849, 0.936200808097813, -0.4646781816411222), (-1.3547606279942772, 1.06905976675466, -0.6144781822951864), (-1.8594385508961713, 1.0474898060747946, -0.7634197276212886), (-2.2502425712009155, 0.9632170154889748, -0.8471199931993941), (-2.669831854513724, 0.8519490537554246, -0.9190415433952195), (-3.0252464909474726, 0.7535359627233389, -0.9703609127304332), (-3.396783716489545, 0.6522127518338097, -1.017381011413165), (-3.782982409270029, 0.5514945941087888, -1.0609092805037956), (-4.182390631899553, 0.4539616943895193, -1.1015560236652886), (-4.593623055935767, 0.36154377854902764, -1.1397955995262439), (-5.015382878552094, 0.2757069246164725, -1.1760053713047458), (-5.446466447925676, 0.19758037155160224, -1.2104915774476568), (-5.885759537735215, 0.128044922574435, -1.2435071299604457), (-6.332229782586076, 0.0677959588917112, -1.2752642285701128), (-6.784917576828879, 0.017389207226694015, -1.3059435336355965), (-7.242926600554975, -0.02272547939995262, -1.3357009905311772), (-7.705414536081933, -0.05217883883171481, -1.3646730135069276), (-8.171584217025336, -0.0706630475332431, -1.3929805012243572), (-8.640675279099039, -0.07791706127933506, -1.4207320072102418), (-9.11195628864128, -0.07371529733535015, -1.4480262919321976), (-9.584717274759612, -0.05785883779396561, -1.4749544192797202), (-10.0582625636811, -0.03016856391441808, -1.501601517199723), (-10.531903797960753, 0.009520205279789348, -1.5280482929479287), (-11.004953011978266, 0.0613618781578808, -1.5543723734452939), (-11.399999999999956, 0.09999999999999964, -1.5707963267948966)]

WPS_FL_OUT = [(0, 0, 0), (0.15523534725572996, 2.227647602778637, 0.11135584446690257), (0.15089173448854576, 3.135325965884032, 0.15841289143741044), (0.12215053922476515, 3.8190956085951955, 0.19517024644595857), (0.08180549701617135, 4.3843667294181685, 0.2267124384944659), (0.03481382003862077, 4.872307815214516, 0.25499847359857286), (-0.016274395781347817, 5.304201107453389, 0.281028408535016), (-0.06993522526547324, 5.692789776047037, 0.30539390127418015), (-0.1251666801346083, 6.046443574278847, 0.328479076817715), (-0.23770633259080165, 6.670835642075531, 0.371799662153295), (-0.3501034657615665, 7.208557030299985, 0.4123852563902447), (-0.4600049577830221, 7.678482996963938, 0.451061921977083), (-0.5657893490001586, 8.09317347925801, 0.48836728432919235), (-0.6662547695442034, 8.461564189307193, 0.5246750875298275), (-0.7604624935389444, 8.790343097458166, 0.5602581182640115), (-0.8884126706566837, 9.220356006949423, 0.6127129856350485), (-0.9985459591099459, 9.586370727137865, 0.6645108771342585), (-1.0892717702637973, 9.89885509864493, 0.716026098324045), (-1.1779899107924587, 10.246661201402818, 0.7847453995720506), (-1.2344742669779358, 10.593572781176102, 0.8713459990351307), (-1.1969027514114194, 11.007204160863093, 1.0128751849895892), (-1.0422985806472371, 11.287929067894327, 1.1404877176644754), (-0.8347094481882009, 11.508538448294674, 1.252715503881417), (-0.579218707720409, 11.736961169883193, 1.367186300229552), (-0.34894134434743673, 11.945542178256428, 1.4638203939606245), (-0.12182058264822082, 12.175765226154217, 1.561060005876094), (-0.19999999999997886, 12.2, 1.5707963267948966)]
WPS_FR_OUT = [(0, 0, 0), (0.18410632417433637, 7.910454930361933, -0.1269078388190303), (0.5543470962652282, 11.174219142376163, -0.1801486024731867), (1.3748547837727578, 15.756372995472358, -0.2566913519355102), (2.2431619609135045, 19.233406803028018, -0.31676382831226874), (3.138708092394258, 22.129853305760026, -0.36854994593400686), (4.0536149002145265, 24.6496225892435, -0.41519748299303855), (4.983900375673225, 26.89759058563453, -0.4583105660504799), (6.403325162741389, 29.89025927107964, -0.518329407939342), (7.847650466246358, 32.535777885460554, -0.5743912765389371), (9.314208171497253, 34.9107037574561, -0.6276388879923217), (10.801327384863669, 37.064789460558046, -0.6788101609447642), (12.307884725232455, 39.03240110349034, -0.7284126213161425), (13.833073510711397, 40.838334644759904, -0.7768115497734946), (15.376272908431563, 42.501065369331414, -0.8242788348344029), (16.936967741503302, 44.03469437465022, -0.8710219934965044), (19.044314066129548, 45.897301860364614, -0.932493560038417), (21.180885522977597, 47.56941145223393, -0.9932523132442834), (23.34557803092354, 49.06564168252821, -1.0535131763793544), (25.53717321292873, 50.39687928557318, -1.113435239405778), (27.75429294278782, 51.57124626428755, -1.1731355842475875), (29.995371266351217, 52.594770231219734, -1.2326989224426461), (32.25864053866081, 53.4718638536102, -1.2921846574812776), (34.542130010476924, 54.20567581369976, -1.3516323344469587), (37.421612911958206, 54.924639215319615, -1.425923997109528), (40.324696586719924, 55.425464093993014, -1.5002155083959363), (43.199999999999946, 55.7, -1.5707963267948966)]
WPS_BR_OUT = [(0, 0, 0), (0.9998184407210391, -6.773689207249706, 0.16927250878953445), (1.7462362615765445, -9.52195737104515, 0.23883260679665558), (3.1248140682833667, -13.323025268499723, 0.33623814598017154), (4.43262783101448, -16.15701528430713, 0.4100157784676611), (5.699141782325812, -18.48153153718085, 0.47145995006090746), (6.93627739814264, -20.475397413845574, 0.5249755772935827), (8.750267720218828, -23.037750048438895, 0.5950938697053109), (10.524878093915595, -25.230188408363404, 0.6565701341568244), (12.267715576083166, -27.148450187211314, 0.7117565513029568), (13.983906025001978, -28.85195617226272, 0.7621140630637101), (15.677187978403445, -30.380639759434537, 0.8086261934172884), (17.90414812512396, -32.194878758864995, 0.8658449889524674), (20.100736833510126, -33.79600067265838, 0.9186456399741485), (22.27107818991855, -35.217924623251506, 0.9678759313644826), (24.41849254298431, -36.48559475304682, 1.0141655537027308), (26.54572337255631, -37.617934189598, 1.0579984372320765), (29.179869362805636, -38.86514708532443, 1.1099099434735717), (31.789875993853155, -39.94586780937846, 1.159166136054802), (34.37894436923816, -40.87703788698097, 1.2062339891942535), (36.949811570282925, -41.671784565528796, 1.2514922447535595), (39.50485238100085, -42.34037828997926, 1.2952554543893746), (42.552932866173734, -42.987396856218645, 1.3461712162173451), (45.58439454896397, -43.47494491401311, 1.395712361963527), (48.60204266964074, -43.81081720521982, 1.4442220033328952), (52.108515330257205, -44.0181078385816, 1.4999203583972842), (55.60321088702764, -44.03146421290695, 1.555077258831053), (56.999999999999915, -44.0, 1.5707963267948966)]
WPS_BL_OUT = [(0, 0, 0), (-0.4474238707814683, 0.5919864057819066, -0.20182252577403453), (-0.7084585366522612, 0.9919268020840675, -0.345253848654185), (-0.9425981787923821, 1.298872224106233, -0.47979915559957603), (-1.2589433809416557, 1.5190105014770179, -0.6326610717454763), (-1.7205053106966535, 1.565294037842158, -0.783428988925416), (-2.1681610187188505, 1.496269964765618, -0.8828645572030379), (-2.578806086603235, 1.4035200213549377, -0.952952981438169), (-3.0203057983311856, 1.2962569698409885, -1.014854253086554), (-3.393224918759836, 1.2068746578662555, -1.0598517618554604), (-3.7816557933555175, 1.118199991381322, -1.101629370595112), (-4.183863262310638, 1.0328077254882186, -1.1407416877761507), (-4.598252274768317, 0.95262442085918, -1.1776241111746963), (-5.0233660111854554, 0.8791142120749643, -1.2126259296400115), (-5.457875195971996, 0.8134053745610228, -1.2460326968524542), (-5.900564101693799, 0.7563787424663518, -1.2780818479143479), (-6.350315844997755, 0.708730788720866, -1.3089739043924642), (-6.806098155882712, 0.6710194421578257, -1.338880711699303), (-7.266950096451626, 0.6436978831486987, -1.3679516295170273), (-7.731969853334773, 0.6271398057305224, -1.3963182807086327), (-8.20030355474433, 0.6216585169451275, -1.4240982679688008), (-8.671134980813877, 0.6275215137008481, -1.4513981419853552), (-9.14367599924869, 0.6449616887204234, -1.478315822779064), (-9.617157543530746, 0.6741859828198928, -1.504942621204636), (-10.090820945148316, 0.7153820669391594, -1.531364970750256), (-10.56390942740956, 0.7687234697418641, -1.5576659548925094), (-10.999999999999957, 0.8000000000000007, -1.5707963267948966)]

WPS_FL = WPS_FL_IN if INDOOR else WPS_FL_OUT
WPS_FR = WPS_FR_IN if INDOOR else WPS_FR_OUT
WPS_BR = WPS_BR_IN if INDOOR else WPS_BR_OUT
WPS_BL = WPS_BL_IN if INDOOR else WPS_BL_OUT

BUFFER = 5.01
OUTER_ARC_POINTS = 20
INNER_ARC_POINTS = 10

# +--------FORWARD RIGHT TURN RADIUS (Measureable) ------------+
FORWARD_RIGHT_SEMI_MAJOR_AXIS_INNER_ELLIPSE = 20.2
FORWARD_RIGHT_SEMI_MINOR_AXIS_INNER_ELLIPSE = 21.8
FORWARD_RIGHT_SEMI_MAJOR_AXIS_OUTER_ELLIPSE = 58.2
FORWARD_RIGHT_SEMI_MINOR_AXIS_OUTER_ELLIPSE = 59.8

# +--------FORWARD LEFT TURN RADIUS (Measureable) ------------+
FORWARD_LEFT_SEMI_MAJOR_AXIS_INNER_ELLIPSE = 6
FORWARD_LEFT_SEMI_MINOR_AXIS_INNER_ELLIPSE = 4.8
FORWARD_LEFT_SEMI_MAJOR_AXIS_OUTER_ELLIPSE = 47
FORWARD_LEFT_SEMI_MINOR_AXIS_OUTER_ELLIPSE = 45.8

# +--------BACKWARD RIGHT TURN RADIUS (Measureable) ------------+
BACKWARD_RIGHT_SEMI_MAJOR_AXIS_INNER_ELLIPSE = 20.2
BACKWARD_RIGHT_SEMI_MINOR_AXIS_INNER_ELLIPSE = 21.8
BACKWARD_RIGHT_SEMI_MAJOR_AXIS_OUTER_ELLIPSE = 58.2
BACKWARD_RIGHT_SEMI_MINOR_AXIS_OUTER_ELLIPSE = 59.8

# +--------BACKWARD LEFT TURN RADIUS (Measureable) ------------+
BACKWARD_LEFT_SEMI_MAJOR_AXIS_INNER_ELLIPSE = 6
BACKWARD_LEFT_SEMI_MINOR_AXIS_INNER_ELLIPSE = 4.8
BACKWARD_LEFT_SEMI_MAJOR_AXIS_OUTER_ELLIPSE = 47
BACKWARD_LEFT_SEMI_MINOR_AXIS_OUTER_ELLIPSE = 45.8

# +-------+
# | astar |
# +-------+

FL_A_IN, FL_B_IN = 15.6, 21.6
FR_A_IN, FR_B_IN = 35.2, 40.6
BR_A_IN, BR_B_IN = 42.7, 34.1
BL_A_IN, BL_B_IN = 21.3, 14.9

FL_A_OUT, FL_B_OUT = 15.1, 22.2
FR_A_OUT, FR_B_OUT = 33.1, 40.7
BR_A_OUT, BR_B_OUT = 41.6, 34
BL_A_OUT, BL_B_OUT = 20.8, 14.2

FL_A, FL_B = (FL_A_IN, FL_B_IN) if INDOOR else (FL_A_OUT, FL_B_OUT)
FR_A, FR_B = (FR_A_IN, FR_B_IN) if INDOOR else (FR_A_OUT, FR_B_OUT)
BR_A, BR_B = (BR_A_IN, BR_B_IN) if INDOOR else (BR_A_OUT, BR_B_OUT)
BL_A, BL_B = (BL_A_IN, BL_B_IN) if INDOOR else (BL_A_OUT, BL_B_OUT)

_DIST_STR = 5
DIST_BW = _DIST_STR
DIST_FW = _DIST_STR

_circum = lambda a, b: math.pi * ( 3*(a+b) - math.sqrt( (3*a + b) * (a + 3*b) ) )
# x displacement, y displacement, arc length
DIST_FL = WPS_FL[-1][0], WPS_FL[-1][1], _circum(FL_A, FL_B)/4
DIST_FR = WPS_FR[-1][0], WPS_FR[-1][1], _circum(FR_A, FR_B)/4
DIST_BL = WPS_BL[-1][0], WPS_BL[-1][1], _circum(BL_A, BL_B)/4
DIST_BR = WPS_BR[-1][0], WPS_BR[-1][1], _circum(BR_A, BR_B)/4

PENALTY_STOP = 40
MAX_THETA_ERR = math.pi / 12
MAX_X_ERR = 5, 5  # L, R
MAX_Y_ERR = 7.5, 35 # U, D

# +---------------------+
# | obstacle dimensions |
# +---------------------+

OBSTACLE_WIDTH = 10
IMG_THICKNESS = 2
EDGE_ERR = 0.1
CONE = [10, 10, 4, 40]

# +--------------------+
# | Priority obstacles |
# +--------------------+

# *_X = LEFT, RIGHT
# *_Y = UP, DOWN

FL_OUTER_IN = 41
FR_OUTER_IN = 54
BL_OUTER_IN = 47
BR_OUTER_IN = 69

FL_OUTER_OUT = 40.8
FR_OUTER_OUT = 51.6
BL_OUTER_OUT = 46.7
BR_OUTER_OUT = 63

FL_OUTER = FL_OUTER_IN if INDOOR else FL_OUTER_OUT
FR_OUTER = FR_OUTER_IN if INDOOR else FR_OUTER_OUT
BL_OUTER = BL_OUTER_IN if INDOOR else BL_OUTER_OUT
BR_OUTER = BR_OUTER_IN if INDOOR else BR_OUTER_OUT


FL_X_BOUND = [OBSTACLE_WIDTH/2 + FL_A - ROBOT_WIDTH/2 + ROBOT_HEIGHT - ROBOT_VERT_OFFSET, 
              OBSTACLE_WIDTH/2 + ROBOT_WIDTH]

FL_Y_BOUND = [OBSTACLE_WIDTH/2 + FL_OUTER + (FL_B - FL_A) + ROBOT_VERT_OFFSET, 
              OBSTACLE_WIDTH/2]

FR_X_BOUND = [OBSTACLE_WIDTH/2, 
              OBSTACLE_WIDTH/2 + FR_A + ROBOT_WIDTH/2 + ROBOT_HEIGHT - ROBOT_VERT_OFFSET]

FR_Y_BOUND = [OBSTACLE_WIDTH/2 + FR_OUTER + (FR_B - FL_A) + ROBOT_VERT_OFFSET, 
              OBSTACLE_WIDTH/2]

BL_X_BOUND = [OBSTACLE_WIDTH/2 + BL_A - ROBOT_WIDTH/2 + ROBOT_VERT_OFFSET, 
              OBSTACLE_WIDTH/2 + BL_OUTER - (BL_A - ROBOT_WIDTH/2)] 

BL_Y_BOUND = [OBSTACLE_WIDTH/2 + ROBOT_HEIGHT, 
              OBSTACLE_WIDTH/2 + BL_B + ROBOT_WIDTH/2 - ROBOT_VERT_OFFSET]

BR_X_BOUND = [OBSTACLE_WIDTH/2 + BR_OUTER - BR_A - ROBOT_WIDTH/2, 
              OBSTACLE_WIDTH/2 + BR_A + ROBOT_WIDTH/2 + ROBOT_VERT_OFFSET]

BR_Y_BOUND = [OBSTACLE_WIDTH/2 + ROBOT_HEIGHT, 
              OBSTACLE_WIDTH/2 + BR_B + ROBOT_WIDTH/2 - ROBOT_VERT_OFFSET]

ROBOT_BTM_LEFT_CIRCLE_RAD = 2 # indicates bottom left of the robot footprint
ROBOT_MIN_CAMERA_DIST = 20

# -------- deprecated --------
ROBOT_TURNING_RADIUS = 25
# -------- ---------- --------

# +----------------+
# | map dimensions |
# +----------------+

TK_SCALE = 2
MAP_WIDTH = 200 
MAP_HEIGHT = 200
GRID_WIDTH = 5 # for display on simulator
SNAP_COORD = _DIST_STR # for cell snap (coords) 5. Max value < 1.5* min(DIST_BL, DIST_BR, ... DIST_FW)
SNAP_THETA = 15 # for cell snap (theta) 15

# +-----------------+
# | robot movements |
# +-----------------+

# -------- deprecated --------
ROBOT_TIME_STEP = 10 
TURNING_RADIUS = 25
# -------- ---------- --------

# scale values
# do not modify
SCALED_MAP_WIDTH = int(MAP_WIDTH * TK_SCALE)
SCALED_MAP_HEIGHT = int(MAP_HEIGHT * TK_SCALE)
GRID_WIDTH = int(GRID_WIDTH * TK_SCALE)
SCALED_ROBOT_WIDTH = ROBOT_WIDTH * TK_SCALE
SCALED_ROBOT_HEIGHT = ROBOT_HEIGHT * TK_SCALE
SCALED_ROBOT_TURNING_RADIUS = ROBOT_TURNING_RADIUS * TK_SCALE
ROBOT_BTM_LEFT_CIRCLE_RAD *= TK_SCALE
SCALED_ROBOT_MIN_CAMERA_DIST = ROBOT_MIN_CAMERA_DIST * TK_SCALE
SCALED_OBSTACLE_WIDTH = OBSTACLE_WIDTH * TK_SCALE
IMG_THICKNESS *= TK_SCALE