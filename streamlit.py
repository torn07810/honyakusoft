import streamlit as st
from pykakasi import kakasi
import unicodedata
import re

def moji_list(*args):
    moji = []
    for i in range(len(args)):
        moji.extend([chr(j) for j in range(args[i][0], args[i][1])])
    return moji

moji_lists = moji_list((97, 123),  (48, 58), (12353, 12436), ) 

st.title('翻訳こんにゃく-暗号化・複合化ソフト-')

menu = st.selectbox('メニュー',['ホーム','暗号化','復合化'])

if menu == 'ホーム':
    st.subheader('利用規約')

    st.write('「翻訳こんにゃく-暗号化・複合化ソフト-」は、サービス（以下「本サービス」）を提供するにあたり、次の通り利用規約（以下「本規約」）を定めます。\
        本規約は、利用者及び登録ユーザの方が本サービスを利用するにあたって適用されるルールとなります。\
            本サービスを快適にご利用になるために、本規約の内容をよくお読みください。\
            本サービスをご利用頂いた場合、本規約の内容を理解しており、かつ、本規約の全ての条項について承諾したものとみなします。')

    st.write('（用語の定義）')
    st.write('第2条')
    st.write(' 本契約書上で使用する用語の定義は、次の通りとします。\
    本サービスとは当社が運営する投稿サイト及び関連するサービスです。\
    本サイトとは本サービスのコンテンツが掲載されたウェブサイトをいいます。\
    コンテンツとは当社が本サイトにて提供したもの、または投稿情報を含む情報・画像等の総称です。\
    利用者とは本サイトを閲覧する全ての方をいいます。\
    登録ユーザーとは本サイトのユーザー登録が完了した方をいいます。\
    投稿情報とは登録ユーザーが投稿等により掲載した文章、文字列、画像、コメント等の情報の総称です。\
    登録情報とは登録ユーザーが本サイトにて登録した投稿情報以外の情報の総称です。')

    st.write('（本規約の範囲と変更）')
    st.write('第3条')
    st.write('本規約は、本サービスの提供条件及び本サービスの利用に関する当社と本利用者との間の権利義務関係を定めることを目的とし、本利用者と当社との間の本サービスの利用に関わる一切の関係に適用されます。\
    当社は、本利用者の承諾を得ることなく、当社が適当と判断する方法で本利用者に通知することにより、本規約を変更できるものとします。\
    当社は本利用規約の変更にあたり、変更後の本利用規約の効力発生日の前に相当な期間をもって、本利用規約を変更する旨及び変更後の本利用規約の内容とその効力発生日を当社のウェブサイトに掲示し、\
    またはお客さまに電子メールで通知します。\
    当社がお客さまに変更後の本利用規約の内容を通知し、変更後の本利用規約の効力発生日以降にお客さまが本サービスを利用した場合、お客さまは本利用規約の変更に同意したものとみなします。\
    当社が本サービス用サイト上で掲載する本サービスの利用に関するルールは、そのルールの名称を問わず、本規約の一部を構成するものとします。\
    本規約の内容と、前項のルールその他の本規約外における本サービスの説明等とが矛盾・抵触する場合は、当該説明等の規定を優先させる旨の特段の定めがない限り、\
    本規約の規定が優先して適用されるものとします。')

    st.write('（禁止行為）')
    st.write('第4条')
    st.write('本サービスの利用に際し、当社は登録ユーザに対し、次に掲げる行為を禁止します。\
    違反した場合、強制退会、利用停止、掲載情報の削除等、当社は必要な措置を取ることができます。\
    1.当社または第三者の知的財産権を侵害する行為\
    2.当社または第三者の名誉・信用を毀損または不当に差別もしくは誹謗中傷する行為\
    3.当社または第三者のプライバシー権を侵害する行為\
    4.当社または第三者の個人情報を、事前の許諾なく開示する行為\
    5.当社または第三者の財産を侵害する行為、または侵害する恐れのある行為\
    6.当社または第三者に経済的損害を与える行為\
    7.当社または第三者に対する脅迫的な行為\
    8.IDの利用を停止された者に代わってIDを取得する行為\
    9.本サービスの運営及びシステムに支障を与える行為\
    10.わいせつ、児童ポルノ、品性を欠く内容と当社が判断する投稿を行うこと\
    11.虚偽の情報を投稿すること\
    12.本サイトの趣旨と関係のない画像、文章等の投稿を行うこと\
    13.同一または類似の投稿を行うこと\
    14.法令に違反する投稿を行うこと\
    15.民族的・人種的差別につながる投稿を行うこと\
    16.利用者に嫌悪感を与える投稿を行うこと\
    17.上記の他、当社が不適切と判断する行為')

