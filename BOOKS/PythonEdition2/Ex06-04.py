total1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
math1 = {1, 3, 5, 6, 7, 9}
eng1 = {1, 3, 5, 8, 10}
print("คนที่เรียนคณิตศาสตร์ ได้แก่", math1, "เท่ากับ", len(math1), "คน")
print("คนที่เรียนภาษาอังกฤษ ได้แก่", eng1, "เท่ากับ",  len(eng1), "คน")
print("คนที่เรียนทั้งสองวิชา ได้แก่", math1.intersection(eng1), "เท่ากับ",
      len(math1.intersection(eng1)), "คน")
print("คนที่เรียนคณิตศาสตร์แต่ไม่เรียนภาษาอังกฤษ ได้แก่", math1.difference(eng1), "เท่ากับ",
      len(math1.difference(eng1)), "คน")
print("คนที่เรียนภาษาอังกฤษแต่ไม่เรียนคณิตศาสตร์ ได้แก่", eng1.difference(math1), "เท่ากับ",
      len(eng1.difference(math1)), "คน")
both = math1.union(eng1)
print("จำนวนคนที่เรียนภาษาอังกฤษและคณิตศาสตร์ทั้งหมด", len(both), "คน ได้แก่", both)
print("คนที่ไม่เรียนทั้งสองวิชา ได้แก่", total1.difference(both), "เท่ากับ", len(total1.difference(both)), "คน")

