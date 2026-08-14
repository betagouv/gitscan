## Changelog : domifa (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi des étapes importantes en enrichissant l'expérience utilisateur avec de nouveaux contenus (vidéo de présentation, téléchargement d'affiches) et l'intégration du RGAA sur le portail usagers. Parallèlement, des optimisations majeures ont été réalisées sur le moteur d'importation et l'infrastructure pour garantir une meilleure stabilité et performance du service.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités**
    - Intégration du RGAA sur le portail usagers ([#4227](https://github.com/SocialGouv/domifa/pull/4227)).
    - Ajout d'une vidéo de présentation "Découvrir Domifa".
    - Mise à disposition d'un bouton de téléchargement pour les affiches "Mon Domifa".
    - Ajout d'une section dédiée aux témoins avec option d'affichage global ([#4212](https://github.com/SocialGouv/domifa/pull/4212)).
- **Améliorations et corrections**
    - Mise en place de notifications utilisateurs lors de la suppression d'un compte.
    - Amélioration de la clarté des informations de statut lors de la génération massive de comptes ([#4219](https://github.com/SocialGouv/domifa/pull/4219)).
    - Mise à jour des Conditions Générales d'Utilisation (CGU) pour l'année 2026.
    - Correction de l'affichage de la date de dernière connexion pour les superviseurs administrateurs ([#4223](https://github.com/SocialGouv/domifa/pull/4223)).
    - Diverses corrections d'interface (popups, liens, positionnement d'éléments et formulaires).

### Évolutions techniques
- **Performance et Backend**
    - Optimisation critique du processus d'importation : passage par des *worker threads* pour éviter le blocage du serveur et limitation de la concurrence pour stabiliser la charge.
    - Refactorisation complète de la gestion des codes OTP (One-Time Password).
    - Migration de la base de données pour les utilisateurs connectés n'ayant pas effectué leur dernière mise à jour de mot de passe ([#4241](https://github.com/SocialGouv/domifa/issues/4241)).
- **Infrastructure et CI/CD**
    - Migration des processus de construction d'images vers `buildkit-operator`.
    - Amélioration de la résilience des déploiements (détection des pods backend gelés et gestion du *zero-downtime*).
    - Optimisation de la configuration Nginx pour renforcer la gestion des en-têtes de sécurité.
    - Mise à jour majeure de l'environnement de développement (passage à Angular 20 et mise à jour des bibliothèques de monitoring comme Matomo et Sentry).

### Autres changements
- Mise à jour de la documentation d'aide (FAQ).
- Refactorisation de composants internes pour améliorer la maintenance du code (notamment le traitement des grands nombres).
