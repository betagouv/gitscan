## Changelog : france-chaleur-urbaine (30 derniers jours, au 05 novembre 2026)

### Résumé
Ce mois-ci est marqué par une refonte majeure de l'expérience utilisateur, incluant une nouvelle page d'accueil et le lancement d'un espace dédié aux gestionnaires territoriaux (CCRT). Le projet a également franchi une étape technique cruciale avec la migration complète des données hors d'Airtable et le renforcement de la sécurité des comptes administrateurs.

### Évolutions fonctionnelles
- **Nouvelle interface utilisateur** : Refonte complète de la page d'accueil (design plus compact, nouveaux visuels) et intégration de la méthodologie via une fenêtre modale [#1343](https://github.com/betagouv/france-chaleur-urbaine/pull/1343).
- **Espace CCRT (Gestionnaires territoriaux)** : Création d'un espace dédié permettant un meilleur suivi des demandes, une gestion simplifiée des dossiers et des notifications personnalisées selon les préférences des utilisateurs [#1321](https://github.com/betagouv/france-chaleur-urbaine/pull/1321).
- **Amélioration des outils de simulation** : Affinement des critères de faisabilité géothermique (basés sur les sources BRGM et BatEnR) et mise en place du suivi des simulations pour le parcours chaleur renouvelable [#1347](https://github.com/betagouv/france-chaleur-urbaine/pull/1347).
- **Gestion administrative** : Ajout de la possibilité d'exporter les tableaux de gestion en format Excel et amélioration de la synchronisation des rôles avec ADEME Connect [#1324](https://github.com/betagouv/france-chaleur-urbaine/pull/1324).

### Évolutions techniques
- **Migration de données majeure** : Suppression définitive de la dépendance à Airtable pour la gestion des réseaux et des fichiers, désormais gérés nativement dans l'application [#1327](https://github.com/betagouv/france-chaleur-urbaine/pull/1327).
- **Sécurité renforcée** : Mise en place de l'authentification à deux facteurs (TOTP) pour les comptes administrateurs [#1355](https://github.com/betagouv/france-chaleur-urbaine/pull/1355) et durcissement de la politique de sécurité du contenu (CSP).
- **Observabilité et Tracking** : Amélioration du suivi analytique via PostHog (événements de navigation et de formulaires) et isolation des erreurs Sentry par environnement pour éviter la pollution des données de production [#1336](https://github.com/betagouv/france-chaleur-urbaine/pull/1336).
- **Optimisation de la CI** : Parallélisation des tests d'intégration pour réduire les temps de validation des changements [#1326](https://github.com/betagouv/france-chaleur-urbaine/pull/1326).

### Autres changements
- **Documentation** : Mise à jour de la page méthodologie et documentation des règles de choix de solution (Publicodes) [#1356](https://github.com/betagouv/france-chaleur-urbaine/pull/1356).
- **Nettoyage** : Suppression des commandes CLI et des dépendances obsolètes.
