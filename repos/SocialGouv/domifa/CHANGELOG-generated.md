## Changelog : domifa (30 derniers jours, au 24 octobre 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de la sécurité des comptes et de l'expérience utilisateur. Les principales évolutions incluent la mise en place de nouvelles politiques de gestion des mots de passe, l'introduction d'un "mode support" pour faciliter l'assistance technique, et une refonte visuelle de plusieurs interfaces (connexion, navigation). La gestion des bénéficiaires au sein des familles a également été renforcée.

### Évolutions fonctionnelles
- **Sécurité et gestion des comptes** :
    - Mise en place d'une politique de renouvellement de mot de passe (expiration à 60 mois et renouvellement forcé après une longue période d'inactivité).
    - Ajout de la possibilité de consulter l'historique des changements de mot de passe.
    - Amélioration de la sécurité des identifiants via l'utilisation d'UUID pour les bénéficiaires.
- **Mode Support** :
    - Création d'un nouveau mode "support" permettant de simuler ou d'assister l'utilisateur, incluant la désactivation des formulaires pour éviter les erreurs de saisie et l'ajustement des conditions de CGU.
- **Gestion des bénéficiaires et accès** :
    - Nouvelle fonctionnalité de gestion des bénéficiaires au sein des familles [#4291](https://github.com/SocialGouv/domifa/pull/4291).
    - Renforcement des capacités d'audit sur les accès.
    - Ajout de nouveaux droits pour la consultation de l'historique et création d'un rôle "super admin" par domaine.
- **Interface Utilisateur (UI)** :
    - Refonte de la page de connexion (logo, en-tête et mise en page) [#4313](https://github.com/SocialGouv/domifa/pull/4313).
    - Amélioration de la navigation dans la page d'historique [#4318](https://github.com/SocialGouv/domifa/pull/4318).
    - Ajustements esthétiques sur les boutons d'accès et les titres pour une meilleure lisibilité [#4303](https://github.com/SocialGouv/domifa/pull/4303), [#4311](https://github.com/SocialGouv/domifa/pull/4311).
    - Correction de l'alignement du formulaire d'inscription [#4328](https://github.com/SocialGouv/domifa/pull/4328).

### Évolutions techniques
- **Infrastructure et CI/CD** :
    - Mise à jour de l'environnement de développement vers Node.js 24.
    - Optimisation des pipelines GitLab CI/CD (gestion des images runtime, injection de variables Sentry et rendu des bundles frontend).
- **Base de données et Backend** :
    - Migration des commandes de base de données vers des fichiers de migration formels pour une meilleure traçabilité.
    - Normalisation des données (noms et prénoms) au niveau du backend.
    - Amélioration de la robustesse des validations de données.
- **Qualité logicielle** :
    - Introduction de tests de bout en bout (E2E) pour sécuriser les flux critiques.

### Autres changements
- Nettoyage de la base de données en supprimant les migrations déjà appliquées en production.
