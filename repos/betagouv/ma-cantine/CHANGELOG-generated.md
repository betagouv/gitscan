## Changelog : ma-cantine (30 derniers jours, au 09/10/2026)

### Résumé
Ce mois a été marqué par une préparation intensive de la campagne de télédéclaration 2026. Le projet a bénéficié d'une refonte majeure du parcours utilisateur pour les télédéclarations, incluant un nouveau tunnel de saisie plus intuitif, des formulaires enrichis et une meilleure gestion des erreurs. Parallèlement, des optimisations techniques importantes ont été réalisées sur le traitement des données (dbt), l'automatisation des tâches et la performance de la chaîne d'intégration continue (CI/CD).

### Évolutions fonctionnelles

* **Télédéclaration (TD) :**
    * Mise en place d'un nouveau tunnel de saisie structuré par étapes (origine, couverts annuels, EGalim, circuit court, etc.) ([#7034](https://github.com/betagouv/ma-cantine/issues/7034)).
    * Introduction de deux modes de saisie : un formulaire simplifié et un formulaire détaillé ([#7051](https://github.com/betagouv/ma-cantine/issues/7051), [#7294](https://github.com/betagouv/ma-cantine/issues/7294)).
    * Ajout d'un écran récapitulatif permettant de vérifier les données avant la validation finale ([#7102](https://github.com/betagouv/ma-cantine/issues/7102)).
    * Possibilité de modifier une télédéclaration déjà enregistrée ([#7275](https://github.com/betagouv/ma-cantine/issues/7275)).
    * Améliorations de l'expérience utilisateur (UX) : ajout de popups d'avertissement avant de quitter le tunnel, affichage dynamique des erreurs de saisie et mise à jour automatique de la page après validation ([#7174](https://github.com/betagouv/ma-cantine/issues/7174), [#7172](https://github.com/betagouv/ma-cantine/issues/7172), [#1093c20](https://github.com/betagouv/ma-cantine/commit/1093c20)).
    * Intégration de nouveaux indicateurs pour la campagne 2026 (pêche durable, produits fermiers, circuit court, etc.) ([#7180](https://github.com/betagouv/ma-cantine/issues/7180), [#7148](https://github.com/betagouv/ma-cantine/issues/7148)).
* **Diagnostics & Observatoire :**
    * Enrichissement des diagnostics avec de nouveaux champs (définition locale, distance en km) pour la campagne 2026 ([#7230](https://github.com/betagouv/ma-cantine/issues/7230)).
    * Amélioration de l'affichage des notes liées aux objectifs EGalim dans l'observatoire ([#7290](https://github.com/betagouv/ma-cantine/issues/7290)).
* **Administration & Sécurité :**
    * Amélioration de l'interface d'administration pour les applications OAuth2 (filtres par nom d'entreprise, affichage des statistiques de création) ([#7277](https://github.com/betagouv/ma-cantine/issues/7277), [#7274](https://github.com/betagouv/ma-cantine/issues/7274)).
    * Renforcement de la sécurité lors de l'inscription en bloquant les adresses email jetables ([#7060](https://github.com/betagouv/ma-cantine/issues/7060)).
* **Achats :**
    * Augmentation de la taille maximale autorisée pour l'envoi de factures ([#7159](https://github.com/betagouv/ma-cantine/issues/7159)).

### Évolutions techniques

* **Architecture & API :**
    * Refactorisation majeure de la logique de télédéclaration pour isoler les règles de gestion par année dans des fichiers de configuration dédiés ([#7129](https://github.com/betagouv/ma-cantine/issues/7129), [#7108](https://github.com/betagouv/ma-cantine/issues/7108)).
    * Optimisation de l'API via l'utilisation d'un mixin pour les serializers en lecture seule ([#7293](https://github.com/betagouv/ma-cantine/issues/7293)).
    * Correction d'un bug sur l'API Achats concernant la mise à jour partielle des caractéristiques ([#7287](https://github.com/betagouv/ma-cantine/issues/7287)).
* **Données & dbt :**
    * Optimisation des performances de transfert de données en remplaçant pandas par la commande `COPY` ([#7207](https://github.com/betagouv/ma-cantine/issues/7207)).
    * Automatisation de l'exécution des modèles dbt via une tâche asynchrone nocturne ([#7118](https://github.com/betagouv/ma-cantine/issues/7118)).
    * Amélioration de la qualité du code SQL avec l'intégration de `sqlfluff` ([#7117](https://github.com/betagouv/ma-cantine/issues/7117)).
* **Infrastructure & CI/CD :**
    * Optimisation de la CI : parallélisation des tests frontend/backend et exécution conditionnelle basée sur les fichiers modifiés ([#7160](https://github.com/betagouv/ma-cantine/issues/7160), [#7169](https://github.com/betagouv/ma-cantine/issues/7169)).
    * Augmentation de la puissance de calcul (vCPU) pour les pipelines de test ([#7240](https://github.com/betagouv/ma-cantine/issues/7240)).
    * Extension de l'historique de conservation des tâches Celery à 30 jours ([#7233](https://github.com/betagouv/ma-cantine/issues/7233)).
* **Monitoring :**
    * Amélioration de la fiabilité de la remontée d'erreurs vers Sentry ([#7286](https://github.com/betagouv/ma-cantine/issues/7286)).

### Autres changements

* **SEO & Visibilité :** Optimisation du sitemap, mise en cache et ajout d'un fichier `robots.txt` pour protéger les environnements de staging ([#7111](https://github.com/betagouv/ma-cantine/issues/7111), [#7099](https://github.com/betagouv/ma-cantine/issues/7099)).
* **Documentation :** Mise à jour de la documentation technique et des procédures d'onboarding ([#7247](https://github.com/betagouv/ma-cantine/issues/7247), [#7188](https://github.com/betagouv/ma-cantine/issues/7188)).
* **Maintenance :** Nettoyage du projet et suppression de dépendances de test inutilisées ([#7239](https://github.com/betagouv/ma-cantine/issues/7239)).
