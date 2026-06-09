## Changelog : depots-sauvages (30 derniers jours, au 8 juin 2026)

### Résumé
Ce changelog fait état d'une période d'amélioration continue de l'application, avec une migration majeure du formulaire de constatation depuis Démarches Numériques, des améliorations de sécurité (CSP, PERMISSIONS_POLICY, robots.txt), et des corrections de bugs pour une meilleure expérience utilisateur, notamment sur mobile. La documentation de l'API a également été enrichie.

### Évolutions fonctionnelles
- **Formulaire de constatation :** Migration complète du formulaire de constatation depuis Démarches Numériques vers l'application, incluant des mises à jour de textes et des correctifs post-migration. [#154](https://github.com/betagouv/depots-sauvages/issues/154) [#156](https://github.com/betagouv/depots-sauvages/issues/156) [#157](https://github.com/betagouv/depots-sauvages/issues/157)
- **Affichage conditionnel :** La section "préjudice" n'est plus affichée si aucune plainte n'est déposée. [#165](https://github.com/betagouv/depots-sauvages/issues/165)
- **Page d'accueil :** Mise à jour du contenu de la page d'accueil. [#153](https://github.com/betagouv/depots-sauvages/issues/153)
- **Amélioration du footer et des pages associées :** Mise à jour du footer et des pages associées. [#163](https://github.com/betagouv/depots-sauvages/issues/163)
- **Amélioration des titres et descriptions :** Amélioration des titres, descriptions des pages et du tracking analytics. [#164](https://github.com/betagouv/depots-sauvages/issues/164)
- **Simplification de la connexion :** Simplification du processus de connexion pour les démonstrations. [#155](https://github.com/betagouv/depots-sauvages/issues/155)

### Évolutions techniques
- **Sécurité :** Ajout de la configuration Content Security Policy (CSP) pour renforcer la sécurité de l'application. [#151](https://github.com/betagouv/depots-sauvages/issues/151)
- **Sécurité :** Mise à jour de la politique `PERMISSIONS_POLICY` pour une meilleure gestion des permissions.
- **Indexation :** Ajout d'un fichier `robots.txt` pour empêcher l'indexation de l'environnement de staging par les moteurs de recherche. [#166](https://github.com/betagouv/depots-sauvages/issues/166)
- **Documentation :** Ajout de la documentation de l'API. [#160](https://github.com/betagouv/depots-sauvages/issues/160)
- **Licence :** Ajout du fichier de licence. [#159](https://github.com/betagouv/depots-sauvages/issues/159)
- **Suppression de doublons :** Suppression de l'email de contact en doublon avec l'email de l'utilisateur. [#161](https://github.com/betagouv/depots-sauvages/issues/161)
- **Correction des tests unitaires :** Correction de problèmes dans les tests unitaires.

### Autres changements
- **Analytics :** Correction d'un bug lié à la remontée des données analytics dans Matomo et amélioration des popups Tally. [#152](https://github.com/betagouv/depots-sauvages/issues/152)
- **Correction bug mobile :** Correction d'un bug empêchant la fermeture du menu sur la version mobile. [#150](https://github.com/betagouv/depots-sauvages/issues/150)
- **Correctif champs préjudice :** Correction d'un problème avec les champs "préjudice". [#162](https://github.com/betagouv/depots-sauvages/issues/162)
- **Migration dossiers DN :** Migration des dossiers manquants de Démarches Numériques. [#158](https://github.com/betagouv/depots-sauvages/issues/158)
