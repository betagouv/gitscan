## Changelog : helmdex (30 derniers jours, au 21 août 2026)

### Résumé
Ce mois a marqué une étape majeure pour helmdex avec la transition vers une plateforme multi-surfaces. Le projet propose désormais une application desktop complète, une interface web moderne (SPA) et une gestion optimisée des registres OCI. Parallèlement, une attention particulière a été portée à la sécurité et à la robustesse de la gestion des données (YAML/JSON) et des authentifications.

### Évolutions fonctionnelles
- **Application Desktop** :
    - Introduction de la gestion de plusieurs espaces de travail (workspaces) avec thèmes et modes d'affichage personnalisables.
    - Mise en place de l'auto-mise à jour avec redémarrage automatique.
    - Amélioration de la navigation avec un rail de dossiers extensible affichant le nom et le chemin.
    - Ajout d'une boîte de dialogue "À propos" incluant la vérification des mises à jour.
- **Interface Web (Web UI)** :
    - Déploiement d'une nouvelle application React (SPA) incluant un tableau de bord, la gestion des dépendances, des valeurs, des fichiers et un catalogue.
    - Ajout d'un configurateur de formulaires via schémas, d'un éditeur de sources et du support des fichiers README en Markdown.
- **Gestion des registres et OCI** :
    - Possibilité de lister les versions des charts directement depuis les tags du registre [#1](https://github.com/SocialGouv/helmdex/issues/1).
    - Correction du sélecteur de version, de l'affichage des listes et du ciblage des diffs [#2](https://github.com/SocialGouv/helmdex/issues/2).
- **Expérience utilisateur et données** :
    - Authentification simplifiée pour les sources privées (OCI, dépôts Helm, Git).
    - Validation des schémas lors de la sauvegarde des valeurs et rejet des fichiers YAML/JSON malformés pour garantir l'intégrité des données.
    - Amélioration de l'inspection : distinction claire entre l'absence d'artefacts et les échecs de récupération, et suppression des rechargements inutiles des onglets.

### Évolutions techniques
- **Architecture** :
    - Mise en place d'une API HTTP locale avec une interface Web intégrée (embedded shell).
    - Migration de l'application desktop vers Wails v2 pour encapsuler le serveur interne.
    - Refonte de l'authentification pour permettre une détection parallèle et une réduction des doublons de code.
- **Sécurité et Robustesse** :
    - Durcissement majeur contre les attaques par traversée de chemin (path traversal), l'injection de commandes (shell injection), les fuites de configuration et les accès concurrents (race conditions) [#3](https://github.com/SocialGouv/helmdex/issues/3).
    - Amélioration de la gestion des identifiants par endpoint pour les registres.
- **CI/CD et Environnement** :
    - Correction des pipelines de build pour Linux (AppImage et Desktop) sur Ubuntu 24.04.
    - Mise à jour de l'environnement de développement et des conteneurs vers Go 1.25.
    - Mise en place d'une couverture de tests E2E hermétiques sur l'ensemble des surfaces (Desktop, Web, TUI, CLI).

### Autres changements
- **Documentation** : Mise à jour du README pour présenter l'application desktop comme une interface de premier plan et clarification de la présentation des différentes surfaces d'utilisation.
- **Maintenance** : Nettoyage des sorties de build desktop et synchronisation des fichiers de verrouillage (lockfiles).
