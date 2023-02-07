from django.shortcuts import render

from tg_bot.Globals import TEXTS
from tg_bot.buttons import btns, inline_btn
from tg_bot.models import *


# Create your views here.


def start(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()

    if not tglog:
        tglog = Log()
        tglog.user_id = user.id
        tglog.message = {"state": 0}
        tglog.save()

    log = tglog.messages

    if not tg_user:
        tg_user = User()
        tg_user.user_id = user.id
        tg_user.name = user.name
        tg_user.username = user.username
        tg_user.save()
        log['state'] = 0
        update.message.reply_text(TEXTS['START'], reply_markup=btns("lang"))

    else:
        if log['state'] >= 10:
            log.clear()
            log['state'] = 10
            update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
        else:
            log['state'] = 0
            update.message.reply_text(TEXTS['START'], reply_markup=btns("lang"))

    tglog.messages = log
    tglog.save()


def message_handler(update, context, ):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()
    log = tglog.messages
    state = log.get('state', 0)
    print(log, state)

    msg = update.message.text
    user = update.message.from_user
    tg_user = User.objects.get(user_id=user.id)
    tglog = Log.objects.filter(user_id=user.id).first()
    msg = update.message.text
    log = tglog.messages
    state = log.get('state', 0)

    if state == 0:
        log['state'] = 1
        if msg == "🇺🇿Uz":
            print("uz")
            tg_user.lang = 1
            tg_user.save()
        elif msg == "🇷🇺Ru":
            print("A")
            tg_user.lang = 2
            tg_user.save()
        else:
            update.message.reply_text(TEXTS['START'], reply_markup=btns("lang"))
            return 0
        update.message.reply_text(TEXTS['NAME'][tg_user.lang])
        tglog.messages = log
        tglog.save()
        return 0

    if log['state'] == 1:
        if msg.isalpha():
            log['name'] = msg
            log['state'] = 2
            update.message.reply_text(TEXTS["CONTACT"][tg_user.lang], reply_markup=btns('contact', lang=tg_user.lang))
        else:
            update.message.reply_text(TEXTS['ERROR1'][tg_user.lang])

    elif log['state'] == 2:
        update.message.reply_text(TEXTS['CONTACT2'][tg_user.lang])
        print(msg)

    if msg == TEXTS['Settings'][1] or msg == TEXTS['Settings'][2]:
        log['state'] = 40
        log['til'] = msg
        update.message.reply_text(TEXTS["LANG"][tg_user.lang], reply_markup=btns("lang", lang=tg_user.lang))
    elif msg == "🇺🇿Uz":
        log['state'] = 41
        tg_user.lang = 1
        tg_user.save()
        update.message.reply_text(TEXTS['SET'][tg_user.lang])
        update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
    elif msg == "🇷🇺Ru":
        log['state'] = 42
        tg_user.lang = 2
        tg_user.save()
        update.message.reply_text(TEXTS['SET'][tg_user.lang])
        update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))

    if msg == TEXTS['Back'][1] or msg == TEXTS['Back'][2]:
        if log['state'] == 17:
            log['state'] = 16
            l = "uz" if tg_user.lang == 1 else "ru"
            d = {
                f"name_{l}": log['cash']
            }
            print("d>>>>>>>>>>", d)
            cash = Cash.objects.filter(**d).first()
            if not cash:
                update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
                return 0
            markup = btns('age', cash=cash)
            print(markup)
            update.message.reply_text(TEXTS['Year'][tg_user.lang], reply_markup=markup)
            tglog.messages = log
            tglog.save()
            return 0

        elif log['state'] == 16:
            log['state'] = 15
            l = "uz" if tg_user.lang == 1 else "ru"
            d = {
                f"name_{l}": log['interests']
            }
            print("d>>>>>>>>>>", d)
            interests = Interests.objects.filter(**d).first()
            if not interests:
                update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
                return 0
            markup = btns('cash', interests=log.get('interests'))
            print(markup)
            update.message.reply_text(TEXTS['Pul'][tg_user.lang], reply_markup=markup)
            tglog.messages = log
            tglog.save()
            return 0
        elif log['state'] == 15:
            log['state'] = 14
            l = "uz" if tg_user.lang == 1 else "ru"
            d = {
                f"name_{l}": log['situation']
            }
            print("d>>>>>>>>>>", d)
            situation = Situation.objects.filter(**d).first()
            if not situation:
                update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
                return 0
            markup = btns('interests', situation=log.get('situation'))
            print(markup)
            update.message.reply_text(TEXTS['Interest'][tg_user.lang], reply_markup=markup)
            tglog.messages = log
            tglog.save()
            return 0
        elif log['state'] == 14:
            log['state'] = 13
            l = "uz" if tg_user.lang == 1 else "ru"
            d = {
                f"name_{l}": log['human']
            }
            print("d>>>>>>>>>>", d)
            human = Human.objects.filter(**d).first()
            if not human:
                update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
                return 0
            markup = btns('situation', human=log.get('human'))
            print(markup)
            update.message.reply_text(TEXTS['Holat'][tg_user.lang], reply_markup=markup)
            tglog.messages = log
            tglog.save()
            return 0
        elif log['state'] == 13:
            log['state'] = 12
            l = "uz" if tg_user.lang == 1 else "ru"
            d = {
                f"name_{l}": log['ctg']
            }
            print("d>>>>>>>>>>", d)
            ctg = Category.objects.filter(**d).first()
            if not ctg:
                update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
                return 0
            markup = btns('human', ctg=log.get('ctg'))
            print(markup)
            update.message.reply_text(TEXTS['Human'][tg_user.lang], reply_markup=markup)
            tglog.messages = log
            tglog.save()
            return 0
        elif log['state'] == 12:
            log['state'] = 11
            update.message.reply_text(TEXTS['SOVGA'][tg_user.lang], reply_markup=btns("ctg", lang=tg_user.lang))
            tglog.messages = log
            tglog.save()
            return 0
        elif log['state'] == 11:
            log['state'] = 10
            update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
            tglog.messages = log
            tglog.save()
            return 0

    if msg == TEXTS['SOVGA'][1] or msg == TEXTS['SOVGA'][2]:
        log['state'] = 11
        update.message.reply_text(TEXTS['SOVGA'][tg_user.lang], reply_markup=btns("ctg", lang=tg_user.lang))
        print("ctg ciqti")

    elif log['state'] == 11:
        log['state'] = 12
        log['ctg'] = msg
        l = "uz" if tg_user.lang == 1 else "ru"
        d = {
            f"name_{l}": msg
        }
        print(d, log, )
        ctg = Category.objects.filter(**d).first()
        if not ctg:
            update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
            return 0
        update.message.reply_text(TEXTS['Human'][tg_user.lang], reply_markup=btns('human', ctg=ctg, lang=tg_user.lang))
        print("human ciqti")
    elif log['state'] == 12:
        log['state'] = 13
        log['human'] = msg
        l = "uz" if tg_user.lang == 1 else "ru"
        d = {
            f"name_{l}": msg
        }
        human = Human.objects.filter(**d).first()
        if not human:
            update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
            return 0
        update.message.reply_text(TEXTS['Holat'][tg_user.lang],
                                  reply_markup=btns('situation', human=human, lang=tg_user.lang))
        print("situation ciqti")

    elif log['state'] == 13:
        log['state'] = 14
        log['situation'] = msg
        print("interest ciqti", msg)
        l = "uz" if tg_user.lang == 1 else "ru"
        d = {
            f"name_{l}": msg
        }
        situation = Situation.objects.get(**d)
        if not situation:
            update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
            return 0
        # situation = Interests.objects.filter(situation=stt)
        update.message.reply_text(TEXTS['Interest'][tg_user.lang],
                                  reply_markup=btns('interests', situation=situation, lang=tg_user.lang))
        print("interest buttoni ciqti")

    elif log['state'] == 14:
        log['state'] = 15
        log['interests'] = msg
        print("cash ciqti", msg)
        l = "uz" if tg_user.lang == 1 else "ru"
        d = {
            f"name_{l}": msg
        }
        interests = Interests.objects.get(**d)
        if not interests:
            update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
            return 0
        rm = btns('cash', interests=interests, lang=tg_user.lang)
        print("btns>>>>>>>>>>>>", rm)
        update.message.reply_text(TEXTS['Pul'][tg_user.lang], reply_markup=rm)
        print("cash buttoni ciqti")

    elif log['state'] == 15:
        log['state'] = 16
        log['cash'] = msg
        print("age ciqti", msg)
        l = "uz" if tg_user.lang == 1 else "ru"
        d = {
            f"name_{l}": msg
        }
        cash = Cash.objects.get(**d)
        if not cash:
            update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
            return 0
        rm = btns('age', cash=cash, lang=tg_user.lang)
        print(rm)
        update.message.reply_text(TEXTS['Year'][tg_user.lang], reply_markup=rm)
        print("age buttoni ciqti")

    elif log['state'] == 16:
        log['state'] = 17
        log['age'] = msg
        l = "uz" if tg_user.lang == 1 else "ru"
        d = {
            f"name_{l}": msg
        }
        age = Agee.objects.filter(**d).first()
        if not age:
            update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
            return 0
        update.message.reply_text(TEXTS['Gift'][tg_user.lang],
                                  reply_markup=btns(type='product', age=msg, lang=tg_user.lang))

    elif log['state'] == 17:
        log['state'] = 17
        log['product'] = msg
        print("kirdi")
        # log["nta"] = 1
        l = "uz" if tg_user.lang == 1 else "ru"
        d = {
            f"name_{l}": msg
        }
        product = Product.objects.filter(**d).first()
        log['price'] = product.price
        update.message.reply_text(TEXTS['Gift'][tg_user.lang], reply_markup=btns("prod"))

        print(product)
        Name = f"{getattr(product, f'name_{l}')}\n" if getattr(product, f'name_{l}') else ""
        Price = f"{product.price}"
        Description = f"{getattr(product, f'description_{l}')}\n" if getattr(product, f'description_{l}') else ""
        context.bot.send_photo(
            photo=open(f'{product.img.path}', 'rb'),
            caption=f"{Name}{Description}{Price}",
            chat_id=user.id,
            # reply_markup=inline_btn('prod'),
        )

    tglog.messages = log
    tglog.save()