elif menu == '暗号化':
    st.subheader('暗号化フォーム')
    texts=st.text_input("入力欄")

    st.subheader('ずらす文字数')
    key=int(st.number_input("入力欄",0,100,0))

    if st.button("暗号化") :
        texts = ''.join(texts) #リストエラー対策
        texts = re.findall("[^。]+。?", texts.replace('\n', ''))
        texts = ''.join(texts) #リストエラー対策
        texts = texts.replace('　','') #リストエラー対策
        texts = texts.lower()
        texts = ''.join(texts) #リストエラー対策

        kakasi = kakasi()
        kakasi.setMode('J', 'H') #漢字からひらがなに変換
        kakasi.setMode("K", "H") #カタカナからひらがなに変換
        conv = kakasi.getConverter()

        texts = conv.do(texts)
        en_list = [] # 文字をずらす処理
        for text in texts: #一文字ずつ取り出す
            if text in moji_lists: #文字照合リストに暗号したい文字があれば
                i = moji_lists.index(text) #インデックスを探す何番目か？
                if len(moji_lists) <= (i + key): #文字照合リストよりインデックス＋keyが大きければ
                    s = (key + i) % len(moji_lists) #繰り越したインデックスで追加
                    en_list.append(moji_lists[s])
                else: #文字照合リストよりインデックス＋keyが小さければ
                    en_list.append(moji_lists[i + key]) #そのまま追加
            else: #文字照合リストに暗号したい文字がなければそのまま追加
                en_list.append(text)
                
        texts =  unicodedata.normalize('NFKC', texts)
        en = ''.join(en_list)
        st.write(en)
        
elif  menu == '復合化':
    st.subheader('復号化フォーム')
    texts = st.text_input("入力欄")
    
    st.subheader('ずらした文字数')
    key = int(st.number_input("入力欄",0,100,0))

    if st.button("復号化") :
        de_list = [] # 文字をずらす処理
        
        texts = ''.join(texts) #リストエラー対策
        texts = re.findall("[^。]+。?", texts.replace('\n', ''))
        texts = ''.join(texts) #リストエラー対策
        texts = texts.replace('　','') #リストエラー対策
        texts = texts.lower()
        texts = ''.join(texts) #リストエラー対策
        
        for text in texts: #一文字ずつ取り出す
            if text in moji_lists: #文字照合リストに複合したい文字があれば
                i = moji_lists.index(text) #インデックスを探す
                if i + 1 - key < 0: #インデックスからkeyを引いた値が0より小さければ
                    s = len(moji_lists) - (key - i) # 文字照合リストからkeyからインデックスを引いた値をsとする。
                    if abs(s) >= len(moji_lists): # 絶対値でリスト数から確認
                        s = s % len(moji_lists) # 余りを算定

                    de_list.append(moji_lists[s]) #余り復号化。
                else: #文字照合リストよりインデックス＋keyが小さければ
                    de_list.append(moji_lists[i - key]) #keyを引いたインデックスで複合化
            else: #文字照合リストに複合したい文字がなければそのまま追加
                de_list.append(text)
        de = ''.join(de_list)
        st.write(de)