from secretary import display_name, display_shelf, add_document, delete_document


#pytest
class TestSecretary:

    def test_display_name_pos(self):
        assert display_name('11-2') == 'Геннадий Покемонов'

    def test_display_name_neg(self):
        assert display_name('1') == 'Документа с номером 1 не существует'

    def test_display_shelf_pos(self):
        assert display_shelf('10006') == '2'

    def test_display_shelf_neg(self):
        assert display_shelf('1') == 'Документа с номером 1 не существует'

    def test_add_document_pos(self):
        assert add_document('30', 'insurance', 'O K', '3') == 'Документ номер 30 добавлен на полку 3'

    def test_add_document_neg(self):
        assert add_document('30', 'insurance', 'O K', '5') == 'Полки номер 5 не существует'

    def test_delete_document_pos(self):
        assert delete_document('2207 876234') == 'Документ номер 2207 876234 удален'

    def test_delete_document_neg(self):
        assert delete_document('1') == 'Документа с номером 1 не существует'