def contact_handler(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()
    log = tglog.messages

    contact = update.message.contact
    log['contact'] = contact.phone_number

    print(log, contact)
    if log['state'] == 2:
        tg_user.name = log['name']
        tg_user.phone = log['contact']
        tg_user.save()
        log.clear()
        log['state'] = 10
        update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
        print('number')
    tglog.messages = log
    tglog.save()


def callback_handler(update, context, kwargs=None):
    query = update.callback_query
    data = query.data
    user = query.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()
    log = tglog.messages

    print(data)
    if data == "savat":
        savat = Savat.objects.filter(product=log['product'], user_id=user.id).first()
        if savat:
            # savat.amount = savat.amount + log['nta']
            savat.summ = int(log['price'].strip("so'm").replace(" ", "")) * savat.amount
            savat.save()
        else:
            savat = Savat()
            # savat.amount = log['nta']
            savat.product = log['product']
            savat.priceproduct = log['price']
            savat.user_id = user.id
            print(log)
            # savat.summ = (log['price'])
            savat.save()
        update.callback_query.answer(f"savatga qo'shildi")
        query.message.delete()

    if log['state'] == 30:
        if data == "🧹 Savatni tozalash":
            Savat.objects.filter(user_id=user.id).delete()
            update.callback_query.answer("Savat tozalandi")
            query.message.delete()
        elif data == "⏰ Yetkazib berish vaqti":
            query.message.reply_text(
                "Sizning buyurtmangiz kun davomida yetkazib beriladi aloqada bo'ling kuryermiz siz bilan tez orada bog'landa 😊")
            query.message.delete()
        elif data == "🚕 Buyurtma berish":
            query.message.reply_text(
                f"{user.username} sizning buyurtmangiz qabul qilindi. Qisqa vaqt ichida kuryerimz siz bilan bog'lanadi 😊")
            query.message.delete()
        elif data == "◀️Orqaga":
            log['state'] = 10
            query.message.reply_text("Bosh menulardan birini tanlang!", reply_markup=btns('menu'))
            query.message.delete()
        else:
            Savat.objects.filter(slug=data, user_id=user.id).delete()
            update.callback_query.answer("Savat tozalandi")
            query.message.delete()
            log['state'] = 30
            savat = Savat.objects.filter(user_id=user.id)
            s = "Savatda:\n"
            summa = 0
            for i in savat:
                s += f"{i.amount} ✅ {i.product} {i.summ} \n"
                summa += i.summ
            if summa == 0:
                query.message.reply_text("Savatingiz bo'sh")
            else:
                s += f"Maxsulotlar: {summa} so'm\nYetkazip berish: Shahar ichida bepul"

                query.message.reply_text(s, reply_markup=inline_btn("savat", user_id=user.id))

    tglog.messages = log
    tglog.save()
