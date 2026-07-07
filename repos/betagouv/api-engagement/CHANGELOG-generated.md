## Changelog : api-engagement (30 derniers jours, au 3 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la performance de l'API, notamment au niveau des requêtes liées aux organisations. De nouvelles fonctionnalités ont été ajoutées pour le suivi des newsletters et l'intégration avec des services tiers comme Brevo et Demarches Simplifiées. Des corrections ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment sur la plateforme et dans le back-office.

### Évolutions fonctionnelles
- Ajout de la possibilité d'enregistrer les adresses email des utilisateurs pour la newsletter via Brevo. [#1209](https://github.com/betagouv/api-engagement/issues/1209)
- Intégration avec Demarches Simplifiées pour l'import de données. [#1154](https://github.com/betagouv/api-engagement/issues/1154)
- Amélioration des filtres de recherche de missions sur la plateforme, avec une logique disjonctive. [#1215](https://github.com/betagouv/api-engagement/issues/1215)
- Ajout de badges de compensation sur la plateforme. [#1173](https://github.com/betagouv/api-engagement/issues/1173)
- Ajout d'un filtre "dispositif" pour les missions sur la plateforme. [#1211](https://github.com/betagouv/api-engagement/issues/1211)
- Amélioration de l'affichage des images et de la mise en page sur tablette dans l'application. [#1210](https://github.com/betagouv/api-engagement/issues/1210)
- Ajout d'un lien vers les résultats de la recherche dans les emails. [#1208](https://github.com/betagouv/api-engagement/issues/1208)
- Amélioration de l'expérience utilisateur sur mobile avec des corrections de feedback. [#1228](https://github.com/betagouv/api-engagement/issues/1228)
- Ajout d'une extension Chrome pour faciliter certaines tâches. [#1178](https://github.com/betagouv/api-engagement/issues/1178)

### Évolutions techniques
- Optimisation des requêtes pour accélérer l'affichage des organisations (myorganization). [#1229](https://github.com/betagouv/api-engagement/issues/1229)
- Refonte de la gestion des règles de diffusion des publications. [#1187](https://github.com/betagouv/api-engagement/issues/1187)
- Mise en place d'un système de suivi (tracking) avec PostHog. [#1174](https://github.com/betagouv/api-engagement/issues/1174) et [#1218](https://github.com/betagouv/api-engagement/issues/1218)
- Suppression des tables `publisher_diffusion` et refactorisation du code associé. [#1206](https://github.com/betagouv/api-engagement/issues/1206) et [#1195](https://github.com/betagouv/api-engagement/issues/1195)
- Utilisation de Typesense pour améliorer la recherche. [#1200](https://github.com/betagouv/api-engagement/issues/1200)
- Mise à jour de nombreuses dépendances (Vite, ESLint, etc.).
- Amélioration de la sécurité de l'enrichissement des missions. [#1141](https://github.com/betagouv/api-engagement/issues/1141)
- Suppression du point de terminaison `stats-mean` de l'API. [#1213](https://github.com/betagouv/api-engagement/issues/1213)

### Autres changements
- Amélioration de la documentation sur les règles de diffusion. [#1177](https://github.com/betagouv/api-engagement/issues/1177)
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour des versions de release : v1.14.2, v1.14.1, v1.14.0, v1.13.0, v1.12.0, v1.11.0, v1.9.3, v1.9.2, v1.9.1, v1.9.0.
- Ajout d'un script pour générer automatiquement le changelog. [#1202](https://github.com/betagouv/api-engagement/issues/1202)
- Suppression d'une migration obsolète liée à l'exclusion des publishers pour les analyses.
- Correction de l'erreur "mission not found" lors de la redirection. [#1214](https://github.com/betagouv/api-engagement/issues/1214)
