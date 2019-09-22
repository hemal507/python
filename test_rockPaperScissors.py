import rockPaperScissors

def test_case1() :
	assert rockPaperScissors.rockPaperScissors(["trainee",  "warrior",  "ninja"]) == [("ninja","trainee"),  ("ninja","warrior"),  ("trainee","ninja"),  ("trainee","warrior"),  ("warrior","ninja"),  ("warrior","trainee")]

def test_case2() :
        assert rockPaperScissors.rockPaperScissors(["macho",  "hero"]) == [("hero","macho"),  ("macho","hero")]

def test_case3() :
        assert rockPaperScissors.rockPaperScissors(["Harry",  "Ron",  "Hermione",  "Draco",  "Tom"]) == [("Draco","Harry"),  ("Draco","Hermione"),  ("Draco","Ron"),  ("Draco","Tom"),  ("Harry","Draco"),  ("Harry","Hermione"),  ("Harry","Ron"),  ("Harry","Tom"),  ("Hermione","Draco"),  ("Hermione","Harry"),  ("Hermione","Ron"),  ("Hermione","Tom"),  ("Ron","Draco"),  ("Ron","Harry"),  ("Ron","Hermione"), ("Ron","Tom"),  ("Tom","Draco"),  ("Tom","Harry"),  ("Tom","Hermione"),  ("Tom","Ron")]

def test_case4() :
        assert rockPaperScissors.rockPaperScissors( ["A",  "B"]) == [("A","B"),  ("B","A")]
