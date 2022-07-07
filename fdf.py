Private
Sub
worksheet_change(ByVal
Target
As
Range)

'While True
'Wend

row_save = 3

With
ThisWorkbook.Sheets("save")
While.Cells(row_save, 1).value <> ""
row_save = row_save + 1
Wend
End
With

For
Each
cell
In
Target
If
Not
Intersect(cell, Range("J:M"))
Is
Nothing
Or
Not
Intersect(cell, Range("Q:S"))
Is
Nothing
Or
Not
Intersect(cell, Range("W:X"))
Is
Nothing
Or
Not
Intersect(cell, Range("AA:AA"))
Is
Nothing
Or
Not
Intersect(cell, Range("AC:AC"))
Is
Nothing
Or
Not
Intersect(cell, Range("AE:AE"))
Is
Nothing
Or
Not
Intersect(cell, Range("AG:AI"))
Is
Nothing
Or
Not
Intersect(cell, Range("AL:AL"))
Is
Nothing
Then

sheet_postgres = "BASE_POSTGRES LIENS GC"
sheet_suivi = "SUIVI  infraGC"

Set
coord = ThisWorkbook.Sheets(sheet_postgres).Range("A:A").Find(what := Cells(cell.row, 1).value, lookat := xlWhole)

With
ThisWorkbook.Sheets("save")
Set
coord =.Range("A:A").Find(what :=.Cells(coord.row, 1), lookat := xlWhole)
If
Not
coord
Is
Nothing
Then
tmp = coord.row + 1
Else:
tmp = row_save
.Cells(row_save, 1).value = idx
row_save = row_save + 1
End
If

Set
col =.Range("A1:Q1").Find(what := cell.Column, lookat := xlWhole)

.Cells(tmp, col.Column).value = cell.value

End
With
End
If
Next
cell
End
Sub
