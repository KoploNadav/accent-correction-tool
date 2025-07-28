"""
Phoneme utility functions for the accent correction tool.
"""

from typing import List, Dict, Set


# IPA phoneme sets for different languages
ENGLISH_PHONEMES = {
    'consonants': {
        'p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ',
        'h', 'm', 'n', 'ŋ', 'l', 'r', 'w', 'j', 'tʃ', 'dʒ'
    },
    'vowels': {
        'iː', 'ɪ', 'e', 'æ', 'ɜː', 'ə', 'ʌ', 'ɑː', 'ɒ', 'ɔː', 'ʊ', 'uː',
        'eɪ', 'aɪ', 'ɔɪ', 'əʊ', 'aʊ', 'ɪə', 'eə', 'ʊə'
    }
}

ARABIC_PHONEMES = {
    'consonants': {
        'b', 't', 'd', 'k', 'g', 'q', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ',
        'x', 'ɣ', 'ħ', 'ʕ', 'h', 'm', 'n', 'l', 'r', 'w', 'j'
    },
    'vowels': {
        'a', 'i', 'u', 'aː', 'iː', 'uː', 'aj', 'aw'
    }
}

HEBREW_PHONEMES = {
    'consonants': {
        'b', 'v', 'g', 'd', 'h', 'w', 'z', 'ħ', 't', 'j', 'k', 'l', 'm', 'n',
        's', 'ʕ', 'p', 'f', 'ṣ', 'q', 'r', 'ʃ', 't'
    },
    'vowels': {
        'a', 'e', 'i', 'o', 'u', 'aː', 'eː', 'iː', 'oː', 'uː'
    }
}


def get_phoneme_set(language: str) -> Set[str]:
    """Get phoneme set for a language.
    
    Args:
        language: Language code ('english', 'arabic', 'hebrew')
        
    Returns:
        Set of phonemes for the language
    """
    phoneme_sets = {
        'english': ENGLISH_PHONEMES,
        'arabic': ARABIC_PHONEMES,
        'hebrew': HEBREW_PHONEMES
    }
    
    if language not in phoneme_sets:
        raise ValueError(f"Unsupported language: {language}")
    
    phoneme_set = phoneme_sets[language]
    return phoneme_set['consonants'].union(phoneme_set['vowels'])


def get_common_confusions(l1: str, l2: str) -> List[tuple]:
    """Get common phoneme confusions between L1 and L2.
    
    Args:
        l1: First language
        l2: Second language
        
    Returns:
        List of (l1_phoneme, l2_phoneme) tuples
    """
    confusions = {
        ('english', 'arabic'): [
            ('θ', 't'), ('ð', 'd'), ('v', 'w'), ('ɪ', 'iː'),
            ('æ', 'a'), ('ʌ', 'a'), ('ɜː', 'ə')
        ],
        ('arabic', 'english'): [
            ('q', 'k'), ('ħ', 'h'), ('ʕ', 'ʔ'), ('x', 'h'),
            ('ɣ', 'g'), ('ṣ', 's'), ('ṭ', 't'), ('ḍ', 'd')
        ],
        ('hebrew', 'english'): [
            ('ʁ', 'ɹ'), ('x', 'h'), ('ɣ', 'g'), ('ħ', 'h'),
            ('ʕ', 'ʔ'), ('ṣ', 's'), ('ṭ', 't'), ('ḍ', 'd')
        ]
    }
    
    key = (l1, l2)
    if key in confusions:
        return confusions[key]
    
    # Try reverse direction
    key = (l2, l1)
    if key in confusions:
        return [(l2, l1) for l1, l2 in confusions[key]]
    
    return []


def is_phoneme_valid(phoneme: str, language: str) -> bool:
    """Check if a phoneme is valid for a language.
    
    Args:
        phoneme: Phoneme symbol
        language: Language code
        
    Returns:
        True if phoneme is valid for the language
    """
    phoneme_set = get_phoneme_set(language)
    return phoneme in phoneme_set


def get_phoneme_category(phoneme: str) -> str:
    """Get the category of a phoneme.
    
    Args:
        phoneme: Phoneme symbol
        
    Returns:
        Phoneme category ('consonant', 'vowel', 'diphthong')
    """
    # Check if it's a diphthong (contains two vowel symbols)
    if len(phoneme) > 1 and all(c in 'aeiouɑɒɔʊuɪəɜ' for c in phoneme):
        return 'diphthong'
    
    # Check if it's a vowel
    if phoneme in 'aeiouɑɒɔʊuɪəɜ':
        return 'vowel'
    
    # Otherwise it's a consonant
    return 'consonant'


def get_articulatory_features(phoneme: str) -> Dict[str, str]:
    """Get articulatory features for a phoneme.
    
    Args:
        phoneme: Phoneme symbol
        
    Returns:
        Dictionary of articulatory features
    """
    # TODO: Implement comprehensive articulatory feature mapping
    features = {
        'θ': {
            'manner': 'fricative',
            'place': 'dental',
            'voicing': 'voiceless',
            'description': 'Place tongue tip between teeth, blow air'
        },
        'ð': {
            'manner': 'fricative', 
            'place': 'dental',
            'voicing': 'voiced',
            'description': 'Place tongue tip between teeth, add voice'
        },
        'v': {
            'manner': 'fricative',
            'place': 'labiodental', 
            'voicing': 'voiced',
            'description': 'Lower lip touches upper teeth, add voice'
        }
    }
    
    return features.get(phoneme, {
        'manner': 'unknown',
        'place': 'unknown', 
        'voicing': 'unknown',
        'description': f'Practice {phoneme} pronunciation'
    }) 