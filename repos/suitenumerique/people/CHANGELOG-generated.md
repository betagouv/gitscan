## Changelog : people (30 derniers jours, au 29 avril 2026)

### Résumé
Cette version apporte des améliorations à la sécurité, notamment en remplaçant l'envoi de mots de passe par des liens de connexion uniques via email et en corrigeant une potentielle escalade de privilèges lors des invitations. Des corrections de bugs et des mises à jour de traductions ont également été intégrées pour améliorer l'expérience utilisateur et la stabilité de l'application.

### Évolutions fonctionnelles
- ✨ Envoi de liens de connexion au lieu de mots de passe pour les nouvelles connexions via dimail.
- 🔒 Correction d'une vulnérabilité potentielle d'escalade de privilèges lors de l'invitation d'utilisateurs.
- 🐛 Amélioration du message d'erreur lorsque l'utilisateur n'a pas d'adresse email secondaire.
- 💬 Amélioration du message affiché lorsqu'il n'y a pas d'alias sur la page de domaine.
- 🧑‍💻 Possibilité d'exporter les informations de contact du domaine depuis l'interface d'administration.
- ✅ Les accès testés lors de la création d'invitations par email ont le rôle attendu.
- 🌐 Mise à jour des chaînes de traduction.

### Évolutions techniques
- ⬆️ Mise à jour de la dépendance `dimail` vers la version 0.6.5.
- ⬆️ Mise à jour de la dépendance `pillow` vers la version 12.2.0 pour des raisons de sécurité.
- ⬆️ Mise à jour de la dépendance `pytest` vers la version 9.0.3 pour corriger une vulnérabilité de sécurité.
- ⬆️ Mise à jour de la dépendance `next` vers la version 15.5.15 pour corriger une vulnérabilité de sécurité.
- ⬆️ Mise à jour de la dépendance `lodash` vers la version 4.18.1 pour corriger une vulnérabilité de sécurité.
- ⬆️ Mise à jour de la dépendance `django` vers la version 6.0.4 pour corriger une vulnérabilité de sécurité.
- 🐛 Correction d'une erreur d'importation pour les boîtes aux lettres fonctionnelles.

### Autres changements
- 🐛 Correction d'un bug où le code de connexion était envoyé à une URL dimail incorrecte.
- 🐛 Correction du nom de la langue affiché dans le menu de profil [#1108].
- 💄 Suppression de la bordure du conteneur dans l'interface utilisateur [#1107].
