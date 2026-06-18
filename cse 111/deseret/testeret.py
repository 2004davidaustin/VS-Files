import pytest
from unittest.mock import patch
import re

# Import the functions we're testing
# Assuming the main file is named 'ipa_converter.py'
# If different, adjust the import statement
try:
    from deseret import to_ipa, ipa_fallback, ipa_to_deseret, DIGRAPHS, IPA_TO_GLYPH
except ImportError:
    # Fallback if the module has a different name
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class TestRealIpaWords:
    """Test to_ipa function with real words using the eng-to-ipa library"""
    
    @patch('eng_to_ipa.convert')
    def test_simple_words(self, mock_convert):
        """Test conversion of simple, common words"""
        # Mock the eng_to_ipa library response
        mock_convert.return_value = "hɛˈloʊ"
        result = to_ipa("hello")
        assert "ɛ" in result or "loʊ" in result
        mock_convert.assert_called_once_with("hello")
    
    @patch('eng_to_ipa.convert')
    def test_word_with_asterisk_fallback(self, mock_convert):
        """Test that words with asterisks trigger fallback"""
        # Simulate a word that eng_to_ipa couldn't convert
        mock_convert.return_value = "unknownword*"
        result = to_ipa("unknownword")
        # Should not contain asterisk after fallback processing
        assert "*" not in result
    
    @patch('eng_to_ipa.convert')
    def test_multiple_words(self, mock_convert):
        """Test conversion of multiple words"""
        mock_convert.return_value = "ˈhæpi ˈbərθˌdeɪ"
        result = to_ipa("happy birthday")
        assert len(result) > 0
        # Should contain IPA characters
        assert any(c in result for c in ['ˈ', 'ˌ', 'ə', 'θ'])


class TestFakeIpaWords:
    """Test ipa_fallback function with manual phonetic conversion"""
    
    def test_basic_digraphs(self):
        """Test common digraph conversions"""
        assert "eɪ" in ipa_fallback("rain")  # ai -> eɪ
        assert "i" in ipa_fallback("see")     # ee -> i
        assert "ʧ" in ipa_fallback("chair")   # ch -> ʧ
        assert "ʃ" in ipa_fallback("ship")    # sh -> ʃ
        assert "θ" in ipa_fallback("think")   # th -> θ
    
    def test_silent_e_rule(self):
        """Test the silent 'e' rule"""
        result = ipa_fallback("make")
        assert "eɪ" in result  # a_e -> eɪ
        
        result = ipa_fallback("time")
        assert "aɪ" in result  # i_e -> aɪ
        
        result = ipa_fallback("hope")
        assert "oʊ" in result  # o_e -> oʊ
    
    def test_final_rules(self):
        """Test word-ending rules"""
        assert "ʃən" in ipa_fallback("nation")      # -tion -> ʃən
        assert "ɪŋ" in ipa_fallback("running")      # -ing -> ɪŋ
        assert "aɪzeɪʃən" in ipa_fallback("civilization")  # -ization
    
    def test_punctuation_preservation(self):
        """Test that punctuation is preserved"""
        result = ipa_fallback("hello, world!")
        assert "," in result
        assert "!" in result
    
    def test_apostrophe_handling(self):
        """Test that apostrophes are handled correctly"""
        result = ipa_fallback("don't")
        assert "'" not in result  # Apostrophes should be removed from processing
        assert "d" in result and "t" in result


