## Changelog : conseillers-entreprises (30 derniers jours, au 10 novembre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi des étapes clés avec l'intégration de l'authentification ProConnect et le renforcement des outils d'administration. Les capacités d'importation de données ont été modernisées pour plus de fiabilité, et l'annuaire est devenu plus fluide et précis. Enfin, des mises à jour de conformité RGPD ont été appliquées pour sécuriser la gestion des données sensibles.

### Évolutions fonctionnelles
- **Authentification :** Intégration de ProConnect pour la gestion des connexions, des sessions et de la déconnexion des utilisateurs [#4734](https://github.com/betagouv/conseillers-entreprises/pull/4734).
- **Administration :** 
    - Amélioration de la gestion des qualifications : possibilité d'afficher, filtrer et éditer les informations de qualification directement dans l'interface d'administration [#4780](https://github.com/betagouv/conseillers-entreprises/pull/4780).
    - Déploiement d'une nouvelle interface de gestion pour l'importation de fichiers [#4731](https://github.com/betagouv/conseillers-entreprises/pull/4731).
- **Annuaire :** 
    - Correction de l'affichage des résultats de recherche pour les antennes et les conseillers [#4763](https://github.com/betagouv/conseillers-entreprises/pull/4763).
    - Amélioration de la navigation en permettant de cliquer directement sur une cellule pour accéder aux conseillers d'une antenne [#4763](https://github.com/betagouv/conseillers-entreprises/pull/4763).
- **Conformité et Données :** 
    - Mise à jour des mentions d'information et renforcement des accords de traitement pour les données de santé (sujets TIH) [#4762](https://github.com/betagouv/conseillers-entreprises/pull/4762).
    - Amélioration de la gestion des sujets via l'API, permettant de filtrer précisément les éléments qualifiables [#4772](https://github.com/betagouv/conseillers-entreprises/pull/4772).

### Évolutions techniques
- **Performances :** Optimisation de l'Annuaire par la suppression de requêtes SQL redondantes (problèmes de N+1 queries) lors de la récupération des données utilisateurs [#4728](https://github.com/betagouv/conseillers-entreprises/pull/4728).
- **Fiabilité des imports :** 
    - Renforcement de l'importateur CSV pour prévenir les plantages liés aux en-têtes vides ou aux caractères spéciaux (BOM) [#4738](https://github.com/betagouv/conseillers-entreprises/pull/4738) [#4783](https://github.com/betagouv/conseillers-entreprises/pull/4783).
    - Amélioration de la gestion des erreurs lors des processus d'importation pour garantir l'intégrité des données.
- **Refactorisation :** 
    - Conversion massive des vues de l'Annuaire du format HAML vers ERB pour uniformiser le projet [#4764](https://github.com/betagouv/conseillers-entreprises/pull/4764).
    - Simplification des routes de l'Annuaire et des antennes [#4763](https://github.com/betagouv/conseillers-entreprises/pull/4763).
- **API :** Régénération de la documentation Swagger pour garantir la cohérence des endpoints [#4777](https://github.com/betagouv/conseillers-entreprises/pull/4777).

### Autres changements
- **Maintenance :** Synchronisation de la structure de la base de données (schema.rb) [#4748](https://github.com/betagouv/conseillers-entreprises/pull/4748).
- **Nettoyage :** Corrections de formatage du code et nettoyage de fichiers de vues non utilisés [#4788](https://github.com/betagouv/conseillers-entreprises/pull/4788).
