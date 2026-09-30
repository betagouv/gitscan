## Changelog : ma-cantine (30 derniers jours, au 29 septembre 2026)

### Résumé
Ce mois a été marqué par un travail intensif sur la préparation de la campagne de télédéclaration (TD) 2026. De nouvelles étapes de saisie ont été intégrées, accompagnées d'une amélioration significative de l'expérience utilisateur (UX) pour guider les établissements. Parallèlement, la sécurité a été renforcée avec l'introduction de l'authentification à deux facteurs (2FA) et la qualité de la plateforme a été consolidée par une refonte des processus d'intégration continue (CI/CD) et l'intégration de l'outil dbt pour le traitement des données.

### Évolutions fonctionnelles

* **Télédéclarations (TD) 2026 :**
    - Mise en place d'un nouveau tunnel de saisie structuré (étapes origine, couverture annuelle, EGalim, circuits courts, et récapitulatif) [#7034](https://github.com/betagouv/ma-cantine/issues/7034), [#7050](https://github.com/betagouv/ma-cantine/issues/7050), [#7053](https://github.com/betagouv/ma-cantine/issues/7053), [#7056](https://github.com/betagouv/ma-cantine/issues/7056), [#7102](https://github.com/betagouv/ma-cantine/issues/7102).
    - Ajout de nouveaux champs de données pour 2026 (pêche durable, fermier, approvisionnement local et circuit court) [#7180](https://github.com/betagouv/ma-cantine/issues/7180), [#7148](https://github.com/betagouv/ma-cantine/issues/7148).
    - Amélioration de l'UX : affichage des erreurs en temps réel, indicateurs de progression, popups d'avertissement avant de quitter le tunnel et pré-remplissage automatique des champs à zéro [#7174](https://github.com/betagouv/ma-cantine/issues/7174), [#7172](https://github.com/betagouv/ma-cantine/issues/7172), [#7163](https://github.com/betagouv/ma-cantine/issues/7163), [#7139](https://github.com/betagouv/ma-cantine/issues/7139).
    - Intégration de l'affichage du coût des repas et des informations d'achats directement dans le processus de déclaration [#7176](https://github.com/betagouv/ma-cantine/issues/7176), [#7146](https://github.com/betagouv/ma-cantine/issues/7146), [#7037](https://github.com/betagouv/ma-cantine/issues/7037).
    - Refonte de la page établissement pour mieux refléter l'état d'avancement de la télédéclaration [#7179](https://github.com/betagouv/ma-cantine/issues/7179), [#7184](https://github.com/betagouv/ma-cantine/issues/7184).

* **Sécurité et gestion des utilisateurs :**
    - Déploiement de l'authentification à deux facteurs (2FA) via TOTP pour les administrateurs [#7040](https://github.com/betagouv/ma-cantine/issues/7040).
    - Renforcement de la sécurité lors de l'inscription : blocage des adresses emails jetables [#7060](https://github.com/betagouv/ma-cantine/issues/7060) et prévention de l'utilisation d'un email comme nom d'utilisateur [#7081](https://github.com/betagouv/ma-cantine/issues/7081).
    - Amélioration des outils d'administration : nouveaux filtres pour les utilisateurs (email confirmé, super-utilisateur, groupes) et visibilité du statut 2FA [#7080](https://github.com/betagouv/ma-cantine/issues/7080), [#7058](https://github.com/betagouv/ma-cantine/issues/7058).

* **Référencement (SEO) :**
    - Optimisation du sitemap et mise en place d'un fichier `robots.txt` pour protéger les environnements de staging et de démo [#7111](https://github.com/betagouv/ma-cantine/issues/7111), [#7099](https://github.com/betagouv/ma-cantine/issues/7099).

### Évolutions techniques

* **Infrastructure et CI/CD :**
    - Optimisation des pipelines de tests : exécution conditionnelle selon les dossiers modifiés (backend/frontend) et parallélisation des tests pour gagner en rapidité [#7169](https://github.com/betagouv/ma-cantine/issues/7169), [#7168](https://github.com/betagouv/ma-cantine/issues/7168), [#7160](https://github.com/betagouv/ma-cantine/issues/7160).
    - Création d'une CI dédiée à dbt avec intégration du linting SQL (sqlfluff) [#7162](https://github.com/betagouv/ma-cantine/issues/7162), [#7117](https://github.com/betagouv/ma-cantine/issues/7117).

* **Données et dbt :**
    - Initialisation du projet dbt et création de modèles pour alimenter Metabase [#6421](https://github.com/betagouv/ma-cantine/issues/6421).
    - Automatisation de l'exécution de dbt via une tâche asynchrone nocturne [#7118](https://github.com/betagouv/ma-cantine/issues/7118).
    - Mise à jour des cibles SPE dans les modèles de données [#7143](https://github.com/betagouv/ma-cantine/issues/7143).

* **Architecture et Refactoring :**
    - Refonte de la gestion de la logique métier des télédéclarations : séparation de la configuration des champs et des labels par année dans des fichiers dédiés pour faciliter la maintenance [#7129](https://github.com/betagouv/ma-cantine/issues/7129), [#7108](https://github.com/betagouv/ma-cantine/issues/7108), [#7103](https://github.com/betagouv/ma-cantine/issues/7103).
    - Migration du frontend vers `django-vite` pour une meilleure gestion des assets [#7084](https://github.com/betagouv/ma-cantine/issues/7084).
    - Amélioration de la robustesse du code via de nouvelles méthodes utilitaires (`to_decimal`, `get_or_set_cache`) et une meilleure gestion des calculs de pourcentages [#7152](https://github.com/betagouv/ma-cantine/issues/7152), [#7116](https://github.com/betagouv/ma-cantine/issues/7116).

### Autres changements

* **Documentation :** Mise à jour des instructions pour les agents IA (AGENTS.md) [#7112](https://github.com/betagouv/ma-cantine/issues/7112).
* **Configuration :** Correction de la politique de sécurité du contenu (CSP) [#7124](https://github.com/betagouv/ma-cantine/issues/7124) et mise à jour du domaine Crisp [#7142](https://github.com/betagouv/ma-cantine/issues/7142).
