## Changelog : Docurba (30 derniers jours, au 30 avril 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations de l'interface utilisateur, notamment un nouveau menu déroulant pour la gestion des utilisateurs et un bandeau d'information sur la page de connexion. Des efforts importants ont également été consacrés à l'amélioration de la stabilité et de la performance de l'application, avec des corrections de tests, des optimisations de la base de données et des ajustements de l'infrastructure de déploiement.

### Évolutions fonctionnelles
- **Authentification:** Remplacement des boutons d'authentification dans l'en-tête par un menu déroulant utilisateur plus intuitif [#1868](https://github.com/MTES-MCT/Docurba/issues/1868).
- **Page de connexion:** Ajout d'un bandeau d'information sur la page de connexion pour clarifier la procédure de création de compte [#1865](https://github.com/MTES-MCT/Docurba/issues/1865) et [#1867](https://github.com/MTES-MCT/Docurba/issues/1867).
- **Navigation:** Correction d'un problème de redirection après la récupération du mot de passe.
- **Filtres:** Maintien des filtres appliqués lors du changement de département.
- **Recherche:** Synchronisation des champs de recherche avec les paramètres de l'URL.

### Évolutions techniques
- **Base de données:**
    - Ajout d'une classe d'index personnalisée `OversizedIndex` pour améliorer les performances.
    - La colonne `commune_id` de la table `CommuneProcedure` est maintenant générée automatiquement.
    - La table `CommuneProcedure` est maintenant un modèle managé.
    - Ajout du type de commune `TextChoice`.
- **Tests:**
    - Amélioration de la robustesse des tests, notamment en utilisant une base de données de test plus proche de la production.
    - Ajout de la couverture de code (coverage) dans les tests CI.
    - Suppression de l'activation de l'environnement virtuel dans les tâches de test.
- **Infrastructure:**
    - Augmentation de la taille du disque et du plan Supabase pour les environnements de revue (review apps) afin de résoudre des erreurs de mémoire récurrentes.
    - Déploiement des serveurs toutes les heures pour nettoyer la mémoire plus fréquemment.
    - Utilisation de la variable `git SHA` pour les builds.
    - Collecte des fichiers statiques lors de la CI pour simuler l'environnement de production.
- **Outils:**
    - Mise à jour de la documentation README.
    - Remplacement de `pytest-env` par l'option `--ds` de la ligne de commande.
    - Refonte du Makefile pour simplifier les commandes.
    - Utilisation d'un environnement virtuel (venv).

### Autres changements
- **Documentation:** Mise à jour de la documentation README avec des instructions pour les nouveaux développeurs.
- **Code:** Suppression des procédures de sondage si elles sont archivées.
- **Style:** Utilisation des couleurs du thème Vuetify au lieu de CSS personnalisé dans le `LoginBanner`.
- **Correction:** Correction d'une erreur de typographie dans les applications de revue.
