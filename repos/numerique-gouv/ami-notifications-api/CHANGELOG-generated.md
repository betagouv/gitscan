## Changelog : ami-notifications-api (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes pour améliorer l'expérience utilisateur, notamment grâce à une refonte complète du système de suivi (follow-up) et une navigation plus intuitive. La sécurité et la fiabilité ont également été renforcées par l'amélioration des processus d'authentification (Passkeys, FranceConnect) et une gestion plus fine des consentements des utilisateurs.

### Évolutions fonctionnelles
- **Système de suivi (Follow-up) :** Refonte majeure pour permettre la gestion de structures complexes (hiérarchies à plusieurs niveaux) et une meilleure présentation des détails des éléments [#825](https://github.com/numerique-gouv/ami-notifications-api/issues/825).
- **Navigation et Interface :** 
    - Introduction d'une nouvelle fonction de retour pour une navigation plus fluide [#1200](https://github.com/numerique-gouv/ami-notifications-api/issues/1200).
    - Amélioration de l'affichage des checklists (support du markdown, troncature des textes longs) [#1180](https://github.com/numerique-gouv/ami-notifications-api/issues/1180).
    - Ajout d'un carrousel pour les éléments promotionnels [#1142](https://github.com/numerique-gouv/ami-notifications-api/issues/1142).
    - Mise en place de nouveaux types de services (SOS et étapes) avec des icônes dédiées [#1048](https://github.com/numerique-gouv/ami-notifications-api/issues/1048).
- **Authentification et Consentement :**
    - Amélioration de l'expérience de connexion via Passkeys (gestion des erreurs, adaptation aux grands écrans) [#1179](https://github.com/numerique-gouv/ami-notifications-api/issues/1179) et [#1185](https://github.com/numerique-gouv/ami-notifications-api/issues/1185).
    - Optimisation du parcours de consentement (stockage local et nouveaux endpoints) [#911](https://github.com/numerique-gouv/ami-notifications-api/issues/911).
    - Correction des redirections lors de la déconnexion FranceConnect [#1241](https://github.com/numerique-gouv/ami-notifications-api/issues/1241).
- **Accessibilité et UI :** Corrections de l'accessibilité (RGAA) via l'usage de boutons plutôt que de liens [#1104](https://github.com/numerique-gouv/ami-notifications-api/issues/1104) et ajustements cosmétiques (couleurs, icônes, orthographe) [#1203](https://github.com/numerique-gouv/ami-notifications-api/issues/1203), [#1208](https://github.com/numerique-gouv/ami-notifications-api/issues/1208).

### Évolutions techniques
- **Sécurité et Authentification :**
    - Implémentation du support des Passkeys (WebAuthn) pour une authentification sans mot de passe [#1088](https://github.com/numerique-gouv/ami-notifications-api/issues/1088).
    - Renforcement de la sécurité FranceConnect (vérification des signatures des tokens et support JWT) [#1172](https://github.com/numerique-gouv/ami-notifications-api/issues/1172), [#1219](https://github.com/numerique-gouv/ami-notifications-api/issues/1219).
- **Architecture et API :**
    - Migration importante des champs liés aux partenaires pour harmoniser la base de données [#1131](https://github.com/numerique-gouv/ami-notifications-api/issues/1131).
    - Optimisation de la gestion des notifications (déduplication des événements et des notifications planifiées) [#839](https://github.com/numerique-gouv/ami-notifications-api/issues/839), [#1262](https://github.com/numerique-gouv/ami-notifications-api/issues/1262).
    - Refactorisation de la logique de navigation interne (AMIGoto) [#1311](https://github.com/numerique-gouv/ami-notifications-api/issues/1311) et de la gestion des enregistrements d'appareils [#937](https://github.com/numerique-gouv/ami-notifications-api/issues/937).
- **Infrastructure et CI/CD :**
    - Intégration de Sentry pour le monitoring des erreurs en production [#1240](https://github.com/numerique-gouv/ami-notifications-api/issues/1240).
    - Amélioration des pipelines de tests CI pour les plateformes iOS et Android [#1275](https://github.com/numerique-gouv/ami-notifications-api/issues/1275).
    - Mise en place d'un proxy pour les WebSockets [#1292](https://github.com/numerique-gouv/ami-notifications-api/issues/1292).

### Autres changements
- **Qualité de code :** Nettoyage général (apostrophes typographiques [#1161](https://github.com/numerique-gouv/ami-notifications-api/issues/1161), suppression de logs console [#1312](https://github.com/numerique-gouv/ami-notifications-api/issues/1312)).
- **Développement :** Ajout de contrôles de messages de commit via pre-commit [#157](https://github.com/numerique-gouv/ami-notifications-api/issues/157).
