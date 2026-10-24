## Changelog : docs (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de la gestion administrative et de la collaboration. Les administrateurs disposent désormais d'outils plus puissants pour gérer les utilisateurs et les documents, tandis que les utilisateurs bénéficient d'un système de mentions par email et d'une interface plus intuitive (emojis, liens automatiques). La sécurité et les performances du système ont également été renforcées, notamment sur la partie recherche et gestion des accès.

### Évolutions fonctionnelles
- **Collaboration & Mentions** : 
    - Mise en place d'un système de mentions avec notifications par email envoyées de manière asynchrone.
    - Amélioration de l'éditeur : ajout d'un sélecteur d'emojis et transformation automatique des liens de documents collés en liens internes.
- **Interface Utilisateur (UI/UX)** :
    - Redesign des pages d'erreur (401, 403) et de l'interface de chargement des fichiers.
    - Amélioration de la lisibilité : gestion automatique des titres longs et des textes dans les exports PDF.
    - Optimisation de l'éditeur : limitation des niveaux de titres (H1 à H3) et suppression de certains éléments visuels superflus pour épurer l'interface.
- **Administration** :
    - Nouveaux outils de gestion des utilisateurs : fusion de comptes, transfert de documents et d'invitations, et filtrage des doublons par email.
    - Meilleure visibilité : affichage de la date de dernière connexion des utilisateurs et de la version actuelle dans l'en-tête de l'administration [#2882](https://github.com/suitenumerique/docs/issues/2882).
- **Accessibilité** :
    - Améliorations pour les lecteurs d'écran et la navigation au clavier (boutons de menu, structure de l'arbre de documents, gestion du focus).

### Évolutions techniques
- **Performance** :
    - Optimisation de la recherche d'utilisateurs via l'utilisation d'index trigrammes.
    - Réduction de la charge serveur grâce à la mise en cache des décisions d'autorisation dans YHub.
- **Sécurité** :
    - Renforcement des contrôles d'accès : les écritures de commentaires et de threads sont désormais strictement liées à l'accès au document.
    - Mise à jour de dépendances critiques pour corriger des vulnérabilités (Pillow, Certifi).
    - Sécurisation du système de mentions (validation UUID, limitation du débit/throttling).
- **Infrastructure & Backend** :
    - Optimisation des images Docker (passage en version "slim" et suppression de pip dans l'image backend).
    - Introduction de nouveaux paramètres de configuration pour le mode de repli HTTP (intervalle de polling, gestion de l'awareness).
    - Transition de l'infrastructure de stockage de Minio vers Silo.
    - Amélioration des configurations Helm pour Kubernetes (gestion des probes).

### Autres changements
- **Internationalisation (i18n)** : Mises à jour massives des chaînes traduites et intégration du contexte Crowdin pour faciliter le travail des traducteurs.
- **Documentation** : Corrections de typos dans le README d'installation et mise à jour des guides de déploiement Kubernetes (Keycloak et Minio).
- **CI/CD** : Amélioration des workflows de test, incluant le linting et le type-checking du serveur de collaboration.
