entry1 = input()
entry2 = input()
entry3 = input()

if entry1 == entry2 == entry3:
    print("OK")
elif entry1 == entry2 and entry1 != entry3:
    print("ENTRY 3 MISMATCH")
elif entry1 == entry3 and entry1 != entry2:
    print("ENTRY 2 MISMATCH")
elif entry1 != entry2 and entry1 != entry3:
    print("BOTH MISMATCH")