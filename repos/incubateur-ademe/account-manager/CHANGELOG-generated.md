## Changelog : account-manager (30 derniers jours, au 18 août 2026)

### Résumé
Le projet franchit une étape majeure avec son premier déploiement opérationnel. Les développements récents se sont concentrés sur l'automatisation du processus de départ des utilisateurs (offboarding), l'amélioration de la visibilité sur les capacités du système et la mise en place d'outils de collecte de données avec historique.

### Évolutions fonctionnelles
- **Gestion du cycle de départ (offboarding) :** mise en place des fonctionnalités de préparation du départ, suivi des tâches restantes, validation des plans d'action et clôture des dossiers.
- **Pilotage de la collecte :** possibilité de lancer une collecte directement depuis l'interface et consultation de l'historique des exécutions.
- **Audit et visibilité :** ajout d'un écran récapitulant les capacités de l'outil par système et mise en place d'un outil de confrontation entre l'état déclaré et l'état observé.
- **Corrections de bugs :** 
    - Amélioration de la précision des processus de départ (gestion des plans périmés).
    - Masquage des commandes en échec lors de l'affichage en production.
    - Renforcement de la sécurité et de la validation des fichiers de politique (refus des clés inconnues).

### Évolutions techniques
- **Infrastructure et Déploiement :** 
    - Activation du premier déploiement.
    - Intégration de la récupération automatique de la politique depuis un dépôt privé lors du build.
    - Optimisation de l'image Docker (nettoyage des dépendances Prisma inutiles et alignement avec les exigences de pnpm 11 et Coolify).
- **Refactoring :** 
    - Standardisation des variables de configuration SMTP.
    - Renommage des variables système en anglais pour une meilleure compatibilité machine.
- **CI/CD :** Mise à jour des workflows pour abandonner l'utilisation de Node 20.

### Autres changements
- **Documentation :** 
    - Rédaction des procédures de restauration de sauvegarde.
    - Documentation technique des configurations spécifiques (variables Coolify, ports SMTP, variables d'environnement).
    - Planification des prochains chantiers de développement.