class TestDeseret:
    """Test ipa_to_deseret function for Deseret alphabet conversion"""
    
    def test_basic_vowel_conversion(self):
        """Test conversion of basic vowel sounds"""
        assert ipa_to_deseret("i") == "𐐀"      # i
        assert ipa_to_deseret("æ") == "𐐈"      # æ
        assert ipa_to_deseret("u") == "𐐅"      # u
    
    def test_basic_consonant_conversion(self):
        """Test conversion of basic consonant sounds"""
        assert ipa_to_deseret("b") == "𐐒"      # b
        assert ipa_to_deseret("d") == "𐐔"      # d
        assert ipa_to_deseret("k") == "𐐗"      # k
    
    def test_digraph_conversion(self):
        """Test conversion of IPA digraphs to single Deseret glyphs"""
        assert ipa_to_deseret("oʊ") == "𐐄"     # oʊ -> single glyph
        assert ipa_to_deseret("aɪ") == "𐐌"     # aɪ -> single glyph
        assert ipa_to_deseret("eɪ") == "𐐁"     # eɪ -> single glyph
        assert ipa_to_deseret("aʊ") == "𐐍"     # aʊ -> single glyph
    
    def test_stress_marks_removed(self):
        """Test that stress marks are removed"""
        result = ipa_to_deseret("ˈhɛloʊ")
        assert "ˈ" not in result
        assert "ˌ" not in result
        assert "𐐇" in result  # ɛ should be converted
    
    def test_complex_word(self):
        """Test conversion of a complete IPA word"""
        ipa_word = "hɛloʊ"
        result = ipa_to_deseret(ipa_word)
        # Should contain Deseret characters
        assert any(ord(c) >= 0x10400 and ord(c) <= 0x1044F for c in result)
        # Should not contain Latin characters from the IPA
        assert "h" not in result or ord("h") != ord(result[0])


class TestIpaParagraph:
    """Test full pipeline with paragraph-length text"""
    
    @patch('eng_to_ipa.convert')
    def test_short_paragraph(self, mock_convert):
        """Test conversion of a short paragraph"""
        test_text = "The quick brown fox jumps over the lazy dog."
        mock_convert.return_value = "ðə kwɪk braʊn fɑks ʤʌmps ˈoʊvər ðə ˈleɪzi dɔɡ."
        
        result = to_ipa(test_text)
        
        # Should contain IPA characters
        assert any(c in result for c in ['ə', 'ɪ', 'ʊ', 'ɑ', 'ʤ'])
        # Should not be empty
        assert len(result) > 0
    
    def test_fallback_paragraph(self):
        """Test ipa_fallback with a paragraph"""
        test_text = "Hello world. This is a test."
        result = ipa_fallback(test_text)
        
        # Should preserve punctuation
        assert "." in result
        # Should contain IPA characters
        assert any(c in result for c in ['ɛ', 'ɔ', 'ɪ', 's', 't'])
        # Words should be separated
        assert " " in result
    
    @patch('eng_to_ipa.convert')
    def test_full_pipeline_to_deseret(self, mock_convert):
        """Test complete pipeline: English -> IPA -> Deseret"""
        test_text = "Hello"
        mock_convert.return_value = "hɛˈloʊ"
        
        ipa_result = to_ipa(test_text)
        deseret_result = ipa_to_deseret(ipa_result)
        
        # Should contain Deseret characters
        assert any(ord(c) >= 0x10400 and ord(c) <= 0x1044F for c in deseret_result)
        # Should not contain stress marks
        assert "ˈ" not in deseret_result
        assert "ˌ" not in deseret_result
    
    def test_paragraph_with_mixed_punctuation(self):
        """Test paragraph with various punctuation marks"""
        test_text = "Hello, world! How are you? I'm fine."
        result = ipa_fallback(test_text)
        
        # All punctuation should be preserved
        assert "," in result
        assert "!" in result
        assert "?" in result
        assert "." in result


# Additional edge case tests
class TestEdgeCases:
    """Test edge cases and error handling"""
    
    def test_empty_string(self):
        """Test behavior with empty string"""
        assert ipa_fallback("") == ""
    
    def test_single_character(self):
        """Test single character conversion"""
        result = ipa_fallback("a")
        assert len(result) > 0
    
    def test_numbers_and_special_chars(self):
        """Test handling of numbers"""
        result = ipa_fallback("test123")
        # Numbers should pass through or be handled
        assert len(result) > 0
    
    @patch('eng_to_ipa.convert')
    def test_deseret_unknown_ipa(self, mock_convert):
        """Test Deseret conversion with unmapped IPA character"""
        # Test with a character not in IPA_TO_GLYPH
        test_ipa = "xəx"  # ə is not mapped
        result = ipa_to_deseret(test_ipa)
        # Should still process what it can
        assert len(result) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])