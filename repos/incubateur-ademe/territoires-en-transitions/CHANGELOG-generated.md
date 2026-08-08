## Changelog : territoires-en-transitions (30 derniers jours, au 07/08/2026)

### Résumé
Ce mois a été marqué par un développement majeur autour du nouveau parcours de démarche PCAET, qui intègre désormais un système de suivi par étapes (workflow) pour accompagner les collectivités. Nous avons également progressé sur la transition vers le nouveau référentiel "Climat Ressources" et renforcé significativement la sécurité de la plateforme pour garantir l'étanchéité des données entre les collectivités.

### Évolutions fonctionnelles
- **Parcours PCAET** : Mise en place d'un nouveau système de gestion des démarches PCAET, incluant la création de démarches et un suivi visuel de l'avancement via un workflow dédié.
- **Référentiels** : 
    - Introduction de la vue SGPE avec persistance des réglages (affichage des axes) via le stockage local.
    - Orchestration de la migration des données (services, pilotes, explications) vers le nouveau référentiel.
    - Amélioration de la gestion des statuts et des commentaires lors des transitions de référentiels.
- **Interface Utilisateur (UI)** :
    - Refonte visuelle globale et ajustements de l'ergonomie (taille des badges, espacements, tableaux plus accessibles).
    - Ajout de la fonctionnalité de déconnexion dans la navigation secondaire.
    - Amélioration de la cohérence des exports PDF (alignement des fiches liées).
- **Gestion des données** : Correction de l'affichage des indicateurs et de la courbe des émissions nettes pour une meilleure précision visuelle.

### Évolutions techniques
- **Architecture & Backend** :
    - Création d'un nouveau domaine "démarches" avec une API dédiée (tRPC) et une structure de base de données optimisée (héritage par type).
    - Refonte du `SnapshotsService` utilisant le pattern "Result" pour une gestion d'erreurs plus robuste ([#PR1](https://github.com/incubateur-ademe/territoires-en-transitions/pull/1), [#PR2](https://github.com/incubateur-ademe/territoires-en-transitions/pull/2), [#PR3](https://github.com/incubateur-ademe/territoires-en-transitions/pull/3)).
    - Migration de la gestion des dates de Luxon vers `date-fns`.
    - Refactorisation du module d'authentification, désormais intégré directement dans l'application principale.
- **Sécurité** :
    - Correction de plusieurs vulnérabilités critiques (IDOR) empêchant l'accès aux données d'une collectivité par une autre ([#TET-7358](https://github.com/incubateur-ademe/territoires-en-transitions/issues/7358), [#TET-7359](https://github.com/incubateur-ademe/territoires-en-transitions/issues/7359), [#TET-7360](https://github.com/incubateur-ademe/territoires-en-transitions/issues/7360)).
    - Neutralisation des risques d'injection CSV dans les exports de référentiels.
- **Environnement de développement** :
    - Refonte complète de la stack de développement local : support de conteneurs isolés par "worktree", nouveau tableau de bord interactif en ligne de commande (`make tui`), et gestion simplifiée des variables d'environnement.
    - Amélioration de la CI avec relance automatique des tests E2E en cas de faux négatifs.

### Autres changements
- **Documentation** : Nettoyage et mise à jour du fichier README.
- **Outils** : Création d'un script de génération automatique de diagrammes Mermaid pour visualiser les workflows.
