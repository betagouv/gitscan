## Changelog : Docurba (30 derniers jours, au 4 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations de l'interface utilisateur, notamment au niveau de l'authentification et de la navigation, ainsi que par des optimisations techniques importantes concernant les tests, l'infrastructure et la gestion des bases de données. Ces changements visent à améliorer la stabilité, la performance et l'expérience utilisateur de Docurba.

### Évolutions fonctionnelles
- **Authentification :**
    - Ajout d'un menu déroulant pour la gestion du profil utilisateur, remplaçant les boutons d'authentification précédents. [#1868](https://github.com/MTES-MCT/Docurba/issues/1868)
    - Ajout d'une bannière d'information sur la page de connexion pour clarifier la procédure de création de compte. [#1865](https://github.com/MTES-MCT/Docurba/issues/1865) [#1867](https://github.com/MTES-MCT/Docurba/issues/1867)
- **Navigation :**
    - Correction d'un bug empêchant la redirection vers le tableau de bord après la récupération du mot de passe.
    - Amélioration de la gestion des filtres lors du changement de département.
    - Synchronisation des champs de recherche avec les paramètres de l'URL.
- **Interface utilisateur :**
    - Utilisation des couleurs du thème Vuetify pour le style de la bannière de connexion, améliorant la cohérence visuelle.

### Évolutions techniques
- **Tests :**
    - Mise en place d'une infrastructure de tests plus robuste avec l'utilisation d'une base de données de production simulée en CI.
    - Ajout de couverture de code (cov) dans le processus de CI.
    - Suppression du module de création d'objets de test et intégration de FactoryBoy pour une meilleure gestion des données de test.
    - Création de factories pour les modèles User, Profile, Event, Collectivite, Procedure et CommuneProcedure.
    - Correction de tests défaillants.
    - Remplacement du package `pytest-env` par l'option `--ds` en ligne de commande.
- **Infrastructure :**
    - Augmentation de la taille du disque et du plan Supabase pour les environnements de revue afin de corriger les erreurs de mémoire récurrentes.
    - Déploiement des serveurs toutes les heures pour nettoyer la mémoire plus fréquemment.
    - Mise à jour de la configuration du CI pour utiliser le SHA de commit.
- **Base de données :**
    - La colonne `commune_id` de la table `CommuneProcedure` est maintenant générée automatiquement.
    - Ajout du type de commune `CommuneType` avec des choix prédéfinis.
    - Correction de problèmes de migration de base de données.
- **Outils et dépendances :**
    - Mise à jour de plusieurs dépendances : `ruff`, `pytest`, `pytest-cov`, `django-debug-toolbar`, `django-datadog-logger`, `pygments`, `django`.
    - Utilisation d'un environnement virtuel (venv) pour le développement.
    - Mise à jour du Makefile pour simplifier les commandes.

### Autres changements
- Ajout d'un fichier README pour guider les nouveaux développeurs.
- Mise à jour de la documentation et des exemples de communication.
- Corrections de typographie et améliorations de la lisibilité.
- Suppression du module MISE.
- Correction de liens et de références dans la documentation.
