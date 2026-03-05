## Changelog : acces-cible (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à acces-cible au cours du dernier mois. Les principales évolutions concernent l'amélioration de la gestion des transitions, l'ajout de limites de pagination configurables, l'amélioration de la suppression en masse et des corrections liées au crawler et à l'extraction du taux de conformité. Des mises à jour de dépendances et des améliorations de la maintenance ont également été effectuées.

### Évolutions fonctionnelles
- Amélioration de la suppression en masse : la fonctionnalité de suppression en masse a été améliorée pour une meilleure expérience utilisateur. [#449](https://github.com/betagouv/acces-cible/issues/449)
- Pagination configurable : il est désormais possible de configurer les limites de pagination pour les listes de données. [#454](https://github.com/betagouv/acces-cible/issues/454)
- Amélioration de l'extraction du taux de conformité : la logique d'extraction du taux de conformité a été améliorée pour plus de précision. [#450](https://github.com/betagouv/acces-cible/issues/450)
- Amélioration de la logique du crawler : correction et amélioration de la logique du crawler. [#436](https://github.com/betagouv/acces-cible/issues/436)

### Évolutions techniques
- Correction d'une condition de course lors de la création de transitions : une condition de course potentielle lors de la création de transitions a été corrigée, puis annulée suite à des problèmes. [#455](https://github.com/betagouv/acces-cible/issues/455), [#457](https://github.com/betagouv/acces-cible/issues/457)
- Suppression du helper `time_ago` et mise à jour des vues : le helper `time_ago` a été supprimé et les vues ont été mises à jour avec des formats adaptés. [#452](https://github.com/betagouv/acces-cible/issues/452)
- Suppression du helper de composant DSFR et mise à jour des dépendances : le helper de composant DSFR a été supprimé et les dépendances ont été mises à jour. [#460](https://github.com/betagouv/acces-cible/issues/460)
- Mise à jour de Brakeman : Brakeman a été mis à jour vers la version 8.0.4 puis 8.0.2. [#437](https://github.com/betagouv/acces-cible/issues/437), [#461](https://github.com/betagouv/acces-cible/issues/461)
- Mise à jour d'omniauth-rails_csrf_protection : la gem omniauth-rails_csrf_protection a été mise à jour vers la version 2.0.1. [#422](https://github.com/betagouv/acces-cible/issues/422)

### Autres changements
- Mise à jour du fichier README. [#451](https://github.com/betagouv/acces-cible/issues/451)
- Correction d'un problème lié aux temps d'attente du réseau. [#466](https://github.com/betagouv/acces-cible/issues/466)
- Mises à jour de dépendances mineures : plusieurs dépendances ont été mises à jour. [#465](https://github.com/betagouv/acces-cible/issues/465)
