## Changelog : domifa (30 derniers jours, au 07/08/2026)

### Résumé
Ce mois a été marqué par une montée de version majeure de l'infrastructure technique (passage à Angular 20) et l'enrichissement du portail usagers. Les utilisateurs bénéficient désormais de nouvelles fonctionnalités comme l'intégration du RGAA, la possibilité de télécharger des affiches "Mon Domifa" et l'ajout de contenus pédagogiques via une vidéo de présentation.

### Évolutions fonctionnelles
- **Nouveautés usagers** : Intégration du RGAA sur le portail usagers ([#4227](https://github.com/SocialGouv/domifa/pull/4227)) et ajout d'un bouton de téléchargement pour les affiches "Mon Domifa" ([#4217](https://github.com/SocialGouv/domifa/pull/4217)).
- **Gestion des témoins** : Ajout d'une section et d'un bouton dédié aux témoins ([#4212](https://github.com/SocialGouv/domifa/pull/4212)).
- **Expérience utilisateur** : 
    - Intégration d'une vidéo de présentation pour découvrir Domifa.
    - Amélioration de la clarté des informations de statut lors de la génération de comptes en masse ([#4219](https://github.com/SocialGouv/domifa/pull/4219)).
    - Ajustements ergonomiques sur les pages de gestion des utilisateurs et de l'interface d'administration.

### Évolutions techniques
- **Migration majeure** : Mise à jour complète de l'écosystème frontend vers Angular 20 (incluant CDK, CLI, NGRX) et passage à Node 22.
- **Optimisation Backend** : 
    - Refactorisation de la gestion des codes OTP (One-Time Password).
    - Amélioration du processus de suppression d'utilisateurs (nettoyage des listes et synchronisation avec Brevo).
- **Infrastructure & CI/CD** : 
    - Migration des builds d'images vers `buildkit-operator`.
    - Refactorisation de la configuration Nginx pour centraliser la gestion des fichiers de configuration et renforcer la sécurité via les headers.
- **Corrections de bugs** : 
    - Résolution d'un problème d'affichage des dates de dernière connexion pour les superviseurs admin ([#4223](https://github.com/SocialGouv/domifa/pull/4223)).
    - Correction de l'affichage textuel sur le modal de réinitialisation de mot de passe ([#4228](https://github.com/SocialGouv/domifa/pull/4228)).
    - Refactorisation du composant de formatage des grands nombres (Big Number Pipe) ([#4233](https://github.com/SocialGouv/domifa/pull/4233)).

### Autres changements
- **Documentation** : Mise à jour des contenus de la FAQ et des Conditions Générales d'Utilisation (CGU).
- **Accessibilité & Sécurité** : Amélioration de l'accessibilité (attributs ARIA) et renforcement de la sécurité des liens externes (`noopener noreferrer`).
