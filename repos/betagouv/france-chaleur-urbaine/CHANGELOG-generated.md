## Changelog : france-chaleur-urbaine (30 derniers jours, au 30/10/2026)

### Résumé
Ce mois a été marqué par une transformation majeure de l'outil, notamment avec la refonte complète de l'espace dédié aux gestionnaires territoriaux (CCRT) et le déploiement d'une nouvelle page d'accueil plus intuitive. Parallèlement, le projet a franchi une étape technique cruciale en migrant l'ensemble de ses données depuis Airtable vers une infrastructure interne plus robuste et en renforçant la synchronisation avec ADEME Connect.

### Évolutions fonctionnelles
- **Espace Gestionnaires (CCRT) :** Refonte complète de l'interface pour faciliter le suivi des demandes, la gestion des permissions territoriales, la personnalisation des notifications et le tri des dossiers [#1346](https://github.com/betagouv/france-chaleur-urbaine/pull/1346).
- **Expérience utilisateur :** Nouvelle page d'accueil plus compacte et simplifiée [#1343](https://github.com/betagouv/france-chaleur-urbaine/pull/1343) et amélioration de la clarté des explications sur les choix de solutions via Publicodes [#1349](https://github.com/betagouv/france-chaleur-urbaine/pull/1349).
- **Outils d'administration :** Ajout de la possibilité d'exporter les demandes en format Excel et amélioration des indicateurs de suivi sur le tableau de bord de gestion [#1319](https://github.com/betagouv/france-chaleur-urbaine/pull/1319).
- **Précision des simulations :** Mise à jour des méthodes de calcul du nombre de logements en utilisant la base BDNB pour une meilleure fiabilité des résultats.

### Évolutions techniques
- **Migration de données :** Suppression complète de la dépendance à Airtable au profit d'une gestion interne des réseaux, des fichiers et des demandes, augmentant la stabilité du système [#1327](https://github.com/betagouv/france-chaleur-urbaine/pull/1327).
- **Intégrations :** Optimisation de la synchronisation des rôles et des données avec ADEME Connect [#1324](https://github.com/betagouv/france-chaleur-urbaine/pull/1324).
- **Observabilité et Sécurité :** Amélioration du suivi analytique (PostHog) [#1345](https://github.com/betagouv/france-chaleur-urbaine/pull/1345), séparation des environnements d'erreurs (Sentry) et renforcement de la politique de sécurité du contenu (CSP).
- **Performance des tests :** Parallélisation des tests d'intégration pour réduire les temps de validation.

### Autres changements
- **Documentation :** Mise à jour de la documentation technique concernant Publicodes, la génération des types Kysely et les composants internes.
- **Nettoyage :** Suppression des commandes CLI obsolètes et des reliquats de l'ancienne architecture liée à Airtable.
