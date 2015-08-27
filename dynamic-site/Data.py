'''
Delia Akbari
Dynamic Site
August 26, 2015
'''

class Data(object):
    def __init__(self):
        #data & attributes for each objects - clothing pieces with information

        #1.AztecCropTop
        aztec = Clothing()
        aztec.name = 'Aztec Crop Top'
        aztec.price = '$28.00'
        aztec.size = 'Small, Medium, Large'
        aztec.make = '100% Rayon'
        aztec.color = 'Mixed / Pattern'
        aztec.style = 'Crop Top'
        aztec.image = 'images/aztec.png'

        #2.ChanelDripTop
        chanel = Clothing()
        chanel.name = 'Chanel Drip Top'
        chanel.price = '$40.00'
        chanel.size = 'Small, Medium, Large'
        chanel.make = '95% Rayon, 5% Spandex'
        chanel.color = 'White & Black'
        chanel.style = 'Muscle Tee'
        chanel.image = 'images/chanel.png'

        #3.StripedLeggings
        legging = Clothing()
        legging.price = '$40.00'
        legging.size = 'Small, Medium, Large'
        legging.make = '95% Rayon, 5% Spandex'
        legging.color = 'White & Black'
        legging.style = 'Legging Bottoms'
        legging.image = 'images/legging.png'

        #4.MauveTop
        mauve = Clothing()
        mauve.name = 'Mauve Top'
        mauve.price = '$29.00'
        mauve.size = 'Small, Medium, Large'
        mauve.make = '100% Polyester Chiffon'
        mauve.color = 'Creme'
        mauve.style = 'Overlay Top'
        mauve.image = 'images/mauve.png'

        #5.BaitingSuit
        suit = Clothing()
        suit.name = 'White Plunge One Piece'
        suit.price = '$59.00'
        suit.size = 'Small, Medium'
        suit.make = 'N/A'
        suit.color = 'White'
        suit.style = 'One Piece'
        suit.image = 'images/suit.png'