import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Configuration du logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Fonction pour démarrer le bot et envoyer un message de bienvenue personnalisé
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    keyboard = [
        [InlineKeyboardButton("Dépôt", callback_data='deposit')],
        [InlineKeyboardButton("Retrait", callback_data='withdraw')],
        [InlineKeyboardButton("Assistance", callback_data='support')],
        [InlineKeyboardButton("Pronostics", callback_data='predictions')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_message = f"Bienvenue {user_first_name} sur TRINITYBET !Je suis TRINITY, l'assistant virtuel dédié à TRINITYBET. Mon rôle est de vous aider à effectuer vos dépôts et retraits 1XBET en toute sécurité. De plus, je vous tiendrai informé des dernières actualités sportives et vous fournirai des conseils de pronostics pour maximiser vos chances de succès. Choisissez une option ci-dessous :"
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

# Fonction de gestion des réponses aux boutons interactifs
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Accusé de réception du clic sur le bouton

    if query.data == 'deposit':
        keyboard = [
            [InlineKeyboardButton("Carte de Crédit", url='https://trinitybet.site')],
            [InlineKeyboardButton("PayPal", url='https://trinitybet.site')],
            [InlineKeyboardButton("Virement Bancaire", url='https://trinitybet.site')],
            [InlineKeyboardButton("Autres", url='https://trinitybet.site')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Choisissez une méthode de paiement :", reply_markup=reply_markup)
    
    elif query.data == 'withdraw':
        keyboard = [[InlineKeyboardButton("Poursuivre", url='https://trinitybet.site')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Appuyez sur 'Poursuivre' pour continuer.", reply_markup=reply_markup)
    
    elif query.data == 'support':
        await query.edit_message_text("Contactez notre assistance via WhatsApp : https://wa.me/58241805")
    
    elif query.data == 'predictions':
        await query.edit_message_text("Consultez nos derniers pronostics sportifs : https://www.coze.com/store/bot/7407786417629216774?bot_id=true")

# Fonction principale pour démarrer le bot
def main():
    # Remplacez 'YOUR_TOKEN' par le token de votre bot Telegram
    application = Application.builder().token('7454324787:AAHzVFam7tWBBLHqcQG_G0ZYc7uN2hi_qeA').build()

    # Gestionnaires de commandes
    application.add_handler(CommandHandler('start', start))

    # Gestionnaire de retour des boutons
    application.add_handler(CallbackQueryHandler(button_callback))

    # Démarre le bot en mode polling
    application.run_polling()

# Exécute le bot
if __name__ == '__main__':
    main()
