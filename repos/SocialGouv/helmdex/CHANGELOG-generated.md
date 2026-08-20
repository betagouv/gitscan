## Changelog : helmdex (30 derniers jours, au 19 août 2026)

### Résumé
Ce mois a marqué une étape majeure avec le passage à la version 0.8.0. Helmdex s'est considérablement enrichi avec le lancement d'une interface web complète (React SPA) et l'amélioration de l'expérience desktop via la gestion de workspaces et de thèmes. Parallèlement, un effort important a été porté sur la sécurisation de l'application et la simplification de l'accès aux sources de données privées.

### Évolutions fonctionnelles
- **Nouvelle Interface Web :** Déploiement d'une application web (SPA React) intégrée, incluant un tableau de bord, la gestion des dépendances, des valeurs, des fichiers et un catalogue.
- **Améliorations Desktop :**
    - Introduction de workspaces multi-dossiers avec titres personnalisés et modes d'affichage variés.
    - Navigation améliorée avec un rail de dossiers extensible affichant les détails de chemin.
    - Système d'auto-mise à jour avec redémarrage automatique.
    - Ajout d'une boîte de dialogue "À propos" permettant de vérifier les mises à jour.
- **Gestion des données et édition :**
    - Nouveau configurateur de formulaires basé sur des schémas et éditeur de sources.
    - Support du Markdown pour la lecture des README.
    - Édition de valeurs "in-place" avec affichage des différences (minimal-diff).
    - Validation automatique des schémas lors de l'enregistrement des fichiers de valeurs.
- **Gestion des sources :**
    - Connexion simplifiée (frictionless) pour les sources de charts privées (OCI, dépôts Helm, Git).
    - Support de dépôts agnostiques permettant l'utilisation d'états externes et de chaînes de configuration.
- **Corrections d'interface :**
    - Résolution des problèmes de rechargement intempestif des onglets d'inspection dans l'interface web.
    - Meilleure distinction entre les artefacts de charts absents et les échecs de téléchargement.

### Évolutions techniques
- **Architecture et Serveur :**
    - Migration de l'application desktop vers Wails v2.
    - Mise en place d'une API HTTP locale avec interface web embarquée.
    - Refonte de l'authentification pour permettre une détection parallèle et plus performante.
- **Sécurité et Robustesse :**
    - Correction de vulnérabilités critiques : injections de shell, exfiltration de credentials et traversées de chemin (path traversal).
    - Renforcement de la validation des fichiers pour rejeter le YAML/JSON malformé.
    - Protection contre les corruptions de configuration lors de l'enregistrement.
- **Infrastructure et CI/CD :**
    - Mise à jour de l'environnement de build vers Go 1.25 (Docker et Devbox).
    - Amélioration de la compatibilité Linux : correction des builds AppImage et support de l'affichage sur Ubuntu 24.04 (Wayland/WebKitGTK).
    - Mise en place de tests de bout en bout (E2E) hermétiques couvrant l'ensemble des surfaces (Desktop, Web, TUI, CLI).

### Autres changements
- **Documentation :** Mise à jour du README pour positionner l'application desktop comme une interface de premier plan.
- **Refactoring :** Simplification de l'interface web par l'utilisation de composants de navigation plus standards.
