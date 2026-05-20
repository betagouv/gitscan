## Changelog : sante-psy (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment dans l'espace étudiant avec une refonte majeure (v2). Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fluidité de l'application, en particulier au niveau de la connexion et de la création de patients.

### Évolutions fonctionnelles
- **Espace étudiant v2 :** Refonte complète de l'espace étudiant, améliorant l'interface et les fonctionnalités. [#835](https://github.com/betagouv/sante-psy/issues/835)
- **Connexion :** Correction d'un problème empêchant certains étudiants de se connecter correctement. Le nettoyage de l'email avant la connexion assure une meilleure gestion du token. [#838](https://github.com/betagouv/sante-psy/issues/838)
- **Création de patients (psychologues) :** Désactivation du bouton de création de patient pendant le processus pour éviter les doublons suite à des clics multiples. [#837](https://github.com/betagouv/sante-psy/issues/837)

### Évolutions techniques
- **OpenStreetMap :** Correction de la configuration de l'origine pour les tuiles OpenStreetMap, améliorant la sécurité et la compatibilité. [#832](https://github.com/betagouv/sante-psy/issues/832)

### Autres changements
- **Documentation :** Suppression d'un ancien fichier PDF obsolète concernant les psychologues.
