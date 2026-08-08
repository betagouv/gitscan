## Changelog : gestion-des-subventions-locales (30 derniers jours, au 2026-08-05)

### Résumé
Cette période a été marquée par une refonte majeure du système de notifications, rendant son suivi beaucoup plus visible et intégré au flux de travail des utilisateurs. L'expérience de saisie a également été améliorée grâce à une interface plus réactive et une meilleure gestion des formulaires et des documents. Enfin, l'environnement de développement a été modernisé pour gagner en rapidité.

### Évolutions fonctionnelles
- **Système de notifications** :
    - Refonte complète de l'onglet de gestion des notifications [#783](https://github.com/betagouv/gestion-des-subventions-locales/issues/783).
    - Ajout de badges de notification pour une meilleure visibilité [#788](https://github.com/betagouv/gestion-des-subventions-locales/issues/788).
    - Affichage du statut de notification directement dans les listes de projets [#789](https://github.com/betagouv/gestion-des-subventions-locales/issues/789).
    - Sécurisation du processus : impossibilité de générer ou d'importer des documents lorsqu'un projet est en cours de notification [#790](https://github.com/betagouv/gestion-des-subventions-locales/issues/790).
- **Gestion des projets et documents** :
    - Ajout d'un modèle de lettre de refus [#785](https://github.com/betagouv/gestion-des-subventions-locales/issues/785).
    - Amélioration du formulaire de gestion des projets [#784](https://github.com/betagouv/gestion-des-subventions-locales/issues/784).
    - Corrections diverses sur l'interface (modales de suppression, liens vers les modèles de formulaires).
- **Interface utilisateur** :
    - Correction de l'affichage des erreurs HTMX [#798](https://github.com/betagouv/gestion-des-subventions-locales/issues/798).
    - Amélioration de la gestion des messages d'erreur dans les formulaires.

### Évolutions techniques
- **Infrastructure et outils de développement** :
    - Migration de la gestion des dépendances de `pip-tools` vers `uv` [#786](https://github.com/betagouv/gestion-des-subventions-locales/issues/786).
    - Ajustements de l'environnement pour assurer la compatibilité avec le DSFR [#794](https://github.com/betagouv/gestion-des-subventions-locales/issues/794).
- **Modernisation de l'interface (Frontend)** :
    - Intégration de HTMX pour rendre les formulaires plus dynamiques et fluides (notamment pour l'assiette de dotation [#787](https://github.com/betagouv/gestion-des-subventions-locales/issues/787), les notifications et la génération de documents).
- **Refactorisation du code** :
    - Optimisation du système de notifications (structure de la base de données, propriétés et respect des principes DRY).
    - Refactorisation des filtres et utilisation de "inclusion tags" pour simplifier la gestion des formulaires de documents et de notifications.

### Autres changements
- **Outils métier** : Ajout d'une commande permettant d'importer les données du COG [#782](https://github.com/betagouv/gestion-des-subventions-locales/issues/782).
- **Maintenance** : Nettoyage et optimisation du script de génération de dump `generate_dump.py` [#799](https://github.com/betagouv/gestion-des-subventions-locales/issues/799).
