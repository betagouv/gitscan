## Changelog : infomedicament (30 derniers jours, au 03 juin 2026)

### Résumé
Ce mois-ci, l'équipe s'est concentrée sur l'amélioration de la recherche et de la présentation des informations sur les médicaments. Des optimisations de performance ont été apportées pour accélérer le chargement des données, notamment pour les génériques, les médicaments et les définitions. Une nouvelle fonctionnalité de recherche sémantique basée sur l'IA a été introduite pour les notices, permettant de trouver plus facilement des réponses aux questions des utilisateurs. Enfin, l'interface utilisateur a été modernisée avec de nouvelles cartes de résultats et des filtres améliorés.

### Évolutions fonctionnelles
- **Recherche:** Amélioration de la recherche pour inclure les médicaments de marque dans les résultats de recherche de substances [#194](https://github.com/betagouv/infomedicament/pull/194).
- **Recherche sémantique des notices:** Ajout d'une nouvelle fonctionnalité de recherche sémantique dans les notices, utilisant un modèle de langage (LLM) pour répondre aux questions des utilisateurs et mettre en évidence les passages pertinents.
- **Nouvelle page médicament:** Refonte complète de la page d'un médicament avec une nouvelle présentation des informations et des indications [#222](https://github.com/betagouv/infomedicament/pull/222).
- **Filtres de recherche:** Nouvelle version des filtres de recherche avec une meilleure expérience utilisateur, affichage des filtres même sans résultats et gestion des options "Voir plus / Voir moins".
- **Date de dernière mise à jour:** Ajout d'une indication de la date de dernière mise à jour des données.
- **Icônes des notices:** Correction du fonctionnement des icônes de grossesse, d'alimentation, de pédiatrie et de conduite sur les notices.
- **Affichage des indications:** Amélioration de l'affichage des indications sur les nouvelles cartes de spécifications.

### Évolutions techniques
- **Performance:** Optimisation des performances en déplaçant la récupération des données (génériques, médicaments, définitions) vers le serveur (Server Components).
- **Sitemap:** Génération statique du sitemap lors de la construction du projet avec une revalidation ISR (Incremental Static Regeneration) de 24 heures.
- **Analytics:** Passage de Matomo en mode "cookieless" et suppression du consentement pour les cookies, ainsi que suppression de Hotjar.
- **Refactoring:** Simplification du code lié à la mise en évidence des résultats de recherche dans les notices.
- **Tests:** Ajout de tests unitaires et d'intégration pour la recherche sémantique des notices et les nouvelles fonctionnalités.

### Autres changements
- **Documentation:** Ajout de commentaires "TODO" pour des améliorations futures.
- **Configuration:** Configuration du mode `react-jsx`.
- **Nettoyage de code:** Suppression de code obsolète lié à HyDE/OpenSearch.
- **Corrections:** Correction de bugs mineurs et améliorations de la qualité du code.
