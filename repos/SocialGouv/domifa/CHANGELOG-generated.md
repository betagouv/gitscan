## Changelog : domifa (30 derniers jours, au 16 octobre 2026)

### Résumé
Les dernières semaines ont été marquées par l'introduction d'un mode "support" pour sécuriser les tests et l'assistance, ainsi que par une refonte de l'interface de connexion. La sécurité a été renforcée via une meilleure gestion de l'expiration des mots de passe et une identification plus robuste des bénéficiaires.

### Évolutions fonctionnelles
- **Mode Support :** Création d'un mode dédié permettant de simuler des processus sans impacter les données réelles (désactivation automatique des formulaires et des boutons d'action).
- **Sécurité et Accès :**
    - Mise en place de l'expiration des mots de passe (60 mois) et de l'historique des changements.
    - Amélioration des droits de consultation de l'historique et de l'audit des accès ([#4314](https://github.com/SocialGouv/domifa/pull/4314)).
- **Gestion des bénéficiaires :** Amélioration de la gestion des ayants droit et des membres de la famille ([#4291](https://github.com/SocialGouv/domifa/pull/4291)).
- **Interface Utilisateur :**
    - Refonte de la page de connexion et des en-têtes ([#4313](https://github.com/SocialGouv/domifa/pull/4313), [#4307](https://github.com/SocialGouv/domifa/pull/4307)).
    - Mise à jour de la charte graphique (couleurs des boutons et des titres) ([#4311](https://github.com/SocialGouv/domifa/pull/4311), [#4303](https://github.com/SocialGouv/domifa/pull/4303)).

### Évolutions techniques
- **Infrastructure et CI/CD :**
    - Migration de l'environnement de développement et de production vers Node.js 24.
    - Optimisation des pipelines GitLab (gestion des images runtime et injection d'URLs au démarrage).
- **Architecture et Données :**
    - Migration vers les UUID v7 pour une identification plus performante et sécurisée des bénéficiaires et ayants droit.
    - Renforcement des validations de données et de la sécurité des processus d'authentification.
- **Tests et Observabilité :**
    - Ajout de tests de bout en bout (E2E).
    - Amélioration du suivi des erreurs et de la capture de messages via Sentry.

### Autres changements
- Nettoyage des migrations de base de données et suppression de dépendances inutilisées.
