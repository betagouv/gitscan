## Changelog : autometa (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, Autometa s'est enrichi de nouvelles capacités d'analyse et d'une interface plus flexible. L'accent a été mis sur l'amélioration de l'expérience utilisateur (gestion des tags, personnalisation de l'accueil) et sur l'extension des sources de données. Parallèlement, l'infrastructure a été optimisée pour gagner en rapidité et en fiabilité, notamment via une meilleure gestion des tâches automatisées et des processus de déploiement.

### Évolutions fonctionnelles
- **Gestion des données :** Création d'une page dédiée aux "Sources de données" avec possibilité de rafraîchissement ([#201](https://github.com/gip-inclusion/autometa/issues/201), [#205](https://github.com/gip-inclusion/autometa/issues/205)) et ajout de sources de données de test ([#202](https://github.com/gip-inclusion/autometa/issues/202)).
- **Interface et UX :** 
    - Personnalisation de la page d'accueil ([#199](https://github.com/gip-inclusion/autometa/issues/199)).
    - Refonte du système de tags pour une meilleure organisation des conversations et des tableaux de bord ([#190](https://github.com/gip-inclusion/autometa/issues/190)).
    - Affichage des filtres sur les vues de tableaux de bord publiées ([#210](https://github.com/gip-inclusion/autometa/issues/210)).
    - Amélioration de la clarté des alertes (dépassement d'abonnement) ([#180](https://github.com/gip-inclusion/autometa/issues/180)) et correction de la sélection multi-lignes dans les conversations ([#185](https://github.com/gip-inclusion/autometa/issues/185)).
    - Correction des erreurs de rendu pour les diagrammes Mermaid ([#198](https://github.com/gip-inclusion/autometa/issues/198)).
- **Nouvelles capacités d'analyse :** Intégration de Tally pour le requêtage ([#167](https://github.com/gip-inclusion/autometa/issues/167)) et ajout de capacités de modélisation bayésienne (MMM) ([#212](https://github.com/gip-inclusion/autometa/issues/212)).

### Évolutions techniques
- **Performance et Optimisation :** Accélération du chargement des pages de tableaux de bord et des tâches planifiées ([#207](https://github.com/gip-inclusion/autometa/issues/207)) et compression des assets lors de la synchronisation vers les buckets publics ([#197](https://github.com/gip-inclusion/autometa/issues/197)).
- **Connectivité et IA :** Ajout d'un connecteur Datadog ([#211](https://github.com/gip-inclusion/autometa/issues/211)) et automatisation nocturne de l'embedding des conversations ([#184](https://github.com/gip-inclusion/autometa/issues/184)).
- **Fiabilité et Infrastructure :** 
    - Amélioration de la gestion des erreurs et des timeouts (Metabase, crons) ([#214](https://github.com/gip-inclusion/autometa/issues/214), [#182](https://github.com/gip-inclusion/autometa/issues/182)).
    - Sécurisation des sauvegardes S3 via le versioning ([#187](https://github.com/gip-inclusion/autometa/issues/187)).
    - Changement de la base de données source ([#168](https://github.com/gip-inclusion/autometa/issues/168)).
- **Développement et CI/CD :** 
    - Mise en place de "review apps" pilotées par la CI ([#191](https://github.com/gip-inclusion/autometa/issues/191), [#204](https://github.com/gip-inclusion/autometa/issues/204)).
    - Refactorisation des clients PostgreSQL ([#203](https://github.com/gip-inclusion/autometa/issues/203)) et renforcement de la suite de tests unitaires ([#181](https://github.com/gip-inclusion/autometa/issues/181)).

### Autres changements
- Optimisation du flux de développement ("paved road") ([#208](https://github.com/gip-inclusion/autometa/issues/208)).
- Correction de chemins absolus pour les hooks ([#213](https://github.com/gip-inclusion/autometa/issues/213)).
