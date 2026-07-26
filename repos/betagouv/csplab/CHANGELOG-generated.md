## Changelog : csplab (30 derniers jours, au 2026-07-25)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur, notamment pour la gestion des recrutements et des organismes. Des efforts importants ont également été consacrés à la sécurisation de l'application avec la mise en place de contrôles d'accès basés sur les rôles (RBAC) et à l'amélioration de la robustesse de l'ingestion de données. Enfin, des optimisations techniques et des refactorings ont été réalisés pour améliorer la maintenabilité et la performance du code.

### Évolutions fonctionnelles
- **Recrutement :**
    - Mise en place du RBAC pour la gestion des recrutements (liste, détails) et des organismes recruteurs [#1026](https://github.com/betagouv/csplab/issues/1026), [#1030](https://github.com/betagouv/csplab/issues/1030), [#1002](https://github.com/betagouv/csplab/issues/1002).
    - Ajout de la fonctionnalité de traitement par lot des candidatures (changement d'étape) [#948](https://github.com/betagouv/csplab/issues/948).
    - Ajout d'une vue Kanban et d'un switch liste pour la gestion des recrutements [#947](https://github.com/betagouv/csplab/issues/947).
    - Ajout de la recherche et des filtres sur la page des candidatures [#977](https://github.com/betagouv/csplab/issues/977), [#900](https://github.com/betagouv/csplab/issues/900), [#899](https://github.com/betagouv/csplab/issues/899).
    - Affichage du pipeline actif pour le processus organisme [#821](https://github.com/betagouv/csplab/issues/821).
- **Gestion des organismes :**
    - Mise en place du RBAC pour la création d'un organisme [#1025](https://github.com/betagouv/csplab/issues/1025).
    - Amélioration de l'interface pour la gestion des organismes [#911](https://github.com/betagouv/csplab/issues/911), [#912](https://github.com/betagouv/csplab/issues/912).
- **Ingestion de données :**
    - Gestion des codes NIV_DIPL dans le mapping du niveau d'études [#1028](https://github.com/betagouv/csplab/issues/1028).
    - Prise en charge des coordonnées GPS des offres [#969](https://github.com/betagouv/csplab/issues/969).
    - Ajout des champs `fin_candidature` et `debut_vacance_poste` aux données upsertées [#970](https://github.com/betagouv/csplab/issues/970).
    - Correction de la sérialisation JSON des dates dans les conditions d'offre [#888](https://github.com/betagouv/csplab/issues/888).
    - Restriction de l'authentification par API key par plages d'IP [#885](https://github.com/betagouv/csplab/issues/885).
    - Ajout de retries pour la récupération du token Talentsoft [#873](https://github.com/betagouv/csplab/issues/873).

### Évolutions techniques
- **Architecture et Refactoring :**
    - Utilisation de l'interface `IPage` au lieu de `ListPage` dans `RecrutementListView` [#1040](https://github.com/betagouv/csplab/issues/1040).
    - Refactorisation des tests [#1017](https://github.com/betagouv/csplab/issues/1017).
    - Migration des données de candidatures et des listes de recrutements vers Pinia Colada (gestion d'état) [#1011](https://github.com/betagouv/csplab/issues/1011), [#983](https://github.com/betagouv/csplab/issues/983), [#1003](https://github.com/betagouv/csplab/issues/1003).
    - Refactorisation du code pour utiliser Pinia Colada pour la gestion des étapes de recrutement [#1011](https://github.com/betagouv/csplab/issues/1011).
    - Séparation de `IOffersRepository` en une base et une ingestion [#887](https://github.com/betagouv/csplab/issues/887).
- **Outils et Infrastructure :**
    - Ajout de tâches `mise` pour simplifier l'utilisation de `make` [#1043](https://github.com/betagouv/csplab/issues/1043).
    - Configuration de la barre d'outils de débogage Django via une variable d'environnement [#974](https://github.com/betagouv/csplab/issues/974).
    - Amélioration de la configuration des déploiements GitHub Pages [#871](https://github.com/betagouv/csplab/issues/871).
    - Mise à jour des dépendances (OCR, web, ingestion) [#950](https://github.com/betagouv/csplab/issues/950), [#951](https://github.com/betagouv/csplab/issues/951), [#952](https://github.com/betagouv/csplab/issues/952).
    - Amélioration des logs [#986](https://github.com/betagouv/csplab/issues/986).
    - Permettre le peuplement des review apps [#975](https://github.com/betagouv/csplab/issues/975).

### Autres changements
- Correction de bugs divers (gestion du thème Storybook, annotations Postgres, crash au montage de l'application en production, etc.) [#1045](https://github.com/betagouv/csplab/issues/1045), [#1041](https://github.com/betagouv/csplab/issues/1041), [#1044](https://github.com/betagouv/csplab/issues/1044), [#1001](https://github.com/betagouv/csplab/issues/1001).
- Suppression de la forme de contrat STAGE [#998](https://github.com/betagouv/csplab/issues/998).
- Remplacement de "temps partiel" par "Temps incomplet" dans le référentiel [#999](https://github.com/betagouv/csplab/issues/999).
- Ajout de skeletons pour les composants [#981](https://github.com/betagouv/csplab/issues/981).
- Mise à jour du CHANGELOG pour la version 0.1.13 [#896](https://github.com/betagouv/csplab/issues/896) et 0.1.12 [#799](https://github.com/betagouv/csplab/issues/799).
- Ajout d'un modèle admin readonly pour StatSnapshot [#894](https://github.com/betagouv/csplab/issues/894).
- Ajout de la configuration des tâches cron [#874](https://github.com/betagouv/csplab/issues/874).
- Archivage des offres absentes de Talentsoft pour une source [#868](https://github.com/betagouv/csplab/issues/868).
- Ajout de l'authentification par API key sur OffersBySourceView [#877](https://github.com/betagouv/csplab/issues/877).
- Correction du schéma OpenAPI de OffersListView pour la pagination [#875](https://github.com/betagouv/csplab/issues/875).
