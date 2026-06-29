## Changelog : depots-sauvages (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de sécurité, d'expérience utilisateur et de migration de données. La migration du formulaire de constatation depuis Démarches Numériques est terminée, et de nouvelles fonctionnalités comme une page FAQ ont été ajoutées. Des corrections de bugs et des améliorations de la documentation ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'une page FAQ pour répondre aux questions fréquentes des utilisateurs. [#170](https://github.com/betagouv/depots-sauvages/pull/170)
- Amélioration des redirections après la connexion pour une meilleure expérience utilisateur. [#180](https://github.com/betagouv/depots-sauvages/pull/180)
- Modification des textes et amélioration de l'accessibilité sur la page "mes procédures". [#181](https://github.com/betagouv/depots-sauvages/pull/181)
- Amélioration des titres et descriptions des pages, ainsi que du tracking pour une meilleure analyse. [#164](https://github.com/betagouv/depots-sauvages/pull/164)
- Correction de l'affichage de l'heure. [#176](https://github.com/betagouv/depots-sauvages/pull/176)
- Mise à jour du footer et des pages associées. [#163](https://github.com/betagouv/depots-sauvages/pull/163)
- Le formulaire de constatation a été migré depuis Démarches Numériques vers l'application. [#154](https://github.com/betagouv/depots-sauvages/pull/154)
- Ajout du fichier de licence. [#159](https://github.com/betagouv/depots-sauvages/pull/159)
- Ajout de la documentation API. [#160](https://github.com/betagouv/depots-sauvages/pull/160)

### Évolutions techniques
- Implémentation de mesures de sécurité importantes avec l'ajout de Content Security Policy (CSP) et la correction de problèmes liés à la configuration CSP et CSRF. [#151](https://github.com/betagouv/depots-sauvages/pull/151), [#167](https://github.com/betagouv/depots-sauvages/pull/167), [#169](https://github.com/betagouv/depots-sauvages/pull/169), [#175](https://github.com/betagouv/depots-sauvages/pull/175)
- Suppression du code lié à l'ancienne implémentation Démarches Numériques (DN). [#177](https://github.com/betagouv/depots-sauvages/pull/177)
- Amélioration du "no index" pour les environnements de staging et de développement. [#174](https://github.com/betagouv/depots-sauvages/pull/174)
- Mise à jour de la configuration PERMISSIONS_POLICY. [#168](https://github.com/betagouv/depots-sauvages/pull/168)
- Correction de problèmes liés à la migration des données Démarches Numériques. [#156](https://github.com/betagouv/depots-sauvages/pull/156)
- Suppression des références obsolètes à "dossier" et ajout de tests unitaires. [#183](https://github.com/betagouv/depots-sauvages/pull/183)
- Correction d'un problème lié à `dossierData`. [#182](https://github.com/betagouv/depots-sauvages/pull/182)

### Autres changements
- Mise à jour de la documentation et des librairies. [#178](https://github.com/betagouv/depots-sauvages/pull/178)
- Suppression de l'email de contact en doublon. [#161](https://github.com/betagouv/depots-sauvages/pull/161)
- Mise à jour de textes dans le formulaire de constatation. [#157](https://github.com/betagouv/depots-sauvages/pull/157)
- Modifications de contenus divers. [#173](https://github.com/betagouv/depots-sauvages/pull/173)
- Correction pour les champs préjudice. [#162](https://github.com/betagouv/depots-sauvages/pull/162)
- Ne pas afficher la section préjudice s'il n'y a pas de plainte déposée. [#165](https://github.com/betagouv/depots-sauvages/pull/165)
