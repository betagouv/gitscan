## Changelog : conseillers-entreprises (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'accessibilité, la performance et la qualité du code. Des corrections ont été apportées pour améliorer l'expérience utilisateur, notamment dans la gestion des besoins et des entreprises. L'architecture a été revue avec le passage à esbuild pour remplacer webpack, améliorant ainsi les performances de build. Des améliorations de la documentation et des corrections de bugs ont également été implémentées.

### Évolutions fonctionnelles

*   **Historique des besoins :** Affichage des besoins inaccessibles dans l'historique d'une entreprise [#4550](https://github.com/betagouv/conseillers-entreprises/issues/4550).
*   **Rapports :** Ajustement de la formulation dans les rapports [#4597](https://github.com/betagouv/conseillers-entreprises/issues/4597).
*   **Évolution des statistiques :** Affichage de l'évolution des statistiques en pourcentage relatif [#4518](https://github.com/betagouv/conseillers-entreprises/issues/4518).
*   **Formulaires :** Autofocus sur les champs de localisation et de SIRET en cas d'erreur, améliorant l'accessibilité [#4569](https://github.com/betagouv/conseillers-entreprises/issues/4569).
*   **Sollicitations :** Correction pour éviter de passer des SIRETs vides dans les champs cachés des formulaires [#4524](https://github.com/betagouv/conseillers-entreprises/issues/4524).
*   **Email :** Amélioration de l'affichage du corps des emails de sollicitation dans l'interface d'administration.

### Évolutions techniques

*   **Migration vers esbuild :** Remplacement de webpack par esbuild pour améliorer les performances de build et simplifier la configuration [#4520](https://github.com/betagouv/conseillers-entreprises/issues/4520).
*   **Concurrence :** Augmentation du nombre de threads Rails et de processus Puma pour améliorer la concurrence et la réactivité de l'application [#4546](https://github.com/betagouv/conseillers-entreprises/issues/4546).
*   **Base de données :** Augmentation de la taille du pool de connexions à la base de données pour gérer une charge plus importante.
*   **Suppression de jQuery :** Suppression de l'utilisation de jQuery au profit de code JavaScript moderne [#4542](https://github.com/betagouv/conseillers-entreprises/issues/4542).
*   **Refactoring :** Simplification et nettoyage du code, notamment dans les contrôleurs et les services liés à la gestion du temps.
*   **Documentation :** Mise à jour de la documentation de l'architecture, incluant des informations sur la pile technologique et le pipeline de déploiement [#4463](https://github.com/betagouv/conseillers-entreprises/issues/4463).

### Autres changements

*   **LLM :** Ajout d'un endpoint machine-readable `llms.txt` pour faciliter l'intégration avec des modèles de langage.
*   **Tests :** Ajout de tests unitaires et d'intégration pour améliorer la couverture et la fiabilité du code.
*   **Dépendances :** Mise à jour de certaines dépendances (undici, concurrent-ruby, nokogiri).
*   **Configuration :** Correction de la configuration de la base de données pour la production.
*   **Accessibilité :** Améliorations de l'accessibilité des formulaires avec l'utilisation d'attributs ARIA.
*   **Corrections :** Correction de bugs mineurs et améliorations de la qualité du code.
*   **Matomo :** Réintégration des événements Matomo.
*   **Locales :** Mise à jour des traductions françaises.
