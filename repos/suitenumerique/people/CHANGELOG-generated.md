## Changelog : people (30 derniers jours, au 20 avril 2026)

Ce mois-ci, les améliorations se concentrent sur la sécurité, l'expérience utilisateur et la gestion des invitations. Une modification importante est le passage à l'envoi de liens de connexion plutôt que de mots de passe, renforçant ainsi la sécurité. Des corrections ont également été apportées pour éviter des potentielles failles de sécurité et améliorer la gestion des erreurs.

### Évolutions fonctionnelles

- ✨ Envoi de liens de connexion au lieu des mots de passe pour une meilleure sécurité.
- 🧑‍💻 Possibilité d'exporter les informations de contact d'un domaine depuis l'interface d'administration.
- 💬 Amélioration du message affiché lorsqu'aucun alias n'est configuré pour un domaine.
- ✅ Les tests garantissent que les accès créés par email ont le rôle attendu.
- 🐛 Correction de l'affichage de la langue actuelle dans le menu de profil [#1108].
- 🐛 Amélioration du message d'erreur lorsque l'utilisateur n'a pas d'adresse email secondaire.

### Évolutions techniques

- 🔒 Correction d'une potentielle escalade de privilèges lors de l'invitation d'utilisateurs.
- ⬆️ Mise à jour de la bibliothèque `dimail` vers la version 0.6.5.
- ⬆️ Mise à jour de la bibliothèque `pillow` vers la version 12.2.0 pour corriger des failles de sécurité.
- 🐛 Correction d'un problème d'importation pour les boîtes aux lettres fonctionnelles.
- 🐛 Correction du chargement de la langue dans le menu de profil.

### Autres changements

- 🌐 Mise à jour des chaînes de traduction.
- 📝 Mise à jour de la documentation concernant `dimail`.
- 🔖 Publication de la version 1.25.0.
- 🔖 Publication de la version 1.24.0.
