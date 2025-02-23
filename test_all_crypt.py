import unittest

from vigenere_crypt import vigenere_encrypt, vigenere_decrypt
from transposition_crypt import simple_transposition_encrypt, simple_transposition_decrypt
from transposition_crypt import double_transposition_encrypt, double_transposition_decrypt
from table_crypt import tabular_cipher_decrypt, tabular_cipher_encrypt  # Import the functions to test
from combined_crypt import combined_encryption, combined_decryption


class TestEncryptionMethods(unittest.TestCase):

    # Constant text for encryption and decryption tests
    text_to_encrypt = """The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. 
    The critic is he who can translate into another manner or a new material his impression of beautiful things. 
    The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things 
    are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. 
    For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an 
    immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of 
    Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his 
    own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in 
    the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist 
    has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. 
    The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist 
    materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view 
    of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at 
    their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity 
    of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with 
    himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless 
    thing is that one admires it intensely. All art is quite useless."""


    expected_key_length = 13

    expected_encrypted_text_vigenere = """Vyc pkhojt xz rjv agxozfr dm zgrsibtac twplij. Rd ksbvaa hpv rls vctteps rjv ygmwyk ih hpv'j yxf. 
    Hnv cgprkt gh as cyo rhl viyclzgke xurq rldmvki mpulgi mg t bkn mpactzya awy zmeycujgdg cl sepbrkwsa mvoegh. 
    Afg ygvasyk, ah afg cmlxgz, wogt mh tpxmwizsb pq c dmsx cl ruivzkfegtdnp. Twvqg nfd ywtu uvsw ovycbbmj ic icclrxyir khxueu 
    rpt vcxiuea ukkfdnh hvicn ajrpbbbm. Khxz gu r dpnzz. Khdzc yym ubbj sepbrkwsa fsgeicnq ke zttizzfjs rjzlvl oxv twl awcrxoozvd. 
    Uvp vychx hnvrt pq jfnt. Mvkp agl rjv caxqz ko lomo scpnhowua afkeeh fsge ocsw Dvyjmm. Zyegl gu em hnqn khxue cj y bhfgc og hl 
    kdkdkor sodr. Zqfih tfk neas utzrixb, ui bpkja npxmhke. Twhr kj yae. Hnv nxucvvccmv-ivnibpa ughewqv ou ycccghf wy kht yyiv mu 
    Vorzbpu qgvgcz voj olu dctc xg o mcahz. Rjv lxgszvecaf-evlinfe uihsgmv mu Kcsrnipakjk xl hnv rpnc qw Apewhrn cvr uvcxgu nzs 
    ddl hrat bb g xlpzq. Vyc bhfgc lxmc qw kpg tuimh wytk mu mvk juqqcek kpmhki ou afg rpibgz, sui afg dmgtzoky dm ytk adggojth pl 
    vyc exflvci bqg fd pg wsgegmcek ktwwad. Nd hpvzqi wsyzrtz rq gpdos geyiogpx. Ckxb zyicnq vyyi tfk krjl ace zt ifumes. Um cirxlh 
    nrs tafktya lmsgaioggj. Yc xhnzcps qadnpmve zn pu ytkghm wy rn juncibdgohce bhlpvpxla uw sifjg. Em pkhojt xz cxvp bhfhzd. 
    Ioc cirxlh irn tentvqh xjkiyiogpx. Rwhimyt pub nrlvnomv agl rq kft tfzzsi plukpjfstks dm yp rpi. Owiv ack tkirjx oxv td afg rpibgz 
    dailpkrjh ycx rn pyr. Himb mvk goxur qw txxk uw fdyk, vyc irdk ff psj vyc pkhy zs ioc cir dy hnv mjzgezyc. Yfud twl nqzli ht bzel 
    vd hvcabbm, kht havfp'h vfgwt xz rjv rnis. Gcl pyr kj yi hbiv sjydctc pgr ypmqvj. Vymhx knf gd icpvyia hnv sjydctc sh gu rt 
    iocki ntkwr. Khdzc yym gxoj kht zwosma wc yf ai afgzp exfoc. Ii pq vyc hisikaivp, ceb chh rzft, afck ygm fkrlaf kkipdkg. Jzvtyqkkw 
    dy cvznxvl csmjm o cfrz vd cir haccj twhr vyc lhfq zs clu, efkeesd, miihj. Yycc vfokirz bkjyvksk kht hpvzqi bg oe arjmtu uxmv 
    nzmhljh. Nc rtb lfrvptg r kpg tui mprgpx y jlslll iogpx yh ectx ah oc ffch gcz rdbppg zr. Ias ueln lvelqt ycx dazpli r shxzkjs 
    iogpx gh mvgk ocl yfdggxg ok icacpjcar. Orc aga gu hsxms ajealqu."""


    def test_vigenere_encryption(self):
        """Test Vigenère encryption and decryption process to ensure text can be encrypted and decrypted correctly."""
        key = "CRYPTOGRAPHY"
        encrypted_text = vigenere_encrypt(self.text_to_encrypt, key)
        self.assertNotEqual(encrypted_text, self.text_to_encrypt)

    def test_vigenere_decryption(self):
        """Test Vigenère decryption and decryption process to ensure text can be encrypted and decrypted correctly."""
        key = "CRYPTOGRAPHY"
        encrypted_text = vigenere_encrypt(self.text_to_encrypt, key)
        decrypted_text = vigenere_decrypt(encrypted_text, key)
        self.assertEqual(decrypted_text, self.text_to_encrypt.upper())

    def test_simple_transposition_encryption(self):
        """Test simple transposition encryption and decryption."""
        key = "SECRET"
        encrypted_text = simple_transposition_encrypt(self.text_to_encrypt, key)
        self.assertNotEqual(encrypted_text, self.text_to_encrypt)

    def test_simple_transposition_decryption(self):
        """Test decryption of text encrypted with simple transposition cipher."""
        encrypted_text = simple_transposition_encrypt(self.text_to_encrypt, "SECRET")
        decrypted_text = simple_transposition_decrypt(encrypted_text, "SECRET")
        self.assertEqual(self.normalize_text(decrypted_text), self.normalize_text(self.text_to_encrypt))

    # def test_double_transposition_encryption(self):
    #     """Test double transposition encryption and decryption."""
    #     key1 = "SECRET"
    #     key2 = "CRYPTO"
    #     encrypted_text = double_transposition_encrypt(self.text_to_encrypt, key1, key2)
    #     decrypted_text = double_transposition_decrypt(encrypted_text, key1, key2)
    #     self.assertEqual(self.normalize_text(decrypted_text), self.normalize_text(self.text_to_encrypt))

    # def test_double_transposition_decryption(self):
    #     """Test decryption of text encrypted with double transposition cipher."""
    #     key1 = "SECRET"
    #     key2 = "CRYPTO"
    #     encrypted_text = double_transposition_encrypt(self.text_to_encrypt, key1, key2)
    #     decrypted_text = double_transposition_decrypt(encrypted_text, key1, key2)
    #     self.assertEqual(self.normalize_text(decrypted_text), self.normalize_text(self.text_to_encrypt))

    # def test_tabular_cipher_encryption(self):
    #     """Test tabular cipher encryption and decryption."""
    #     key = "MATRIX"
    #     encrypted_text = tabular_cipher_encrypt(self.text_to_encrypt, key)
    #     decrypted_text = tabular_cipher_decrypt(encrypted_text, key)
    #     self.assertEqual(self.normalize_text(decrypted_text), self.normalize_text(self.text_to_encrypt))

    # def test_tabular_cipher_decryption(self):
    #     """Test decryption of text encrypted with the tabular cipher."""
    #     key = "MATRIX"
    #     encrypted_text = tabular_cipher_encrypt(self.text_to_encrypt, key)
    #     decrypted_text = tabular_cipher_decrypt(encrypted_text, key)
    #     self.assertEqual(self.normalize_text(decrypted_text), self.normalize_text(self.text_to_encrypt))

    # def test_combined_encryption(self):
    #     """Test combined encryption using Vigenère and tabular ciphers."""
    #     vigenere_key = "CRYPTO"
    #     tabular_key = "MATRIX"
    #     encrypted_text = combined_encryption(self.text_to_encrypt, vigenere_key, tabular_key)
    #     decrypted_text = combined_decryption(encrypted_text, vigenere_key, tabular_key)
    #     self.assertEqual(self.normalize_text(decrypted_text), self.normalize_text(self.text_to_encrypt))

    # def test_combined_decryption(self):
    #     """Test decryption of text encrypted with combined Vigenère and tabular ciphers."""
    #     vigenere_key = "CRYPTO"
    #     tabular_key = "MATRIX"
    #     encrypted_text = combined_encryption(self.text_to_encrypt, vigenere_key, tabular_key)
    #     decrypted_text = combined_decryption(encrypted_text, vigenere_key, tabular_key)
    #     self.assertEqual(self.normalize_text(decrypted_text), self.normalize_text(self.text_to_encrypt))

if __name__ == "__main__":
    unittest.main()
