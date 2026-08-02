## Changelog : cdtn-admin (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, l'administration du Code du travail numérique a bénéficié d'améliorations significatives en matière d'analyse des données, notamment avec l'ajout de nouveaux indicateurs de performance (NPS, funnels) et le suivi des contributions. Des corrections ont également été apportées au sitemap et à la gestion des fichiers pour une meilleure expérience utilisateur et un référencement optimisé.

### Évolutions fonctionnelles
- Ajout d'un funnel pour l'outil "Trouver sa CC" afin de mieux comprendre le parcours utilisateur. [#1707](https://github.com/SocialGouv/cdtn-admin/issues/1707)
- Ajout d'une table pour suivre le Net Promoter Score (NPS) et évaluer la satisfaction des utilisateurs. [#1705](https://github.com/SocialGouv/cdtn-admin/issues/1705)
- Correction du remplacement de fichiers sur les modèles et les infographies. [#1708](https://github.com/SocialGouv/cdtn-admin/issues/1708)
- Correction des URLs sur la contribution congés pour évènement familiaux dans le sitemap.
- Ajout du slug de la convention collective dans l'URL du sitemap. [#1701](https://github.com/SocialGouv/cdtn-admin/issues/1701)
- Ajout du suivi des contributions par vues mensuelles pour une meilleure analyse de l'audience. [#1697](https://github.com/SocialGouv/cdtn-admin/issues/1697)
- Intégration de l'ingestion des accords d'entreprise. [#1702](https://github.com/SocialGouv/cdtn-admin/issues/1702)
- Exclusion des accords et statuts des alertes de suppression. [#1696](https://github.com/SocialGouv/cdtn-admin/issues/1696)

### Évolutions techniques
- Mise à jour de la version de Node dans la configuration CI.
- Migration des builds d'images Docker de buildkit-service vers buildkit-operator. [#1695](https://github.com/SocialGouv/cdtn-admin/issues/1695)
- Ajout du job d'analyse dans le fichier docker-compose et documentation associée. [#1704](https://github.com/SocialGouv/cdtn-admin/issues/1704)
- Correction d'une erreur lors de l'ingestion des contributions. [#1706](https://github.com/SocialGouv/cdtn-admin/issues/1706)
- Amélioration du filtrage des documents pour le sitemap, ne conservant que les contributions.

### Autres changements
- Travail en cours sur l'ajout d'indicateurs de performance clés (KPI) et correction d'un problème de recherche de statistiques. [#1693](https://github.com/SocialGouv/cdtn-admin/issues/1693)
