## Changelog : statistiques-impact (30 derniers jours, au 2026-06-15)

### Résumé
Ce changelog présente les améliorations apportées au site statistiques-impact au cours du dernier mois. Les modifications incluent des corrections liées à l'affichage des données France Transfert, des ajustements pour la compatibilité avec la librairie `datagouv_client` et une correction concernant la régénération des slugs dans les modèles de données.

### Évolutions fonctionnelles
- Correction de l'affichage du client France Transfert. [#4d9196f](https://github.com/numerique-gouv/statistiques-impact/commit/4d9196f)
- Correction des tests liés à datagouv. [#f1d76ab](https://github.com/numerique-gouv/statistiques-impact/commit/f1d76ab)
- Correction d'un test qui dépendait d'une ressource non disponible sur demo.data.gouv.fr. Le test est maintenant ignoré. [#9a274e6](https://github.com/numerique-gouv/statistiques-impact/commit/9a274e6)

### Évolutions techniques
- Mise à jour de la librairie `datagouv_client` vers la version 0.3.2. [#e8aa04c](https://github.com/numerique-gouv/statistiques-impact/commit/e8aa04c)
- Mise à jour du schéma de l'API. [#5228b4d](https://github.com/numerique-gouv/statistiques-impact/commit/5228b4d)
- Correction : Les slugs des modèles ne sont plus régénérés à chaque sauvegarde, évitant ainsi des comportements inattendus. [#16cf5b2](https://github.com/numerique-gouv/statistiques-impact/commit/16cf5b2)
