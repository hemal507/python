import memoryPills

def test_case1() :
        assert memoryPills.memoryPills(["Notforgetan",  "Antimoron",  "Rememberin",  "Bestmedicen",  "Superpillsus"]) == ["Bestmedicen",  "Superpillsus",  ""]

def test_case2() :
        assert memoryPills.memoryPills(["Pillin"]) == ["", "", ""]

def test_case3() :
        assert memoryPills.memoryPills(["Med 1",  "Med 2",  "Med 3",  "Med 10",  "Med 11",  "Med 12",  "Med 14",  "Med 42",  "Med 239"]) == ["Med 11",  "Med 12",  "Med 14"]

def test_case4() :
        assert memoryPills.memoryPills(["Pills",  "Shmills",  "Medicine",  "Phedicine", "Hey",  "Hoy"] ) == ["Phedicine",  "Hey",  "Hoy"]

def test_case5() :
        assert memoryPills.memoryPills( ["Test",  "Where",  "The",  "First",  "Element",  "Is",  "Even"]) == ["Where",  "The",  "First"]

