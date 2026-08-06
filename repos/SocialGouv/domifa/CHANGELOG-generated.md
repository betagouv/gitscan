## Changelog : domifa (30 derniers jours, au 05 août 2026)

### Résumé
Ce mois a été marqué par une modernisation majeure de l'infrastructure technique, notamment avec le passage à Angular 20. Côté utilisateur, l'expérience a été enrichie par l'ajout de contenus pédagogiques (vidéo de présentation), de nouveaux outils de téléchargement (affiches) et d'une meilleure gestion des témoins et de la génération de comptes en masse.

### Évolutions fonctionnelles
- **Nouveautés et contenu :**
    - Intégration d'une vidéo pour découvrir la plateforme Domifa [#4216](https://github.com/SocialGouv/domifa/pull/4216).
    - Ajout d'un menu et d'un bouton de téléchargement pour les affiches "Mon Domifa" [#cdc9b6a](https://github.com/SocialGouv/domifa/commit/cdc9b6a20b721d8402d9718721ca80c4ae130b84).
    - Ajout d'une section dédiée et d'un bouton pour la gestion des témoins [#ed1e83a](https://github.com/SocialGouv/domifa/pull/4212).
    - Mise à jour des Conditions Générales d'Utilisation (CGU) pour l'année 2026.
- **Améliorations de l'expérience utilisateur (UX) :**
    - Amélioration de la clarté lors de la génération de comptes en masse avec des informations de statut plus précises [#4219](https://github.com/SocialGouv/domifa/pull/4219).
    - Optimisation de l'interface : ajustements de textes, repositionnement de la vidéo et nettoyage visuel (suppression de séparateurs inutiles).
    - Correction du comportement du copier-coller dans les notes [#4211](https://github.com/SocialGouv/domifa/pull/4211).
    - Amélioration de l'accessibilité via l'ajout d'attributs ARIA dans les tableaux.

### Évolutions techniques
- **Modernisation du framework :** Migration complète de l'écosystème frontend vers **Angular 20** (incluant la CLI, le CDK, NgRx et les outils de linting).
- **Infrastructure et CI/CD :**
    - Migration des processus de build d'images vers `buildkit-operator`.
    - Optimisation de la configuration Nginx pour centraliser la gestion des en-têtes de sécurité et partager la configuration entre les différentes applications SPA.
    - Passage à **Node.js 22**.
- **Backend et Sécurité :**
    - Correction d'un bug d'affichage de la date de dernière connexion des superviseurs dans l'administration [#4223](https://github.com/SocialGouv/domifa/pull/4223).
    - Renforcement de la sécurité avec l'ajout systématique des attributs `noopener noreferrer` sur les liens externes.
    - Amélioration de la gestion des domaines autorisés (whitelist) et de la synchronisation des contacts avec Brevo.
- **Observabilité :** Intégration du package **Sentry** pour un meilleur suivi des erreurs en production.

### Autres changements
- Mise à jour de la documentation (FAQ et pages statiques).
- Nettoyage général du code et corrections suite aux revues de code.
